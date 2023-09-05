from flask import Flask, request, render_template
import utils.generate_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-password', methods=['get', 'post'])
def generatePassword():
    if request.method == 'post':
        print(request.form)
        password_length = int(request.form.get('password_length'))
        include_numbers = request.form.get('include_numbers') == 'true'
        include_symbols = request.form.get('include_symbols') == 'true'
        
        return render_template('index.html')
    return "error"

if __name__ == '__main__':
    app.run(port=8080)