#!/usr/bin/env python3

import gspread
from google.oauth2.service_account import Credentials
import json
from datetime import datetime, timedelta

def get_daily_actions():
    """Get today's communication actions."""
    
    today = datetime.now()
    print(f"🎯 DAILY ACTION PLAN - {today.strftime('%A, %B %d, %Y')}")
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
        high_priority = [c for c in all_data if c.get('Training Priority') == 'High']
        
        # Today's actions
        print("📧 TODAY'S EMAIL TARGET:")
        print("-" * 30)
        
        # First company for today (adjust based on actual start date)
        target_company = high_priority[0]  # Turner Pest Control
        
        print(f"🎯 COMPANY: {target_company.get('Company Name', '')}")
        print(f"📧 EMAIL: {target_company.get('Email', '')}")
        print(f"👥 CONTACT: {target_company.get('Contact Person', '')}")
        print(f"📞 PHONE: {target_company.get('Phone', '')}")
        print(f"💰 PIPELINE: ${target_company.get('Annual Value', 0)}")
        
        print(f"\n📝 EMAIL TEMPLATE TO SEND:")
        print("=" * 50)
        
        # Generate the exact email to send
        email_content = f"""Subject: Professional Training for {target_company.get('Company Name', '')} - No Contracts, Unlimited Users

Hi there,

I noticed many pest control companies are struggling with hiring and retention challenges.

I'm reaching out because Pest Pro University helps companies like {target_company.get('Company Name', '')} standardize training across all your locations through our comprehensive online training platform.

What makes us different:
• Unlimited users per branch with no per-seat fees
• CEU credits accepted in 22 states  
• Three specialized tracks: Service Tech, Sales/Office, Business Management
• Industry-specific content designed for pest control professionals
• Our termite-specific training modules are particularly popular with specialists like yourselves

Many companies your size appreciate our flexibility - you can start immediately, add unlimited team members, and there are no long-term contracts.

Would you be interested in a brief 10-minute call to see how this might help {target_company.get('Company Name', '')}? I can show you exactly how other similar-sized companies are using our training to improve their operations.

Best regards,
[Your Name]
Pest Pro University
[Your Phone] | [Your Email]

P.S. - I'll follow up with a quick call next week if I don't hear back. Sometimes it's easier to discuss training needs over the phone."""

        print(email_content)
        
        print(f"\n📞 PHONE CALL PREP (for next week):")
        print("=" * 40)
        print(f"📅 Call Date: {(today + timedelta(days=7)).strftime('%A, %B %d')}")
        print(f"📞 Number: {target_company.get('Phone', '')}")
        print(f"👥 Ask for: Owner")
        print(f"🎯 Opening: 'Hi, this is [Your Name] from Pest Pro University. I'm calling to speak with the owner about training opportunities for {target_company.get('Company Name', '')}. Is this a good time for a quick conversation?'")
        
        print(f"\n📊 PROGRESS TRACKING:")
        print("=" * 25)
        print(f"✅ Companies researched: 24")
        print(f"📧 Emails to send this week: 10")
        print(f"📞 Calls scheduled next week: 10")
        print(f"💰 Total pipeline value: $223,800")
        
        print(f"\n🎯 TODAY'S CHECKLIST:")
        print("□ Send email to Turner Pest Control")
        print("□ Set reminder for follow-up call next week")
        print("□ Prepare tomorrow's email (Gato Guard Services)")
        print("□ Update tracking spreadsheet")
        
        print(f"\n📈 TOMORROW'S TARGET:")
        if len(high_priority) > 1:
            next_company = high_priority[1]
            print(f"📧 {next_company.get('Company Name', '')} - {next_company.get('Contact Person', '')}")
            print(f"📞 {next_company.get('Phone', '')} | 📧 {next_company.get('Email', '')}")
        
        print(f"\n🔥 THIS WEEK'S SCHEDULE:")
        print("-" * 30)
        for i, company in enumerate(high_priority[:5], 1):
            send_date = today + timedelta(days=i-1)
            print(f"{send_date.strftime('%a %m/%d')}: {company.get('Company Name', '')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error getting daily actions: {e}")
        return False

def main():
    """Main execution function."""
    
    get_daily_actions()
    
    print(f"\n🚀 LET'S DO THIS!")
    print("Copy the email above and send it now!")
    print("Remember to personalize [Your Name], [Your Phone], [Your Email]")

if __name__ == "__main__":
    main() 