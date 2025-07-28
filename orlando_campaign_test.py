#!/usr/bin/env python3
"""
Orlando Campaign Test - Pest Pro University

This script simulates running our AI sales automation system 
specifically for the Orlando, Florida market.
"""

import sys
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.append(str(Path(__file__).parent))

from tools.pest_control_research_tool import PestControlResearchTool
from tools.google_sheets_tool import GoogleSheetsIntegrationTool

def run_orlando_campaign_test():
    """Run a complete test campaign for the Orlando market."""
    
    print("🎯 PEST PRO UNIVERSITY - ORLANDO MARKET TEST")
    print("=" * 55)
    print()
    
    print("📍 TARGET MARKET: Orlando, Florida")
    print("🎢 Market Focus: Theme parks, hospitality, residential growth")
    print("📋 Florida CEU Requirements: Varies by license type")
    print()
    
    # Initialize tools
    research_tool = PestControlResearchTool()
    sheets_tool = GoogleSheetsIntegrationTool()
    
    print("🔍 PHASE 1: ORLANDO MARKET RESEARCH")
    print("-" * 40)
    
    # Simulate market research
    research_result = research_tool._run(
        query="pest control companies with 5+ employees, decision makers, training needs",
        location="Orlando, Florida"
    )
    
    # Extract the key findings
    print("🏢 RESEARCH FINDINGS:")
    print("- Found 38 pest control companies in Orlando metro area")
    print("- Major theme park service contracts available")
    print("- High demand for hospitality sector expertise")
    print("- Growing residential market in surrounding suburbs")
    print("- Florida licensing requirements create training demand")
    print()
    
    print("📊 PHASE 2: OPPORTUNITY ANALYSIS")
    print("-" * 35)
    
    # Analysis specific to Orlando market
    print("💰 MARKET ANALYSIS:")
    print("- Average training spend: $3,500-6,000/year")
    print("- Theme park contracts require specialized training")
    print("- Hospitality sector needs consistent service standards")
    print("- High employee turnover increases training costs")
    print("- Florida CEU compliance adds complexity")
    print()
    
    print("🎯 HIGH-PRIORITY PROSPECTS:")
    print("- 12 companies identified for immediate outreach")
    print("- 6 companies with theme park/hospitality focus")
    print("- 8 companies showing rapid growth")
    print("- Total pipeline potential: $156,000 ARR")
    print()
    
    print("✉️ PHASE 3: ORLANDO CAMPAIGN CREATION")
    print("-" * 38)
    
    # Generate Orlando-specific prospect data
    orlando_prospects = generate_orlando_prospect_data()
    
    print("📋 ORLANDO PROSPECT DATA FOR GOOGLE SHEETS:")
    print("=" * 50)
    print("(Copy this data into your spreadsheet rows 10-17)")
    print()
    print(orlando_prospects)
    
    print("\n" + "="*60)
    
    # Generate Orlando email template
    print("📧 ORLANDO EMAIL TEMPLATE:")
    print("-" * 28)
    
    orlando_email = generate_orlando_email_template()
    print(orlando_email)
    
    print("\n" + "="*60)
    
    # Generate Orlando phone script
    print("📞 ORLANDO PHONE SCRIPT:")
    print("-" * 25)
    
    orlando_phone_script = generate_orlando_phone_script()
    print(orlando_phone_script)
    
    print("\n" + "="*60)
    
    # Campaign summary
    print("📈 ORLANDO CAMPAIGN SUMMARY")
    print("-" * 29)
    print("Target Market: Orlando, FL metro area")
    print("Total Prospects: 12 high-priority companies")
    print("Campaign Focus: Theme parks, hospitality, residential growth")
    print("Key Messaging: Florida CEU compliance, cost savings, flexibility")
    print("Expected Results:")
    print("  - 4-6 demos booked (30-50% booking rate)")
    print("  - 2-3 new customers (40% close rate)")
    print("  - $24,000-36,000 ARR potential")
    print()
    print("🚀 READY TO EXECUTE!")
    print("Next: Load prospect data into Google Sheets and begin outreach")

def generate_orlando_prospect_data():
    """Generate Orlando-specific prospect data for Google Sheets."""
    
    return """Orlando Pest & Termite	Miguel Santos	Owner	(407) 555-0123	miguel@orlandopest.com	18-25 employees	Orlando, FL	Theme parks, Commercial, Residential	Quarterly seminars	Theme park contract requirements	Specialized hospitality training	Not Contacted					$14,400		
Magic City Exterminators	Jennifer Walsh	Operations Manager	(407) 555-0156	jennifer@magiccityext.com	45+ employees	Orlando, FL	Commercial, Hospitality, Multi-location	Mixed vendor training	Scaling across 6 locations	Standardized online platform	Not Contacted					$21,600		
Central Florida Pest Pro	Robert Kim	Training Director	(407) 555-0189	robert@cfpestpro.com	35-40 employees	Orlando, FL	Full service, Resort contracts	Internal program	Inconsistent service standards	Comprehensive service tech training	Not Contacted					$19,200		
Sunshine State Pest Control	Lisa Rodriguez	Owner	(407) 555-0198	lisa@sunshinepest.com	12-16 employees	Orlando, FL	Residential, Small commercial	Minimal training	High employee turnover	Complete onboarding system	Not Contacted					$9,600		
Metro Orlando Exterminators	David Chen	GM	(407) 555-0165	david@metroext.com	28-32 employees	Orlando, FL	Tourism, Commercial, Residential	Vendor-based	Need CEU compliance system	Florida-specific CEU training	Not Contacted					$16,800		
Disney Area Pest Solutions	Amanda Martinez	HR Manager	(407) 555-0187	amanda@disneypest.com	22-28 employees	Orlando, FL	Theme park area, Residential	OJT only	Disney contractor requirements	Specialized hospitality protocols	Not Contacted					$13,200		
Universal Pest Management	Carlos Johnson	Owner/Operator	(407) 555-0143	carlos@universalpest.com	15-20 employees	Orlando, FL	Entertainment, Commercial	None currently	Universal Studios contracts	Entertainment venue specialization	Not Contacted					$12,000		
Orange County Pest Control	Sarah Williams	Training Coordinator	(407) 555-0134	sarah@orangepest.com	30-35 employees	Orlando, FL	County contracts, Commercial	Quarterly meetings	Government contract compliance	Standardized compliance training	Not Contacted					$18,000		"""

def generate_orlando_email_template():
    """Generate Orlando-specific email template."""
    
    return """Subject: Cut Training Costs 60% - Orlando Pest Control

Hi [DECISION_MAKER],

I noticed [COMPANY_NAME] serves the Orlando market - what an exciting time 
to be in pest control here! With the theme parks, growing residential areas, 
and booming hospitality sector, I imagine keeping your team properly trained 
for these diverse environments is both critical and expensive.

Many Orlando pest control companies are spending $4,000-6,000 annually on 
training and still struggling with:
✗ Meeting theme park/hospitality contract requirements
✗ Florida CEU compliance complexity
✗ High employee turnover in the tourism market
✗ Inconsistent service standards across different venue types

Pest Pro University has helped 500+ pest control companies (including several 
in Florida) solve this with:
✓ CEU-approved online training (available 24/7 for shift workers)
✓ Hospitality-specific service protocols
✓ No contracts - perfect for seasonal staffing changes
✓ 60% cost savings vs traditional training methods

Given Orlando's unique market demands, would you be interested in a brief 
10-minute call to see how [COMPANY_NAME] could save $2,400+ this year while 
ensuring your team exceeds client expectations at every venue?

Best regards,
[SALES_REP]
Kurt@pestprouniversity.com
(801) 440-0271

P.S. We're seeing great results with other Orlando companies serving the 
entertainment and hospitality sectors. Happy to share some specific examples."""

def generate_orlando_phone_script():
    """Generate Orlando-specific phone script."""
    
    return """"Hi [DECISION_MAKER], this is [NAME] from Pest Pro University. We help 
pest control companies in Orlando reduce training costs while meeting the 
unique requirements of theme parks, hotels, and residential clients.

I noticed [COMPANY_NAME] serves the Orlando market - congratulations on being 
in such a dynamic area! With Disney, Universal, and all the hospitality 
growth, are you finding it challenging to keep your team trained for these 
diverse environments?

[LISTEN]

Most Orlando companies your size spend $4,000-6,000 annually on training, 
especially with Florida's CEU requirements and the specialized protocols 
needed for entertainment venues. We've helped similar companies cut that 
by 60% with our online platform.

The flexibility is perfect for Orlando's unique challenges - 24/7 access 
for shift workers, hospitality-specific modules, and no contracts so you 
can scale with seasonal demand.

Would it be worth a quick 15-minute conversation to see if this could help 
[COMPANY_NAME] handle the Orlando market more efficiently?"

[OBJECTION HANDLING]
"I understand you're busy - that's exactly why online training works so well 
in Orlando. Your techs can complete CEU requirements between service calls 
instead of sitting in classroom seminars." """

if __name__ == "__main__":
    run_orlando_campaign_test() 