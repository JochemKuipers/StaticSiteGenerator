import unittest
from htmlnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("div", [ParentNode("p", "This is a paragraph", {"class": "paragraph"}), ParentNode("p", "This is another paragraph", {"class": "paragraph"})], {"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container"><p class="paragraph">This is a paragraph</p><p class="paragraph">This is another paragraph</p></div>')
        
    def test_to_html_no_tag(self):
        node = ParentNode(None, [ParentNode("p", "This is a paragraph", {"class": "paragraph"}), ParentNode("p", "This is another paragraph", {"class": "paragraph"})], {"class": "container"})
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_to_html_no_children(self):
        node = ParentNode("div", None, {"class": "container"})
        with self.assertRaises(ValueError):
            node.to_html()
        
    def test_to_html_empty_children(self):
        node = ParentNode("div", [], {"class": "container"})
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_to_html_children_are_parent_type(self):
        node = ParentNode("div", [ParentNode("p", "This is a paragraph", {"class": "paragraph"}), "This is another paragraph"], {"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container"><p class="paragraph">This is a paragraph</p>This is another paragraph</div>')