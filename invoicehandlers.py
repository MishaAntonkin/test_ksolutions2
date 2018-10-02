import hashlib

from flask import current_app, render_template, redirect
import requests

from utils import clear_data_to_payload, InvoiceCounter, create_sign


get_invoice_id = InvoiceCounter()


def pay_method(form):
    keys_required = ('amount', 'currency', 'shop_id', 'shop_order_id')

    invoice_id = get_invoice_id()
    amount, currency, description = clear_data_to_payload(form)

    payload = {'description': description, 'shop_order_id': invoice_id,
               'currency': currency, 'amount': amount,
               'shop_id': current_app.config['SHOP_ID']}
    sign = create_sign(payload, keys_required,
                     current_app.config['SECRET_SHOP_KEY'])
    payload['sign'] = sign
    #write_log('success', payload)
    return render_template('invoice.html', input_fields=payload, method='post',
                           action='https://pay.piastrix.com/ru/pay')


def bill_method(form):
    keys_required = ('shop_amount', 'shop_currency', 'shop_id',
                     'shop_order_id', 'payer_currency')
    invoice_id = get_invoice_id()
    amount, currency, description = clear_data_to_payload(form)

    payload = {'description': description, 'shop_order_id': invoice_id,
               'shop_currency': currency, 'payer_currency': currency,
               'shop_amount': amount, 'shop_id': current_app.config['SHOP_ID']}
    sign = create_sign(payload, keys_required,
                     current_app.config['SECRET_SHOP_KEY'])
    payload['sign'] = sign

    r = requests.post('https://core.piastrix.com/bill/create', json=payload)

    if r.status_code == 200:
        response_json = r.json()
    else:
        return redirect('/')

    if response_json.get('result', False):
        return redirect(response_json['data']['url'])
    else:
        return redirect('/')


def invoice_method(form):
    keys_required = ('amount', 'currency', 'payway', 'shop_id',
                     'shop_order_id')
    invoice_id = get_invoice_id()
    amount, currency, description = clear_data_to_payload(form)

    payload = {'description': description, 'shop_order_id': invoice_id,
               'currency': currency, 'payway': 'payeer_rub',
               'amount': amount, 'shop_id': current_app.config['SHOP_ID']}
    sign = create_sign(payload, keys_required,
                     current_app.config['SECRET_SHOP_KEY'])
    payload['sign'] = sign

    r = requests.post('https://core.piastrix.com/invoice/create', json=payload)

    if r.status_code == 200:
        response_json = r.json()
    else:
        return redirect('/')

    if response_json.get('result', False):
        payload = response_json['data']['data']
        method = response_json['data']['method']
        action = response_json['data']['url']
        return render_template('invoice.html', input_fields=payload,
                               method=method, action=action)
    else:
        return redirect('/')
