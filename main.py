from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
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
        <h1>Web-Caesar</h1>
         <form method="post">
            <div>
             <label for="rot">Rotate by:</label>
             <input name="rot" value="0" type"text">
             <p class="error"></p>
            </div>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input type="submit" name="submit" value="Submit Query">
        </form> 
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route('/', methods=['POST'])
def encrypt():
    rot_input = int(request.form["rot"])
    text_input = str(request.form["text"])
    encrypted = rotate_string(text_input, rot_input)
    return form.format(encrypted)


app.run()