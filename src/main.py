from textnode import *
from copy_static import *
from gencontent import *

def main():
    copy_static("static", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()