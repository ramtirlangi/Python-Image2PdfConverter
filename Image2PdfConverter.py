#Importing Libraries
import pdf2image
import os
from PyPDF2 import PdfFileMerger
import argparse

# Argument parser
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--inputFilePath", required=True, help="path to Itext Redacted input image")
#args = vars(ap.parse_args())

#PDF_PATH = args["inputFilePath"]
PDF_PATH = "D:\\test\\RamTirlagi_Resume.pdf"


def pdftopil():
    pil_images = pdf2image.convert_from_bytes(open(PDF_PATH, "rb").read(), dpi=300, output_folder=None, first_page=None, last_page=None, fmt="pdf", jpegopt=None,
    thread_count=1, userpw=None, use_cropbox=False, strict=False, transparent=False, single_file=False, poppler_path=None, grayscale=False, size=None, paths_only=False)
    
    return pil_images

def save_images(pil_images):

    index = 1
    for image in pil_images:
        image.save(str(index) + ".pdf", resolution=300)
        index += 1

    source_dir = os.getcwd()
    merger = PdfFileMerger()
    splittedInvoices = os.listdir(source_dir)
    for item in splittedInvoices:
            if item.endswith('pdf'):
                merger.append(item)
                merger.write(args["inputFilePath"])
                merger.close()
    splittedInvoices.clear()
    splittedInvoicesremove = os.listdir(source_dir)
    for item in splittedInvoicesremove:
        if item.endswith('pdf'):
            os.remove(item);


if __name__ == "__main__":
    try:
	# Flatening of pages in PDF document
        pil_images = pdftopil()
	# Merging of Flatned pages into one PDF document
        save_images(pil_images)
        print("code executed")
    except:
        print("Something went wrong when writing to the file")

