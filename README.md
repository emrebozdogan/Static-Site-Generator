# Static Site Generator

A powerful, Python-based static site generator that converts Markdown files into beautiful HTML websites with support for nested directory structures, automatic asset copying, and a built-in development server.

## 🚀 Features

- **Markdown to HTML Conversion**: Converts Markdown files to clean, semantic HTML
- **Recursive Directory Processing**: Automatically processes nested content directories
- **Static Asset Management**: Copies images, CSS, and other assets to the output directory
- **Template System**: Uses HTML templates with placeholder substitution
- **Development Server**: Built-in HTTP server for local development
- **GitHub Pages Ready**: Output directory configured for easy GitHub Pages deployment
- **Comprehensive Testing**: Full test suite with unit tests for all components
- **Clean Architecture**: Modular design with separate concerns for parsing, generation, and output

## 📁 Project Structure

```
StaticSiteGenerator/
├── src/                      # Source code
│   ├── main.py              # Main entry point
│   ├── gencontent.py        # Page generation logic
│   ├── markdown_utils.py    # Markdown processing utilities
│   ├── htmlnode.py          # Base HTML node class
│   ├── parentnode.py        # HTML nodes with children
│   ├── leafnode.py          # HTML nodes with values
│   ├── textnode.py          # Text node representation
│   ├── textnode_utils.py    # Text processing utilities
│   ├── blocktypes.py        # Block type detection
│   ├── copy_static.py       # Static file copying
│   └── test_*.py           # Unit tests
├── content/                 # Markdown content files
│   ├── index.md            # Homepage content
│   ├── blog/               # Blog posts
│   │   ├── glorfindel/
│   │   ├── majesty/
│   │   └── tom/
│   └── contact/            # Contact page
├── static/                 # Static assets (CSS, images)
├── docs/                   # Generated HTML output (GitHub Pages ready)
├── template.html           # HTML template
├── main.sh                # Build and serve script
├── build.sh               # Alternative build script
└── test.sh                # Test runner script
```

## 🛠 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd StaticSiteGenerator
   ```

2. **Ensure Python 3.x is installed**:
   ```bash
   python3 --version
   ```

3. **No additional dependencies required** - uses only Python standard library!

## 🚀 Usage

### Quick Start

Generate your site and start the development server:

```bash
./main.sh
```

This will:
1. Generate HTML files from your Markdown content
2. Copy static assets to the docs directory
3. Start a local server at `http://localhost:8888`

### Build Options

**Option 1 - Full build and serve** (recommended for development):
```bash
./main.sh
```

**Option 2 - Build only** (for deployment):
```bash
./build.sh
```

**Option 3 - Manual build**:
```bash
python3 src/main.py
```

### Testing and Development

**Run tests**:
```bash
./test.sh
# or
python3 -m unittest discover -s src
```

**Start development server** (after building):
```bash
cd docs && python3 -m http.server 8888
```

## 📝 Content Creation

### Adding Pages

1. Create a new Markdown file in the `content/` directory
2. Use the following structure:

```markdown
# Page Title

Your content here with **bold**, *italic*, and `code` formatting.

## Subheadings

- Lists
- Are supported
- Too

> Blockquotes work great

```code blocks```
are also supported
```

### Directory Structure

The generator preserves your content directory structure:

- `content/index.md` → `docs/index.html`
- `content/blog/post/index.md` → `docs/blog/post/index.html`
- `content/about.md` → `docs/about.html`

### Supported Markdown Features

- **Headings**: `# H1`, `## H2`, etc.
- **Text Formatting**: `**bold**`, `*italic*`, `` `code` ``
- **Links**: `[text](url)`
- **Images**: `![alt](url)`
- **Lists**: Both ordered and unordered
- **Blockquotes**: `> quoted text`
- **Code Blocks**: ``` fenced code blocks ```

## 🎨 Customization

### HTML Template

Edit `template.html` to customize the page structure:

```html
<!doctype html>
<html>
  <head>
    <title>{{ Title }}</title>
    <link href="/index.css" rel="stylesheet" />
  </head>
  <body>
    <article>{{ Content }}</article>
  </body>
</html>
```

**Template Variables**:
- `{{ Title }}`: Extracted from the first H1 heading in your Markdown
- `{{ Content }}`: Generated HTML content

### Styling

Add your CSS to `static/index.css`. The file will be automatically copied to `docs/index.css`.

### Static Assets

Place images, fonts, and other assets in the `static/` directory. They'll be copied to `docs/` maintaining the same structure.

## 🌐 Deployment

### GitHub Pages

This project is configured for easy GitHub Pages deployment:

1. **Push your changes** to your GitHub repository
2. **Enable GitHub Pages** in your repository settings
3. **Set source** to "Deploy from a branch"
4. **Select branch** `main` and folder `/docs`
5. **Your site will be live** at `https://yourusername.github.io/repository-name`

The `docs/` directory contains all the generated HTML files and assets needed for GitHub Pages.

### Other Hosting Platforms

You can deploy the contents of the `docs/` directory to any static hosting service:
- Netlify
- Vercel  
- AWS S3
- Firebase Hosting

## 🏗 Architecture

### Core Components

- **HTMLNode**: Base class for HTML element representation
- **ParentNode**: HTML elements that contain children
- **LeafNode**: HTML elements with text content only
- **TextNode**: Represents text with formatting information
- **Block Processing**: Converts Markdown blocks to HTML structures

### Processing Pipeline

1. **Content Discovery**: Recursively finds all `.md` files
2. **Markdown Parsing**: Converts Markdown to intermediate representation
3. **HTML Generation**: Creates HTML nodes from parsed content
4. **Template Application**: Injects content into HTML template
5. **File Output**: Writes HTML files maintaining directory structure
6. **Asset Copying**: Copies static files to docs directory

## 🧪 Testing

The project includes comprehensive unit tests:

```bash
# Run all tests
./test.sh

# Run specific test files
python3 -m unittest src.test_markdown_utils
python3 -m unittest src.test_htmlnode
python3 -m unittest src.test_gencontent
```

### Test Coverage

- Markdown parsing and conversion
- HTML node generation and rendering
- Block type detection
- Text node processing
- Content generation workflows

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests: `./test.sh`
5. Commit changes: `git commit -m "Description"`
6. Push to branch: `git push origin feature-name`
7. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

This static site generator was built as part of the [Boot.dev](https://www.boot.dev) Python course, demonstrating practical application of:

- Object-oriented programming
- File system operations
- Text processing and parsing
- HTML generation
- Test-driven development

---

**Happy site building!** 🎉

For questions or issues, please open an issue on GitHub.
