from ..models import db, Invoice


def save_invoice(amount: float, currency: str, description: str) -> int:
    invoice = Invoice(amount=amount, currency=currency,
                      description=description)
    db.session.add(invoice)
    db.session.flush()
    identifier = invoice.id
    db.session.commit()
    return identifier
