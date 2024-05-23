from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('/home/index.html')

if __name__ == "__main__":
    app.run(debug=True)
    