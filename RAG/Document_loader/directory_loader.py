from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
loader=DirectoryLoader(
    path='books', #path to the directory where your files are stored
    # path=r"C:\Users\harsh\OneDrive\Desktop\langchain\RAG\Document_loader\Ai in  drug discovery.pdf",
    glob='*.pdf', #for pdf files only
    #'*.txt' #for text files only
    #'data/*csv' #for csv files in data
    #'**/*' for any files
    loader_cls=PyPDFLoader
)
docs=loader.load()
print(docs[0].page_content)
print(len(docs))
print(docs[0].metadata)