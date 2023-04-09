from flask import Flask, render_template, request
import os
import PyPDF2
import docx2txt
import summary as sm

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    message = ''
    message_text = ''
    message_file = ''
    
    if request.method == 'POST':
        text = request.form.get('text')
        file = request.files.get('file')
        if text and file:
            message = 'Please enter either text or upload file, not both'
        elif text:
            message_text = sm.summarize_text(text,1500)
        elif file:
            filename = file.filename
            ext = os.path.splitext(filename)[1]
            if ext == '.txt':
                message_file = sm.summarize_text( file.read().decode('utf-8'),1500)
            elif ext == '.pdf':
                pdfReader = PyPDF2.PdfReader(file)
                num_pages = len(pdfReader.pages)
                text = ''
                for i in range(num_pages):
                    pageObj = pdfReader.pages[i]
                    text += sm.summarize_text( pageObj.extract_text(),1500)
                message_file = '<br>'.join(text.split('\n'))
                #message_file = text
            elif ext == '.docx':
                text = docx2txt.process(file)
                message_file = text
            else:
                message = 'Unsupported file format'
    
    return render_template('index.html', message=message, message_text=message_text, message_file=message_file)

if __name__ == '__main__':
    app.run(debug=True)
