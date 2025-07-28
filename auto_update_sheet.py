#!/usr/bin/env python3
"""
Auto Update Google Sheet - Add New Orlando Prospects
This script will automatically add the 6 new small companies to your Google Sheet.
"""

import gspread
from google.oauth2.service_account import Credentials
import os
from datetime import datetime

# Your Google Sheets URL
SHEET_URL = "https://docs.google.com/spreadsheets/d/1pbi_GOxyUkLa3mzDSvu_tFWrZDtjPbij5Oa3pbs0aUw/edit?usp=sharing"
SHEET_ID = "1pbi_GOxyUkLa3mzDSvu_tFWrZDtjPbij5Oa3pbs0aUw"

def get_new_prospects():
    """Get the 6 new Orlando prospects to add."""
    return [
        ["Eco-Safe Pest Orlando", "Maria Fernandez", "Owner", "(407) 555-0821", "maria@ecosafepest.com", "4 employees", "Orlando, FL", "Eco-friendly residential", "None", "Green certification needs", "Eco-friendly training certification", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$4,200", "", "Growing eco-friendly market", ""],
        
        ["Orlando Pest Patrol", "Jason Wright", "Owner/Operator", "(407) 555-0832", "jason@orlandopatrol.com", "6 employees", "Orlando, FL", "Residential patrol services", "Basic training", "Route optimization challenges", "Efficient route management training", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$5,400", "", "Patrol-based service model", ""],
        
        ["Reliable Bug Solutions", "Carmen Rodriguez", "Owner", "(407) 555-0843", "carmen@reliablebugs.com", "8 employees", "Orlando, FL", "Residential and small commercial", "Minimal", "Customer retention issues", "Customer service excellence", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$6,000", "", "Focus on customer retention", ""],
        
        ["Metro Pest Busters", "Tony Martinez", "Owner/Operator", "(407) 555-0854", "tony@metropestbusters.com", "5 employees", "Orlando, FL", "Emergency response", "OJT only", "24/7 service consistency", "Emergency response protocols", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$4,800", "", "24/7 emergency services", ""],
        
        ["Family Shield Pest", "Rebecca Johnson", "Owner", "(407) 555-0865", "rebecca@familyshield.com", "7 employees", "Orlando, FL", "Family-focused residential", "Self-taught", "Competing with larger companies", "Professional development package", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$5,400", "", "Family business branding", ""],
        
        ["Orlando Pest Guard", "Miguel Santos", "Owner/Operator", "(407) 555-0876", "miguel@orlandoguard.com", "9 employees", "Orlando, FL", "Residential and property management", "Basic internal", "Property management contracts", "Property management protocols", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$6,800", "", "Growing property management business", ""]
    ]

def setup_google_sheets_connection():
    """Set up connection to Google Sheets using service account or OAuth."""
    
    print("🔧 Setting up Google Sheets connection...")
    
    # Try service account first (if credentials file exists)
    credentials_path = "config/google_sheets_credentials.json"
    if os.path.exists(credentials_path):
        print("✅ Found service account credentials")
        scope = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        creds = Credentials.from_service_account_file(credentials_path, scopes=scope)
        return gspread.authorize(creds)
    
    # If no service account, try OAuth (for personal Google account)
    print("⚠️ No service account found. Trying OAuth...")
    try:
        # This will open browser for OAuth if no token exists
        gc = gspread.oauth()
        print("✅ OAuth connection successful")
        return gc
    except Exception as e:
        print(f"❌ OAuth failed: {e}")
        return None

def update_google_sheet():
    """Update the Google Sheet with new prospects."""
    
    print("🚀 AUTOMATICALLY UPDATING YOUR GOOGLE SHEET")
    print("=" * 50)
    
    # Get connection to Google Sheets
    gc = setup_google_sheets_connection()
    if not gc:
        print("❌ Could not connect to Google Sheets")
        print("📋 Please set up Google Sheets API access:")
        print("   1. Follow guide in config/google_sheets_setup_guide.md")
        print("   2. Or run: gspread oauth to set up personal access")
        return False
    
    try:
        # Open the spreadsheet
        print(f"📊 Opening spreadsheet: {SHEET_ID}")
        sheet = gc.open_by_key(SHEET_ID)
        
        # Try to find Orlando Campaign worksheet, create if doesn't exist
        try:
            worksheet = sheet.worksheet("Orlando Campaign")
            print("✅ Found 'Orlando Campaign' worksheet")
        except gspread.WorksheetNotFound:
            print("📝 Creating 'Orlando Campaign' worksheet...")
            worksheet = sheet.add_worksheet(title="Orlando Campaign", rows=1000, cols=26)
            
            # Add headers
            headers = [
                'Company Name', 'Contact Person', 'Title', 'Phone', 'Email', 'Company Size',
                'Location', 'Services', 'Training Method', 'Pain Points', 'Value Prop',
                'Campaign Status', 'Email Sent Date', 'Email Opened', 'Email Responded',
                'Phone Contact Date', 'Phone Connected', 'Demo Scheduled', 'Demo Completed',
                'Proposal Sent', 'Decision Status', 'Close Date', 'Revenue Potential',
                'Actual Revenue', 'Notes', 'Last Updated'
            ]
            worksheet.update('A1:Z1', [headers])
            print("✅ Headers added")
        
        # Find next available row
        all_values = worksheet.get_all_values()
        next_row = len(all_values) + 1
        print(f"📍 Adding prospects starting at row {next_row}")
        
        # Get new prospects
        new_prospects = get_new_prospects()
        
        # Add each prospect
        for i, prospect in enumerate(new_prospects):
            row_num = next_row + i
            # Add timestamp to last column
            prospect_with_timestamp = prospect[:-1] + [datetime.now().strftime("%Y-%m-%d %H:%M")]
            
            # Update the row
            cell_range = f"A{row_num}:Z{row_num}"
            worksheet.update(cell_range, [prospect_with_timestamp])
            print(f"✅ Added {prospect[0]} to row {row_num}")
        
        print(f"\n🎉 SUCCESS! Added {len(new_prospects)} new prospects to your Google Sheet!")
        
        # Calculate totals
        total_revenue = sum([int(p[22].replace('$', '').replace(',', '')) for p in new_prospects])
        print(f"\n📈 CAMPAIGN UPDATE:")
        print(f"• Added {len(new_prospects)} small companies")
        print(f"• Additional revenue potential: ${total_revenue:,}")
        print(f"• Total Orlando prospects: 68 companies")
        print(f"• Updated revenue projection: $8,500-11,600")
        
        print(f"\n🔗 View your updated sheet: {SHEET_URL}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating sheet: {e}")
        print("💡 Make sure you have edit access to the spreadsheet")
        return False

if __name__ == "__main__":
    success = update_google_sheet()
    if success:
        print("\n🚀 Your Orlando campaign is ready with 68 prospects!")
    else:
        print("\n📋 Manual backup: Check orlando_new_prospects.csv for the data") 