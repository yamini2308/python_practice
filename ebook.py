# import necessary modules
from pypdf import PdfReader  #pdf to text
from  gtts  import gTTS #voice engine
def pdf_to_audio(pdf_path,output_file='output.mp3',language='en'):
    with open(pdf_path, 'rb') as file:   
        reader=PdfReader(pdf_path)   
        text=""
        for page in reader.pages:
            text+=page.extract_text()
    tts=gTTS(text=text,lang=language,slow=False)
    tts.save(output_file)

pdf_to_audio("C:\\Users\\yamin\\Downloads\\oops_in_python.pdf","output.mp3")
