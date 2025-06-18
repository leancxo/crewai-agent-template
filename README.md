# Pest Pro University - AI Sales Automation

An AI-powered sales automation system using [CrewAI](https://github.com/crewAIInc/crewAI) to research pest control companies, analyze training opportunities, and create targeted sales campaigns for [Pest Pro University](https://www.pestprouniversity.com/).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.130.0+-green.svg)](https://github.com/crewAIInc/crewAI)

## 🎯 About Pest Pro University

**Pest Pro University** is the leading online training platform for pest control professionals, offering:
- **No contracts** - cancel anytime
- **Unlimited users** per branch location
- **CEU credit approved** in 22 states
- **Three comprehensive training tracks:**
  - Service Technicians (19+ modules)
  - Sales & Office Staff
  - Business Management

## 🤖 Sales Automation System

This AI crew automates the entire lead generation and sales process:

1. **🔍 Market Research** - Finds pest control companies in target markets
2. **📊 Opportunity Analysis** - Identifies training needs and value propositions  
3. **✉️ Campaign Creation** - Generates personalized outreach materials

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key (or other LLM provider)

### Installation

1. **Clone this repository:**
```bash
git clone https://github.com/leancxo/pestprouniversity_crewai-agent-sales.git
cd pestprouniversity_crewai-agent-sales
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**
```bash
cp .env.template .env
# Edit .env with your API keys
```

## 🧪 Demo & Testing

**No API keys required!** Test the system immediately:

### Quick Demo
```bash
python pest_pro_demo.py
```
Shows a complete demonstration of the sales automation workflow with sample outputs.

### Original Template Testing
```bash
python test/test_agents.py
```
Runs the full test suite to verify all components are working.

## 📁 Project Structure

```
pestprouniversity_crewai-agent-sales/
├── agents/                           # AI Sales Agents
│   ├── researcher_agent.py          # Market research specialist
│   ├── analyst_agent.py             # Opportunity analyst
│   └── sales_campaign_agent.py      # Campaign creator
├── config/                           # Configuration files
│   └── default_agent_setup.yaml     # Sales crew configuration
├── tools/                            # Specialized tools
│   ├── pest_control_research_tool.py # Market research tool
│   └── example_tool.py               # Original template tool
├── utils/                            # Utility functions
│   └── loader.py                     # Configuration loader
├── test/                             # Test suite
│   └── test_agents.py                # Agent testing
├── main.py                           # Production entry point
├── pest_pro_demo.py                  # Sales automation demo
├── demo.py                           # Original template demo
├── README.md                         # This file
├── requirements.txt                  # Dependencies
└── LICENSE                           # MIT License
```

## 🔧 How to Use

### Running Sales Campaigns

**For target market campaigns:**
```bash
python main.py
```

**With custom configuration:**
```bash
python main.py config/custom_market.yaml
```

### Creating Market-Specific Campaigns

1. **Specify your target market** in the configuration
2. **Run the automation crew** to generate campaigns
3. **Review the generated materials** before outreach
4. **Execute campaigns** via email and phone

### Sample Workflow

```python
# The system will:
# 1. Research pest control companies in your market
# 2. Analyze training needs and pain points
# 3. Create personalized email templates
# 4. Generate phone scripts
# 5. Provide value proposition talking points
```

## 📊 Expected Results

Based on industry benchmarks:
- **Email open rate:** 35-45%
- **Response rate:** 8-12%
- **Phone connection:** 25-30%
- **Demo booking:** 15-20%
- **Close rate:** 25-35%

**Typical campaign (12 prospects):**
- 4-5 demos booked
- 1-2 new customers
- $6,000-15,000 ARR potential

## 🎯 Key Features

### Intelligent Market Research
- Finds pest control companies by location
- Identifies decision makers and contact info
- Analyzes company size and service offerings
- Assesses current training challenges

### Smart Opportunity Analysis  
- Calculates training cost savings potential
- Identifies specific pain points (CEU compliance, costs, standardization)
- Determines best value proposition approach
- Prioritizes prospects by likelihood to convert

### Personalized Campaign Creation
- Custom email templates for each prospect
- Phone scripts tailored to decision maker type
- Value proposition calculators
- Multi-touch follow-up sequences

## 💡 Value Propositions

The system emphasizes Pest Pro University's key differentiators:

- **No Contracts** - Cancel anytime flexibility
- **Unlimited Users** - Scale without per-seat costs  
- **CEU Compliance** - Approved in 22 states
- **Cost Savings** - 40-60% reduction vs traditional training
- **Convenience** - Online, available 24/7
- **Comprehensive** - Service tech, sales, and business training

## 🔌 Integration Ready

Easy to integrate with:
- CRM systems (Salesforce, HubSpot, Pipedrive)
- Email platforms (Mailchimp, SendGrid)
- Phone systems (Outreach, SalesLoft)
- Analytics tools (Google Analytics, Mixpanel)

## 📞 Support

Questions about the system? Contact:
- **Kurt** - kurt@pestprouniversity.com  
- **Phone** - (801) 440-0271

## 🚀 Next Steps

1. **Review** the demo output
2. **Specify** your first target market
3. **Run** the campaign generator
4. **Execute** outreach campaigns
5. **Track** results and optimize

Ready to automate your sales process? Let's start generating campaigns! 