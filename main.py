from common_module.read_file import ReadCSV
from common_module.send_mail import SendMail
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'W\xca\xb4\xda*/\x98\x114\x03\xbc\xd7\x1c(\x14\xca\x19\x90)\xde\x93\x1f\xdas'  

# Replace this with the path to your CSV file
# csv_file1 = "CSV_file/recp_1.csv"
csv_file2 = "CSV_file/cred_1.csv"

# Replace these with your own credentials and mail server details
smtp_server = "smtp.gmail.com"
smtp_port = 587


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

sender_details = ReadCSV.read_file_sender(csv_file2)

@app.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file'] 

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_location)
            recipients = ReadCSV.read_file(save_location)
            SendMail.send_mail(recipients, smtp_server, smtp_port, sender_details)
            return redirect(url_for('operation'))

    return render_template('index.html')

@app.route('/operation',methods=['GET'])
def operation():
    return "All Email are successfully sent!"

if __name__ == '__main__':
    app.run(debug=True, port=8000)