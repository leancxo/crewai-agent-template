# Google Sheets API Setup Guide

This guide will help you set up automatic Google Sheets integration for the Pest Pro University sales automation system.

## 🔧 Setup Steps

### 1. Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the following APIs:
   - Google Sheets API
   - Google Drive API

### 2. Create Service Account

1. Go to **IAM & Admin** > **Service Accounts**
2. Click **Create Service Account**
3. Name it: `pestpro-sheets-automation`
4. Description: `Service account for Pest Pro University sales automation`
5. Click **Create and Continue**

### 3. Generate Credentials

1. Click on the service account you just created
2. Go to **Keys** tab
3. Click **Add Key** > **Create New Key**
4. Select **JSON** format
5. Download the JSON file
6. Rename it to `google_sheets_credentials.json`
7. Place it in the `config/` folder of this project

### 4. Share Your Google Sheet

1. Open your Google Sheets document
2. Click **Share** button
3. Add the service account email (from the JSON file) as an **Editor**
4. The email looks like: `pestpro-sheets-automation@your-project.iam.gserviceaccount.com`

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Usage Examples

### Create New Campaign Sheet
```python
from tools.google_sheets_tool import GoogleSheetsIntegrationTool

tool = GoogleSheetsIntegrationTool()
result = tool._run(
    action="create_sheet",
    campaign_name="Orlando Campaign",
    sheet_url="https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit"
)
```

### Write Prospect Data
```python
csv_data = """Company Name,Contact Person,Email,Phone
ABC Pest Control,John Smith,john@abc.com,(555) 123-4567
Metro Exterminators,Sarah Johnson,sarah@metro.com,(555) 987-6543"""

result = tool._run(
    action="write_prospects",
    campaign_name="Orlando Campaign", 
    data=csv_data,
    sheet_url="https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit"
)
```

### Update Campaign Status
```python
# Update specific cells
updates = "L2:Email Sent,M2:2024-01-15,N2:Yes"

result = tool._run(
    action="update_status",
    campaign_name="Orlando Campaign",
    data=updates,
    sheet_url="https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit"
)
```

### Read Current Data
```python
result = tool._run(
    action="read_data",
    campaign_name="Orlando Campaign",
    sheet_url="https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit",
    cell_range="A1:Z100"
)
```

## 🔐 Security Notes

- Keep `google_sheets_credentials.json` secure and never commit to git
- The service account only has access to sheets you explicitly share with it
- You can revoke access anytime by removing the service account from sheet sharing

## ✅ Testing Your Setup

Run this test to verify everything works:

```python
from tools.google_sheets_tool import GoogleSheetsIntegrationTool

tool = GoogleSheetsIntegrationTool()
if tool._initialize_client():
    print("✅ Google Sheets API configured successfully!")
else:
    print("❌ Setup incomplete. Check credentials file.")
```

## 🚨 Troubleshooting

**Error: "Credentials file not found"**
- Ensure `google_sheets_credentials.json` is in the `config/` folder

**Error: "Permission denied"**  
- Make sure you shared the sheet with the service account email

**Error: "API not enabled"**
- Enable Google Sheets API and Google Drive API in Cloud Console

**Error: "Worksheet not found"**
- The tool will create new worksheets automatically if they don't exist

## 📊 Your Sheet Structure

The tool will automatically create these columns:
- Company Name, Contact Person, Title, Phone, Email
- Company Size, Location, Services, Training Method
- Pain Points, Value Prop, Campaign Status
- Email tracking (Sent Date, Opened, Responded)
- Phone tracking (Contact Date, Connected)
- Demo tracking (Scheduled, Completed)
- Sales tracking (Proposal Sent, Decision Status, Close Date)
- Revenue tracking (Potential, Actual)
- Notes, Last Updated

This gives you complete visibility into your sales pipeline! 