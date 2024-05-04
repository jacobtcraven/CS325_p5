from xml.etree import ElementTree as ET

def txt_to_html(txt_file, html_file):
  """
  Converts a text file with header and paragraph to an HTML file.
  Make necessary changes for multiple news articles. This script is
  only for one news article.

  Args:
      txt_file (str): Path to the text file.
      html_file (str): Path to the output HTML file.
  """
  with open(html_file, 'w') as file:
    file.write('')

  read_file = ''
  content = ''
  with open(txt_file, 'r') as f:


    

    # # Read text file content
    # with open(txt_file, 'r') as f:
    #   content = f.readlines()

    # Extract header and paragraph, since you will be having multiple articles the logic will
    # change for the code given below. 
    # header = content[0].strip()

    # Create root element for HTML, try to remember the structure of a HTML file
    root = ET.Element("html")

    # Create head and body elements, try to understand how subElements works
    head = ET.SubElement(root, "head")
    title = ET.SubElement(head, "title")
    title.text = "My News Aggregation Site"
    body = ET.SubElement(root, "body")

    for i in range(2):
      # content = ''
      header = f.readline()
      read_file = f.readline()
      while read_file != '\n':
        content += read_file
        read_file = f.readline()

      paragraph = "".join(content[0:]).strip()


      # Create header and paragraph elements in body
      h1 = ET.SubElement(body, "h1")
      h1.text = header
      p = ET.SubElement(body, "p")
      p.text = paragraph

      # Write HTML tree to file
      with open(html_file, 'ab') as file:
        tree = ET.ElementTree(root)
        tree.write(file, encoding='utf-8')


txt_file = "./webpage_creation/my_text.txt"
html_file = "./webpage_creation/all_news_articles.html"
txt_to_html(txt_file, html_file)

print(f"Converted text file '{txt_file}' to HTML file '{html_file}'.")
