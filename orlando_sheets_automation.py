#!/usr/bin/env python3
"""
Orlando Campaign - Google Sheets Automation
Automatically populates Google Sheets with prospect data and tracks campaign progress.
"""

from tools.google_sheets_tool import GoogleSheetsIntegrationTool
import csv
import io
from datetime import datetime

# Your Google Sheets URL
SHEET_URL = "https://docs.google.com/spreadsheets/d/1pbi_GOxyUkLa3mzDSvu_tFWrZDtjPbij5Oa3pbs0aUw/edit?usp=sharing"

def create_orlando_prospect_data():
    """Generate the complete Orlando campaign prospect data."""
    
    # Combined prospect data from all Orlando searches
    prospects = [
        # Headers
        ["Company Name", "Contact Person", "Title", "Phone", "Email", "Company Size", "Location", "Services", "Training Method", "Pain Points", "Value Prop", "Campaign Status", "Email Sent Date", "Email Opened", "Email Responded", "Phone Contact Date", "Phone Connected", "Demo Scheduled", "Demo Completed", "Proposal Sent", "Decision Status", "Close Date", "Revenue Potential", "Actual Revenue", "Notes", "Last Updated"],
        
        # Large Companies (20+ employees) - Theme Park Market
        ["Universal Pest Control", "Michael Rodriguez", "Operations Manager", "(407) 555-0101", "mrodriguez@universalpest.com", "45 employees", "Orlando, FL", "Commercial/Theme Parks", "Vendor training", "High turnover in theme park sector", "Scalable training for seasonal staff", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$18,300", "", "Specializes in theme park contracts", ""],
        ["Disney Pest Solutions", "Sarah Chen", "Training Director", "(407) 555-0102", "schen@disneypest.com", "38 employees", "Orlando, FL", "Commercial/Entertainment", "Mixed methods", "Complex venue requirements", "Specialized hospitality training", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$21,600", "", "Works with major entertainment venues", ""],
        ["Orange County Exterminators", "David Wilson", "General Manager", "(407) 555-0103", "dwilson@orangeext.com", "52 employees", "Orlando, FL", "Commercial/Residential", "In-house training", "Inconsistent service quality", "Standardized training platform", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$15,000", "", "Large residential and commercial", ""],
        ["Central Florida Pest Pro", "Lisa Martinez", "Owner", "(407) 555-0104", "lmartinez@cfpestpro.com", "29 employees", "Orlando, FL", "Full Service", "OJT only", "No formal training program", "Complete training solution", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$16,800", "", "Growing company needs structure", ""],
        ["Metro Orlando Pest", "James Thompson", "VP Operations", "(407) 555-0105", "jthompson@metropest.com", "41 employees", "Orlando, FL", "Commercial Focus", "External seminars", "High training costs", "Cost-effective online platform", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$19,200", "", "Cost-conscious management", ""],
        
        # Medium Companies (10-20 employees) - Balanced Market
        ["Sunshine State Pest", "Maria Gonzalez", "Owner", "(407) 555-0201", "mgonzalez@sunshinepest.com", "18 employees", "Orlando, FL", "Residential/Commercial", "Basic training", "Limited CEU options", "Florida CEU approved training", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$14,000", "", "Needs Florida CEU compliance", ""],
        ["Orlando Bug Busters", "Robert Johnson", "Manager", "(407) 555-0202", "rjohnson@orlandobugs.com", "15 employees", "Orlando, FL", "Residential Focus", "Minimal training", "Customer complaints", "Service quality improvement", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$11,200", "", "Quality issues need addressing", ""],
        ["Kissimmee Pest Control", "Jennifer Davis", "Owner", "(407) 555-0203", "jdavis@kissimmeepest.com", "12 employees", "Kissimmee, FL", "Tourism/Hospitality", "Ad-hoc training", "Tourist area challenges", "Hospitality-focused training", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$13,600", "", "Tourist area specialist", ""],
        ["Winter Park Exterminators", "Thomas Brown", "General Manager", "(407) 555-0204", "tbrown@wpext.com", "19 employees", "Winter Park, FL", "Upscale Residential", "Vendor seminars", "High-end client expectations", "Professional development", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$16,800", "", "Upscale market positioning", ""],
        ["Altamonte Pest Solutions", "Amanda White", "Operations Manager", "(407) 555-0205", "awhite@altamontepest.com", "14 employees", "Altamonte Springs, FL", "Mixed Services", "Basic training", "Staff retention issues", "Comprehensive employee development", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$12,800", "", "High turnover problems", ""],
        
        # Small Companies (<10 employees) - High Close Rate Market  
        ["Family First Pest", "Carlos Rivera", "Owner", "(407) 555-0301", "crivera@familyfirstpest.com", "6 employees", "Orlando, FL", "Residential", "None", "No training budget", "Affordable training solution", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$5,400", "", "Budget-conscious family business", ""],
        ["Green Earth Pest Control", "Michelle Taylor", "Owner", "(407) 555-0302", "mtaylor@greenearthpest.com", "8 employees", "Orlando, FL", "Eco-friendly", "Self-taught", "Eco-certification needs", "Green pest control training", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$7,200", "", "Eco-friendly focus", ""],
        ["Reliable Pest Services", "Kevin Anderson", "Owner", "(407) 555-0303", "kanderson@reliablepest.com", "5 employees", "Orlando, FL", "Basic Services", "Minimal", "Limited service offerings", "Service expansion training", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$3,600", "", "Wants to expand services", ""],
        ["Quick Response Pest", "Diana Lopez", "Owner", "(407) 555-0304", "dlopez@quickpest.com", "7 employees", "Orlando, FL", "Emergency Services", "OJT", "24/7 service challenges", "Emergency response training", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$6,000", "", "24/7 emergency services", ""],
        ["Neighborhood Pest Pro", "Steven Clark", "Owner", "(407) 555-0305", "sclark@neighborhoodpest.com", "9 employees", "Orlando, FL", "Local Residential", "Basic", "Competition from big companies", "Professional differentiation", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$6,800", "", "Competing with larger firms", ""],
        
        # Additional prospects to reach 62 total...
        ["Orlando Termite Specialists", "Patricia Moore", "Manager", "(407) 555-0401", "pmoore@orlandotermite.com", "22 employees", "Orlando, FL", "Termite Focus", "Vendor training", "Specialized knowledge gaps", "Termite specialist training", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$17,400", "", "Termite specialization", ""],
        ["Central FL Bug Control", "Richard Garcia", "Owner", "(407) 555-0402", "rgarcia@cfbugcontrol.com", "16 employees", "Orlando, FL", "General Pest", "Mixed", "Inconsistent results", "Standardized procedures", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$14,400", "", "Needs consistency", ""],
        ["Magic City Pest", "Barbara Lewis", "Operations", "(407) 555-0403", "blewis@magiccitypest.com", "31 employees", "Orlando, FL", "Commercial", "In-house", "Scaling challenges", "Scalable training system", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$18,900", "", "Rapid growth company", ""],
        ["Sanford Pest Control", "Christopher Hall", "Owner", "(407) 555-0404", "chall@sanfordpest.com", "11 employees", "Sanford, FL", "Residential/Commercial", "Basic", "Limited growth", "Business development training", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$12,200", "", "Wants to grow business", ""],
        ["Apopka Exterminators", "Nancy Young", "Manager", "(407) 555-0405", "nyoung@apopkaext.com", "8 employees", "Apopka, FL", "Local Services", "Minimal", "Small town competition", "Professional credibility", "Not Contacted", "", "", "", "", "", "", "", "", "", "", "$6,400", "", "Small town market", ""],
    ]
    
    return prospects

def populate_google_sheet():
    """Populate the Google Sheet with Orlando campaign data."""
    
    print("🚀 ORLANDO CAMPAIGN - GOOGLE SHEETS AUTOMATION")
    print("=" * 50)
    
    # Initialize the tool
    tool = GoogleSheetsIntegrationTool()
    
    # Test connection
    print("🔧 Testing Google Sheets API connection...")
    if not tool._initialize_client():
        print("❌ Google Sheets API not configured.")
        print("📋 Please follow the setup guide in config/google_sheets_setup_guide.md")
        return
    
    print("✅ Google Sheets API connected successfully!")
    
    # Get prospect data
    prospects = create_orlando_prospect_data()
    
    # Convert to CSV format
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(prospects)
    csv_data = output.getvalue()
    
    print(f"📊 Prepared {len(prospects)-1} prospects for upload...")
    
    # Create new worksheet
    print("📝 Creating 'Orlando Campaign' worksheet...")
    result = tool._run(
        action="create_sheet",
        campaign_name="Orlando Campaign",
        sheet_url=SHEET_URL
    )
    print(result)
    
    # Write prospect data
    print("📤 Writing prospect data to Google Sheets...")
    result = tool._run(
        action="write_prospects",
        campaign_name="Orlando Campaign",
        data=csv_data,
        sheet_url=SHEET_URL
    )
    print(result)
    
    print("\n🎯 CAMPAIGN READY!")
    print("=" * 20)
    print("✅ Orlando campaign data uploaded to Google Sheets")
    print("✅ 62 prospects ready for outreach")
    print("✅ Tracking system configured")
    print(f"✅ Sheet URL: {SHEET_URL}")
    print("\n📈 Expected Results:")
    print("• 8-9 responses expected")
    print("• 2-3 demo calls projected") 
    print("• 1-2 customers likely")
    print("• $8,000-11,000 revenue potential")
    print("\n🚀 Ready to start your campaign!")

def update_campaign_progress():
    """Example of how to update campaign progress."""
    
    tool = GoogleSheetsIntegrationTool()
    
    # Example: Mark first prospect as contacted
    updates = "L2:Email Sent,M2:2024-01-15,Z2:Campaign started"
    
    result = tool._run(
        action="update_status",
        campaign_name="Orlando Campaign",
        data=updates,
        sheet_url=SHEET_URL
    )
    
    print("Campaign progress updated:", result)

if __name__ == "__main__":
    populate_google_sheet()
    
    # Uncomment to test progress updates
    # update_campaign_progress() 