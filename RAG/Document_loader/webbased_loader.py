#uses BeautifulSoup to extract text from web pages
from langchain_community.document_loaders import WebBaseLoader
url="https://en.wikipedia.org/wiki/Drug_discovery",
loader=WebBaseLoader(url) 
docs=loader.load()

print(docs[0].page_content)
print(len(docs))