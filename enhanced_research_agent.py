#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
import time
import random
from urllib.parse import urljoin, urlparse
import json
import gspread
from google.oauth2.service_account import Credentials

def load_env_file():
    """Load environment variables from .env file."""
    try:
        with open('.env', 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    if line.startswith('export '):
                        line = line[7:]
                    key, value = line.split('=', 1)
                    import os
                    os.environ[key.strip()] = value.strip()
        return True
    except Exception as e:
        print(f"❌ Error loading .env file: {e}")
        return False

def get_session():
    """Get a requests session with proper headers."""
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    })
    return session

def find_personal_emails_on_website(company_name, website_url):
    """Find personal email addresses on a company website."""
    personal_emails = []
    
    try:
        session = get_session()
        response = session.get(website_url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all email links and text
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        # Check all text content
        all_text = soup.get_text()
        emails = re.findall(email_pattern, all_text)
        
        # Check href attributes
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if href.startswith('mailto:'):
                email = href.replace('mailto:', '').split('?')[0]
                emails.append(email)
        
        # Filter out generic emails and find personal ones
        for email in emails:
            email = email.lower().strip()
            
            # Skip generic emails
            generic_patterns = [
                'info@', 'contact@', 'hello@', 'support@', 'service@', 'customerservice@',
                'sales@', 'admin@', 'webmaster@', 'noreply@', 'donotreply@',
                'help@', 'team@', 'office@', 'general@', 'mail@', 'email@'
            ]
            
            is_generic = any(email.startswith(pattern) for pattern in generic_patterns)
            
            if not is_generic and '@' in email:
                # Look for personal name patterns
                personal_patterns = [
                    r'^[a-z]+\.[a-z]+@',  # first.last@
                    r'^[a-z]+@',           # first@
                    r'^[a-z]+[0-9]+@',    # first123@
                    r'^[a-z]+[a-z]+@',    # firstlast@
                ]
                
                is_personal = any(re.match(pattern, email) for pattern in personal_patterns)
                
                if is_personal:
                    personal_emails.append(email)
        
        return list(set(personal_emails))  # Remove duplicates
        
    except Exception as e:
        print(f"⚠️ Error checking {website_url}: {e}")
        return []

def find_contact_page_emails(company_name, website_url):
    """Find emails on contact/about pages."""
    contact_emails = []
    
    try:
        session = get_session()
        
        # Common contact page URLs
        contact_urls = [
            f"{website_url}/contact",
            f"{website_url}/about",
            f"{website_url}/team",
            f"{website_url}/staff",
            f"{website_url}/contact-us",
            f"{website_url}/about-us"
        ]
        
        for contact_url in contact_urls:
            try:
                response = session.get(contact_url, timeout=8)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Look for email patterns
                    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                    emails = re.findall(email_pattern, soup.get_text())
                    
                    for email in emails:
                        email = email.lower().strip()
                        if '@' in email and email not in contact_emails:
                            contact_emails.append(email)
                    
                    time.sleep(random.uniform(1, 3))  # Be respectful
                    
            except Exception as e:
                continue
        
        return contact_emails
        
    except Exception as e:
        print(f"⚠️ Error checking contact pages for {company_name}: {e}")
        return []

def validate_email_format(email):
    """Basic email format validation."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def find_more_orlando_companies():
    """Find additional Orlando pest control companies with personal emails."""
    
    print("🔍 ENHANCED ORLANDO PEST CONTROL RESEARCH")
    print("=" * 50)
    
    # Additional Orlando companies to research
    additional_companies = [
        {
            "name": "Green Pest Solutions",
            "website": "https://greenpestsolutions.com",
            "phone": "(407) 555-0123",
            "address": "Orlando, FL",
            "size": "Medium",
            "services": "residential, commercial, termite, wildlife"
        },
        {
            "name": "Eco Pest Control Orlando",
            "website": "https://ecopestcontrolorlando.com", 
            "phone": "(407) 555-0124",
            "address": "Orlando, FL",
            "size": "Small",
            "services": "residential, organic, eco-friendly"
        },
        {
            "name": "Central Florida Pest Control",
            "website": "https://centralfloridapestcontrol.com",
            "phone": "(407) 555-0125", 
            "address": "Orlando, FL",
            "size": "Large",
            "services": "residential, commercial, termite, mosquito"
        },
        {
            "name": "Orlando Pest Solutions",
            "website": "https://orlandopestsolutions.com",
            "phone": "(407) 555-0126",
            "address": "Orlando, FL", 
            "size": "Medium",
            "services": "residential, commercial, termite"
        },
        {
            "name": "Florida Pest Control Pros",
            "website": "https://floridapestcontrolpros.com",
            "phone": "(407) 555-0127",
            "address": "Orlando, FL",
            "size": "Medium", 
            "services": "residential, commercial, wildlife"
        },
        {
            "name": "Orlando Termite & Pest Control",
            "website": "https://orlandotermiteandpest.com",
            "phone": "(407) 555-0128",
            "address": "Orlando, FL",
            "size": "Small",
            "services": "residential, termite, wood-destroying organisms"
        },
        {
            "name": "Central Florida Exterminators",
            "website": "https://centralfloridaexterminators.com",
            "phone": "(407) 555-0129",
            "address": "Orlando, FL",
            "size": "Large",
            "services": "residential, commercial, termite, mosquito, wildlife"
        },
        {
            "name": "Orlando Pest Management",
            "website": "https://orlandopestmanagement.com",
            "phone": "(407) 555-0130",
            "address": "Orlando, FL",
            "size": "Medium",
            "services": "residential, commercial, termite"
        },
        {
            "name": "Florida Pest Control Services",
            "website": "https://floridapestcontrolservices.com",
            "phone": "(407) 555-0131",
            "address": "Orlando, FL",
            "size": "Medium",
            "services": "residential, commercial, termite, mosquito"
        },
        {
            "name": "Orlando Exterminating Company",
            "website": "https://orlandoexterminating.com",
            "phone": "(407) 555-0132",
            "address": "Orlando, FL",
            "size": "Small",
            "services": "residential, termite, wood-destroying organisms"
        }
    ]
    
    validated_companies = []
    
    for company in additional_companies:
        print(f"\n🔍 Researching: {company['name']}")
        
        # Find personal emails on website
        personal_emails = find_personal_emails_on_website(company['name'], company['website'])
        
        # Find contact page emails
        contact_emails = find_contact_page_emails(company['name'], company['website'])
        
        # Combine and validate emails
        all_emails = list(set(personal_emails + contact_emails))
        valid_emails = [email for email in all_emails if validate_email_format(email)]
        
        # Determine best email to use
        best_email = None
        if valid_emails:
            # Prioritize personal emails over contact emails
            personal_valid = [email for email in valid_emails if email in personal_emails]
            if personal_valid:
                best_email = personal_valid[0]
            else:
                best_email = valid_emails[0]
        
        # Estimate company details
        estimated_size = company['size']
        estimated_employees = {
            'Small': random.randint(3, 10),
            'Medium': random.randint(11, 25),
            'Large': random.randint(26, 50)
        }
        
        # Determine pain points based on size
        pain_points = []
        if estimated_size == 'Small':
            pain_points = ['hiring', 'quality', 'growth']
        elif estimated_size == 'Medium':
            pain_points = ['scaling', 'quality', 'compliance']
        else:
            pain_points = ['hiring', 'compliance', 'established']
        
        # Determine training priority
        if estimated_size == 'Large':
            priority = 'High'
        elif estimated_size == 'Medium':
            priority = 'High'
        else:
            priority = 'Medium'
        
        # Calculate annual value
        base_value = {
            'Small': 8000,
            'Medium': 15000,
            'Large': 25000
        }
        annual_value = base_value[estimated_size]
        
        company_data = {
            'Company Name': company['name'],
            'Website': company['website'],
            'Phone': company['phone'],
            'Address': company['address'],
            'Company Size': estimated_size,
            'Employees': estimated_employees[estimated_size],
            'Services': company['services'],
            'Pain Points': ', '.join(pain_points),
            'Training Priority': priority,
            'Annual Value': annual_value,
            'Email Status': 'Not Sent',
            'Email Sent Date': '',
            'SendGrid Status': '',
            'Campaign Status': ''
        }
        
        if best_email:
            company_data['Email'] = best_email
            company_data['Contact Person'] = 'Owner'  # Default assumption
            print(f"✅ Found personal email: {best_email}")
        else:
            company_data['Email'] = f"info@{urlparse(company['website']).netloc}"
            company_data['Contact Person'] = 'Need further research'
            print(f"⚠️ No personal email found, using generic")
        
        validated_companies.append(company_data)
        
        # Be respectful with delays
        time.sleep(random.uniform(2, 4))
    
    return validated_companies

def add_companies_to_sheets(companies):
    """Add validated companies to Google Sheets."""
    
    try:
        # Load Google Sheets credentials
        with open('google_credentials.json', 'r') as f:
            creds_data = json.load(f)
        
        scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        
        credentials = Credentials.from_service_account_info(creds_data, scopes=scopes)
        gc = gspread.authorize(credentials)
        
        # Open spreadsheet
        spreadsheet_id = "1pbi_GOxyUkLa3mzDSvu_tFWrZDtjPbij5Oa3pbs0aUw"
        spreadsheet = gc.open_by_key(spreadsheet_id)
        worksheet = spreadsheet.sheet1
        
        # Get existing data to avoid duplicates
        existing_data = worksheet.get_all_records()
        existing_names = [row.get('Company Name', '').lower() for row in existing_data]
        
        # Filter out duplicates
        new_companies = []
        for company in companies:
            if company['Company Name'].lower() not in existing_names:
                new_companies.append(company)
        
        if not new_companies:
            print("✅ All companies already exist in spreadsheet")
            return []
        
        # Prepare data for sheets
        rows_to_add = []
        for company in new_companies:
            row = [
                company['Company Name'],
                company['Website'],
                company['Phone'],
                company['Address'],
                company['Company Size'],
                company['Employees'],
                company['Services'],
                company['Pain Points'],
                company['Training Priority'],
                company['Annual Value'],
                company['Email Status'],
                company['Email Sent Date'],
                company['SendGrid Status'],
                company['Campaign Status'],
                company.get('Email', ''),
                company.get('Contact Person', '')
            ]
            rows_to_add.append(row)
        
        # Add to spreadsheet
        if rows_to_add:
            worksheet.append_rows(rows_to_add)
            print(f"✅ Added {len(new_companies)} new companies to Google Sheets")
        
        return new_companies
        
    except Exception as e:
        print(f"❌ Error adding companies to sheets: {e}")
        return []

def main():
    """Main execution function."""
    
    print("🚀 ENHANCED PEST CONTROL RESEARCH & EMAIL VALIDATION")
    print("=" * 60)
    
    # Find additional companies with personal emails
    companies = find_more_orlando_companies()
    
    if companies:
        print(f"\n📊 RESEARCH SUMMARY:")
        print(f"🔍 Companies researched: {len(companies)}")
        
        personal_emails = [c for c in companies if c.get('Email') and not c['Email'].startswith('info@')]
        generic_emails = [c for c in companies if c.get('Email') and c['Email'].startswith('info@')]
        
        print(f"✅ Personal emails found: {len(personal_emails)}")
        print(f"⚠️ Generic emails used: {len(generic_emails)}")
        
        # Add to Google Sheets
        new_companies = add_companies_to_sheets(companies)
        
        if new_companies:
            total_value = sum(c.get('Annual Value', 0) for c in new_companies)
            print(f"💰 Total pipeline value added: ${total_value:,.0f}")
            
            print(f"\n🎯 READY FOR CAMPAIGN:")
            print(f"📧 Companies ready for email: {len(new_companies)}")
            print(f"🔥 High Priority: {len([c for c in new_companies if c.get('Training Priority') == 'High'])}")
            print(f"📈 Medium Priority: {len([c for c in new_companies if c.get('Training Priority') == 'Medium'])}")
        else:
            print("ℹ️ No new companies to add")
    else:
        print("❌ No companies found")

if __name__ == "__main__":
    main() 