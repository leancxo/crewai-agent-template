#!/usr/bin/env python3

import json
import gspread
from google.oauth2.service_account import Credentials
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
                    import os
                    os.environ[key.strip()] = value.strip()
        return True
    except Exception as e:
        print(f"❌ Error loading .env file: {e}")
        return False

def get_campaign_summary():
    """Get comprehensive campaign summary from Google Sheets."""
    
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
        
        # Analyze campaign data
        total_companies = len(all_data)
        sent_emails = [c for c in all_data if c.get('Email Status', '').lower() == 'sent']
        not_sent = [c for c in all_data if c.get('Email Status', '').lower() != 'sent']
        
        high_priority = [c for c in all_data if c.get('Training Priority') == 'High']
        medium_priority = [c for c in all_data if c.get('Training Priority') == 'Medium']
        
        personal_emails = [c for c in all_data if c.get('Email') and not c['Email'].startswith('info@')]
        generic_emails = [c for c in all_data if c.get('Email') and c['Email'].startswith('info@')]
        
        # Calculate pipeline values safely
        total_pipeline = 0
        sent_pipeline = 0
        
        for c in all_data:
            try:
                value_str = str(c.get('Annual Value', 0))
                # Clean the value string
                value_str = value_str.replace('$', '').replace(',', '').replace(' ', '')
                if value_str and value_str != 'nan':
                    value = float(value_str)
                    total_pipeline += value
                    if c.get('Email Status', '').lower() == 'sent':
                        sent_pipeline += value
            except (ValueError, TypeError):
                continue
        
        return {
            'total_companies': total_companies,
            'sent_emails': len(sent_emails),
            'not_sent': len(not_sent),
            'high_priority': len(high_priority),
            'medium_priority': len(medium_priority),
            'personal_emails': len(personal_emails),
            'generic_emails': len(generic_emails),
            'total_pipeline': total_pipeline,
            'sent_pipeline': sent_pipeline,
            'all_data': all_data
        }
        
    except Exception as e:
        print(f"❌ Error getting campaign summary: {e}")
        return None

def print_campaign_summary():
    """Print comprehensive campaign summary."""
    
    print("📊 PEST PRO UNIVERSITY EMAIL CAMPAIGN SUMMARY")
    print("=" * 60)
    print(f"📅 Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}")
    print("=" * 60)
    
    summary = get_campaign_summary()
    if not summary:
        return
    
    print(f"\n🎯 CAMPAIGN OVERVIEW:")
    print(f"📧 Total Companies: {summary['total_companies']}")
    print(f"✅ Emails Sent: {summary['sent_emails']}")
    print(f"⏳ Pending: {summary['not_sent']}")
    print(f"📈 Success Rate: {(summary['sent_emails']/summary['total_companies']*100):.1f}%")
    
    print(f"\n💰 PIPELINE VALUE:")
    print(f"💵 Total Pipeline: ${summary['total_pipeline']:,.0f}")
    print(f"📧 Sent Pipeline: ${summary['sent_pipeline']:,.0f}")
    print(f"⏳ Remaining Pipeline: ${summary['total_pipeline'] - summary['sent_pipeline']:,.0f}")
    
    print(f"\n🎯 PRIORITY BREAKDOWN:")
    print(f"🔥 High Priority: {summary['high_priority']} companies")
    print(f"📈 Medium Priority: {summary['medium_priority']} companies")
    
    print(f"\n📧 EMAIL QUALITY:")
    print(f"✅ Personal Emails: {summary['personal_emails']}")
    print(f"⚠️ Generic Emails: {summary['generic_emails']}")
    print(f"📊 Personal Email Rate: {(summary['personal_emails']/summary['total_companies']*100):.1f}%")
    
    print(f"\n📋 COMPANIES BY STATUS:")
    sent_companies = [c for c in summary['all_data'] if c.get('Email Status', '').lower() == 'sent']
    if sent_companies:
        print(f"\n✅ EMAILS SENT TO:")
        for i, company in enumerate(sent_companies[:10], 1):  # Show first 10
            email = company.get('Email', 'N/A')
            sent_date = company.get('Email Sent Date', 'N/A')
            print(f"{i:2d}. {company.get('Company Name', 'N/A')} - {email} ({sent_date})")
        if len(sent_companies) > 10:
            print(f"    ... and {len(sent_companies) - 10} more")
    
    pending_companies = [c for c in summary['all_data'] if c.get('Email Status', '').lower() != 'sent']
    if pending_companies:
        print(f"\n⏳ PENDING EMAILS:")
        for i, company in enumerate(pending_companies[:10], 1):  # Show first 10
            email = company.get('Email', 'N/A')
            priority = company.get('Training Priority', 'N/A')
            print(f"{i:2d}. {company.get('Company Name', 'N/A')} - {email} ({priority})")
        if len(pending_companies) > 10:
            print(f"    ... and {len(pending_companies) - 10} more")
    
    print(f"\n🚀 NEXT STEPS:")
    print(f"1. Send emails to {summary['not_sent']} remaining companies")
    print(f"2. Follow up with phone calls to high-priority prospects")
    print(f"3. Track responses and schedule demos")
    print(f"4. Continue researching for more personal emails")
    
    print(f"\n💡 RECOMMENDATIONS:")
    if summary['personal_emails'] < summary['total_companies'] * 0.3:
        print(f"• Focus on finding more personal emails (currently {summary['personal_emails']}/{summary['total_companies']})")
    if summary['sent_emails'] < summary['total_companies'] * 0.5:
        print(f"• Continue email campaign (only {summary['sent_emails']}/{summary['total_companies']} sent)")
    if summary['high_priority'] > 0:
        print(f"• Prioritize {summary['high_priority']} high-priority companies for phone calls")
    
    print(f"\n📊 CAMPAIGN METRICS:")
    print(f"• Average Pipeline Value: ${summary['total_pipeline']/summary['total_companies']:,.0f}")
    print(f"• Email Success Rate: {(summary['sent_emails']/summary['total_companies']*100):.1f}%")
    print(f"• Personal Email Rate: {(summary['personal_emails']/summary['total_companies']*100):.1f}%")

def main():
    """Main execution function."""
    print_campaign_summary()

if __name__ == "__main__":
    main() 