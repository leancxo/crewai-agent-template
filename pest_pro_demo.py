#!/usr/bin/env python3
"""
Pest Pro University Sales Automation Demo

This script demonstrates the AI-powered sales automation system for Pest Pro University.
It shows how the crew researches pest control companies, analyzes opportunities, 
and creates targeted sales campaigns.
"""

import os
import sys
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.append(str(Path(__file__).parent))

def demo_pest_pro_sales_automation():
    """Demonstrate the Pest Pro University sales automation system."""
    
    print("🎯 PEST PRO UNIVERSITY - SALES AUTOMATION DEMO")
    print("=" * 60)
    print()
    
    print("About Pest Pro University:")
    print("- Leading online training platform for pest control professionals")
    print("- No contracts, unlimited users per branch, cancel anytime")
    print("- CEU credit approved in 22 states")
    print("- Comprehensive training tracks: Service Tech, Sales/Office, Business Management")
    print()
    
    print("🤖 INITIALIZING AI SALES CREW...")
    print("-" * 40)
    
    # Simulate agent creation
    agents = [
        "✅ Pest Control Market Researcher - Ready",
        "✅ Sales Opportunity Analyst - Ready", 
        "✅ Sales Campaign Creator - Ready"
    ]
    
    for agent in agents:
        print(agent)
    
    print()
    print("🔍 DEMO WORKFLOW: Researching Phoenix, AZ Market")
    print("-" * 50)
    
    # Simulate the research phase
    print("\n📋 PHASE 1: Market Research")
    print("Agent: Pest Control Market Researcher")
    print("Task: Research pest control companies in Phoenix, AZ")
    print()
    print("Research Results:")
    print("- Found 47 pest control companies in Phoenix area")
    print("- Average company size: 12-30 employees")
    print("- Key challenges: CEU compliance, employee training, standardization")
    print("- Decision makers identified: 23 owners, 15 training managers")
    
    # Simulate the analysis phase
    print("\n📊 PHASE 2: Opportunity Analysis")
    print("Agent: Sales Opportunity Analyst")
    print("Task: Analyze training needs and value propositions")
    print()
    print("Analysis Results:")
    print("- High-priority prospects: 12 companies")
    print("- Primary pain point: CEU compliance costs ($2,500-5,000/year)")
    print("- ROI opportunity: 40-60% cost savings with PPU subscription")
    print("- Best approach: Lead with compliance value, emphasize flexibility")
    
    # Simulate the campaign creation phase
    print("\n✉️ PHASE 3: Campaign Creation")
    print("Agent: Sales Campaign Creator")
    print("Task: Create personalized outreach campaigns")
    print()
    print("Campaign Assets Created:")
    print("- 12 personalized email templates")
    print("- 3 phone script variations (owner, manager, decision committee)")
    print("- Value proposition calculators")
    print("- Follow-up sequences (5-touch campaign)")
    
    print("\n🎯 SAMPLE EMAIL TEMPLATE")
    print("-" * 30)
    sample_email = """
Subject: Cut Your Training Costs 60% - Phoenix Pest Control

Hi [DECISION_MAKER],

I noticed [COMPANY_NAME] provides excellent pest control services in Phoenix. 
With Arizona's strict CEU requirements, I imagine training compliance is a 
significant expense for your team.

Many Phoenix pest control companies are spending $3,000-5,000 annually on 
training and still struggling with:
✗ Inconsistent training quality
✗ Scheduling conflicts with field work  
✗ High per-person training costs

Pest Pro University has helped 500+ pest control companies solve this with:
✓ CEU-approved online training (available 24/7)
✓ No contracts - cancel anytime
✓ Unlimited users per location
✓ 60% cost savings vs traditional training

Would you be interested in a 5-minute call to see how [COMPANY_NAME] could 
save $2,000+ this year while improving training consistency?

Best regards,
[SALES_REP]
Kurt@pestprouniversity.com
(801) 440-0271

P.S. We offer a free training consultation to assess your current costs. 
No obligation.
    """
    print(sample_email.strip())
    
    print("\n📞 SAMPLE PHONE SCRIPT")
    print("-" * 25)
    phone_script = """
"Hi [DECISION_MAKER], this is [NAME] from Pest Pro University. We help pest 
control companies in Phoenix reduce training costs while staying CEU compliant.

I noticed [COMPANY_NAME] has been growing - congratulations! With Arizona's 
CEU requirements, are you spending much on keeping your technicians certified?

[LISTEN]

Most companies your size spend $3,000-5,000 annually. We've helped similar 
Phoenix companies cut that by 60% with our online platform. No contracts, 
unlimited users per location.

Would it be worth a quick 10-minute conversation to see if this could work 
for [COMPANY_NAME]?"
    """
    print(phone_script.strip())
    
    print("\n📈 EXPECTED RESULTS")
    print("-" * 20)
    print("Based on similar campaigns:")
    print("- Email open rate: 35-45%")
    print("- Response rate: 8-12%")
    print("- Phone connection rate: 25-30%")
    print("- Demo booking rate: 15-20%")
    print("- Close rate: 25-35%")
    print()
    print("Projected outcome from 12 prospects:")
    print("- 4-5 demos booked")
    print("- 1-2 new customers acquired")
    print("- Revenue potential: $6,000-15,000 ARR")
    
    print("\n🚀 NEXT STEPS")
    print("-" * 15)
    print("1. Review and approve campaign materials")
    print("2. Load prospect list into CRM")
    print("3. Execute email campaign (Day 1)")
    print("4. Begin phone outreach (Day 3)")
    print("5. Track responses and book demos")
    print("6. Follow up with nurture sequence")
    
    print("\n" + "=" * 60)
    print("✅ DEMO COMPLETED - Ready to generate real campaigns!")
    print("Specify your target market to begin...")

if __name__ == "__main__":
    demo_pest_pro_sales_automation() 