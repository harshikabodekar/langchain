from langchain_community.document_loaders import CSVLoader  
loader=CSVLoader(
  file_path='social_media_data.csv', #path to the csv file
 )
docs= loader.load()
print(len(docs))
print(docs[0])

print(docs[0].page_content)

