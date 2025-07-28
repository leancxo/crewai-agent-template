# Web Scraping Best Practices Guide

## Overview
This guide outlines the web scraping best practices implemented in the Pest Pro University sales automation system. Our approach prioritizes **REAL DATA ONLY** - no fake or simulated information.

## Core Principles

### 1. Real Data Only
- **NO FAKE COMPANIES**: Every company must be real and verifiable
- **NO SIMULATED DATA**: All information comes from actual websites
- **NO GENERATED CONTACTS**: Only use real contact information found online
- **VERIFICATION REQUIRED**: Each company must have a working website and contact details

### 2. Ethical Web Scraping
- **Respect robots.txt**: Check and follow website scraping policies
- **Rate Limiting**: 1-3 second delays between requests
- **Proper User Agents**: Use realistic browser headers
- **Timeout Handling**: 10-second timeouts to avoid hanging
- **Error Recovery**: Graceful handling of failed requests

### 3. Multi-Source Verification
- **Google Search Results**: Primary source for company discovery
- **Yellow Pages**: Business directory verification
- **Yelp**: Customer review and business info validation
- **Company Websites**: Direct source for detailed analysis

## Implementation Details

### Web Scraping Tool (`tools/web_scraping_tool.py`)

```python
# Key Features:
- Multiple search sources (Google, Yellow Pages, Yelp)
- Realistic browser headers to avoid blocking
- Random delays between requests (0.5-2 seconds)
- Comprehensive error handling
- Data validation and verification
- Pest control business identification
```

### Company Analysis Tool (`tools/company_analysis_tool.py`)

```python
# Analysis Capabilities:
- Company size assessment based on website indicators
- Services analysis from actual website content
- Decision maker identification from team pages
- Training needs assessment using content analysis
- Deal potential calculation using industry standards
- Contact information extraction with validation
```

## Three-Agent Workflow

### Agent 1: Pest Control Market Researcher
**Role**: Find real companies using web scraping
- **Tools**: WebScrapingTool
- **Sources**: Google, Yellow Pages, Yelp
- **Output**: Verified company list with contact details
- **Validation**: Each company must have working website

### Agent 2: Sales Opportunity Analyst  
**Role**: Analyze real companies for training opportunities
- **Tools**: CompanyAnalysisTool
- **Input**: Real company websites from Agent 1
- **Analysis**: Size, services, training needs, decision makers
- **Output**: Detailed business intelligence reports

### Agent 3: Sales Campaign Strategist
**Role**: Create personalized campaigns using real data
- **Tools**: GoogleSheetsIntegrationTool
- **Input**: Real analysis data from Agent 2
- **Output**: Personalized email sequences, phone scripts, LinkedIn messages
- **Approach**: Reference specific company details found during research

## Technical Best Practices

### Request Headers
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}
```

### Rate Limiting
```python
import time
import random

# Random delay between requests
time.sleep(random.uniform(0.5, 2.0))

# Longer delays for detailed analysis
time.sleep(random.uniform(1, 3))
```

### Error Handling
```python
try:
    response = session.get(url, timeout=10)
    response.raise_for_status()
    return response
except requests.RequestException as e:
    print(f"Request failed for {url}: {str(e)}")
    return None
```

## Data Validation

### Company Verification
- ✅ Working website URL
- ✅ Valid phone number format
- ✅ Physical address mentioned
- ✅ Pest control keywords in content
- ✅ Professional website structure

### Information Quality Checks
- **Name**: Extract from title tag or main heading
- **Phone**: Validate using regex patterns
- **Email**: Check format and domain
- **Address**: Look for street address patterns
- **Services**: Identify from website content

## Search Sources

### 1. Google Search
- **URL Pattern**: `https://www.google.com/search?q=pest+control+{location}`
- **Extraction**: Business listings from search results
- **Validation**: Filter for pest control companies only

### 2. Yellow Pages
- **URL Pattern**: `https://www.yellowpages.com/{location}/pest-control`
- **Extraction**: Business directory listings
- **Data**: Name, phone, address, website

### 3. Yelp
- **URL Pattern**: `https://www.yelp.com/search?find_desc=pest+control&find_loc={location}`
- **Extraction**: Business profiles and reviews
- **Validation**: Verify active business status

## Output Quality Standards

### Company Research Output
```
✅ REAL COMPANIES FOUND - Google Search: pest control Orlando FL
================================================================

1. ABC Pest Control
   Website: https://abcpestcontrol.com
   Phone: (407) 555-0123
   Address: 123 Main St, Orlando, FL 32801
   Services: Residential, Commercial, Termite
   Source: Google Search

Total verified companies found: 10
All data sourced from real websites and directories.
```

### Analysis Report Output
```
📊 COMPANY OVERVIEW:
Name: ABC Pest Control
Location: Orlando, FL
Website: https://abcpestcontrol.com
Years in Business: 15
Licensed: Yes
Insured: Yes

📏 SIZE ASSESSMENT:
Estimated Size: Medium (10-20 employees)
Size Confidence Score: 6/10

🎓 TRAINING ASSESSMENT:
Training Priority: High
Training Gaps Identified:
  • No formal training program mentioned
  • Hiring challenges indicate training needs

💰 SALES OPPORTUNITY:
Opportunity Level: High
Deal Potential: $11,200 - $16,800
```

## Legal and Ethical Considerations

### Compliance
- **Public Information Only**: Only scrape publicly available data
- **No Personal Data**: Avoid scraping personal/private information  
- **Respect Terms of Service**: Follow website usage policies
- **Rate Limiting**: Avoid overwhelming servers

### Data Usage
- **Business Purpose**: Use data only for legitimate business outreach
- **Accuracy**: Verify information before using in campaigns
- **Respect**: Honor opt-out requests and privacy preferences
- **Professional**: Maintain professional standards in all communications

## Troubleshooting

### Common Issues
1. **Blocked Requests**: Rotate user agents, increase delays
2. **Empty Results**: Check website structure changes
3. **Timeout Errors**: Increase timeout values, check connectivity
4. **Invalid Data**: Improve validation regex patterns

### Debug Mode
```python
# Enable verbose logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Test individual components
tool = WebScrapingTool()
result = tool._run("pest control", "Orlando FL", 5, "google")
print(result)
```

## Best Practice Checklist

### Before Running
- [ ] Internet connectivity verified
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Rate limiting configured
- [ ] Error handling implemented
- [ ] Validation rules defined

### During Execution
- [ ] Monitor request timing
- [ ] Check data quality
- [ ] Verify company authenticity
- [ ] Handle errors gracefully
- [ ] Log important events

### After Completion
- [ ] Validate all company data
- [ ] Verify contact information
- [ ] Review analysis accuracy
- [ ] Test campaign personalization
- [ ] Document any issues

## Success Metrics

### Data Quality
- **Verification Rate**: >95% of companies have working websites
- **Contact Accuracy**: >90% of phone numbers are valid
- **Business Relevance**: >98% are actually pest control companies
- **Geographic Accuracy**: 100% located in target area

### Campaign Effectiveness
- **Personalization**: References specific company details
- **Relevance**: Addresses actual business needs
- **Professionalism**: Maintains high communication standards
- **Response Rate**: Track engagement and replies

---

## Implementation Example

```python
# Run real prospect research
from real_prospect_research import run_real_prospect_research

# Research 10 real companies in Orlando
result = run_real_prospect_research("Orlando, FL", 10)

# Output includes:
# - 10 verified pest control companies
# - Detailed analysis of each company  
# - Personalized sales campaigns
# - All data from real web scraping
```

**Remember: This system generates real revenue by finding real companies. Always prioritize data accuracy and professional ethics.** 