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
        try:
            password = generate_password(password_length,include_numbers, include_symbols)
            print(password)
        except ValueError as error:
            error_msg = str(error)
            return render_template('index.html',error_generate_password_message=error_msg)
        return render_template('index.html',password=password)
    abort(405)
 
@app.route('/generate-hash-password', methods=['GET', 'POST'])
def generateHashPassword():
    if request.method == "POST":
        global password
        generated_password = request.form.get('generated_password')
        if generated_password == password:
            hash_method = request.form.get('include_hash')
            try:
                password_hashed = hash_password(password,hash_method)
            except ValueError as error:
                error_msg = str(error)
                return render_template('index.html',error_password_hashed_message=error_msg)
            return render_template('index.html',password=password,password_hashed=password_hashed)
    if request.method == "POST" and password:
        return render_template('index.html',error_password_hashed_message="Veuillez générer un mot de passe")
    abort(405)

if __name__ == '__main__':
    app.run(port=8080)