import pdftotext as ptt

class PDFParse(object):
    def __init__(self, file_name):
        self.file = file_name
    
    def extract_text(self):
        with open(self.file, "rb") as f:
            pdf = ptt.PDF(f)

            return "".join(pdf)
    
    def extract_images(self):
        pass

