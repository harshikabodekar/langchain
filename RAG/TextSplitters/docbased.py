# we work on markdown files,
#usually for code documentation, readme files, etc.
from langchain_core.documents import Document
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

# 1. Simple Python code for student passing logic
code = """
def check_pass_status(score):
    if score >= 40:
        return "Passed"
    else:
        return "Failed"

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
"""

# # 2. Put the code inside a LangChain Document
doc = Document(
    page_content=code, 
    metadata={"source": "student_grading.py", "subject": "Python 101"}
)

# 3. Create a Python-aware splitter (small chunk size to demonstrate splitting)
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0
)

# 4. Split the document into chunks
chunks = splitter.split_documents([doc])

# 5. Print the split chunks
print(f"Total Chunks Created: {len(chunks)}\n")

print(len(chunks))
print(chunks[2].page_content)