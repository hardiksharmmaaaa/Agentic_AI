from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

#making the Web Search Agent 
web_Search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-8b-8192"),
    tools=[DuckDuckGo()],
    instructions=["Always include the source from where you parse the information"],
    show_tool_calls=True,
    markdown=True
)

web_Search_agent.print_response("Tell me something about the current trends for Elections in Delhi")