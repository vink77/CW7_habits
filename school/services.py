import stripe
from config.settings import SECRET_TOKEN_STRIPE

def get_payment(course):
    stripe.api_key = SECRET_TOKEN_STRIPE

    product = stripe.Product.create(name=course.kurs_name, description=course.description, price=course.price, currency)
    kurse = stripe.Charge.retrieve(course)
    return kurse
