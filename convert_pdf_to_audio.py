# pip install pyttsx3 PyPDF2

import PyPDF2
import pyttsx3


def pdf_to_speech(pdf_file_path):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Open the PDF file
    pdf_file = open('App-Monitoring.pdf', 'rb')

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Get the total number of pages in the PDF
    total_pages = len(pdf_reader.pages)

    # Read and speak each page
    for page_num in range(total_pages):
        # Extract text from the page
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        # Set the speech rate (optional)
        engine.setProperty('rate', 150)  

        # Convert and speak the text
        engine.say(text)
        engine.runAndWait()

    # Close the PDF file
    pdf_file.close()


if __name__ == "__main__":
    pdf_file_path = "App-Monitoring.pdf"  
    pdf_to_speech(pdf_file_path)
