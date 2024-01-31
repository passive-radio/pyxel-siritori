"""
Component classes are bundled in this module.
"""

from typing import List
from dataclasses import dataclass, field
from pigframe import Component

@dataclass
class CpmSiritori(Component):
    current_word: str = ""
    current_word_jp: str = ""
    history: List[str] = field(default_factory=list)