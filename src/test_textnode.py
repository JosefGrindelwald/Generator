import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_equal_different_text(self):
        node1 = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("World", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_url_none(self):
        node1 = TextNode("Link text", TextType.LINK, None)
        node2 = TextNode("Link text", TextType.LINK, None)
        self.assertEqual(node1, node2)

    def test_not_equal_different_url(self):
        node1 = TextNode("Link", TextType.LINK, "https://a.com")
        node2 = TextNode("Link", TextType.LINK, "https://b.com")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
