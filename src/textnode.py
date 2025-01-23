from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINKS = 5
    IMAGES = 6
    
class TextNode:
    def __init__(self, text: str, text_type: TextType, url:str=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(self, text_node):
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(text_node.text)
            case TextType.BOLD:
                return LeafNode(text_node.text, "b")
            case TextType.ITALIC:
                return LeafNode(text_node.text, "i")
            case TextType.CODE:
                return LeafNode(text_node.text, "code")
            case TextType.LINKS:
                return LeafNode(text_node.text, "a", {"href": text_node.url})
            case TextType.IMAGES:
                return LeafNode(" ", "img", {"src": text_node.url, "alt": text_node.text})