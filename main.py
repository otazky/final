from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route('/', methods = ['GET','POST', 'PUT'])
@app.route('/home', methods = ['GET','POST', 'PUT'])
def home():
    return render_template('index.html')

@app.route('/ok', methods = ['GET','POST', 'PUT'])
def form():
    output = request.form.to_dict()
    email = output["email"]

    return render_template('ok.html', user_input = email)

@app.route('/password', methods = ['GET','POST', 'PUT'])
def password():
    output = request.form.to_dict()
    psw = output["password"]

    return render_template('password.html', admin_input = psw)

if __name__ == '__main__':
  app.run(debug=True, port=8080)