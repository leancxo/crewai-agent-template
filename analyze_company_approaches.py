#!/usr/bin/env python3

import gspread
from google.oauth2.service_account import Credentials
import json
from agents.analyst_agent import create_sales_opportunity_analyst
from agents.sales_campaign_agent import create_sales_campaign_strategist
from crewai import Task, Crew

def analyze_companies_for_approaches():
    """Use our analyst and campaign agents to determine the best approach for each company."""
    
    print("🔍 ANALYZING COMPANIES FOR OPTIMAL SALES APPROACHES")
    print("=" * 60)
    
    try:
        # Load Google Sheets data
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
        print(f"📊 Found {len(all_data)} companies to analyze")
        
        # Create agents
        analyst = create_sales_opportunity_analyst()
        campaign_strategist = create_sales_campaign_strategist()
        
        print("\n🎯 ANALYZING TOP PRIORITY COMPANIES:")
        
        # Focus on High priority companies first
        high_priority_companies = [company for company in all_data if company.get('Training Priority') == 'High']
        
        for i, company in enumerate(high_priority_companies[:10], 1):  # Analyze top 10 high priority
            print(f"\n📋 {i}. {company['Company Name']}")
            print(f"   📞 {company.get('Phone', 'N/A')}")
            print(f"   👥 Contact: {company.get('Contact Person', 'N/A')}")
            print(f"   🏢 Size: {company.get('Company Size', 'N/A')}")
            print(f"   💰 Pipeline: ${company.get('Annual Value', 0):,}")
            
            # Current campaign angle
            current_angle = company.get('Campaign Angle', 'Not specified')
            print(f"   📝 Current Angle: {current_angle}")
            
            # Create analysis task
            analysis_task = Task(
                description=f"""Analyze {company['Company Name']} for optimal sales approach:
                
                Company Details:
                - Size: {company.get('Company Size', 'Unknown')}
                - Services: {company.get('Services', 'General pest control')}
                - Training Priority: {company.get('Training Priority', 'Medium')}
                - Pain Points: {company.get('Pain Points', 'Unknown')}
                - Current Campaign Angle: {current_angle}
                - Contact Person: {company.get('Contact Person', 'Unknown')}
                - Title: {company.get('Title', 'Unknown')}
                - Website: {company.get('Website', 'Unknown')}
                
                Determine:
                1. Best communication channel (phone vs email first)
                2. Key value proposition to emphasize
                3. Specific pain points to address
                4. Recommended messaging tone
                5. Follow-up strategy
                """,
                agent=analyst,
                expected_output="Detailed sales approach recommendations including communication strategy, value proposition, and messaging approach."
            )
            
            # Create campaign strategy task
            campaign_task = Task(
                description=f"""Create a personalized outreach strategy for {company['Company Name']}:
                
                Based on the analysis, create:
                1. Initial outreach message (email or phone script)
                2. Key talking points specific to their business
                3. Value proposition tailored to their pain points
                4. Follow-up sequence recommendations
                5. ROI examples relevant to their company size
                
                Company focus areas:
                - Size: {company.get('Company Size', 'Unknown')}
                - Current challenges: {company.get('Pain Points', 'Unknown')}
                - Decision maker: {company.get('Contact Person', 'Unknown')}
                """,
                agent=campaign_strategist,
                expected_output="Customized outreach strategy with specific messaging and follow-up plan."
            )
            
            # Execute analysis
            try:
                crew = Crew(
                    agents=[analyst, campaign_strategist],
                    tasks=[analysis_task, campaign_task],
                    verbose=True
                )
                
                result = crew.kickoff()
                
                print(f"   ✅ Analysis complete for {company['Company Name']}")
                print(f"   📋 Strategy: {str(result)[:200]}...")
                
            except Exception as e:
                print(f"   ❌ Analysis failed for {company['Company Name']}: {str(e)}")
                
                # Provide manual recommendations based on company data
                manual_recommendations = analyze_company_manually(company)
                print(f"   📋 Manual Analysis: {manual_recommendations}")
        
        print(f"\n✅ COMPANY ANALYSIS COMPLETE!")
        print(f"🎯 Focus on the high-priority companies with personalized approaches")
        
    except Exception as e:
        print(f"❌ Error analyzing companies: {e}")

def analyze_company_manually(company):
    """Provide manual analysis when automated analysis fails."""
    
    size = company.get('Company Size', '')
    pain_points = company.get('Pain Points', '')
    contact_person = company.get('Contact Person', '')
    
    recommendations = []
    
    # Communication channel recommendation
    if 'Owner' in contact_person or 'President' in contact_person:
        recommendations.append("📞 PHONE FIRST - Direct to decision maker")
    else:
        recommendations.append("📧 EMAIL FIRST - Professional approach to staff")
    
    # Value proposition based on size
    if 'Large' in size:
        recommendations.append("🎯 FOCUS: Standardization, efficiency, compliance at scale")
    elif 'Medium' in size:
        recommendations.append("🎯 FOCUS: Growth support, operational efficiency")
    else:
        recommendations.append("🎯 FOCUS: Flexible training, no contracts, cost-effective")
    
    # Pain point specific messaging
    if 'hiring' in pain_points.lower():
        recommendations.append("💡 KEY MESSAGE: Training helps with recruitment and retention")
    if 'quality' in pain_points.lower():
        recommendations.append("💡 KEY MESSAGE: Standardized training improves service quality")
    if 'compliance' in pain_points.lower():
        recommendations.append("💡 KEY MESSAGE: CEU credits and regulatory training")
    
    return "; ".join(recommendations)

def main():
    """Main execution function."""
    
    print("🎯 SALES APPROACH ANALYSIS")
    print("=" * 40)
    print("Using AI agents to determine optimal approaches for each company")
    print("=" * 40)
    
    analyze_companies_for_approaches()

if __name__ == "__main__":
    main() 