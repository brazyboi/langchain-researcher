import arxiv
from langchain.tools import tool
from models.paper import Paper
from state import paper_store

def _format_paper_string(paper: Paper) -> str:
    return f"""
    arxiv_id: {paper.arxiv_id}
    Title: {paper.title}
    Authors: {', '.join(paper.authors)}
    Abstract: {paper.abstract}
    Published: {paper.date}
    """

@tool
def search_papers(query: str, max_results: int = 5) -> str:
    """
    Searches arXiv for research papers matching a query.
    Use this when you need to find answers to a question. 
    Use this when you need to find sources for a topic.
    Returns the title, authors, published date, and the abstract (but not the full text).
    """
    results = arxiv.Search(query=query, max_results=max_results).results()
    formatted_papers = []

    for paper in results:
        paper_obj = Paper(
                        arxiv_id=paper.get_short_id(),
                        title=paper.title,
                        authors=[author.name for author in paper.authors],
                        date=paper.published.date(), 
                        abstract=paper.summary
                    )
        paper_store.setdefault(paper_obj.arxiv_id, paper_obj)
        formatted_papers.append(_format_paper_string(paper_obj))

    return "\n\n".join(formatted_papers)
