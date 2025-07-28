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

def reset_and_fix_sheet():
    """Reset incorrect email status and properly mark only companies we actually emailed."""
    
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
        
        print("🔄 RESETTING AND FIXING EMAIL STATUS")
        print("=" * 50)
        
        # First, reset all companies to "Not Sent"
        print("📋 Resetting all companies to 'Not Sent'...")
        for i, company in enumerate(all_data):
            row_index = i + 2
            try:
                worksheet.update_cell(row_index, 11, 'Not Sent')  # Column K - Email Status
                worksheet.update_cell(row_index, 12, '')  # Column L - Email Sent Date
                worksheet.update_cell(row_index, 13, '')  # Column M - SendGrid Status Code
                worksheet.update_cell(row_index, 14, '')  # Column N - Campaign Status
            except Exception as e:
                print(f"❌ Error resetting row {row_index}: {e}")
        
        print("✅ All companies reset to 'Not Sent'")
        
        # Now mark only the companies we actually emailed
        actually_emailed_companies = [
            "Turner Pest Control",
            "Gato Guard Services", 
            "AAA Plus Exterminating Inc",
            "Rick Ricker Termite & Pest Control Inc",
            "Rowland Pest Management Inc",
            "ProForce Pest Control Orlando",
            "ASAP Pest Solutions Inc",
            "Nozzle Nolen Orlando",
            "Bulwark Exterminating Orlando",
            "Cimex Solutions Central Florida",
            "Truly Nolen Pest Control",
            "Lewis Cobb Pest Control",
            "Byrne Termite & Pest Control LLC",
            "Forex Pest Detection and Elimination",
            "Ladybug Pest and Lawn Inc",
            "Creature Control Orlando",
            "Meryl's Termite & Pest Control",
            "Organa Pest Control LLC",
            "JT Wildlife Removal",
            "WildGuard Solutions Orlando",
            "Proteck Wildlife Solutions",
            "Freedom Pest Inc"
        ]
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        marked_count = 0
        
        print(f"\n📧 Marking companies we actually emailed...")
        
        # Update each row for companies we actually emailed
        for i, company in enumerate(all_data):
            company_name = company.get('Company Name', '')
            
            if company_name in actually_emailed_companies:
                row_index = i + 2
                
                try:
                    worksheet.update_cell(row_index, 11, 'Sent')  # Column K - Email Status
                    worksheet.update_cell(row_index, 12, current_time)  # Column L - Email Sent Date
                    worksheet.update_cell(row_index, 13, '202')  # Column M - SendGrid Status Code
                    worksheet.update_cell(row_index, 14, 'Active Campaign')  # Column N - Campaign Status
                    
                    print(f"✅ Marked as sent: {company_name}")
                    marked_count += 1
                    
                except Exception as e:
                    print(f"❌ Error marking {company_name}: {e}")
        
        print(f"\n🎉 SHEET FIX COMPLETED:")
        print(f"📧 Companies marked as sent: {marked_count}")
        print(f"⏰ Timestamp: {current_time}")
        
        # Show final summary
        all_data_updated = worksheet.get_all_records()
        sent_count = len([c for c in all_data_updated if c.get('Email Status', '').lower() == 'sent'])
        total_count = len(all_data_updated)
        
        print(f"\n📊 FINAL SUMMARY:")
        print(f"📧 Total Companies: {total_count}")
        print(f"✅ Emails Sent: {sent_count}")
        print(f"⏳ Pending: {total_count - sent_count}")
        print(f"📈 Success Rate: {(sent_count/total_count*100):.1f}%")
        
    except Exception as e:
        print(f"❌ Error fixing sheet: {e}")

def main():
    """Main execution function."""
    reset_and_fix_sheet()

if __name__ == "__main__":
    main() 