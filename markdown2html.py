#!/usr/bin/python3
"""
Convert a Markdown file to HTML.

Usage: ./markdown2html.py <input.md> <output.html>
"""

import sys
import os.path
import markdown

def convert_to_html(input_file, output_file):
    """
    Convert the Markdown file to HTML and write it to the output file.

    Args:
        input_file (str): The name of the input Markdown file.
        output_file (str): The name of the output HTML file.
    """
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print("Missing {}".format(input_file), file=sys.stderr)
        sys.exit(1)

    # Read the input file
    with open(input_file, 'r') as f:
        markdown_text = f.read()

    # Convert the Markdown to HTML
    html_text = markdown.markdown(markdown_text)

    # Write the HTML to the output file
    with open(output_file, 'w') as f:
        f.write(html_text)

if __name__ == "__main__":
    # Check if the correct number of arguments was provided
    if len(sys.argv) != 3:
        print("Usage: {} <input.md> <output.html>".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    # Get the input and output filenames
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert the Markdown to HTML and write it to the output file
    convert_to_html(input_file, output_file)

    # Exit with success code
    sys.exit(0)
