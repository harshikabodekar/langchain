# used to extract text from pdf files
# not greate with scanned pdf or complex layouts, but works well with simple text-based pdfs

from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader(r"C:\Users\harsh\OneDrive\Desktop\langchain\RAG\Document_loader\Ai in  drug discovery.pdf")
docs=loader.load()
print(docs[0].page_content)
print(len(docs))
print(docs[0].metadata)
