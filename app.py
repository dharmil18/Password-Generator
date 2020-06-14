from flask import Flask, request, render_template
import string, secrets

def pwd_generate(pwd_len):
    pwd = ''
    characters =  string.ascii_letters + string.digits + string.punctuation
    for i in range(0,pwd_len):
        pwd += secrets.choice(characters)
    return pwd

output = None
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate',methods=['POST'])
def generate():
    pwd_len = request.form['range']
    pwd_len = int(pwd_len)
    output = pwd_generate(pwd_len)
    return render_template('index.html', output = output)

if __name__ == "__main__":
    app.run(debug=True)