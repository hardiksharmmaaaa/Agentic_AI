from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

import os 
from phi.playground import Playground, serve_playground_app

load_dotenv()

# Create the Web Search Agent
web_Search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[DuckDuckGo()],
    instructions=["Always include the source from where you parse the information"],
    show_tool_calls=True,
    markdown=True
)

# Create the Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Combining both agents into a MultiModal Agent
multi_ai_agent = Agent(
    team=[web_Search_agent, finance_agent],
    model=Groq(id="llama-3.1-8b-instant"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
multi_ai_agent.print_response("share the latest news for Zomato", stream=True)

# Initialize Playground properly
apps = Playground(agents=[finance_agent, web_Search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:apps", reload=True)
