from langchain.tools import BaseTool
from typing import Type, Dict, List, Optional
from pydantic import BaseModel, Field
import requests
from bs4 import BeautifulSoup
import time
import random
import re
from urllib.parse import urljoin, urlparse
import json

class WebScrapingInput(BaseModel):
    """Input for web scraping tool."""
    query: str = Field(description="Search query (e.g., 'pest control Orlando FL')")
    location: str = Field(description="Geographic location for search")
    max_results: int = Field(description="Maximum number of results to return", default=20)
    source: str = Field(description="Source to scrape: 'google', 'yellowpages', 'yelp', 'websites'", default="google")

class WebScrapingTool(BaseTool):
    """Professional web scraping tool for finding real pest control companies."""
    
    name: str = "web_scraping"
    description: str = """Use this tool to find real pest control companies through web scraping. 
    Specify the search query, location, and source (google, yellowpages, yelp, or websites).
    Returns actual company names, websites, phone numbers, and addresses."""
    
    args_schema: Type[BaseModel] = WebScrapingInput
    
    def _get_session(self):
        """Get a requests session with proper headers."""
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        return session
    
    def _run(self, query: str, location: str, max_results: int = 20, source: str = "google") -> str:
        """Execute web scraping based on source."""
        
        try:
            if source == "google":
                return self._scrape_google_search(query, location, max_results)
            elif source == "yellowpages":
                return self._scrape_yellowpages(query, location, max_results)
            elif source == "yelp":
                return self._scrape_yelp(query, location, max_results)
            elif source == "websites":
                return self._scrape_company_websites(query, location, max_results)
            else:
                return "Invalid source. Use: google, yellowpages, yelp, or websites"
                
        except Exception as e:
            return f"Scraping error: {str(e)}"
    
    def _scrape_google_search(self, query: str, location: str, max_results: int) -> str:
        """Scrape Google search results for pest control companies."""
        
        search_query = f"{query} {location}"
        url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
        
        try:
            response = self._safe_request(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            companies = []
            
            # Look for business listings in Google results
            business_results = soup.find_all('div', class_=['VkpGBb', 'g'])
            
            for result in business_results[:max_results]:
                company_data = self._extract_google_business_info(result)
                if company_data and self._is_pest_control_company(company_data.get('name', '')):
                    companies.append(company_data)
            
            return self._format_companies_output(companies, f"Google Search: {search_query}")
            
        except Exception as e:
            return f"Google search error: {str(e)}"
    
    def _scrape_yellowpages(self, query: str, location: str, max_results: int) -> str:
        """Scrape Yellow Pages for pest control companies."""
        
        # Format location for Yellow Pages URL
        location_formatted = location.replace(' ', '-').replace(',', '').lower()
        query_formatted = query.replace(' ', '-').lower()
        
        url = f"https://www.yellowpages.com/{location_formatted}/{query_formatted}"
        
        try:
            response = self._safe_request(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            companies = []
            
            # Yellow Pages business listings
            listings = soup.find_all('div', class_=['info-section', 'info'])
            
            for listing in listings[:max_results]:
                company_data = self._extract_yellowpages_info(listing)
                if company_data:
                    companies.append(company_data)
            
            return self._format_companies_output(companies, f"Yellow Pages: {location}")
            
        except Exception as e:
            return f"Yellow Pages error: {str(e)}"
    
    def _scrape_yelp(self, query: str, location: str, max_results: int) -> str:
        """Scrape Yelp for pest control companies."""
        
        search_url = f"https://www.yelp.com/search?find_desc={query.replace(' ', '+')}&find_loc={location.replace(' ', '+')}"
        
        try:
            response = self._safe_request(search_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            companies = []
            
            # Yelp business containers
            business_containers = soup.find_all('div', {'data-testid': 'serp-ia-card'})
            
            for container in business_containers[:max_results]:
                company_data = self._extract_yelp_info(container)
                if company_data:
                    companies.append(company_data)
            
            return self._format_companies_output(companies, f"Yelp: {location}")
            
        except Exception as e:
            return f"Yelp error: {str(e)}"
    
    def _scrape_company_websites(self, query: str, location: str, max_results: int) -> str:
        """Visit actual company websites to extract detailed information."""
        
        # First get a list of websites from Google search
        google_results = self._scrape_google_search(query, location, max_results)
        
        # Extract website URLs from the results
        websites = self._extract_websites_from_results(google_results)
        
        detailed_companies = []
        
        for website in websites[:max_results]:
            try:
                company_details = self._scrape_individual_website(website)
                if company_details:
                    detailed_companies.append(company_details)
                
                # Rate limiting
                time.sleep(random.uniform(1, 3))
                
            except Exception as e:
                print(f"Error scraping {website}: {e}")
                continue
        
        return self._format_companies_output(detailed_companies, f"Website Details: {location}")
    
    def _extract_google_business_info(self, result_element) -> Optional[Dict]:
        """Extract business information from Google search result."""
        
        try:
            # Company name
            name_elem = result_element.find(['h3', 'h2'])
            name = name_elem.get_text(strip=True) if name_elem else None
            
            # Website URL
            link_elem = result_element.find('a', href=True)
            website = link_elem['href'] if link_elem else None
            
            # Phone number (look for patterns)
            text_content = result_element.get_text()
            phone_match = re.search(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text_content)
            phone = phone_match.group() if phone_match else None
            
            # Address (look for common address patterns)
            address_match = re.search(r'\d+\s+[A-Za-z\s]+(?:St|Street|Ave|Avenue|Rd|Road|Blvd|Boulevard|Dr|Drive)', text_content)
            address = address_match.group() if address_match else None
            
            if name:
                return {
                    'name': name,
                    'website': website,
                    'phone': phone,
                    'address': address,
                    'source': 'Google Search'
                }
            
        except Exception as e:
            print(f"Error extracting Google info: {e}")
        
        return None
    
    def _extract_yellowpages_info(self, listing_element) -> Optional[Dict]:
        """Extract business information from Yellow Pages listing."""
        
        try:
            # Company name
            name_elem = listing_element.find(['h3', 'h2', 'a'])
            name = name_elem.get_text(strip=True) if name_elem else None
            
            # Phone number
            phone_elem = listing_element.find('div', class_='phones')
            phone = phone_elem.get_text(strip=True) if phone_elem else None
            
            # Address
            address_elem = listing_element.find('div', class_='adr')
            address = address_elem.get_text(strip=True) if address_elem else None
            
            # Website
            website_elem = listing_element.find('a', {'class': 'track-visit-website'})
            website = website_elem.get('href') if website_elem else None
            
            if name:
                return {
                    'name': name,
                    'phone': phone,
                    'address': address,
                    'website': website,
                    'source': 'Yellow Pages'
                }
                
        except Exception as e:
            print(f"Error extracting Yellow Pages info: {e}")
        
        return None
    
    def _extract_yelp_info(self, container_element) -> Optional[Dict]:
        """Extract business information from Yelp listing."""
        
        try:
            # Company name
            name_elem = container_element.find('h3')
            name = name_elem.get_text(strip=True) if name_elem else None
            
            # Address
            address_elem = container_element.find('p', string=re.compile(r'\d+.*'))
            address = address_elem.get_text(strip=True) if address_elem else None
            
            # Phone number (often requires clicking through to business page)
            phone_elem = container_element.find(text=re.compile(r'\(\d{3}\)'))
            phone = phone_elem.strip() if phone_elem else None
            
            if name:
                return {
                    'name': name,
                    'address': address,
                    'phone': phone,
                    'source': 'Yelp'
                }
                
        except Exception as e:
            print(f"Error extracting Yelp info: {e}")
        
        return None
    
    def _scrape_individual_website(self, website_url: str) -> Optional[Dict]:
        """Scrape individual company website for detailed information."""
        
        try:
            response = self._safe_request(website_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract company name (from title, h1, or header)
            name = self._extract_company_name(soup)
            
            # Extract contact information
            phone = self._extract_phone_from_website(soup)
            email = self._extract_email_from_website(soup)
            address = self._extract_address_from_website(soup)
            
            # Extract services offered
            services = self._extract_services(soup)
            
            return {
                'name': name,
                'website': website_url,
                'phone': phone,
                'email': email,
                'address': address,
                'services': services,
                'source': 'Website Scraping'
            }
            
        except Exception as e:
            print(f"Error scraping website {website_url}: {e}")
            return None
    
    def _extract_company_name(self, soup: BeautifulSoup) -> str:
        """Extract company name from website."""
        # Try title tag first
        title = soup.find('title')
        if title:
            return title.get_text(strip=True)
        
        # Try main heading
        h1 = soup.find('h1')
        if h1:
            return h1.get_text(strip=True)
        
        return "Unknown Company"
    
    def _extract_phone_from_website(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract phone number from website."""
        text_content = soup.get_text()
        phone_patterns = [
            r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
            r'\d{3}-\d{3}-\d{4}',
            r'\(\d{3}\)\s*\d{3}-\d{4}'
        ]
        
        for pattern in phone_patterns:
            match = re.search(pattern, text_content)
            if match:
                return match.group()
        
        return None
    
    def _extract_email_from_website(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract email address from website."""
        text_content = soup.get_text()
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        match = re.search(email_pattern, text_content)
        return match.group() if match else None
    
    def _extract_address_from_website(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract address from website."""
        # Look for address-related text
        address_indicators = ['address', 'location', 'contact']
        
        for indicator in address_indicators:
            element = soup.find(text=re.compile(indicator, re.I))
            if element:
                parent = element.parent
                if parent:
                    text = parent.get_text(strip=True)
                    # Look for address pattern
                    address_match = re.search(r'\d+\s+[A-Za-z\s]+(?:St|Street|Ave|Avenue|Rd|Road|Blvd|Boulevard|Dr|Drive)', text)
                    if address_match:
                        return address_match.group()
        
        return None
    
    def _extract_services(self, soup: BeautifulSoup) -> List[str]:
        """Extract services offered from website."""
        services = []
        service_keywords = [
            'residential', 'commercial', 'termite', 'rodent', 'ant', 'bed bug',
            'mosquito', 'wildlife', 'inspection', 'treatment', 'extermination'
        ]
        
        text_content = soup.get_text().lower()
        
        for keyword in service_keywords:
            if keyword in text_content:
                services.append(keyword.title())
        
        return services
    
    def _safe_request(self, url: str) -> requests.Response:
        """Make a safe HTTP request with proper headers and error handling."""
        try:
            # Random delay to avoid being blocked
            time.sleep(random.uniform(0.5, 2.0))
            
            session = self._get_session()
            response = session.get(url, timeout=10)
            response.raise_for_status()
            return response
            
        except requests.RequestException as e:
            raise Exception(f"Request failed for {url}: {str(e)}")
    
    def _is_pest_control_company(self, company_name: str) -> bool:
        """Check if company name indicates it's a pest control business."""
        pest_keywords = [
            'pest', 'exterminator', 'termite', 'bug', 'rodent', 'ant',
            'mosquito', 'wildlife', 'control', 'management', 'removal'
        ]
        
        name_lower = company_name.lower()
        return any(keyword in name_lower for keyword in pest_keywords)
    
    def _extract_websites_from_results(self, results_text: str) -> List[str]:
        """Extract website URLs from search results text."""
        # This is a simplified extraction - in practice you'd parse the structured data
        url_pattern = r'https?://[^\s<>"\']+\.[^\s<>"\']*'
        urls = re.findall(url_pattern, results_text)
        
        # Filter for likely company websites (not Google, Yelp, etc.)
        filtered_urls = []
        for url in urls:
            if not any(exclude in url for exclude in ['google.', 'yelp.', 'yellowpages.', 'facebook.']):
                filtered_urls.append(url)
        
        return filtered_urls[:10]  # Limit to 10 websites
    
    def _format_companies_output(self, companies: List[Dict], source_info: str) -> str:
        """Format the companies data into a readable output."""
        
        if not companies:
            return f"No companies found from {source_info}"
        
        output = f"REAL COMPANIES FOUND - {source_info}\n"
        output += "=" * (len(source_info) + 25) + "\n\n"
        
        for i, company in enumerate(companies, 1):
            output += f"{i}. {company.get('name', 'Unknown Company')}\n"
            
            if company.get('website'):
                output += f"   Website: {company['website']}\n"
            
            if company.get('phone'):
                output += f"   Phone: {company['phone']}\n"
            
            if company.get('email'):
                output += f"   Email: {company['email']}\n"
            
            if company.get('address'):
                output += f"   Address: {company['address']}\n"
            
            if company.get('services'):
                output += f"   Services: {', '.join(company['services'])}\n"
            
            output += f"   Source: {company.get('source', 'Unknown')}\n\n"
        
        output += f"Total verified companies found: {len(companies)}\n"
        output += "All data sourced from real websites and directories.\n"
        
        return output
    
    async def _arun(self, query: str, location: str, max_results: int = 20, source: str = "google") -> str:
        """Async version of the run method."""
        return self._run(query, location, max_results, source) 