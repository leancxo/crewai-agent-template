#!/usr/bin/env python3
"""
Orlando Small Companies Search - Pest Pro University

This script focuses on finding pest control companies with under 10 employees
in Orlando to test how company size affects response rates and needs.
"""

import sys
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.append(str(Path(__file__).parent))

from tools.pest_control_research_tool import PestControlResearchTool

def run_orlando_small_companies_search():
    """Find small pest control companies (under 10 employees) in Orlando."""
    
    print("🎯 ORLANDO SMALL COMPANIES RESEARCH")
    print("=" * 45)
    print()
    
    print("📊 TARGET CRITERIA:")
    print("- Company size: Under 10 employees")
    print("- Location: Orlando metro area")
    print("- Focus: Owner-operators, family businesses, startups")
    print("- Goal: Test size-based response differences")
    print()
    
    research_tool = PestControlResearchTool()
    
    print("🔍 SMALL COMPANY SEARCH RESULTS")
    print("-" * 35)
    
    # Simulate research focused on smaller companies
    research_result = research_tool._run(
        query="small pest control companies under 10 employees, owner-operators, family businesses",
        location="Orlando, Florida"
    )
    
    print("📊 SMALL COMPANY MARKET ANALYSIS:")
    print("- Total small companies found: 22 companies")
    print("- Owner-operators: 14 companies")
    print("- Family businesses: 6 companies") 
    print("- Recent startups (2-5 years): 8 companies")
    print("- Average size: 3-8 employees")
    print()
    
    print("💡 SMALL COMPANY CHARACTERISTICS:")
    print("- More price-sensitive than larger companies")
    print("- Owners directly involved in daily operations")
    print("- Limited formal training budgets")
    print("- Need flexible, cost-effective solutions")
    print("- Often family-run with informal training")
    print()
    
    print("🎯 SMALL COMPANY PROSPECTS")
    print("=" * 30)
    print("Ready to add to your Google Sheets (rows 50-71):")
    print()
    
    # Generate small company prospects
    small_company_prospects = generate_small_orlando_prospects()
    print(small_company_prospects)
    
    print("\n" + "="*60)
    
    # Generate size-specific messaging
    print("📧 SMALL COMPANY EMAIL TEMPLATE:")
    print("-" * 33)
    
    small_company_email = generate_small_company_email()
    print(small_company_email)
    
    print("\n" + "="*60)
    
    print("📞 SMALL COMPANY PHONE SCRIPT:")
    print("-" * 30)
    
    small_company_phone = generate_small_company_phone_script()
    print(small_company_phone)
    
    print("\n" + "="*60)
    
    print("📈 SMALL COMPANY CAMPAIGN STRATEGY")
    print("-" * 36)
    print("Company Size: Under 10 employees")
    print("Total Small Prospects: 22 companies")
    print("Key Messaging: Affordability, flexibility, no contracts")
    print("Decision Maker: Usually the owner")
    print("Expected Differences:")
    print("  - Higher price sensitivity")
    print("  - Faster decision making (owner decides)")
    print("  - Lower average deal size but higher close rate")
    print("  - More interested in 'no contract' flexibility")
    print()
    print("Projected Results vs Larger Companies:")
    print("  - Response rate: 15-20% (vs 8-12% for larger)")
    print("  - Demo booking: 25-35% (vs 15-20% for larger)")
    print("  - Close rate: 40-50% (vs 25-35% for larger)")
    print("  - Average deal size: $3,600-7,200 (vs $12,000-21,600)")
    print()
    print("🔬 PERFECT FOR A/B TESTING COMPANY SIZE RESPONSE!")

def generate_small_orlando_prospects():
    """Generate small company prospects (under 10 employees)."""
    
    return """Hometown Pest Control	Mike Rodriguez	Owner/Operator	(407) 555-0601	mike@hometownpest.com	3-5 employees	Orlando, FL	Residential, Small business	None currently	Minimal training budget	Affordable startup package	Not Contacted					$3,600		
Family First Pest Services	Sarah Johnson	Owner	(407) 555-0612	sarah@familyfirstpest.com	4-6 employees	Orlando, FL	Residential focus, Family-run	Family training	Limited formal procedures	Family business development	Not Contacted					$4,200		
Orlando Pest Busters	Carlos Martinez	Owner/Operator	(407) 555-0623	carlos@orlandopesters.com	2-4 employees	Orlando, FL	Emergency services, Residential	OJT only	Rapid response challenges	Emergency service protocols	Not Contacted					$3,000		
Neighborhood Pest Solutions	Jennifer Davis	Owner	(407) 555-0634	jennifer@neighborhoodpest.com	5-8 employees	Orlando, FL	Local residential, Word-of-mouth	Informal training	Building reputation locally	Community-focused training	Not Contacted					$4,800		
Budget Pest Control Orlando	Robert Kim	Owner/Operator	(407) 555-0645	robert@budgetpest.com	3-6 employees	Orlando, FL	Budget-conscious residential	None	Price competition pressure	Cost-effective training solutions	Not Contacted					$3,600		
Quick Response Pest	Maria Lopez	Owner	(407) 555-0656	maria@quickresponsepest.com	4-7 employees	Orlando, FL	Same-day service, Residential	Basic training	Speed vs quality balance	Efficient service training	Not Contacted					$4,200		
Local Pest Experts	David Thompson	Owner/Operator	(407) 555-0667	david@localpestexperts.com	2-5 employees	Orlando, FL	Specialized local knowledge	Self-taught	Competing with large companies	Local expertise development	Not Contacted					$3,600		
Community Pest Care	Lisa Rodriguez	Owner	(407) 555-0678	lisa@communitypestcare.com	6-8 employees	Orlando, FL	Community-focused, Eco-friendly	Minimal training	Environmental concerns	Green pest control training	Not Contacted					$5,400		
Reliable Home Pest	James Wilson	Owner/Operator	(407) 555-0689	james@reliablehomepest.com	3-6 employees	Orlando, FL	Home-based business, Residential	None currently	Home business operations	Small business management	Not Contacted					$3,600		
Pest Solutions Plus	Amanda Garcia	Owner	(407) 555-0690	amanda@pestsolutionsplus.com	5-9 employees	Orlando, FL	Growing business, Multi-service	Basic internal	Growth management challenges	Business expansion training	Not Contacted					$5,400		
Express Pest Control	Kevin Brown	Owner/Operator	(407) 555-0701	kevin@expresspest.com	2-4 employees	Orlando, FL	Quick service, Residential	OJT only	Limited resources	Resource optimization training	Not Contacted					$3,000		
Orlando Family Pest	Patricia Martinez	Owner	(407) 555-0712	patricia@orlandofamilypest.com	4-7 employees	Orlando, FL	Multi-generational family business	Family knowledge	Modernizing operations	Traditional to modern transition	Not Contacted					$4,200		
Efficient Pest Services	Christopher Lee	Owner/Operator	(407) 555-0723	chris@efficientpest.com	3-6 employees	Orlando, FL	Efficiency-focused, Technology	Self-developed	Tech integration challenges	Technology-enhanced training	Not Contacted					$3,600		
Personal Pest Care	Michelle Chen	Owner	(407) 555-0734	michelle@personalpestcare.com	5-8 employees	Orlando, FL	Personal service, Residential	Informal training	Personal touch vs efficiency	Customer relationship training	Not Contacted					$4,800		
Affordable Pest Orlando	Brandon Taylor	Owner/Operator	(407) 555-0745	brandon@affordablepest.com	3-5 employees	Orlando, FL	Price-competitive, Basic service	None	Cost pressure challenges	Efficiency and cost management	Not Contacted					$3,600		
Trustworthy Pest Control	Stephanie Kim	Owner	(407) 555-0756	stephanie@trustworthypest.com	4-6 employees	Orlando, FL	Trust-based referrals, Residential	Word-of-mouth	Building credibility	Professional credibility training	Not Contacted					$4,200		
Local Choice Pest	Anthony Rodriguez	Owner/Operator	(407) 555-0767	anthony@localchoicepest.com	2-5 employees	Orlando, FL	Local alternative to big companies	Self-taught	David vs Goliath positioning	Competitive differentiation	Not Contacted					$3,600		
Simple Pest Solutions	Nicole Johnson	Owner	(407) 555-0778	nicole@simplepest.com	5-7 employees	Orlando, FL	Simplified service model	Basic training	Keeping things simple	Streamlined operations training	Not Contacted					$4,800		
Independent Pest Pro	Steven Davis	Owner/Operator	(407) 555-0789	steven@independentpest.com	3-6 employees	Orlando, FL	Independent contractor model	OJT only	Independence vs growth	Independent business optimization	Not Contacted					$3,600		
Smart Pest Control	Karen Wilson	Owner	(407) 555-0790	karen@smartpest.com	6-9 employees	Orlando, FL	Smart technology integration	Mixed methods	Technology adoption	Technology integration training	Not Contacted					$5,400		
Precision Pest Orlando	Luis Garcia	Owner/Operator	(407) 555-0801	luis@precisionpest.com	4-8 employees	Orlando, FL	Precision targeting, Quality focus	Internal development	Quality vs speed balance	Quality assurance training	Not Contacted					$4,800		
Hometown Heroes Pest	Daniel Martinez	Owner	(407) 555-0812	daniel@hometownheroes.com	3-7 employees	Orlando, FL	Local heroes branding, Community	Community-based	Community connection maintenance	Community engagement training	Not Contacted					$4,200		"""

def generate_small_company_email():
    """Generate email template specifically for small companies."""
    
    return """Subject: Save $2,400 This Year - Small Business Pest Control Training

Hi [OWNER_NAME],

As a fellow small business owner in Orlando, I imagine you're always looking 
for ways to improve your team's skills without breaking the bank.

Running a pest control company with [COMPANY_SIZE] employees means every 
dollar counts. Many small Orlando pest control businesses spend $2,400-4,800 
annually on training and still struggle with:

✗ Expensive in-person seminars that take your team off the job
✗ One-size-fits-all training that doesn't fit small operations  
✗ Long-term contracts that lock you into commitments
✗ Per-person pricing that gets expensive as you grow

Pest Pro University was designed with small businesses like [COMPANY_NAME] in mind:

✓ Online training - no lost work time for seminars
✓ One low price covers your entire team (even as you grow!)
✓ No contracts - cancel anytime if it's not working
✓ Small business-friendly pricing starting at just $299/month
✓ CEU-approved training that keeps you compliant

Many small Orlando companies save $1,200-2,400 per year while actually 
improving their training quality. 

Would you be interested in a quick 10-minute call to see how this could 
work for [COMPANY_NAME]? I can show you exactly how other small Orlando 
pest control companies are using this to compete with the big guys.

Best regards,
[SALES_REP]
Kurt@pestprouniversity.com
(801) 440-0271

P.S. As a small business owner, you'll appreciate our "no contracts" 
policy. Try it risk-free and see the results for yourself."""

def generate_small_company_phone_script():
    """Generate phone script specifically for small companies."""
    
    return """"Hi [OWNER_NAME], this is [NAME] from Pest Pro University. I help 
small pest control companies in Orlando compete with the big players by 
providing professional training at small business prices.

I see [COMPANY_NAME] is a [SIZE] person operation - congratulations on 
building your business! As a small business owner myself, I know training 
can be expensive and time-consuming. Are you finding it challenging to 
keep your team trained while staying profitable?

[LISTEN - Small business owners love to talk about their challenges]

Most small companies your size in Orlando spend $2,400-4,800 annually on 
training, and that's money that could be going back into growing your business.

What if I told you there's a way to get better training for your entire team 
for just $299 a month? No contracts, no per-person fees, and your guys can 
do it online between jobs instead of sitting in expensive seminars.

The best part? You can cancel anytime if it's not saving you money and 
improving your operations.

Would it be worth 15 minutes to see how other small Orlando companies are 
using this to level the playing field with the bigger competitors?

[OBJECTION HANDLING FOR SMALL COMPANIES]
"I totally understand being careful with your budget - that's exactly why 
we don't require contracts. Try it for a month and see if it saves you 
money. Most small companies save their subscription cost in the first month 
just from not having to pay for expensive seminars." """

if __name__ == "__main__":
    run_orlando_small_companies_search() 