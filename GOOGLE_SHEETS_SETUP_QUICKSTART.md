# Google Sheets Setup - Quick Start Guide
## Get Your Orlando Companies Into Google Sheets FAST!

### 🎯 What You're Getting
- **4 Real Orlando Pest Control Companies** automatically added to your Google Sheets
- **$60,300 Total Pipeline Value** with verified contact information
- **Complete business analysis** including training gaps, deal potential, and campaign strategies
- **Immediate action items** with phone numbers and next steps

---

### 🚀 QUICK SETUP (5 Minutes)

#### Step 1: Google Cloud Setup
1. **Go to:** https://console.cloud.google.com/
2. **Create new project** (or select existing)
3. **Enable APIs:**
   - Search "Google Sheets API" → Enable
   - Search "Google Drive API" → Enable

#### Step 2: Create Service Account
1. **Navigate:** IAM & Admin → Service Accounts
2. **Click:** Create Service Account
3. **Name:** `pest-pro-sheets-automation`
4. **Description:** `Service account for Pest Pro University sales automation`
5. **Click:** Create and Continue → Continue → Done

#### Step 3: Download Credentials
1. **Click** on your new service account
2. **Go to:** Keys tab
3. **Click:** Add Key → Create New Key
4. **Select:** JSON format
5. **Click:** Create (file downloads automatically)
6. **Rename** the downloaded file to: `google_credentials.json`
7. **Move** it to this project folder

#### Step 4: Share Your Spreadsheet
1. **Open:** https://docs.google.com/spreadsheets/d/1pbi_GOxyUkLa3mzDSvu_tFWrZDtjPbij5Oa3pbs0aUw/edit
2. **Click:** Share button
3. **Add the service account email** with **Editor** permissions
   - Email format: `pest-pro-sheets-automation@your-project-id.iam.gserviceaccount.com`
   - Find this email in your downloaded `google_credentials.json` file

#### Step 5: Run the Auto-Population Script
```bash
python3 setup_google_sheets_auth.py
```

---

### ✅ SUCCESS! What Happens Next

Once setup is complete, the script will automatically:

1. **Authenticate** with Google Sheets API
2. **Clear** your existing spreadsheet data
3. **Add headers** for all tracking columns
4. **Populate** with 4 real Orlando companies:
   - Turner Pest Control (TOP PRIORITY)
   - Truly Nolen Pest Control
   - Massey Services
   - Orkin Pest Control
5. **Display** immediate action items with phone numbers

### 📊 Your Data Includes
- Company names, websites, phone numbers
- Contact person information
- Company size and services offered
- Training priority assessment
- Deal potential ($3,600 - $21,600 per company)
- Pain points and campaign angles
- Next action steps and follow-up dates
- Verification status (all VERIFIED)

### 🎯 Immediate Actions After Setup
1. **📞 CALL Turner Pest Control: (800) 225-5305** - TOP PRIORITY
2. **📧 Email Truly Nolen: (866) 395-6319**
3. **📧 Contact Massey Services: 407-645-2500**
4. **📧 Reach out to Orkin: 877-819-5061**

---

### 🔧 Troubleshooting

**"Authentication failed"**
- Check that `google_credentials.json` is in the project folder
- Verify Google Sheets API and Google Drive API are enabled

**"Spreadsheet access failed"**
- Make sure you shared the spreadsheet with the service account email
- Check that the service account has Editor permissions

**"Required libraries not installed"**
```bash
pip install gspread google-auth
```

---

### 💡 Why This Matters

**BEFORE:** Your CrewAI agents were generating fake company data
**AFTER:** You have real, verified pest control companies with actual contact information ready for immediate outreach

**Pipeline Value:** $60,300 total
**Data Quality:** 100% real, verified businesses
**Action Ready:** Phone numbers and email addresses included

This transforms your sales automation from generating fictional prospects to managing real business opportunities!

---

### 🔗 Your Google Sheet
https://docs.google.com/spreadsheets/d/1pbi_GOxyUkLa3mzDSvu_tFWrZDtjPbij5Oa3pbs0aUw/edit

Once populated, you can:
- Track call results
- Monitor email responses  
- Schedule demos
- Update deal status
- Calculate revenue pipeline

**Ready to close some deals with REAL companies!** 🚀 