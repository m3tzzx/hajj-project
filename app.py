from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')
  
@app.route("/client.html")
def hello_client():
    return render_template('client.html')
  
@app.route("/user.html")
def hello_user():
    return render_template('user.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)