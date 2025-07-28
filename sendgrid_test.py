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
                    # Handle both "export KEY=value" and "KEY=value" formats
                    if line.startswith('export '):
                        line = line[7:]  # Remove "export " prefix
                    
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()
        print("✅ .env file loaded successfully")
    except FileNotFoundError:
        print("❌ .env file not found")
        return False
    except Exception as e:
        print(f"❌ Error loading .env file: {e}")
        return False
    return True

def send_test_email():
    """Send a test email using SendGrid."""
    
    # Load API key from .env file
    if not load_env_file():
        return False
    
    # SendGrid API key from .env file
    api_key = os.getenv('SENDGRID_API_KEY')
    if not api_key:
        print("❌ Error: SENDGRID_API_KEY not found in .env file")
        print("Please add SENDGRID_API_KEY=your_api_key_here to your .env file")
        return False
    
    # Create the email
    from_email = Email("kurt@pestprouniversity.com", "Kurt - Pest Pro University")
    to_email = To("pkp121@gmail.com", "Patrick Phillips")
    
    subject = "Test Email - Pest Pro University Sales System"
    
    # HTML content
    html_content = """
    <html>
    <body>
        <h2>🎯 Pest Pro University Sales System Test</h2>
        <p>Hello Patrick,</p>
        <p>This is a test email from the Pest Pro University sales automation system.</p>
        <p><strong>System Status:</strong> ✅ SendGrid integration working</p>
        <p><strong>From:</strong> kurt@pestprouniversity.com</p>
        <p><strong>To:</strong> pkp121@gmail.com</p>
        <p><strong>Time:</strong> {}</p>
        <hr>
        <p><em>This email was sent automatically by the CrewAI sales system.</em></p>
    </body>
    </html>
    """.format(datetime.now().strftime("%B %d, %Y at %I:%M %p"))
    
    # Plain text content
    text_content = f"""
    Pest Pro University Sales System Test
    
    Hello Patrick,
    
    This is a test email from the Pest Pro University sales automation system.
    
    System Status: ✅ SendGrid integration working
    From: kurt@pestprouniversity.com
    To: pkp121@gmail.com
    Time: {datetime.now().strftime("%B %d, %Y at %I:%M %p")}
    
    This email was sent automatically by the CrewAI sales system.
    """
    
    # Create mail object
    mail = Mail(from_email, to_email, subject, Content("text/plain", text_content))
    mail.add_content(HtmlContent(html_content))
    
    try:
        # Send the email
        sg = SendGridAPIClient(api_key=api_key)
        response = sg.send(mail)
        
        print("✅ Test email sent successfully!")
        print(f"📧 From: kurt@pestprouniversity.com")
        print(f"📧 To: pkp121@gmail.com")
        print(f"📧 Subject: {subject}")
        print(f"📊 Status Code: {response.status_code}")
        print(f"📊 Headers: {response.headers}")
        
        if response.status_code == 202:
            print("🎉 Email accepted by SendGrid for delivery!")
        else:
            print(f"⚠️ Unexpected status code: {response.status_code}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

def main():
    """Main execution function."""
    
    print("🚀 SENDGRID EMAIL TEST")
    print("=" * 40)
    
    success = send_test_email()
    
    if success:
        print("\n✅ Test completed successfully!")
        print("Check pkp121@gmail.com for the test email.")
    else:
        print("\n❌ Test failed. Please check your .env file and SendGrid API key.")

if __name__ == "__main__":
    main() 