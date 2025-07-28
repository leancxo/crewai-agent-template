#!/usr/bin/env python3

import gspread
from google.oauth2.service_account import Credentials
import json

def analyze_company_approach(company):
    """Analyze a company and provide detailed sales approach recommendations."""
    
    name = company.get('Company Name', '')
    size = company.get('Company Size', '')
    contact_person = company.get('Contact Person', '')
    title = company.get('Title', '')
    pain_points = company.get('Pain Points', '')
    services = company.get('Services', '')
    current_angle = company.get('Campaign Angle', '')
    priority = company.get('Training Priority', '')
    annual_value = company.get('Annual Value', 0)
    
    analysis = {
        'company': name,
        'communication_channel': '',
        'primary_value_prop': '',
        'key_pain_points': '',
        'messaging_tone': '',
        'follow_up_strategy': '',
        'specific_talking_points': []
    }
    
    # 1. Communication Channel Strategy
    if 'Owner' in contact_person or 'Owner' in title:
        analysis['communication_channel'] = "📞 PHONE FIRST - Direct to decision maker"
        analysis['messaging_tone'] = "Direct, business-focused, ROI-driven"
    elif 'President' in contact_person or 'President' in title:
        analysis['communication_channel'] = "📞 PHONE FIRST - Executive level contact"
        analysis['messaging_tone'] = "Strategic, high-level, competitive advantage"
    elif 'Manager' in contact_person or 'Manager' in title:
        analysis['communication_channel'] = "📧 EMAIL FIRST - Professional approach to management"
        analysis['messaging_tone'] = "Professional, operational efficiency focused"
    else:
        analysis['communication_channel'] = "📧 EMAIL FIRST - Gentle introduction"
        analysis['messaging_tone'] = "Informative, educational, benefit-focused"
    
    # 2. Value Proposition Based on Size
    if 'Large' in size:
        analysis['primary_value_prop'] = "🎯 Standardization, compliance, and scalable training across multiple locations"
        analysis['specific_talking_points'].extend([
            "Unlimited users per branch - no per-seat fees",
            "Standardized training across all locations",
            "CEU credits accepted in 22 states",
            "Compliance and regulatory training"
        ])
    elif 'Medium' in size:
        analysis['primary_value_prop'] = "🎯 Growth support, operational efficiency, and competitive advantage"
        analysis['specific_talking_points'].extend([
            "Scale your training as you grow",
            "Improve service consistency",
            "Reduce hiring and retention challenges",
            "No long-term contracts - flexibility for growing business"
        ])
    else:  # Small
        analysis['primary_value_prop'] = "🎯 Flexible, cost-effective training with no contracts"
        analysis['specific_talking_points'].extend([
            "No contracts - start and stop as needed",
            "Unlimited users - train your whole team",
            "Small business pricing",
            "Immediate access to professional training"
        ])
    
    # 3. Pain Point Specific Messaging
    pain_lower = pain_points.lower()
    if 'hiring' in pain_lower:
        analysis['key_pain_points'] = "Hiring and retention challenges"
        analysis['specific_talking_points'].extend([
            "Professional training attracts better candidates",
            "Structured onboarding reduces turnover",
            "Career development path for employees"
        ])
    
    if 'quality' in pain_lower:
        analysis['key_pain_points'] = "Service quality and consistency"
        analysis['specific_talking_points'].extend([
            "Standardized service protocols",
            "Customer satisfaction improvements",
            "Consistent service delivery"
        ])
    
    if 'compliance' in pain_lower:
        analysis['key_pain_points'] = "Regulatory compliance and licensing"
        analysis['specific_talking_points'].extend([
            "CEU credits for license renewal",
            "Regulatory compliance training",
            "Stay current with industry standards"
        ])
    
    if 'scaling' in pain_lower or 'growth' in pain_lower:
        analysis['key_pain_points'] = "Business growth and scaling challenges"
        analysis['specific_talking_points'].extend([
            "Systematic training for expansion",
            "Maintain quality during growth",
            "Standardized processes for new locations"
        ])
    
    # 4. Service-Specific Messaging
    services_lower = services.lower()
    if 'termite' in services_lower:
        analysis['specific_talking_points'].append("Specialized termite inspection and treatment training")
    if 'commercial' in services_lower:
        analysis['specific_talking_points'].append("Commercial account management training")
    if 'wildlife' in services_lower:
        analysis['specific_talking_points'].append("Wildlife handling and safety protocols")
    if 'mosquito' in services_lower:
        analysis['specific_talking_points'].append("Seasonal service management and mosquito control")
    
    # 5. Follow-up Strategy
    if priority == 'High':
        if annual_value > 15000:
            analysis['follow_up_strategy'] = "🚀 AGGRESSIVE: Phone → Email → LinkedIn → Follow-up call (7-day cycle)"
        else:
            analysis['follow_up_strategy'] = "📈 ACTIVE: Email → Phone → Email (14-day cycle)"
    elif priority == 'Medium':
        analysis['follow_up_strategy'] = "📧 STEADY: Email → Email → Phone (21-day cycle)"
    else:
        analysis['follow_up_strategy'] = "📬 GENTLE: Email → Email (30-day cycle)"
    
    return analysis

def main():
    """Main execution function."""
    
    print("🎯 SALES APPROACH ANALYSIS - DETAILED RECOMMENDATIONS")
    print("=" * 70)
    
    try:
        # Load Google Sheets data
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
        
        # Get all data
        all_data = worksheet.get_all_records()
        print(f"📊 Analyzing {len(all_data)} companies for optimal sales approaches\\n")
        
        # Separate by priority
        high_priority = [c for c in all_data if c.get('Training Priority') == 'High']
        medium_priority = [c for c in all_data if c.get('Training Priority') == 'Medium']
        
        print("🔥 HIGH PRIORITY COMPANIES (Contact immediately):")
        print("=" * 60)
        
        for i, company in enumerate(high_priority, 1):
            analysis = analyze_company_approach(company)
            
            print(f"\\n{i}. {analysis['company']}")
            print(f"   📞 {company.get('Phone', 'N/A')} | 👥 {company.get('Contact Person', 'N/A')}")
            print(f"   💰 Pipeline: ${company.get('Annual Value', 0):,}")
            print(f"   {analysis['communication_channel']}")
            print(f"   📝 Tone: {analysis['messaging_tone']}")
            print(f"   {analysis['primary_value_prop']}")
            print(f"   🎯 Key Pain Point: {analysis['key_pain_points']}")
            print(f"   📋 Follow-up: {analysis['follow_up_strategy']}")
            
            if analysis['specific_talking_points']:
                print(f"   💡 Key Talking Points:")
                for point in analysis['specific_talking_points'][:3]:  # Top 3
                    print(f"      • {point}")
        
        print(f"\\n\\n📈 MEDIUM PRIORITY COMPANIES (Follow-up sequence):")
        print("=" * 60)
        
        for i, company in enumerate(medium_priority[:10], 1):  # Show top 10 medium priority
            analysis = analyze_company_approach(company)
            
            print(f"\\n{i}. {analysis['company']}")
            print(f"   📞 {company.get('Phone', 'N/A')} | 👥 {company.get('Contact Person', 'N/A')}")
            print(f"   {analysis['communication_channel']}")
            print(f"   {analysis['primary_value_prop']}")
            print(f"   📋 {analysis['follow_up_strategy']}")
        
        print(f"\\n\\n🎯 EXECUTIVE SUMMARY:")
        print("=" * 30)
        print(f"📊 Total Companies: {len(all_data)}")
        print(f"🔥 High Priority: {len(high_priority)} companies")
        print(f"📈 Medium Priority: {len(medium_priority)} companies")
        print(f"💰 Total Pipeline: ${sum(c.get('Annual Value', 0) for c in all_data):,}")
        
        print(f"\\n🚀 IMMEDIATE ACTIONS:")
        print("1. Start with HIGH PRIORITY companies - use phone calls")
        print("2. Focus on business owners and decision makers first")
        print("3. Emphasize no-contract, unlimited users value prop")
        print("4. Address specific pain points (hiring, quality, compliance)")
        print("5. Use industry-specific talking points based on services")
        
        return True
        
    except Exception as e:
        print(f"❌ Error analyzing companies: {e}")
        return False

if __name__ == "__main__":
    main() 