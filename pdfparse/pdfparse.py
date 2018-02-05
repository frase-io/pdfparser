import subprocess
import random
import string
import os

import pdftotext as ptt


class PDFParse(object):
    def __init__(self, file_name):
        self.file = file_name
    
    def extract_text(self):
        """
        returns unformatted text as a string
        """
        with open(self.file, "rb") as f:
            pdf = ptt.PDF(f)

            return "".join(pdf)
    
    def extract_images(self):
        """
        returns list of paths to the images
        extracted from the pdf
        """
        prefix = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        subprocess.call(['pdfimages', '-all', self.file, '/tmp/' + prefix])
        
        ret = []
        files = os.listdir("/tmp")
        for f in files:
            if prefix in f:
                ret.append(os.path.join("/tmp", f))

        return sorted(ret)
