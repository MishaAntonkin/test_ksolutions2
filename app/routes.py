from flask import render_template

from . import app
from .invoicehandlers import pay_method, bill_method, invoice_method
from .forms import TextForm


@app.route('/', methods=['GET', 'POST'])
def home():
    form = TextForm()
    if form.validate_on_submit():
        if form.currencies.data == '978':
            return pay_method(form)
        elif form.currencies.data == '840':
            return bill_method(form)
        else:
            return invoice_method(form)
    else:
        app.logger.info(form.errors, 'home_route')
    return render_template("buypage.html", form=form)
