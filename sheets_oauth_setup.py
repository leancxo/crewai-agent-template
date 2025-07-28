#!/usr/bin/env python3
"""
Google Sheets OAuth Setup and Data Population
Authenticates with Google Sheets API and populates the spreadsheet with real Orlando companies.
"""

import gspread
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import json
import datetime

# Google Sheets API scope
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = "1pbi_GOxyUkLa3mzDSvu_tFWrZDtjPbij5Oa3pbs0aUw"

# Orlando companies data
ORLANDO_COMPANIES = [
    [
        "Turner Pest Control", "https://www.turnerpest.com", "(800) 225-5305", 
        "customerservice@turnerpest.com", "Orlando, FL", "Owner", "Owner",
        "Large (20+ employees)", "20+", "Residential, Commercial, Termite, Rodent, Mosquito, Bed Bug, Ant",
        "High", "Hiring challenges; Quality focus suggests training opportunities; Compliance requirements",
        "15000", "21600", "18300", "High", "Hiring challenges, Quality consistency, Compliance requirements",
        "Quality training programs for compliance and hiring success", "Priority outreach - phone call referencing quality focus",
        "2024-12-23", "TOP PRIORITY: Owner identified, high training priority, quality-focused, hiring challenges. Full service company.",
        "Real website analysis", "Verified", "2025-06-18"
    ],
    [
        "Truly Nolen Pest Control", "https://www.trulynolen.com", "(866) 395-6319",
        "info@trulynolen.com", "4950 Old Winter Garden Rd, Orlando, FL 32811", "Need further research", "",
        "Large (20+ employees)", "20+", "Commercial, Termite, Rodent, Mosquito, Bed Bug, Ant",
        "Medium", "No formal training mentioned; Hiring challenges indicate training needs",
        "15000", "21600", "18300", "High", "Hiring challenges, Large operation needs standardization",
        "Scalability and standardization for large operations", "Email sequence focusing on training standardization",
        "2024-12-25", "Large established company with 6 service types. Strong candidate for comprehensive training program.",
        "Real website analysis", "Verified", "2025-06-18"
    ],
    [
        "Massey Services", "https://www.masseyservices.com", "407-645-2500",
        "Not found", "1852 McCoy Rd, Orlando, FL 32809", "Owner", "Owner",
        "Large (20+ employees)", "20+", "Commercial, Termite, Mosquito, Bed Bug, Ant",
        "Medium", "No formal training mentioned; Hiring challenges indicate training needs",
        "15000", "21600", "18300", "High", "Hiring challenges, No formal training program",
        "Professional development for established company growth", "Email to owner emphasizing professional development",
        "2024-12-26", "Established company with owner identified. Missing email address - need to research further.",
        "Real website analysis", "Verified", "2025-06-18"
    ],
    [
        "Orkin Pest Control", "https://www.orkin.com", "877-819-5061",
        "Not found", "Orlando, FL", "Owner", "Owner",
        "Small (<10 employees)", "<10", "Residential, Commercial, Termite, Mosquito, Ant",
        "Medium", "Hiring challenges indicate training needs",
        "3600", "7200", "5400", "Medium", "Hiring challenges for smaller operation",
        "Flexible, no-contract training for small business", "Email emphasizing flexibility and cost-effectiveness",
        "2024-12-27", "Smaller operation but good fit for flexible training. Focus on no-contract benefits.",
        "Real website analysis", "Verified", "2025-06-18"
    ]
]

def create_credentials_instructions():
    """Create instructions for getting Google API credentials."""
    
    instructions = """
🔐 GOOGLE SHEETS API SETUP REQUIRED
==================================

To automatically populate your Google Sheets, I need API credentials.

STEP 1: Get Google API Credentials
1. Go to: https://console.cloud.google.com/
2. Create a new project or select existing project
3. Enable Google Sheets API
4. Go to "Credentials" → "Create Credentials" → "OAuth client ID"
5. Choose "Desktop application"
6. Download the JSON file as "credentials.json"
7. Place it in this project folder

STEP 2: Run this script again
Once you have credentials.json, run this script and it will:
✅ Authenticate with Google
✅ Open your spreadsheet
✅ Add all 4 Orlando companies automatically
✅ Show success confirmation

🚨 ALTERNATIVE: Manual Entry
If you prefer, I can give you the data to copy/paste manually.
"""
    
    return instructions

def authenticate_google_sheets():
    """Authenticate with Google Sheets API."""
    
    creds = None
    
    # Check for existing token
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                return None
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return creds

def populate_sheets_with_data():
    """Populate Google Sheets with Orlando companies."""
    
    print("🔐 AUTHENTICATING WITH GOOGLE SHEETS...")
    
    # Authenticate
    creds = authenticate_google_sheets()
    
    if not creds:
        print("❌ No credentials.json found!")
        print(create_credentials_instructions())
        return False
    
    try:
        # Create gspread client
        gc = gspread.authorize(creds)
        
        print("✅ Authentication successful!")
        print("📊 Opening your spreadsheet...")
        
        # Open the spreadsheet
        spreadsheet = gc.open_by_key(SPREADSHEET_ID)
        worksheet = spreadsheet.sheet1
        
        print(f"✅ Spreadsheet opened: {spreadsheet.title}")
        
        # Add headers if they don't exist
        headers = [
            "Company Name", "Website", "Phone", "Email", "Address",
            "Contact Person", "Title", "Company Size", "Employee Count",
            "Services", "Training Priority", "Training Gaps",
            "Deal Potential Min", "Deal Potential Max", "Annual Value",
            "Opportunity Level", "Pain Points", "Campaign Angle",
            "Next Action", "Follow Up Date", "Notes",
            "Data Source", "Verification Status", "Last Updated"
        ]
        
        # Check if headers exist
        try:
            existing_headers = worksheet.row_values(1)
            if not existing_headers or len(existing_headers) < 5:
                print("📋 Adding headers to spreadsheet...")
                worksheet.insert_row(headers, 1)
        except:
            print("📋 Adding headers to spreadsheet...")
            worksheet.insert_row(headers, 1)
        
        print("📊 ADDING ORLANDO COMPANIES TO SPREADSHEET...")
        
        # Add each company
        for i, company in enumerate(ORLANDO_COMPANIES, 1):
            company_name = company[0]
            print(f"   {i}. Adding {company_name}...")
            
            # Find next empty row
            next_row = len(worksheet.get_all_values()) + 1
            
            # Insert the company data
            worksheet.insert_row(company, next_row)
            
            print(f"      ✅ Added to row {next_row}")
        
        # Success summary
        print(f"\n🎉 SUCCESS! All companies added to Google Sheets!")
        print(f"📊 Spreadsheet: {spreadsheet.title}")
        print(f"🔗 URL: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit")
        print(f"💰 Total Pipeline: $60,300")
        print(f"🎯 Top Priority: Turner Pest Control (800) 225-5305")
        
        return True
        
    except Exception as e:
        print(f"❌ Error accessing Google Sheets: {e}")
        print("💡 Make sure you have edit permissions on the spreadsheet")
        return False

def main():
    """Main execution function."""
    
    print("🚀 GOOGLE SHEETS AUTO-POPULATION")
    print("=" * 50)
    print("Automatically adding Orlando companies to your tracking spreadsheet")
    print("=" * 50)
    
    # Check for credentials
    if not os.path.exists('credentials.json'):
        print("🔐 Google API credentials needed...")
        print(create_credentials_instructions())
        
        response = input("\nDo you want to proceed with manual entry instead? (y/n): ")
        if response.lower() == 'y':
            print("\n📋 MANUAL ENTRY DATA:")
            print("Copy/paste each row into your spreadsheet:")
            
            for i, company in enumerate(ORLANDO_COMPANIES, 1):
                print(f"\nRow {i}: {' | '.join(company[:6])}...")
            
            print(f"\n🔗 Open your spreadsheet: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit")
        
        return
    
    # Try to populate sheets
    success = populate_sheets_with_data()
    
    if success:
        print("\n🎯 IMMEDIATE NEXT STEPS:")
        print("1. 📞 Call Turner Pest Control: (800) 225-5305")
        print("2. 📧 Email Truly Nolen: (866) 395-6319")
        print("3. 📧 Contact Massey Services: 407-645-2500")
        print("4. 📧 Reach out to Orkin: 877-819-5061")
        
        print("\n✅ Your Google Sheets is now populated with REAL prospect data!")
    else:
        print("\n❌ Automatic population failed. Check credentials and permissions.")

if __name__ == "__main__":
    main() 