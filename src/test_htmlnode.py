import unittest

from htmlnode import *
from leafnode import LeafNode
from parentnode import ParentNode

class TestHTMLNode(unittest.TestCase):
       
    def test_props_to_html_empty(self):
        node = HTMLNode("p", "test", None, None)
        result = node.props_to_html()
        self.assertEqual(result, '')
        
    def test_props_to_html_with_props(self):
        node = HTMLNode("p", "test", None, {"href": "https://www.google.com", "target": "_blank",})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')
        
    def test_props_to_html_not_equal(self):
        node = HTMLNode("p", "test", None, {"href": "https://www.google.com", "target": "_blank",})
        result = node.props_to_html()
        self.assertNotEqual(result, ' href="https://www.boot.dev" target="_blank"')
        

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click here")
        self.assertEqual(node.to_html(), "<a>Click here</a>")
        
    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")
        
    def test_leaf_to_html_div(self):
        node = LeafNode("div", "This is a div")
        self.assertEqual(node.to_html(), "<div>This is a div</div>")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_without_tag(self):
        child_node = LeafNode("c", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
        
    def test_to_html_without_children(self):
        parent_node = ParentNode("<p>", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
        
    def test_to_html_nested_nodes(self):
        parent_node = ParentNode("div", [
            ParentNode("p", [LeafNode("c", "child")])
        ])
        self.assertEqual(parent_node.to_html(), "<div><p><c>child</c></p></div>")
        

if __name__ == "__main__":
    unittest.main()