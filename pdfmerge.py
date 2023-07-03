import os
from PyPDF2 import PdfMerger

def merge_pdfs(directory_path, output_filename):
    merger = PdfMerger()
    pdf_files = [f for f in os.listdir(directory_path) if f.endswith('.pdf')]

    for pdf_file in pdf_files:
        file_path = os.path.join(directory_path, pdf_file)
        merger.append(file_path)

    output_path = os.path.join(directory_path, output_filename)
    merger.write(output_path)
    merger.close()

# Example usage
directory_path = r'Insert\your\own\path' 
output_filename = 'merged.pdf'
merge_pdfs(directory_path, output_filename)
