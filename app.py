from flask import Flask, render_template, jsonify

#from forms import TextForm
from configmodule import Config
#from invoicehandlers import tip, invoice


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def home():
    return jsonify({'test': 12})


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)