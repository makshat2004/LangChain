from pyexpat import model
from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_tavily import TavilySearch

tavily_search = TavilySearch(max_results=5, topic="general")

tools = [tavily_search]

llm = ChatOpenAI(model="gpt-4.1-nano")
agent = create_agent(llm, tools , system_prompt="You are a helpful research assistant. Use web search to find accurate, up-to-date information.")



if __name__ == "__main__":
  response = agent.invoke({
      "messages": [{"role": "user", "content": "Search for 3 job postings on linkedn for pune in india for a ai engineer role"}]
  })  
  print(response)

