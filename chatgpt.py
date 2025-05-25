# generate_html_index.py
# This script generates an index.html file that lists and displays the content
# of Python scripts in this repository, with syntax highlighting.

import os
import glob
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def get_pygments_css():
    """Generates CSS definitions for Pygments highlighting."""
    # Using a specific style, e.g., 'default' or 'friendly'
    # Using noclasses=False means Pygments will use predefined CSS classes like .k, .s etc.
    # cssclass="highlight" means the outer div will have class "highlight"
    formatter = HtmlFormatter(style='default', cssclass="highlight", noclasses=False)
    return formatter.get_style_defs('.highlight') # Pass the main class selector

def generate_html_for_files(file_paths, category_title):
    """
    Generates HTML for a list of Python files, including syntax-highlighted code.
    Args:
        file_paths (list): A list of paths to Python files.
        category_title (str): The title for this category of files.
    Returns:
        str: HTML string for the given files.
    """
    if not file_paths:
        return ""

    html_sections = [f"<h2>{category_title}</h2>"]
    lexer = get_lexer_by_name("python")
    # Using noclasses=False with a chosen style for Pygments
    formatter = HtmlFormatter(style='default', cssclass="highlight", noclasses=False)

    for file_path in sorted(file_paths):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code_content = f.read()
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            code_content = f"# Error reading file: {e}"

        # Generate highlighted code (this will be a full HTML document snippet if full=True,
        # or just the <div class="highlight">...</div> part if full=False)
        # For embedding, we typically want full=False or to extract from full=True.
        # The HtmlFormatter(full=True) includes <html>, <head>, <body> and <style> tags.
        # We want just the highlighted code block.
        # So, we use a formatter that does not generate a full document.
        # The CSS is generated once and included in the main HTML shell.
        highlighted_code = highlight(code_content, lexer, formatter)

        # Create an accordion-like section for each file
        html_sections.append(f"""
        <div class="script-section">
            <details>
                <summary>{os.path.basename(file_path)} ({os.path.dirname(file_path) or 'root'})</summary>
                <div class="code-container">
                    {highlighted_code}
                </div>
            </details>
        </div>
        """)
    return "\n".join(html_sections)

def main():
    """Main function to discover files and generate index.html."""
    print("Generating index.html...")

    # --- File Discovery ---
    # Root .py files (excluding this script itself)
    root_py_files = [f for f in glob.glob("*.py") if f != "generate_html_index.py"]

    # Files in custom_module_example/
    custom_module_files = glob.glob("custom_module_example/*.py")

    # Files in tests/
    test_files = glob.glob("tests/*.py")


    # --- HTML Structure and Content ---
    pygments_css = get_pygments_css()

    # Generate HTML for each category
    root_scripts_html = generate_html_for_files(root_py_files, "Root Scripts")
    custom_module_html = generate_html_for_files(custom_module_files, "Custom Module Examples (custom_module_example/)")
    test_scripts_html = generate_html_for_files(test_files, "Test Scripts (tests/)")

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Learning Scripts - Index</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
            line-height: 1.6;
        }}
        .container {{
            width: 80%;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
            border-radius: 8px;
        }}
        h1 {{
            text-align: center;
            color: #2c3e50;
            margin-bottom: 30px;
        }}
        h2 {{
            color: #34495e;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
            margin-top: 40px;
        }}
        .script-section details {{
            margin-bottom: 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #fff;
            transition: box-shadow 0.3s ease;
        }}
        .script-section details[open] {{
            box-shadow: 0 5px 10px rgba(0,0,0,0.1);
        }}
        .script_section details:hover {{
            border-color: #3498db;
        }}
        .script-section summary {{
            padding: 12px 15px;
            background-color: #ecf0f1;
            cursor: pointer;
            font-weight: bold;
            color: #2980b9;
            border-radius: 5px 5px 0 0;
            outline: none; /* Removes default focus outline */
            transition: background-color 0.3s ease;
        }}
        .script-section summary:hover {{
            background-color: #dde4e6;
        }}
        .script-section details[open] summary {{
            background-color: #3498db;
            color: #fff;
        }}
        .code-container {{
            padding: 0; /* Padding is handled by pre block */
            border-top: 1px solid #ddd;
        }}
        /* Pygments CSS - .highlight is the main container */
        .highlight pre {{
            padding: 15px;
            margin: 0; /* Reset margin for pre inside .highlight */
            overflow-x: auto; /* Allow horizontal scrolling for code */
            border-radius: 0 0 5px 5px; /* Match details border radius */
        }}
        {pygments_css}
    </style>
</head>
<body>
    <div class="container">
        <h1>Index of Python Learning Scripts</h1>
        <div class="script-list">
            {root_scripts_html}
            {custom_module_html}
            {test_scripts_html}
        </div>
    </div>
</body>
</html>
"""

    # --- Output ---
    try:
        with open("index.html", "w", encoding='utf-8') as f:
            f.write(html_template)
        print("index.html generated successfully.")
    except Exception as e:
        print(f"Error writing index.html: {e}")

if __name__ == "__main__":
    main()
# The erroneous ``` line was removed from the end of the file.