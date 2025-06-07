from flask import Flask


from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World! This is a basic Flask app by Jagan."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
