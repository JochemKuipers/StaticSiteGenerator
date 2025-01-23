import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_nodes

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)])
    
    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bold word**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("bold word", TextType.BOLD)])
        
    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with a *italic word*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("italic word", TextType.ITALIC)])
        
    def test_split_nodes_delimiter_link(self):
        node = TextNode("This is text with a [link](https://www.google.com)", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "[link](", TextType.LINKS)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("https://www.google.com", TextType.LINKS)])
        
    def test_split_nodes_delimiter_image(self):
        node = TextNode("This is text with an ![image](https://www.google.com)", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "![image](", TextType.IMAGES)
        self.assertEqual(new_nodes, [TextNode("This is text with an ", TextType.TEXT), TextNode("https://www.google.com", TextType.IMAGES)])

    def test_extract_markdown_images(self):
        images = extract_markdown_images("This is text with an ![google](https://www.google.com) and ![yahoo](https://www.yahoo.com)")
        self.assertEqual(images, [("google", "https://www.google.com"), ("yahoo", "https://www.yahoo.com")])
        
    def test_extract_markdown_links(self):
        links = extract_markdown_links("This is text with a [google](https://www.google.com) and [yahoo](https://www.yahoo.com)")
        self.assertEqual(links, [("google", "https://www.google.com"), ("yahoo", "https://www.yahoo.com")])
        
    def test_split_nodes_image(self):
        node = TextNode("This is text with an ![google](https://www.google.com) and ![yahoo](https://www.yahoo.com)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [TextNode("This is text with an ", TextType.TEXT), TextNode("google", TextType.IMAGES, "https://www.google.com"), TextNode(" and ", TextType.TEXT), TextNode("yahoo", TextType.IMAGES, "https://www.yahoo.com")])
        
    def test_split_nodes_link(self):
        node = TextNode("This is text with a [google](https://www.google.com) and [yahoo](https://www.yahoo.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("google", TextType.LINKS, "https://www.google.com"), TextNode(" and ", TextType.TEXT), TextNode("yahoo", TextType.LINKS, "https://www.yahoo.com")])
        
    def test_text_to_nodes(self):
        nodes = text_to_nodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(nodes, [TextNode("This is ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" with an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word and a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" and an ", TextType.TEXT), TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode(" and a ", TextType.TEXT), TextNode("link", TextType.LINKS, "https://boot.dev")])