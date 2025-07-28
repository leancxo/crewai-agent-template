#!/usr/bin/env python3

import gspread
from google.oauth2.service_account import Credentials
import json
from datetime import datetime, timedelta

def create_email_template(company, analysis):
    """Create personalized email template for each company."""
    
    name = company.get('Company Name', '')
    contact_person = company.get('Contact Person', 'Team')
    size = company.get('Company Size', '')
    pain_points = company.get('Pain Points', '')
    services = company.get('Services', '')
    
    # Personalize greeting
    if contact_person and contact_person != 'Need further research':
        if 'Owner' in contact_person:
            greeting = f"Hi {contact_person.replace('Owner', '').strip() or 'there'},"
        elif any(name in contact_person for name in ['Johnny', 'Rick', 'Meryl', 'Andreas', 'Kevin', 'Jason', 'Anthony', 'Steve', 'Lauren', 'Jake']):
            greeting = f"Hi {contact_person.split()[0]},"
        else:
            greeting = f"Hi {contact_person},"
    else:
        greeting = "Hello,"
    
    # Value proposition based on size
    if 'Large' in size:
        value_prop = "unlimited users per branch with no per-seat fees"
        benefit = "standardize training across all your locations"
    elif 'Medium' in size:
        value_prop = "flexible training that scales with your growth"
        benefit = "improve operational efficiency and service consistency"
    else:
        value_prop = "no-contract training with unlimited users"
        benefit = "train your entire team without long-term commitments"
    
    # Pain point specific hook
    hook = ""
    if 'hiring' in pain_points.lower():
        hook = "I noticed many pest control companies are struggling with hiring and retention challenges."
    elif 'quality' in pain_points.lower():
        hook = "I see that quality and consistency are important priorities for your business."
    elif 'compliance' in pain_points.lower():
        hook = "With regulatory requirements constantly evolving, staying compliant can be challenging."
    elif 'growth' in pain_points.lower() or 'scaling' in pain_points.lower():
        hook = "Growing pest control businesses often face the challenge of maintaining quality during expansion."
    else:
        hook = f"I came across {name} and was impressed by your commitment to professional service."
    
    # Service-specific mention
    service_mention = ""
    if 'termite' in services.lower():
        service_mention = " Our termite-specific training modules are particularly popular with specialists like yourselves."
    elif 'commercial' in services.lower():
        service_mention = " We have specialized commercial account management training that many B2B-focused companies find valuable."
    elif 'wildlife' in services.lower():
        service_mention = " Our wildlife handling and safety protocol training addresses the unique challenges of your specialized services."
    
    email_template = f"""Subject: Professional Training for {name} - No Contracts, Unlimited Users

{greeting}

{hook}

I'm reaching out because Pest Pro University helps companies like {name} {benefit} through our comprehensive online training platform.

What makes us different:
• {value_prop.title()}
• CEU credits accepted in 22 states  
• Three specialized tracks: Service Tech, Sales/Office, Business Management
• Industry-specific content designed for pest control professionals{service_mention}

Many companies your size appreciate our flexibility - you can start immediately, add unlimited team members, and there are no long-term contracts.

Would you be interested in a brief 10-minute call to see how this might help {name}? I can show you exactly how other {'similar-sized companies' if 'Medium' in size or 'Large' in size else 'pest control businesses'} are using our training to {'improve their operations' if 'Large' in size else 'grow their business' if 'Medium' in size else 'strengthen their team'}.

Best regards,
[Your Name]
Pest Pro University
[Your Phone] | [Your Email]

P.S. - I'll follow up with a quick call next week if I don't hear back. Sometimes it's easier to discuss training needs over the phone.
"""
    
    return email_template

def create_phone_script(company, analysis):
    """Create phone call script for each company."""
    
    name = company.get('Company Name', '')
    contact_person = company.get('Contact Person', 'the business owner')
    size = company.get('Company Size', '')
    pain_points = company.get('Pain Points', '')
    phone = company.get('Phone', '')
    
    # Opening based on contact type
    if 'Owner' in contact_person:
        opening = f"Hi, this is [Your Name] from Pest Pro University. I'm calling to speak with the owner about training opportunities for {name}."
    elif 'Manager' in contact_person:
        opening = f"Hi, this is [Your Name] from Pest Pro University. I sent an email about training programs and wanted to follow up with {contact_person if contact_person != 'Operations Manager' else 'your operations manager'}."
    else:
        opening = f"Hi, this is [Your Name] from Pest Pro University. I'm calling about professional training opportunities for {name}."
    
    # Pain point hook
    pain_hook = ""
    if 'hiring' in pain_points.lower():
        pain_hook = "Many pest control companies tell us that professional training helps them attract better candidates and reduce turnover."
    elif 'quality' in pain_points.lower():
        pain_hook = "I know maintaining consistent service quality is crucial in the pest control industry."
    elif 'compliance' in pain_points.lower():
        pain_hook = "With all the regulatory requirements, having a structured training program with CEU credits can be really valuable."
    else:
        pain_hook = "Professional training can make a real difference in team performance and customer satisfaction."
    
    # Value prop based on size
    if 'Large' in size:
        value_focus = "The unlimited users per branch really makes sense for companies like yours - no per-seat fees, just one price for each location."
    elif 'Medium' in size:
        value_focus = "What's great is there are no contracts - you can scale the training up or down as your business grows."
    else:
        value_focus = "For a company your size, the unlimited users and no-contract approach gives you maximum flexibility."
    
    phone_script = f"""
📞 PHONE SCRIPT - {name}
================================
Phone: {phone}
Contact: {contact_person}
Best time to call: [Business hours, avoid early morning/late afternoon]

OPENING:
"{opening} Is this a good time for a quick conversation?"

[If NO]: "No problem, when would be a better time to call back?"
[If YES]: Continue below

HOOK:
"{pain_hook}"

VALUE PROPOSITION:
"We provide online training specifically for pest control companies. {value_focus}"

KEY POINTS:
• No contracts - start and stop as needed
• Unlimited users {'per branch' if 'Large' in size else 'for your team'}
• CEU credits accepted in 22 states
• Three tracks: Service Tech, Sales/Office, Business Management

DISCOVERY QUESTIONS:
1. "What kind of training are you currently doing for your team?"
2. "How do you handle onboarding new technicians?"
3. "Are you needing CEU credits for license renewals?"
4. "What's your biggest challenge with {'standardizing across locations' if 'Large' in size else 'growing your team' if 'Medium' in size else 'training your staff'}?"

OBJECTION HANDLING:
- "We don't have time": "That's exactly why online works - your team can train when it's convenient"
- "Too expensive": "What's your current cost per employee for training? Ours is typically much lower"
- "Need to think about it": "I understand. What specific information would help you make a decision?"

CLOSE:
"Would you like me to set up a quick 15-minute demo so you can see exactly how this works?"

FOLLOW-UP:
"I'll send you some information by email and follow up in a few days. What's the best email address?"

NEXT STEPS:
□ Schedule demo
□ Send information packet  
□ Add to follow-up sequence
□ Notes: ___________________
"""
    
    return phone_script

def generate_communication_plan():
    """Generate comprehensive communication plan with emails and phone scripts."""
    
    print("📧 ORLANDO PEST CONTROL COMMUNICATION PLAN")
    print("=" * 60)
    
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
        
        # Separate by priority
        high_priority = [c for c in all_data if c.get('Training Priority') == 'High']
        medium_priority = [c for c in all_data if c.get('Training Priority') == 'Medium']
        
        # Create communication schedule
        today = datetime.now()
        
        print(f"📅 COMMUNICATION SCHEDULE STARTING {today.strftime('%B %d, %Y')}")
        print("=" * 60)
        
        # Week 1: High Priority Email Outreach
        print(f"\n📧 WEEK 1: HIGH PRIORITY EMAIL OUTREACH")
        print("=" * 50)
        
        for i, company in enumerate(high_priority, 1):
            send_date = today + timedelta(days=i-1)
            company_name = company.get('Company Name', '')
            contact_person = company.get('Contact Person', '')
            email = company.get('Email', 'Not found')
            phone = company.get('Phone', '')
            
            print(f"\n{send_date.strftime('%a %m/%d')} - Day {i}")
            print(f"📧 EMAIL: {company_name}")
            print(f"   To: {contact_person} ({email})")
            print(f"   📞 Phone ready: {phone}")
            print(f"   💰 Pipeline: ${company.get('Annual Value', 0)}")
        
        # Week 2: Follow-up calls to high priority
        print(f"\n📞 WEEK 2: HIGH PRIORITY FOLLOW-UP CALLS")
        print("=" * 50)
        
        for i, company in enumerate(high_priority, 1):
            call_date = today + timedelta(days=7+i-1)
            company_name = company.get('Company Name', '')
            contact_person = company.get('Contact Person', '')
            phone = company.get('Phone', '')
            
            print(f"\n{call_date.strftime('%a %m/%d')} - Call Day {i}")
            print(f"📞 CALL: {company_name}")
            print(f"   Contact: {contact_person}")
            print(f"   Phone: {phone}")
            print(f"   Purpose: Follow up on email, schedule demo")
        
        # Week 3: Medium priority emails
        print(f"\n📧 WEEK 3: MEDIUM PRIORITY EMAIL OUTREACH")
        print("=" * 50)
        
        for i, company in enumerate(medium_priority[:10], 1):  # First 10 medium priority
            send_date = today + timedelta(days=14+i-1)
            company_name = company.get('Company Name', '')
            contact_person = company.get('Contact Person', '')
            email = company.get('Email', 'Not found')
            
            print(f"\n{send_date.strftime('%a %m/%d')} - Day {14+i}")
            print(f"📧 EMAIL: {company_name}")
            print(f"   To: {contact_person} ({email})")
        
        # Create detailed templates and scripts
        print(f"\n\n📝 DETAILED EMAIL TEMPLATES & PHONE SCRIPTS")
        print("=" * 60)
        
        # Analysis for personalization
        analysis = {}  # Placeholder for analysis data
        
        # Generate templates for top 5 high priority companies
        print(f"\n🔥 TOP 5 HIGH PRIORITY - EMAIL TEMPLATES:")
        print("=" * 50)
        
        for i, company in enumerate(high_priority[:5], 1):
            print(f"\n{'='*80}")
            print(f"COMPANY {i}: {company.get('Company Name', '')}")
            print(f"{'='*80}")
            
            # Email template
            email_template = create_email_template(company, analysis)
            print(email_template)
            
            print(f"\n{'-'*80}")
            print(f"PHONE SCRIPT:")
            print(f"{'-'*80}")
            
            # Phone script
            phone_script = create_phone_script(company, analysis)
            print(phone_script)
        
        # Summary and timeline
        print(f"\n\n📊 COMMUNICATION PLAN SUMMARY")
        print("=" * 40)
        print(f"📧 Total Companies: {len(all_data)}")
        print(f"🔥 High Priority: {len(high_priority)} companies")
        print(f"📈 Medium Priority: {len(medium_priority)} companies")
        print(f"💰 Total Pipeline: ${sum(c.get('Annual Value', 0) for c in all_data)}")
        
        print(f"\n📅 TIMELINE:")
        print(f"Week 1: Email {len(high_priority)} high priority companies")
        print(f"Week 2: Call {len(high_priority)} high priority companies")
        print(f"Week 3: Email {min(10, len(medium_priority))} medium priority companies")
        print(f"Week 4: Call medium priority + second round high priority")
        
        print(f"\n🎯 SUCCESS METRICS:")
        print(f"Target: 30% email response rate ({int(len(high_priority) * 0.3)} responses)")
        print(f"Target: 50% call connection rate ({int(len(high_priority) * 0.5)} conversations)")
        print(f"Target: 10% demo conversion rate ({int(len(all_data) * 0.1)} demos)")
        print(f"Target: 20% demo-to-close rate ({int(len(all_data) * 0.02)} new customers)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error generating communication plan: {e}")
        return False

def main():
    """Main execution function."""
    
    generate_communication_plan()

if __name__ == "__main__":
    main() 