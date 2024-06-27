from flask import Flask, render_template, request

app = Flask(__name__)

# Store the submitted payload
the_payload = ""

# Receive the payload
@app.route('/', methods=['GET', 'POST'])
def index():
    global the_payload
    if request.method == 'POST':
        the_payload = request.form['input_payload']
    return render_template('index.html', the_payload=the_payload)

if __name__ == '__main__':
    app.run()
