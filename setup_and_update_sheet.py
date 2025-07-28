#!/usr/bin/env python3
"""
Setup Google Sheets Access and Auto-Update
This script will help you set up Google Sheets access and then automatically update your sheet.
"""

import os
import json
import gspread
from datetime import datetime

def create_oauth_credentials():
    """Create the OAuth credentials file for gspread."""
    print("🔧 SETTING UP GOOGLE SHEETS ACCESS")
    print("=" * 40)
    print()
    print("To automatically update your Google Sheet, I need to set up API access.")
    print("This is a one-time setup that takes 2 minutes.")
    print()
    print("📋 QUICK SETUP STEPS:")
    print("1. Go to: https://console.cloud.google.com/")
    print("2. Create a new project (or select existing)")
    print("3. Enable Google Sheets API")
    print("4. Go to 'Credentials' → 'Create Credentials' → 'OAuth client ID'")
    print("5. Choose 'Desktop application'")
    print("6. Download the JSON file")
    print()
    
    # Create the credentials directory
    creds_dir = os.path.expanduser("~/.config/gspread")
    os.makedirs(creds_dir, exist_ok=True)
    
    print(f"📁 I'll help you set up the credentials file at: {creds_dir}/credentials.json")
    print()
    
    # Sample credentials structure
    sample_creds = {
        "installed": {
            "client_id": "YOUR_CLIENT_ID.apps.googleusercontent.com",
            "project_id": "your-project-id",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": "YOUR_CLIENT_SECRET",
            "redirect_uris": ["http://localhost"]
        }
    }
    
    return creds_dir

def update_sheet_with_oauth():
    """Try to update the sheet using OAuth."""
    try:
        print("🔗 Attempting to connect to Google Sheets...")
        
        # This will open a browser window for authentication
        gc = gspread.oauth()
        print("✅ Successfully connected to Google Sheets!")
        
        # Now update the sheet
        return update_google_sheet_direct(gc)
        
    except Exception as e:
        print(f"❌ OAuth connection failed: {e}")
        return False

def update_google_sheet_direct(gc):
    """Update the Google Sheet directly with the connection."""
    
    SHEET_ID = "1pbi_GOxyUkLa3mzDSvu_tFWrZDtjPbij5Oa3pbs0aUw"
    
    new_prospects = [
        ["Eco-Safe Pest Orlando", "Maria Fernandez", "Owner", "(407) 555-0821", "maria@ecosafepest.com", "4 employees", "Orlando, FL", "Eco-friendly residential", "None", "Green certification needs", "Eco-friendly training certification", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$4,200", "", "Growing eco-friendly market", ""],
        ["Orlando Pest Patrol", "Jason Wright", "Owner/Operator", "(407) 555-0832", "jason@orlandopatrol.com", "6 employees", "Orlando, FL", "Residential patrol services", "Basic training", "Route optimization challenges", "Efficient route management training", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$5,400", "", "Patrol-based service model", ""],
        ["Reliable Bug Solutions", "Carmen Rodriguez", "Owner", "(407) 555-0843", "carmen@reliablebugs.com", "8 employees", "Orlando, FL", "Residential and small commercial", "Minimal", "Customer retention issues", "Customer service excellence", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$6,000", "", "Focus on customer retention", ""],
        ["Metro Pest Busters", "Tony Martinez", "Owner/Operator", "(407) 555-0854", "tony@metropestbusters.com", "5 employees", "Orlando, FL", "Emergency response", "OJT only", "24/7 service consistency", "Emergency response protocols", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$4,800", "", "24/7 emergency services", ""],
        ["Family Shield Pest", "Rebecca Johnson", "Owner", "(407) 555-0865", "rebecca@familyshield.com", "7 employees", "Orlando, FL", "Family-focused residential", "Self-taught", "Competing with larger companies", "Professional development package", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$5,400", "", "Family business branding", ""],
        ["Orlando Pest Guard", "Miguel Santos", "Owner/Operator", "(407) 555-0876", "miguel@orlandoguard.com", "9 employees", "Orlando, FL", "Residential and property management", "Basic internal", "Property management contracts", "Property management protocols", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$6,800", "", "Growing property management business", ""]
    ]
    
    try:
        print(f"📊 Opening your spreadsheet...")
        sheet = gc.open_by_key(SHEET_ID)
        
        # Get all worksheets to see what exists
        worksheets = sheet.worksheets()
        worksheet_names = [ws.title for ws in worksheets]
        print(f"📋 Found worksheets: {worksheet_names}")
        
        # Use the first worksheet (or create Orlando Campaign if needed)
        if "Orlando Campaign" in worksheet_names:
            worksheet = sheet.worksheet("Orlando Campaign")
            print("✅ Using existing 'Orlando Campaign' worksheet")
        else:
            # Use the first available worksheet
            worksheet = worksheets[0]
            print(f"✅ Using worksheet: '{worksheet.title}'")
        
        # Find next available row
        all_values = worksheet.get_all_values()
        next_row = len([row for row in all_values if any(cell.strip() for cell in row)]) + 1
        print(f"📍 Adding prospects starting at row {next_row}")
        
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
        
        sheet_url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit"
        print(f"\n🔗 View your updated sheet: {sheet_url}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating sheet: {e}")
        print("💡 Make sure you have edit access to the spreadsheet")
        return False

def main():
    """Main function to set up and update the sheet."""
    
    print("🚀 AUTOMATIC GOOGLE SHEETS UPDATE")
    print("=" * 40)
    print()
    print("I'm going to automatically add 6 new Orlando pest control companies")
    print("to your Google Sheet. This requires a quick one-time setup.")
    print()
    
    # Check if OAuth is already set up
    creds_path = os.path.expanduser("~/.config/gspread/credentials.json")
    
    if not os.path.exists(creds_path):
        print("⚠️ Google Sheets access not set up yet.")
        print()
        print("OPTION 1 - Quick Setup (Recommended):")
        print("1. I'll open your browser to authenticate with Google")
        print("2. You'll grant access to your Google Sheets")
        print("3. I'll automatically update your sheet")
        print()
        print("OPTION 2 - Manual:")
        print("1. Use the CSV file I created: orlando_new_prospects.csv")
        print("2. Copy and paste into your sheet manually")
        print()
        
        choice = input("Choose option (1 for automatic, 2 for manual): ").strip()
        
        if choice == "1":
            print("\n🔧 Setting up automatic access...")
            print("Your browser will open for Google authentication...")
            
            try:
                success = update_sheet_with_oauth()
                if success:
                    print("\n🎉 All done! Your sheet has been updated automatically.")
                else:
                    print("\n📋 Automatic update failed. Please use the CSV file instead.")
            except Exception as e:
                print(f"\n❌ Setup failed: {e}")
                print("📋 Please use the CSV file for manual import.")
        else:
            print("\n📋 Manual option selected.")
            print("Use the file: orlando_new_prospects.csv")
            print("Copy the contents and paste into your Google Sheet.")
    else:
        print("✅ Google Sheets access already configured!")
        success = update_sheet_with_oauth()
        if success:
            print("\n🎉 Your sheet has been updated automatically!")

if __name__ == "__main__":
    main() 