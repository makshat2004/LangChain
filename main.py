from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
from langchain_ollama import ChatOllama

import warnings
warnings.filterwarnings("ignore", message="Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater")

from langchain_openai import ChatOpenAI

def main():
  print("Info LLM Call")

  info = """
  
  Harbhajan Singh (born 3 July 1980), also known by the nickname Bhajji, is a former Indian cricketer. He later became a politician, serving as a Member of Parliament in Rajya Sabha. He is also a film actor, a television celebrity, and a cricket commentator.

  Harbhajan played for India from 1998 to 2016 as an off spin bowler. In domestic cricket, he played for the Punjab cricket team; and in the Indian Premier League for the Mumbai Indians, Chennai Super Kings, and Kolkata Knight Riders. Considered one of the best Indian spin bowlers of his era, he was on the Indian teams that won the 2007 T20 World Cup and the 2011 Cricket World Cup, and also the team that were joint-winners with Sri Lanka of the 2002 ICC Champions Trophy. He was also a lower-order batter, having two centuries in tests with a top score of 115.
  
  """

  summary_info = """

    given the information {info} abput a person, I want you to create:
    1. A short summary
    2. Two interesing facts about them

  """

  summary_tempelate = PromptTemplate(
    input_variables=["info"],template=summary_info
  )

  # llm = ChatOllama(temperature = 0, model="gemma3:270m")

  llm = ChatOpenAI(model="gpt-4.1-nano",temperature=0)

  chain = summary_tempelate | llm

  response = chain.invoke(input = {"info": info})

  print(response.content)


main()