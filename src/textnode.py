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
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(self, text_node):
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)
        if text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text)
        if text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text)
        if text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)
        if text_node.text_type == TextType.LINKS:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        if text_node.text_type == TextType.IMAGES:
            return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
            return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})