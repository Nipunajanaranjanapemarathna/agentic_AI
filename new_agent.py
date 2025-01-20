from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

# Define Web Agent for news search
web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Fetch the latest news about the specified companies and include sources."],
    show_tool_calls=True,
    markdown=True,
)

# Define Finance Agent for financial data
finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Provide financial details and analyst recommendations for the given companies in table format."],
    show_tool_calls=True,
    markdown=True,
)

# Define Team Agent to combine results
agent_team = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[web_agent, finance_agent],
    instructions=[
        "For the two companies specified, compare financial details, analyst recommendations, and recent news.",
        "Present the information in a clear comparison table or structured format.",
        "Ensure all information includes sources.",
    ],
    show_tool_calls=True,
    markdown=True,
)

# Prompt Function
def compare_companies(company1, company2):
    prompt = f"""
    Compare the following two companies:
    1. {company1}
    2. {company2}

    For each company, include:
    - Financial details (e.g., current stock price, market cap, P/E ratio, etc.)
    - Analyst recommendations
    - Recent news highlights

    Provide the comparison in a structured table format and include sources.
    """
    response = agent_team.print_response(prompt, stream=False)
    return response

# Example Usage
if __name__ == "__main__":
    company1 = input("Enter the first company name: ")
    company2=input("Enter the second company name: ")
    result = compare_companies(company1, company2)
    print(result)
