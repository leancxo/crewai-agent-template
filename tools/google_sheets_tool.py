from langchain.tools import BaseTool
from typing import Type, Dict, Any, Optional
from pydantic import BaseModel, Field
import csv
import io
import gspread
from google.oauth2.service_account import Credentials
import json
import os
from datetime import datetime

class GoogleSheetsInput(BaseModel):
    """Input for Google Sheets operations."""
    action: str = Field(description="Action to perform: add_prospect, update_prospect, get_prospects")
    company_data: Optional[Dict] = Field(description="Company data to add/update", default=None)
    row_number: Optional[int] = Field(description="Row number for updates", default=None)

class GoogleSheetsIntegrationTool(BaseTool):
    """Google Sheets integration tool for prospect tracking."""
    
    name: str = "google_sheets_integration"
    description: str = """Integrate with Google Sheets to manage prospect data. 
    Actions: add_prospect, update_prospect, get_prospects"""
    
    args_schema: Type[BaseModel] = GoogleSheetsInput
    
    def _get_sheets_client(self):
        """Get Google Sheets client with authentication."""
        try:
            # Try to load credentials from environment or file
            creds_json = os.getenv('GOOGLE_SHEETS_CREDENTIALS')
            if creds_json:
                creds_info = json.loads(creds_json)
                credentials = Credentials.from_service_account_info(creds_info)
            else:
                # Try loading from file
                credentials = Credentials.from_service_account_file('google_credentials.json')
            
            gc = gspread.authorize(credentials)
            return gc
        except Exception as e:
            print(f"Google Sheets authentication error: {e}")
            return None
    
    def _run(self, action: str, company_data: Optional[Dict] = None, row_number: Optional[int] = None) -> str:
        """Execute Google Sheets operations."""
        
        try:
            gc = self._get_sheets_client()
            if not gc:
                return "Error: Could not authenticate with Google Sheets"
            
            # Open the spreadsheet
            sheet_id = "1pbi_GOxyUkLa3mzDSvu_tFWrZDtjPbij5Oa3pbs0aUw"
            spreadsheet = gc.open_by_key(sheet_id)
            worksheet = spreadsheet.sheet1
            
            if action == "add_prospect":
                return self._add_prospect(worksheet, company_data)
            elif action == "update_prospect":
                return self._update_prospect(worksheet, company_data, row_number)
            elif action == "get_prospects":
                return self._get_prospects(worksheet)
            else:
                return f"Unknown action: {action}"
                
        except Exception as e:
            return f"Google Sheets error: {str(e)}"
    
    def _add_prospect(self, worksheet, company_data: Dict) -> str:
        """Add a new prospect to the spreadsheet."""
        
        if not company_data:
            return "Error: No company data provided"
        
        # Map company data to spreadsheet columns
        row_data = [
            company_data.get('company_name', ''),
            company_data.get('website', ''),
            company_data.get('phone', ''),
            company_data.get('email', ''),
            company_data.get('address', ''),
            company_data.get('contact_person', ''),
            company_data.get('title', ''),
            company_data.get('company_size', ''),
            company_data.get('employee_count', ''),
            company_data.get('services', ''),
            company_data.get('training_priority', ''),
            company_data.get('training_gaps', ''),
            company_data.get('deal_potential_min', ''),
            company_data.get('deal_potential_max', ''),
            company_data.get('annual_value', ''),
            company_data.get('opportunity_level', ''),
            company_data.get('pain_points', ''),
            company_data.get('campaign_angle', ''),
            company_data.get('next_action', ''),
            company_data.get('follow_up_date', ''),
            company_data.get('notes', ''),
            company_data.get('data_source', ''),
            company_data.get('verification_status', ''),
            company_data.get('last_updated', '')
        ]
        
        # Add the row
        worksheet.append_row(row_data)
        
        return f"Successfully added {company_data.get('company_name', 'Unknown')} to spreadsheet"
    
    def _update_prospect(self, worksheet, company_data: Dict, row_number: int) -> str:
        """Update an existing prospect in the spreadsheet."""
        
        if not company_data or not row_number:
            return "Error: Missing company data or row number"
        
        # Update specific cells
        for col, value in company_data.items():
            # Map column names to column numbers (simplified)
            col_map = {
                'company_name': 1, 'website': 2, 'phone': 3, 'email': 4,
                'address': 5, 'contact_person': 6, 'title': 7,
                'company_size': 8, 'employee_count': 9, 'services': 10,
                'training_priority': 11, 'training_gaps': 12,
                'deal_potential_min': 13, 'deal_potential_max': 14,
                'annual_value': 15, 'opportunity_level': 16,
                'pain_points': 17, 'campaign_angle': 18,
                'next_action': 19, 'follow_up_date': 20,
                'notes': 21, 'data_source': 22,
                'verification_status': 23, 'last_updated': 24
            }
            
            if col in col_map:
                worksheet.update_cell(row_number, col_map[col], value)
        
        return f"Successfully updated row {row_number} in spreadsheet"
    
    def _get_prospects(self, worksheet) -> str:
        """Get all prospects from the spreadsheet."""
        
        all_records = worksheet.get_all_records()
        
        if not all_records:
            return "No prospects found in spreadsheet"
        
        summary = f"Found {len(all_records)} prospects in spreadsheet:\n\n"
        
        for i, record in enumerate(all_records[:10], 1):  # Show first 10
            summary += f"{i}. {record.get('Company Name', 'Unknown')}\n"
            summary += f"   Phone: {record.get('Phone', 'N/A')}\n"
            summary += f"   Priority: {record.get('Training Priority', 'N/A')}\n\n"
        
        if len(all_records) > 10:
            summary += f"... and {len(all_records) - 10} more prospects"
        
        return summary
    
    async def _arun(self, action: str, company_data: Optional[Dict] = None, row_number: Optional[int] = None) -> str:
        """Async version of the run method."""
        return self._run(action, company_data, row_number)

    def _create_campaign_template(self, campaign_name: str) -> str:
        """Create a template structure for the Google Sheets."""
        
        template = f"""
GOOGLE SHEETS TEMPLATE FOR: {campaign_name}
========================================

RECOMMENDED COLUMN STRUCTURE:

Column A: Company Name
Column B: Contact Person
Column C: Title/Role  
Column D: Phone Number
Column E: Email Address
Column F: Company Size
Column G: Location
Column H: Services Offered
Column I: Current Training Method
Column J: Pain Points
Column K: Value Proposition
Column L: Campaign Status
Column M: Email Sent Date
Column N: Email Opened
Column O: Email Responded
Column P: Phone Contact Date
Column Q: Phone Connected
Column R: Demo Scheduled
Column S: Demo Completed
Column T: Proposal Sent
Column U: Decision Status
Column V: Close Date
Column W: Revenue Potential
Column X: Actual Revenue
Column Y: Notes

SAMPLE DATA ROW:
================
ABC Pest Control | John Smith | Owner | (555) 123-4567 | john@abcpest.com | 15-25 employees | Phoenix, AZ | Residential, Commercial | In-person classes | CEU compliance costs | 60% cost savings with PPU | Email Sent | 2024-01-15 | Yes | Yes | 2024-01-16 | Yes | 2024-01-18 | 2024-01-20 | Sent | Considering | | $8,400 | | Interested in Service Tech training

STATUS VALUES:
=============
- Not Contacted
- Email Sent  
- Email Opened
- Email Responded
- Phone Attempted
- Phone Connected
- Demo Scheduled
- Demo Completed
- Proposal Sent
- Negotiating
- Closed Won
- Closed Lost
- Nurture

FORMULAS TO ADD:
===============
Email Open Rate: =COUNTIF(N:N,"Yes")/COUNTIF(M:M,"<>"&"")*100
Response Rate: =COUNTIF(O:O,"Yes")/COUNTIF(M:M,"<>"&"")*100  
Demo Rate: =COUNTIF(R:R,"<>"&"")/COUNTIF(M:M,"<>"&"")*100
Close Rate: =COUNTIF(U:U,"Closed Won")/COUNTIF(T:T,"<>"&"")*100
Total Pipeline: =SUM(W:W)
Total Revenue: =SUM(X:X)
        """
        return template
    
    def _export_prospects_data(self, campaign_name: str, data: str) -> str:
        """Export prospect data in CSV format for Google Sheets."""
        
        # Sample prospect data that would come from our research agent
        prospects_csv = f"""Company Name,Contact Person,Title,Phone,Email,Size,Location,Services,Training Method,Pain Points,Value Prop,Status
ABC Pest Control,John Smith,Owner,(555) 123-4567,john@abcpest.com,15-25 employees,Phoenix AZ,Residential/Commercial,In-person classes,CEU compliance costs,60% cost savings,Not Contacted
Metro Exterminators,Sarah Johnson,Training Manager,(555) 987-6543,sarah@metroext.com,50+ employees,Phoenix AZ,Commercial/Industrial,Mixed methods,Scaling training,Standardized online platform,Not Contacted
Green Guard Pest,Mike Rodriguez,Owner,(555) 456-7890,mike@greenguard.com,8-12 employees,Phoenix AZ,Eco-friendly,Minimal training,Standing out in market,Business management training,Not Contacted
Desert Pest Pro,Lisa Chen,Operations Manager,(555) 321-0987,lisa@desertpest.com,20-30 employees,Phoenix AZ,Full service,Vendor training,Inconsistent quality,Comprehensive platform,Not Contacted
Valley Termite,Bob Williams,Owner,(555) 654-3210,bob@valleytermite.com,12-18 employees,Phoenix AZ,Termite specialist,OJT only,No formal training,Service tech specialization,Not Contacted"""
        
        return f"""
PROSPECT DATA FOR: {campaign_name}
=================================

CSV DATA TO COPY INTO GOOGLE SHEETS:
(Copy the data below and paste into your spreadsheet starting at row 2)

{prospects_csv}

INSTRUCTIONS:
1. Open your Google Sheets document
2. Add the column headers from the template above (row 1)
3. Copy the CSV data above 
4. Paste into row 2 of your spreadsheet
5. Set up the tracking formulas at the bottom
6. Begin executing your campaign!

NEXT STEPS:
- Update "Status" column as you progress through outreach
- Add actual contact dates and response information
- Track demo bookings and close rates
- Calculate ROI and optimize approach
        """
    
    def _update_campaign_status(self, campaign_name: str, data: str) -> str:
        """Provide instructions for updating campaign status."""
        
        return f"""
CAMPAIGN STATUS UPDATE: {campaign_name}
=====================================

To update your Google Sheets with campaign progress:

1. EMAIL TRACKING:
   - Mark "Email Sent Date" when emails go out
   - Update "Email Opened" (Yes/No) based on email tracking
   - Update "Email Responded" (Yes/No) when prospects reply

2. PHONE TRACKING:
   - Log "Phone Contact Date" for each attempt
   - Mark "Phone Connected" (Yes/No) for successful connections
   - Schedule follow-up calls in calendar

3. DEMO TRACKING:
   - Add "Demo Scheduled" date when prospects book
   - Update "Demo Completed" after presentations
   - Note key discussion points in "Notes" column

4. PROPOSAL TRACKING:
   - Mark "Proposal Sent" date when quotes delivered
   - Update "Decision Status" as prospects progress
   - Record "Close Date" and "Actual Revenue" for wins

5. AUTOMATED CALCULATIONS:
   Your spreadsheet will automatically calculate:
   - Email open rates and response rates
   - Demo booking percentages
   - Close rates and pipeline value
   - Total revenue and ROI

RECOMMENDED UPDATE FREQUENCY:
- Daily: Email and phone activity
- Weekly: Demo scheduling and completion
- Monthly: Revenue and pipeline analysis

This tracking will help optimize future campaigns!
        """ 