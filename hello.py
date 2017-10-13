from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/safecheck", methods = ['POST'])
def safetycheck():
    return render_template('safetycheck.html')

if __name__ == "__main__":
    app.run(host = 'localhost', port = 8000)
