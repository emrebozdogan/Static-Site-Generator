from markdown_utils import *
from htmlnode import *
import os

def extract_title(markdown):
    markdowns = markdown.split("\n")
    for line in markdowns:
        if line.startswith("# "):
            return line[2:].strip()
        
    raise ValueError("No title found")
        

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as markdown_file:
        content = markdown_file.read()
    
    with open(template_path, "r") as template_file:
        template = template_file.read()

    html_content = markdown_to_html_node(content).to_html()

    extracted_title = extract_title(content)

    final_html = template.replace("{{ Title }}", extracted_title).replace("{{ Content }}", html_content)

    import os
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as dest_file:
        dest_file.write(final_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    os.makedirs(dest_dir_path, exist_ok=True)
    
    for file in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, file)
        
        if file.endswith(".md"):
            dest_file_path = os.path.join(dest_dir_path, file.replace(".md", ".html"))
            generate_page(full_path, template_path, dest_file_path)
        
        elif os.path.isdir(full_path):
            dest_subdir_path = os.path.join(dest_dir_path, file)
            generate_pages_recursive(full_path, template_path, dest_subdir_path)
