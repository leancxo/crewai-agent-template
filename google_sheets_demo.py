#!/usr/bin/env python3
"""
Google Sheets Integration Demo for Pest Pro University

This script demonstrates how to populate the Google Sheets document with 
campaign data from our AI sales automation system.
"""

import sys
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.append(str(Path(__file__).parent))

from tools.google_sheets_tool import GoogleSheetsIntegrationTool

def demo_google_sheets_integration():
    """Demonstrate the Google Sheets integration for campaign tracking."""
    
    print("📊 GOOGLE SHEETS INTEGRATION DEMO")
    print("=" * 50)
    print()
    
    print("🔗 Your Google Sheets Document:")
    print("https://docs.google.com/spreadsheets/d/1pbi_GOxyUkLa3mzDSvu_tFWrZDtjPbij5Oa3pbs0aUw/edit")
    print()
    
    # Initialize the tool
    sheets_tool = GoogleSheetsIntegrationTool()
    
    # Demo 1: Create spreadsheet template
    print("📋 STEP 1: Creating Spreadsheet Template")
    print("-" * 40)
    
    template_result = sheets_tool._run(
        action="create_template",
        campaign_name="Phoenix AZ - Q1 2024"
    )
    print(template_result)
    
    print("\n" + "="*60)
    
    # Demo 2: Export prospect data
    print("📊 STEP 2: Exporting Prospect Data")
    print("-" * 35)
    
    export_result = sheets_tool._run(
        action="export_prospects", 
        campaign_name="Phoenix AZ - Q1 2024"
    )
    print(export_result)
    
    print("\n" + "="*60)
    
    # Demo 3: Campaign tracking instructions
    print("📈 STEP 3: Campaign Tracking Instructions")
    print("-" * 42)
    
    tracking_result = sheets_tool._run(
        action="update_status",
        campaign_name="Phoenix AZ - Q1 2024"
    )
    print(tracking_result)
    
    print("\n" + "="*60)
    print("✅ INTEGRATION COMPLETE!")
    print()
    print("🚀 NEXT STEPS:")
    print("1. Copy the column headers into row 1 of your Google Sheet")
    print("2. Copy the CSV prospect data into row 2 and below")
    print("3. Add the formulas at the bottom for automatic calculations")
    print("4. Begin your campaign and update status as you progress!")
    print()
    print("💡 PRO TIP: You can share this spreadsheet with your team")
    print("   for collaborative campaign management and real-time updates.")

if __name__ == "__main__":
    demo_google_sheets_integration() 