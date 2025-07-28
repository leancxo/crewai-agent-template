#!/usr/bin/env python3

import gspread
from google.oauth2.service_account import Credentials
import json
from datetime import datetime, timedelta

def safe_float(value):
    """Safely convert value to float, handling currency formatting."""
    if isinstance(value, (int, float)):
        return float(value)
    elif isinstance(value, str):
        # Remove currency symbols and commas
        cleaned = value.replace('$', '').replace(',', '').replace(' ', '')
        try:
            return float(cleaned)
        except ValueError:
            return 0
    return 0

def generate_personalized_email(company):
    """Generate a personalized email using sales campaign strategy."""
    
    name = company.get('Company Name', '')
    contact_person = company.get('Contact Person', 'Team')
    size = company.get('Company Size', '')
    pain_points = company.get('Pain Points', '')
    services = company.get('Services', '')
    email = company.get('Email', '')
    phone = company.get('Phone', '')
    
    # Personalize greeting based on contact person
    if contact_person and contact_person != 'Need further research':
        if 'Johnny Gato' in contact_person:
            greeting = "Hi Johnny,"
        elif 'Rick Ricker' in contact_person:
            greeting = "Hi Rick,"
        elif 'Meryl' in contact_person:
            greeting = "Hi Meryl,"
        elif 'Andreas' in contact_person:
            greeting = "Hi Andreas,"
        elif 'Steve Bloom' in contact_person:
            greeting = "Hi Steve,"
        elif 'Lauren Shelton' in contact_person:
            greeting = "Hi Lauren,"
        elif 'Kevin' in contact_person:
            greeting = "Hi Kevin,"
        elif 'Jason' in contact_person:
            greeting = "Hi Jason,"
        elif 'Anthony' in contact_person:
            greeting = "Hi Anthony,"
        elif 'Jake' in contact_person:
            greeting = "Hi Jake,"
        elif 'Roger Lewis' in contact_person:
            greeting = "Hi Roger,"
        elif 'Ruston Stegall' in contact_person:
            greeting = "Hi Ruston,"
        elif 'Owner' in contact_person:
            greeting = "Hello,"
        elif 'Manager' in contact_person:
            greeting = "Hello,"
        else:
            greeting = f"Hi {contact_person.split()[0]}," if contact_person else "Hello,"
    else:
        greeting = "Hello,"
    
    # Create pain point hook
    if 'hiring' in pain_points.lower():
        hook = "I know finding and keeping quality technicians is one of the biggest challenges in pest control right now."
    elif 'quality' in pain_points.lower():
        hook = f"I noticed that {name} has built a reputation for quality service - that's exactly the kind of company we love working with."
    elif 'compliance' in pain_points.lower():
        hook = "With all the regulatory changes in pest control, staying compliant while keeping your team trained can be challenging."
    elif 'growth' in pain_points.lower() or 'scaling' in pain_points.lower():
        hook = f"Growing companies like {name} often face the challenge of maintaining service quality while expanding."
    elif 'family' in pain_points.lower():
        hook = f"Family-owned businesses like {name} understand the importance of doing things right."
    elif 'established' in pain_points.lower():
        hook = f"After seeing {name}'s long track record in the industry, I thought you might be interested in something that could help streamline operations."
    else:
        hook = f"I came across {name} and was impressed by your professional approach to pest control."
    
    # Value proposition based on company size and type
    if 'Large' in size:
        value_prop = "unlimited users per branch with no per-seat fees - perfect for companies with multiple locations like yours"
        benefit = "standardize training across all your locations while reducing per-employee costs"
    elif 'Medium' in size:
        value_prop = "flexible training that grows with your business - no long-term contracts"
        benefit = "improve service consistency and operational efficiency as you continue to grow"
    else:
        value_prop = "no-contract approach with unlimited users for your entire team"
        benefit = "get professional training without the overhead of traditional programs"
    
    # Service-specific benefits
    service_benefit = ""
    if 'termite' in services.lower():
        service_benefit = "\n\nOur termite inspection and treatment training modules are particularly popular with specialists - covering both subterranean and drywood termite protocols."
    elif 'commercial' in services.lower():
        service_benefit = "\n\nSince you work with commercial accounts, you'll appreciate our business management track that covers client retention and account growth strategies."
    elif 'wildlife' in services.lower():
        service_benefit = "\n\nOur wildlife control training includes safety protocols and humane handling procedures that are essential for specialized services like yours."
    elif 'mosquito' in services.lower():
        service_benefit = "\n\nFor seasonal services like mosquito control, our training helps standardize service delivery and customer communication throughout the season."
    
    # Call to action based on contact person
    if 'Owner' in contact_person:
        cta = f"Would you have 10 minutes for a quick call this week? I can show you exactly how other {'established companies' if 'Large' in size else 'growing businesses' if 'Medium' in size else 'pest control companies'} are using this to {'improve their bottom line' if 'Large' in size else 'scale more efficiently' if 'Medium' in size else 'strengthen their operations'}."
    else:
        cta = f"Would you be interested in a brief call to see how this might help {name}? I can share some specific examples of how companies your size are benefiting."
    
    # Create the email
    email_content = f"""Subject: Training Solution for {name} - No Contracts, Unlimited Users

{greeting}

{hook}

I'm reaching out because Pest Pro University helps companies like {name} {benefit} through our comprehensive online training platform.

What makes us different:
• {value_prop.title()}
• CEU credits accepted in 22 states
• Three specialized tracks: Service Tech, Sales/Office, Business Management
• Industry-specific content designed specifically for pest control{service_benefit}

{cta}

The setup is simple - you can start immediately, train unlimited team members, and there are no long-term commitments.

Best regards,
[Your Name]
Pest Pro University
[Your Phone] | [Your Email]

P.S. - I'll follow up with a call next week if I don't hear back. Many business owners find it easier to discuss training needs over the phone.

---
TO: {email}
PHONE FOR FOLLOW-UP: {phone}
CONTACT: {contact_person}
PRIORITY: {company.get('Training Priority', 'Medium')}
 PIPELINE VALUE: ${safe_float(company.get('Annual Value', 0)):,.0f}
"""
    
    return email_content

def create_all_campaign_emails():
    """Generate personalized emails for all companies using campaign strategy."""
    
    print("📧 PERSONALIZED EMAIL CAMPAIGN GENERATOR")
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
        
        today = datetime.now()
        
        print(f"📅 CAMPAIGN EMAILS GENERATED - {today.strftime('%B %d, %Y')}")
        print(f"🔥 High Priority: {len(high_priority)} companies")
        print(f"📈 Medium Priority: {len(medium_priority)} companies")
        total_pipeline = sum(safe_float(c.get('Annual Value', 0)) for c in all_data)
        print(f"💰 Total Pipeline: ${total_pipeline:,.0f}")
        
        print(f"\n🔥 HIGH PRIORITY EMAILS - WEEK 1 CAMPAIGN:")
        print("=" * 60)
        
        for i, company in enumerate(high_priority, 1):
            send_date = today + timedelta(days=i-1)
            
            print(f"\n{'='*80}")
            print(f"EMAIL {i} - SEND {send_date.strftime('%A, %B %d')}")
            print(f"{'='*80}")
            
            email = generate_personalized_email(company)
            print(email)
            
            print(f"\n{'='*80}")
            print(f"END EMAIL {i}")
            print(f"{'='*80}")
        
        print(f"\n\n📈 MEDIUM PRIORITY EMAILS - WEEK 3 CAMPAIGN:")
        print("=" * 60)
        
        for i, company in enumerate(medium_priority[:5], 1):  # First 5 medium priority
            send_date = today + timedelta(days=14+i-1)
            
            print(f"\n{'='*80}")
            print(f"EMAIL {i+10} - SEND {send_date.strftime('%A, %B %d')}")
            print(f"{'='*80}")
            
            email = generate_personalized_email(company)
            print(email)
            
            print(f"\n{'='*80}")
            print(f"END EMAIL {i+10}")
            print(f"{'='*80}")
        
        print(f"\n\n📊 CAMPAIGN SUMMARY:")
        print("=" * 30)
        print(f"📧 Total emails generated: {len(high_priority) + 5}")
        print(f"🎯 Ready for immediate execution")
        print(f"📅 Timeline: {len(high_priority)} emails over 10 days + 5 follow-up emails")
        combined_pipeline = sum(safe_float(c.get('Annual Value', 0)) for c in high_priority[:10]) + sum(safe_float(c.get('Annual Value', 0)) for c in medium_priority[:5])
        print(f"💰 Combined pipeline value: ${combined_pipeline:,.0f}")
        
        print(f"\n🚀 EXECUTION INSTRUCTIONS:")
        print("1. Copy each email and paste into your email client")
        print("2. Replace [Your Name], [Your Phone], [Your Email] with actual details")
        print("3. Send according to the date schedule")
        print("4. Track responses in your CRM")
        print("5. Follow up with phone calls as scheduled")
        
        return True
        
    except Exception as e:
        print(f"❌ Error generating campaign emails: {e}")
        return False

def main():
    """Main execution function."""
    
    create_all_campaign_emails()

if __name__ == "__main__":
    main() 