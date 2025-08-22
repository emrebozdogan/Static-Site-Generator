import unittest

from textnode import *
from textnode_utils import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
        
    def test_neq(self):
        node = TextNode("This is a text node", TextType.TEXT_TYPE, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT_TYPE, "https://www.google.com")
        self.assertNotEqual(node, node2)
    
    def test_neq2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)
            
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '`', TextType.CODE_TEXT)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE_TEXT), TextNode(" word", TextType.TEXT)])
        
    def test_split_nodes_delimiter_with_text_type(self):
        node = TextNode("_italic word_", TextType.ITALIC_TEXT)
        new_nodes = split_nodes_delimiter([node], '_', TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes, [TextNode("_italic word_", TextType.ITALIC_TEXT)])
        
    def test_split_nodes_delimiter_without_closing_delimiter(self):
        node = TextNode("This is a text with a **bold word without a closing delimiter", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )
    
    def test_split_images_without_image(self):
        node = TextNode(
            "This is a text without images",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("This is a text without images", TextType.TEXT)], new_nodes)
     
    def test_split_images_without_link(self):
        node = TextNode(
            "This is a text without link",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("This is a text without link", TextType.TEXT)], new_nodes)
        
    def test_text_to_textnodes(self):
        node = TextNode("This is a text with a **bold word** and a _italic word_ and a `code block` and a link [to boot dev](https://www.boot.dev) and an image ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        new_nodes = text_to_textnodes(node)
        self.assertListEqual(
            [TextNode("This is a text with a ", TextType.TEXT), TextNode("bold word", TextType.BOLD_TEXT), TextNode(" and a ", TextType.TEXT), TextNode("italic word", TextType.ITALIC_TEXT), TextNode(" and a ", TextType.TEXT), TextNode("code block", TextType.CODE_TEXT), TextNode(" and a link ", TextType.TEXT), TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"), TextNode(" and an image ", TextType.TEXT), TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png")], new_nodes)
        
if __name__ == "__main__":
    unittest.main()