from enum import Enum
from htmlnode import *
from leafnode import LeafNode
from parentnode import ParentNode

class TextType(Enum):
    TEXT = "text"
    TEXT_TYPE = "text_type"
    URL = "url"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGES = "images"
    
    
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

