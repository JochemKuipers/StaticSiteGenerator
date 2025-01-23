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
        node = TextNode("This is a text node", TextType.TEXT)
        to_html = node.text_node_to_html_node(node).to_html()
        self.assertEqual(to_html, "This is a text node")
            
    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        to_html = node.text_node_to_html_node(node).to_html()
        self.assertEqual(to_html, "<b>This is a text node</b>")
        
    def test_text_node_to_html_node_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        to_html = node.text_node_to_html_node(node).to_html()
        self.assertEqual(to_html, "<i>This is a text node</i>")
        
    def test_text_node_to_html_node_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        to_html = node.text_node_to_html_node(node).to_html()
        self.assertEqual(to_html, "<code>This is a text node</code>")
        
    def test_text_node_to_html_node_links(self):
        node = TextNode("This is a text node", TextType.LINKS, "https://www.google.com")
        to_html = node.text_node_to_html_node(node).to_html()
        self.assertEqual(to_html, '<a href="https://www.google.com">This is a text node</a>')
        
    def test_text_node_to_html_node_images(self):
        node = TextNode("This is a text node", TextType.IMAGES, "https://www.google.com")
        to_html = node.text_node_to_html_node(node).to_html()
        self.assertEqual(to_html, '<img src="https://www.google.com" alt="This is a text node">')
if __name__ == "__main__":
    unittest.main()