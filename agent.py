from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from tools.fetch_paper import fetch_paper
from tools.search_papers import search_papers

def run(query: str, reading_level: str):
    SYSTEM_PROMPT = f"""
    You are a helpful research assistant. Your goal is to help the user find answers, papers, and sources on topics of their choosing. 

    Always be concise, clear, and to-the-point.

    Use the user's reading level when explaining concepts: {reading_level}
    Always cite papers by arxiv ID
    Fetch a paper's full text only if the abstract suggests it's relevant
    Stop searching when you have 2-3 solid relevant sources
    """

    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    agent = create_agent(llm, [fetch_paper, search_papers], system_prompt=SYSTEM_PROMPT)
    
    result = agent.invoke({
        "messages": [
            {"role": "user", "content": query}
        ]
    })
    
    return result
