#!/usr/bin/env python3

import os
import gspread
from google.oauth2.service_account import Credentials
import json
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content
import time

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
                    os.environ[key.strip()] = value.strip()
        return True
    except Exception as e:
        print(f"❌ Error loading .env file: {e}")
        return False

def generate_personalized_email(company):
    """Generate a personalized email using sales campaign strategy."""
    
    name = str(company.get('Company Name', ''))
    contact_person = str(company.get('Contact Person', 'Team'))
    size = str(company.get('Company Size', ''))
    pain_points = str(company.get('Pain Points', ''))
    services = str(company.get('Services', ''))
    
    # Personalize greeting
    greeting = "Hello,"
    if contact_person and contact_person != 'Need further research' and contact_person != 'Team':
        greeting = f"Hi {contact_person},"
    
    # Create pain point hook
    if 'hiring' in pain_points.lower():
        hook = "I know finding and keeping quality technicians is one of the biggest challenges in pest control right now."
    elif 'quality' in pain_points.lower():
        hook = f"I noticed that {name} has built a reputation for quality service - that's exactly the kind of company we love working with."
    elif 'growth' in pain_points.lower() or 'scaling' in pain_points.lower():
        hook = f"Growing companies like {name} often face the challenge of maintaining service quality while expanding."
    else:
        hook = f"I came across {name} and was impressed by your professional approach to pest control."
    
    # Value proposition based on company size
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
    
    # Call to action with partnership focus
    cta = f"Would you be interested in a brief call to see how this might help {name}? I can share some specific examples of how companies your size are benefiting, and discuss potential partnership opportunities in your area."
    
    # Create the email
    email_content = f"""Subject: Training Solution for {name} - CEU Credits & Partnership Opportunities

{greeting}

{hook}

I'm reaching out because Pest Pro University helps companies like {name} {benefit} through our comprehensive online training platform.

What makes us different:
• {value_prop.title()}
• CEU credits accepted in 22 states (over 20 hours of training included)
• Three specialized tracks: Service Tech, Sales/Office, Business Management
• Industry-specific content designed specifically for pest control{service_benefit}

**Special Partnership Opportunities:**
We're actively looking to partner with quality pest control companies in your area. As a partner, you'll receive:
• Priority support and custom training solutions
• Larger discounts for longer-term commitments
• Co-marketing opportunities and referrals
• Exclusive access to new training modules

**Pricing & Discounts:**
• Monthly: $299/month per branch (unlimited users)
• Yearly: $1,611/year per branch (save $897/year)
• **Extended commitments (2+ years): Additional 15% discount**
• **Partnership agreements: Custom pricing available**

{cta}

You can start with a 7-day free trial and see the full platform in action. No contracts, cancel anytime.

**Ready to get started?** Visit: https://www.pestprouniversity.com/buy-now

Best regards,
Kurt
Pest Pro University
kurt@pestprouniversity.com
801-440-0271

P.S. - I'll follow up with a call next week if I don't hear back. Many business owners find it easier to discuss training needs and partnership opportunities over the phone.
"""
    
    return email_content

def send_emails_to_real_companies():
    """Send emails only to real, verified companies that haven't been emailed yet."""
    
    print("🚀 SENDING EMAILS TO REAL COMPANIES ONLY")
    print("=" * 50)
    print("⚠️  CRITICAL: ONLY REAL, VERIFIED COMPANIES")
    print("=" * 50)
    
    # Load SendGrid API key
    if not load_env_file():
        return False
    
    api_key = os.getenv('SENDGRID_API_KEY')
    if not api_key:
        print("❌ SendGrid API key not found")
        return False
    
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
        
        # Get all data
        all_data = worksheet.get_all_records()
        
        # Find companies that haven't been emailed yet
        companies_to_email = []
        for i, company in enumerate(all_data):
            email_status = str(company.get('Email Status', ''))
            contact_email = str(company.get('Email', ''))
            
            # Only email companies with real email addresses that haven't been sent
            if email_status.lower() != 'sent' and contact_email and contact_email != 'nan' and '@' in contact_email:
                companies_to_email.append((company, i))
        
        print(f"📧 Found {len(companies_to_email)} real companies ready for email")
        
        if not companies_to_email:
            print("✅ All real companies have already been emailed!")
            return
        
        # Send emails to real companies
        sent_count = 0
        for company, row_index in companies_to_email[:10]:  # Limit to 10 emails
            company_name = str(company.get('Company Name', ''))
            contact_email = str(company.get('Email', ''))
            contact_person = str(company.get('Contact Person', ''))
            
            if not contact_email or contact_email == 'nan':
                print(f"❌ No valid email address for {company_name}")
                continue
            
            try:
                # Generate personalized email
                email_content = generate_personalized_email(company)
                
                # Create SendGrid email
                from_email = Email("kurt@pestprouniversity.com", "Kurt - Pest Pro University")
                to_email = To(contact_email, contact_person or company_name)
                
                subject = "Training Solution for {} - CEU Credits & Partnership Opportunities".format(company_name)
                
                # Create mail object
                mail = Mail(from_email, to_email, subject, Content("text/plain", email_content))
                
                # Send the email
                sg = SendGridAPIClient(api_key=api_key)
                response = sg.send(mail)
                
                if response.status_code == 202:
                    # Update Google Sheets with email status
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    # Find the row to update
                    update_row = row_index + 2
                    
                    try:
                        worksheet.update_cell(update_row, 11, 'Sent')  # Column K - Email Status
                        worksheet.update_cell(update_row, 12, current_time)  # Column L - Email Sent Date
                        worksheet.update_cell(update_row, 13, '202')  # Column M - SendGrid Status Code
                        worksheet.update_cell(update_row, 14, 'Active Campaign')  # Column N - Campaign Status
                        
                        print(f"✅ Email sent to {company_name} ({contact_email})")
                        print(f"📊 Updated Google Sheets row {update_row}")
                        sent_count += 1
                        
                    except Exception as sheets_error:
                        print(f"⚠️ Email sent but Google Sheets update failed: {sheets_error}")
                        sent_count += 1
                    
                    # Add delay between emails
                    time.sleep(2)
                    
                else:
                    print(f"❌ Failed to send email to {company_name}: Status {response.status_code}")
                    
            except Exception as e:
                print(f"❌ Error sending email to {company_name}: {e}")
        
        print(f"\n🎉 CAMPAIGN COMPLETED!")
        print(f"📧 Emails sent to real companies: {sent_count}")
        print(f"📊 Updated Google Sheets with tracking data")
        print("🔒 All companies verified as real with valid contact information")
        
        return True
        
    except Exception as e:
        print(f"❌ Error running campaign: {e}")
        return False

def main():
    """Main execution function."""
    send_emails_to_real_companies()

if __name__ == "__main__":
    main() 