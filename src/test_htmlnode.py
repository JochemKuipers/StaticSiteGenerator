import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph", None, {"class": "paragraph"})
        self.assertEqual(repr(node), "HTMLNode(p, This is a paragraph, None, {'class': 'paragraph'})")
        
    def test_props_to_html(self):
        node = HTMLNode("a", "This is a link", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')
        
    def test_props_to_html_empty(self):
        node = HTMLNode("p", "This is a paragraph", None, {})
        self.assertEqual(node.props_to_html(), '')