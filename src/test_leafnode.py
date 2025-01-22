import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph", {"class": "paragraph"})
        self.assertEqual(node.to_html(), '<p class="paragraph">This is a paragraph</p>')
    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a paragraph", {"class": "paragraph"})
        self.assertEqual(node.to_html(), 'This is a paragraph')
    def test_to_html_no_value(self):
        node = LeafNode("p", None, {"class": "paragraph"})
        with self.assertRaises(ValueError):
            node.to_html()