#!/usr/bin/env python3
"""
Real Prospect Research Script
Demonstrates the three-agent workflow with real web scraping for Pest Pro University.

This script uses REAL web scraping to find actual pest control companies,
analyze their businesses, and create personalized sales campaigns.
"""

import os
from crewai import Crew, Task
from agents.researcher_agent import create_pest_control_researcher
from agents.analyst_agent import create_sales_opportunity_analyst  
from agents.sales_campaign_agent import create_sales_campaign_strategist

def create_real_research_tasks(location: str, max_companies: int = 10):
    """Create tasks for the three-agent real research workflow."""
    
    # Task 1: Find Real Companies
    research_task = Task(
        description=f"""Find {max_companies} REAL pest control companies in {location} using web scraping.
        
        Use the web_scraping tool to search multiple sources:
        1. Start with Google search: "pest control {location}"
        2. Search Yellow Pages for pest control in {location}
        3. Check Yelp for pest control businesses in {location}
        
        For each company found, verify:
        - Company name and website URL
        - Phone number and address
        - Basic services offered
        - That it's a real, existing business
        
        CRITICAL: NO FAKE DATA. Only return companies that actually exist with real websites.
        
        Provide a structured list with:
        - Company Name
        - Website URL  
        - Phone Number
        - Address
        - Source (Google/Yellow Pages/Yelp)
        - Basic services mentioned
        
        Aim for {max_companies} verified companies with complete information.""",
        
        agent=create_pest_control_researcher(),
        expected_output=f"List of {max_companies} real pest control companies with verified contact information and websites"
    )
    
    # Task 2: Analyze Real Companies
    analysis_task = Task(
        description="""Analyze each REAL company found by the researcher using the company_analysis tool.
        
        For each company with a website URL, perform comprehensive analysis:
        
        1. Company size assessment (small/medium/large)
        2. Services offered and specializations
        3. Training needs identification
        4. Decision maker research
        5. Pain points analysis
        6. Sales opportunity scoring
        7. Deal potential calculation
        
        Use the company_analysis tool with:
        - Company name
        - Website URL
        - Location
        
        Create detailed analysis reports for each company showing:
        - Size category and confidence score
        - Training priority level
        - Identified decision makers
        - Deal potential range
        - Key pain points for outreach
        - Recommended approach strategy
        
        Focus on companies with Medium to High training priority.""",
        
        agent=create_sales_opportunity_analyst(),
        expected_output="Detailed analysis reports for each company with training needs assessment and sales opportunity scoring",
        context=[research_task]
    )
    
    # Task 3: Create Personalized Campaigns
    campaign_task = Task(
        description="""Create personalized sales campaigns for the top prospects based on real analysis data.
        
        Using the company analysis results, develop tailored outreach campaigns for companies with:
        - Medium to High training priority
        - Clear decision makers identified
        - Specific pain points uncovered
        
        For each target company, create:
        
        1. **Personalized Email Sequence** (3 emails):
           - Email 1: Introduction referencing specific company details
           - Email 2: Value proposition addressing identified pain points
           - Email 3: Case study and ROI calculation
        
        2. **Phone Script** with:
           - Company-specific opening reference
           - Pain point discussion points
           - Value proposition tailored to their size/services
           - Next steps and scheduling language
        
        3. **LinkedIn Connection Message** referencing:
           - Specific company details found during research
           - Mutual interest in pest control training
           - Soft introduction to Pest Pro University
        
        Include Pest Pro University key benefits:
        - No contracts, unlimited users per branch
        - CEU credits accepted in 22 states  
        - Three training tracks: Service Tech, Sales/Office, Business Management
        - ROI through improved service quality and compliance
        
        Tailor messaging to company size:
        - Small companies: Focus on flexibility and cost-effectiveness
        - Medium companies: Emphasize scaling and standardization  
        - Large companies: Highlight enterprise features and ROI
        
        Create a campaign summary with target priority ranking.""",
        
        agent=create_sales_campaign_strategist(),
        expected_output="Personalized sales campaigns with email sequences, phone scripts, and LinkedIn messages for top prospects",
        context=[research_task, analysis_task]
    )
    
    return [research_task, analysis_task, campaign_task]

def run_real_prospect_research(location: str = "Orlando, FL", max_companies: int = 10):
    """Run the complete real prospect research workflow."""
    
    print(f"🔍 Starting REAL prospect research for {location}")
    print("=" * 60)
    print("This workflow uses actual web scraping to find real companies.")
    print("NO FAKE DATA - only verified, existing businesses.")
    print("=" * 60)
    
    # Create agents
    researcher = create_pest_control_researcher()
    analyst = create_sales_opportunity_analyst()
    campaign_strategist = create_sales_campaign_strategist()
    
    # Create tasks
    tasks = create_real_research_tasks(location, max_companies)
    
    # Create crew
    crew = Crew(
        agents=[researcher, analyst, campaign_strategist],
        tasks=tasks,
        verbose=2,
        memory=True
    )
    
    # Execute the workflow
    print(f"\n🚀 Executing three-agent workflow:")
    print(f"1. Researcher: Finding real companies in {location}")
    print(f"2. Analyst: Analyzing {max_companies} companies for training needs")
    print(f"3. Campaign Strategist: Creating personalized outreach campaigns")
    print("\n" + "=" * 60)
    
    try:
        result = crew.kickoff()
        
        print("\n✅ REAL PROSPECT RESEARCH COMPLETED")
        print("=" * 60)
        print("Results include:")
        print("• Real companies with verified contact information")
        print("• Detailed analysis based on actual website content")
        print("• Personalized campaigns referencing real business details")
        print("• Ready-to-use email templates and phone scripts")
        print("=" * 60)
        
        return result
        
    except Exception as e:
        print(f"\n❌ Error during research: {str(e)}")
        print("This may be due to:")
        print("• Network connectivity issues")
        print("• Website access restrictions")
        print("• Rate limiting from web scraping")
        print("• Missing dependencies")
        return None

if __name__ == "__main__":
    # Example usage
    print("Pest Pro University - Real Prospect Research System")
    print("=" * 60)
    
    # Get user input for location
    location = input("Enter location to research (e.g., 'Orlando, FL'): ").strip()
    if not location:
        location = "Orlando, FL"
    
    # Get number of companies
    try:
        max_companies = int(input("Number of companies to research (default 10): ").strip() or "10")
    except ValueError:
        max_companies = 10
    
    # Run the research
    result = run_real_prospect_research(location, max_companies)
    
    if result:
        print(f"\n📊 Research Summary:")
        print(f"Location: {location}")
        print(f"Companies Researched: {max_companies}")
        print(f"Data Source: Real web scraping")
        print(f"Output: Personalized sales campaigns")
        
        # Save results to file
        timestamp = __import__('datetime').datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"real_research_{location.replace(', ', '_').replace(' ', '_')}_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write(f"REAL PROSPECT RESEARCH RESULTS\n")
            f.write(f"Location: {location}\n")
            f.write(f"Date: {timestamp}\n")
            f.write(f"Companies: {max_companies}\n")
            f.write("=" * 50 + "\n\n")
            f.write(str(result))
        
        print(f"📁 Results saved to: {filename}")
    else:
        print("\n❌ Research failed. Please check your setup and try again.")
        print("\nTroubleshooting:")
        print("1. Ensure all dependencies are installed: pip install -r requirements.txt")
        print("2. Check internet connectivity")
        print("3. Verify the location format is correct")
        print("4. Try with a smaller number of companies") 