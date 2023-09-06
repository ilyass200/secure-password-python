from flask import Flask, request, render_template, abort
from utils.generate_password import generate_password
from utils.generate_password import hash_password

app = Flask(__name__)

generated_password = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-password', methods=['GET', 'POST'])
def generatePassword():
    if request.method == 'POST':
        global password
        password_length = int(request.form.get('password_length'))
        include_numbers = request.form.get('include_numbers') == 'true'
        include_symbols = request.form.get('include_symbols') == 'true'
        password = generate_password(password_length,include_numbers, include_symbols)
        
        return render_template('index.html',password=password)
    abort(405)
 
@app.route('/generate-hash-password', methods=['GET', 'POST'])
def generateHashPassword():
    if request.method == "POST":
        global password
        generated_password = request.form.get('generated_password')
        if generated_password == password:
            hash_method = request.form.get('include_hash')
            password_hashed = hash_password(password,hash_method)

            return render_template('index.html',password=password,password_hashed=password_hashed)
    abort(405)

if __name__ == '__main__':
    app.run(port=8080)