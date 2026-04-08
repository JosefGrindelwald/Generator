import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_multiple(self):
        node = HTMLNode(
            tag="a",
            props={
                "href": "https://www.google.com",
                "target": "_blank"
            }
        )
        result = node.props_to_html()
        self.assertIn(' href="https://www.google.com"', result)
        self.assertIn(' target="_blank"', result)

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(
            tag="p",
            value="Hello",
            children=None,
            props={"class": "text"}
        )
        repr_str = repr(node)
        self.assertIn("p", repr_str)
        self.assertIn("Hello", repr_str)
        self.assertIn("text", repr_str)


if __name__ == "__main__":
    unittest.main()
