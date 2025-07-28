from langchain.tools import BaseTool
from typing import Type, Dict, List, Optional
from pydantic import BaseModel, Field
import requests
from bs4 import BeautifulSoup
import re
import time
import random
from urllib.parse import urljoin

class CompanyAnalysisInput(BaseModel):
    """Input for company analysis tool."""
    company_name: str = Field(description="Name of the company to analyze")
    website_url: str = Field(description="Company website URL")
    location: str = Field(description="Company location")

class CompanyAnalysisTool(BaseTool):
    """Tool for analyzing real pest control companies to assess training needs and opportunities."""
    
    name: str = "company_analysis"
    description: str = """Use this tool to analyze a real pest control company's website and online presence 
    to determine company size, services, training needs, decision makers, and sales opportunity potential.
    Requires company name, website URL, and location."""
    
    args_schema: Type[BaseModel] = CompanyAnalysisInput
    
    def _get_session(self):
        """Get requests session with headers."""
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        return session
    
    def _run(self, company_name: str, website_url: str, location: str) -> str:
        """Analyze a real company for training needs and sales opportunities."""
        
        try:
            session = self._get_session()
            response = session.get(website_url, timeout=10)
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.get_text().lower()
            
            # Size assessment
            size_score = 0
            if "team" in text or "staff" in text: size_score += 1
            if "locations" in text or "offices" in text: size_score += 2
            if "fleet" in text or "trucks" in text: size_score += 1
            if len(soup.find_all('img')) > 10: size_score += 1
            
            if size_score >= 4: size = "Large (20+ employees)"
            elif size_score >= 2: size = "Medium (10-20 employees)"
            else: size = "Small (<10 employees)"
            
            # Training needs assessment
            gaps = []
            if "training" not in text: gaps.append("No formal training mentioned")
            if "hiring" in text or "careers" in text: gaps.append("Hiring challenges indicate training needs")
            if "quality" in text and "service" in text: gaps.append("Quality focus suggests training opportunities")
            if "compliance" in text or "licensed" in text: gaps.append("Compliance requirements")
            
            # Services analysis
            services = []
            service_keywords = ['residential', 'commercial', 'termite', 'rodent', 'mosquito', 'bed bug', 'ant']
            for keyword in service_keywords:
                if keyword in text:
                    services.append(keyword.title())
            
            # Decision makers (basic extraction)
            decision_makers = []
            if "owner" in text: decision_makers.append("Owner")
            if "president" in text: decision_makers.append("President") 
            if "manager" in text: decision_makers.append("Manager")
            
            # Deal potential
            deals = {
                "Large (20+ employees)": "$15,000-$21,600",
                "Medium (10-20 employees)": "$11,200-$16,800",
                "Small (<10 employees)": "$3,600-$7,200"
            }
            
            # Phone and email extraction
            phone_match = re.search(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', soup.get_text())
            phone = phone_match.group() if phone_match else "Not found"
            
            email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.get_text())
            email = email_match.group() if email_match else "Not found"
            
            return f"""COMPANY ANALYSIS REPORT - {company_name}
================================

📊 COMPANY OVERVIEW:
Name: {company_name}
Location: {location}
Website: {website_url}
Estimated Size: {size}
Size Score: {size_score}/5

🛠️ SERVICES OFFERED:
{', '.join(services) if services else 'General pest control'}

🎓 TRAINING ASSESSMENT:
Training Priority: {'High' if len(gaps) >= 3 else 'Medium' if len(gaps) >= 1 else 'Low'}
Training Gaps Identified:
{chr(10).join(f'  • {gap}' for gap in gaps)}

👥 DECISION MAKERS:
{', '.join(decision_makers) if decision_makers else 'Need further research'}

📞 CONTACT INFORMATION:
Phone: {phone}
Email: {email}
Website: {website_url}

💰 SALES OPPORTUNITY:
Deal Potential: {deals.get(size, '$3,600-$7,200')}
Opportunity Level: {'High' if len(gaps) >= 2 else 'Medium'}

This analysis is based on real website content."""
            
        except Exception as e:
            return f"Analysis error for {company_name}: {str(e)}"
    
    async def _arun(self, company_name: str, website_url: str, location: str) -> str:
        """Async version of the run method."""
        return self._run(company_name, website_url, location) 