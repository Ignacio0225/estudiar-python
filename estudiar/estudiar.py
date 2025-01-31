from bs4 import BeautifulSoup

html_doc = "<html><head><title>Test</title></head><body><p>Hello, World!</p></body></html>"
soup = BeautifulSoup(html_doc, "html.parser")

print(soup.title.string)
