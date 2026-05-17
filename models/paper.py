from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Paper:
    """
    Class for keeping track of info related to the paper when passing through LangChain phases.
    """
    arxiv_id: str
    title: str
    authors: list[str]
    date: date
    abstract: str
    content: Optional[str] = None
    is_relevant: Optional[bool] = None
