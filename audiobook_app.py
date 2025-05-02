import PyPDF2 as ppf
import pyttsx3 as ppt
pdfReader = ppf.PdfReader(open('BISHAL DATTA_CV.pdf', 'rb'))
speaker = ppt.init()
full_text = ""
for page_num in range(len(pdfReader.pages)):
    text = pdfReader.pages[page_num].extract_text()
    if text:
        full_text += text
speaker.say(full_text)
speaker.runAndWait()
speaker.save_to_file(full_text, "audio.mp3")
speaker.runAndWait()
