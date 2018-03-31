from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action='/' method='POST'>
            <label for='rot'>Rotate by:</label>
            <input type='text' name='rot' id='rot' value='0'>
            <textarea rows='4' cols='50' name='text'>{0}</textarea>
            <input type='submit' value='Submit'>
        </form>
    </body>
</html>
"""

@app.route('/')
def index():
    return form.format("")

@app.route('/', methods=['POST'])
def encrypt():
    num1 = int(request.form['rot'])
    text1 = request.form['text']
    encrypt_str = rotate_string(text1, num1)
    #content = "<h1>" + encrypt_str + "</h1>"
    return form.format(encrypt_str)

app.run()    