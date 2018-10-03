import hashlib


class InvoiceCounter:
    """
    Needed to assign a unique id
    """
    def __init__(self):
        self.counter = 0

    def __call__(self):
        self.counter += 1
        print('last counter - ', self.counter)
        return str(self.counter)


def clear_data_to_payload(form):
    amount = '%.2f' % form.money.data
    currency = form.currencies.data
    description = form.description.data
    return amount, currency, description


def create_sign(payload, keys_required, secret):
    """
    form sign, from data which you want to send and secret key
    """
    keys_sorted = sorted(keys_required)
    string_to_sign = ':'.join([payload[k] for k in keys_sorted]) + secret
    sign = hashlib.sha256(string_to_sign.encode('utf-8')).hexdigest()
    return sign
