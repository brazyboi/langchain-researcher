from langchain.tools import tool
import pymupdf
import arxiv
import os

@tool
def fetch_paper(arxiv_id: str) -> str:
    """
    Fetches a research paper's content based on its arXiv ID. 
    Use this when you need to extract the whole content of a specific research paper.
    Only call this after search_papers has identified a paper worth reading in full.
    Returns the content, with pages separated by two newlines.
    """
    paper = next(arxiv.Search(id_list=[arxiv_id]).results())
    paper.download_pdf(filename="temp.pdf")
    with pymupdf.open("temp.pdf") as doc: 
        content = []
        for page in doc:
            content.append(page.get_text())
    os.remove("temp.pdf")
    return "\n\n".join(content)
