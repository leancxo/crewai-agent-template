#!/usr/bin/env python3

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content, HtmlContent
from datetime import datetime

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

def generate_test_campaign_email():
    """Generate a test campaign email using the same personalization logic."""
    
    # Create a sample company for testing
    test_company = {
        'Company Name': 'Test Pest Control Company',
        'Contact Person': 'Patrick Phillips',
        'Company Size': 'Medium',
        'Pain Points': 'hiring, quality, growth',
        'Services': 'residential, commercial, termite',
        'Email': 'pkp121@gmail.com',
        'Phone': '(555) 123-4567',
        'Training Priority': 'High',
        'Annual Value': 15000
    }
    
    name = test_company.get('Company Name', '')
    contact_person = test_company.get('Contact Person', 'Team')
    size = test_company.get('Company Size', '')
    pain_points = test_company.get('Pain Points', '')
    services = test_company.get('Services', '')
    email = test_company.get('Email', '')
    phone = test_company.get('Phone', '')
    
    # Personalize greeting
    greeting = "Hi Patrick,"
    
    # Create pain point hook
    if 'hiring' in pain_points.lower():
        hook = "I know finding and keeping quality technicians is one of the biggest challenges in pest control right now."
    elif 'quality' in pain_points.lower():
        hook = f"I noticed that {name} has built a reputation for quality service - that's exactly the kind of company we love working with."
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
    
    # Create the email with updated content
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

---
TEST EMAIL - This is a test of the automated campaign system
Company: {name}
Contact: {contact_person}
Priority: {test_company.get('Training Priority')}
Pipeline Value: ${test_company.get('Annual Value'):,.0f}
"""
    
    return email_content

def send_test_campaign_email():
    """Send a test campaign email to pkp121@gmail.com."""
    
    print("🚀 TEST CAMPAIGN EMAIL")
    print("=" * 40)
    
    # Load SendGrid API key
    if not load_env_file():
        return False
    
    api_key = os.getenv('SENDGRID_API_KEY')
    if not api_key:
        print("❌ SendGrid API key not found")
        return False
    
    try:
        # Generate personalized email
        email_content = generate_test_campaign_email()
        
        # Create SendGrid email
        from_email = Email("kurt@pestprouniversity.com", "Kurt - Pest Pro University")
        to_email = To("pkp121@gmail.com", "Patrick Phillips")
        
        subject = "Training Solution for Test Pest Control Company - CEU Credits & Partnership Opportunities"
        
        # Create mail object
        mail = Mail(from_email, to_email, subject, Content("text/plain", email_content))
        
        # Send the email
        sg = SendGridAPIClient(api_key=api_key)
        response = sg.send(mail)
        
        if response.status_code == 202:
            print("✅ Test campaign email sent successfully!")
            print(f"📧 From: kurt@pestprouniversity.com")
            print(f"📧 To: pkp121@gmail.com")
            print(f"📧 Subject: {subject}")
            print(f"📊 Status Code: {response.status_code}")
            print(f"📊 Message ID: {response.headers.get('X-Message-Id', 'N/A')}")
            print(f"⏰ Sent at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            print("\n🎯 This email demonstrates:")
            print("• Personalized greeting and content")
            print("• Pain point-based messaging")
            print("• Company size-specific value propositions")
            print("• Service-specific benefits")
            print("• Clear call to action")
            print("• Professional signature")
            
            return True
        else:
            print(f"❌ Failed to send email: Status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error sending test email: {e}")
        return False

def main():
    """Main execution function."""
    
    success = send_test_campaign_email()
    
    if success:
        print("\n✅ Test completed successfully!")
        print("Check pkp121@gmail.com for the campaign-style test email.")
        print("\n🚀 Ready to run the full automated campaign!")
    else:
        print("\n❌ Test failed. Please check your SendGrid API key.")

if __name__ == "__main__":
    main() 