import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, TextType.BOLD, None)")
        
    def test_repr_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, TextType.BOLD, https://www.google.com)")
        
    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertEqual(node, node2)
        
    def test_eq_with_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.yahoo.com")
        self.assertNotEqual(node, node2)
    
    def test_eq_with_one_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_eq_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node too", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_eq_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node_text(self):
        text_node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(text_node.text_node_to_html_node(text_node).to_html(), "This is a text node")
    
    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(text_node.text_node_to_html_node(text_node).to_html(), "<b>This is a text node</b>")
    
    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(text_node.text_node_to_html_node(text_node).to_html(), "<i>This is a text node</i>")
    
    def test_text_node_to_html_node_code(self):
        text_node = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(text_node.text_node_to_html_node(text_node).to_html(), "<code>This is a text node</code>")
        
    def test_text_node_to_html_node_links(self):
        text_node = TextNode("This is a text node", TextType.LINKS, "https://www.google.com")
        self.assertEqual(text_node.text_node_to_html_node(text_node).to_html(), '<a href="https://www.google.com">This is a text node</a>')
        
    def test_text_node_to_html_node_images(self):
        text_node = TextNode("This is a text node", TextType.IMAGES, "https://www.google.com")
        self.assertEqual(text_node.text_node_to_html_node(text_node).to_html(), '<img src="https://www.google.com" alt="This is a text node">')

if __name__ == "__main__":
    unittest.main()