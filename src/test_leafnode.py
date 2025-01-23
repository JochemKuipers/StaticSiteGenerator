import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("This is a paragraph", "p", {"class": "paragraph"})
        self.assertEqual(node.to_html(), '<p class="paragraph">This is a paragraph</p>')
    def test_to_html_no_tag(self):
        node = LeafNode("This is a paragraph", None, {"class": "paragraph"})
        self.assertEqual(node.to_html(), 'This is a paragraph')
    def test_to_html_no_value(self):
        node = LeafNode(None, "p", {"class": "paragraph"})
        with self.assertRaises(ValueError):
            node.to_html()