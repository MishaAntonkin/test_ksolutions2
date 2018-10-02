from flask import Flask, render_template, jsonify

from forms import TextForm
from configmodule import Config
from invoicehandlers import pay_method, bill_method, invoice_method


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def home():
    form=TextForm()
    print(form)
    for d in form:
        print(d)
    if form.validate_on_submit():
        if form.currencies.data == '978':
            return pay_method(form)
        elif form.currencies.data == '840':
            return bill_method(form)
        else:
            return invoice_method(form)
    else:
        # later write log
        print(form.errors)
    return render_template("buypage.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
