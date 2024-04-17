from flask import Flask, jsonify, request
from PyPDF2 import PdfReader  # Example using PyPDF2 library
"""
LIBRARIES
"""

import base64
import vertexai

import IPython.display
from IPython.core.interactiveshell import InteractiveShell

# InteractiveShell.ast_node_interactivity = "all"
import vertexai.preview.generative_models as generative_models

from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
    HarmBlockThreshold,
    HarmCategory,
    Part,
)
# """
# #####################################
# """


# MODEL_ID = "gemini-1.5-pro-preview-0409"
# model = GenerativeModel(MODEL_ID)

# # model with system instructions
# teaching_model = GenerativeModel(
#     MODEL_ID,
# )

# # model parameters
# generation_config = GenerationConfig(
#     temperature=1,
#     top_p=1.0,
#     top_k=32,
#     candidate_count=1,
#     max_output_tokens=8192,
# )

# # safety settings
# safety_settings = {
#     HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
#     HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
#     HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
#     HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
# }


# prompt = """
#     You are a very professional document summarization specialist.
#     Please create flashcards of the given document in Triviador style.
# """


app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'pdf'}  # Allowed file extension

@app.route('/', methods =['GET','POST'])
def generate_QA():
  if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded!'}), 400  # Return JSON with error message

        file = request.files['file']
        
        # Validate the uploaded file
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400  # Return JSON with error message
        
        if file and allowed_file(file.filename):
            # Read the entire file in memory
            
            # Process the PDF bytes (e.g., use PyPDF2 or other libraries)
            response = process_pdf(file)  # Replace with your processing function
            return jsonify({'message': f'{response}'}), 200
        else:
            return jsonify({'error': 'Invalid file type (only PDFs allowed)'}), 400
        
  return "Hello"     
	# let's try PDF document analysis
  # pdf_file_uri = "gs://gemini_mds/Cerințe_teme_Algoritmi_Avansați_2024.pdf"

  # pdf_file = Part.from_uri(pdf_file_uri, mime_type="application/pdf")
  # contents = [pdf_file, prompt]

  # response = model.generate_content(contents)
  # print(response.text)

  # return jsonify(response.text)

# Function to process the uploaded PDF (replace with your actual logic)
def process_pdf(pdf_bytes):
    try:
      reader = PdfReader(pdf_bytes)
      num_pages = len(reader.pages)
      response = f"Processing PDF: {num_pages} pages (in-memory)" # Placeholder for processing
      return response
    except Exception as e:
        return e
    

# main driver function
if __name__ == '__main__':
	app.run(host='0.0.0.0',port='8888')