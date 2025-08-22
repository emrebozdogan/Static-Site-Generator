from textnode import *
from leafnode import *
import re

def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

def text_node_to_html_node(text_node):
        match (text_node.text_type):
            case TextType.TEXT:
                return LeafNode(None, text_node.text)
            case TextType.BOLD_TEXT:
                return LeafNode("b", text_node.text)
            case TextType.ITALIC_TEXT:
                return LeafNode("i", text_node.text)
            case TextType.CODE_TEXT:
                return LeafNode("code", text_node.text)
            case TextType.LINK:
                return LeafNode("a", text_node.text, props={"href": text_node.url})
            case TextType.IMAGES:
                return LeafNode("img", '', props={"src": text_node.url, "alt": text_node.text})
            case _:
                raise ValueError("Undefined text type")
            
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes= []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(TextNode(node.text, node.text_type))
            continue
        
        splitted_text_list = node.text.split(delimiter)
        
        if len(splitted_text_list) % 2 == 0:
             raise Exception("No closing delimiter")
        
        for idx in range(len(splitted_text_list)):
            if idx % 2 == 0:
                new_nodes.append(TextNode(splitted_text_list[idx], TextType.TEXT))
            else:
                new_nodes.append(TextNode(splitted_text_list[idx], text_type))
        
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        text = node.text
        for image in images:
            delimiter = f"![{image[0]}]({image[1]})"
            splitted_text = text.split(delimiter, 1)
            if splitted_text[0].strip() != '':
                new_nodes.append(TextNode(splitted_text[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGES, image[1]))
            text = text.replace(splitted_text[0], '')
            text = text.replace(delimiter, '')
        if text.strip() != '':
            new_nodes.append(TextNode(text, TextType.TEXT))
    
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        text = node.text
        for link in links:
            delimiter = f"[{link[0]}]({link[1]})"
            splitted_text = text.split(delimiter, 1)
            if splitted_text[0].strip() != '':
                new_nodes.append(TextNode(splitted_text[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text = text.replace(splitted_text[0], '')
            text = text.replace(delimiter, '')
        if text.strip() != '':
            new_nodes.append(TextNode(text, TextType.TEXT))
    
    return new_nodes

def text_to_textnodes(text):
    # Accept either a raw string or a TextNode for flexibility
    if isinstance(text, TextNode):
        seed_nodes = [text]
    else:
        seed_nodes = [TextNode(text, TextType.TEXT)]

    new_nodes = split_nodes_delimiter(seed_nodes, "**", TextType.BOLD_TEXT)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC_TEXT)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE_TEXT)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    
    return new_nodes