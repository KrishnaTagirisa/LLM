import PyPDF2

class NLPWorkingWithPDF:

    def __init__(self):
        self.file_path = "/Users/krishnatagirisa/PyWS/LLM/dl-curriculum.pdf"
        self.pdf_reader = PyPDF2.PdfReader(self.file_path)

    def get_page_count(self):
        print("Total pages:", len(self.pdf_reader.pages))

    def get_one_page_text(self, page_number):
        page_one = self.pdf_reader.pages[page_number]  # Page index starts from 0
        page_one_text = page_one.extract_text()
        print(page_one_text)

# Create object
nlppdfobj = NLPWorkingWithPDF()

# Call methods
nlppdfobj.get_page_count()
nlppdfobj.get_one_page_text(21)







