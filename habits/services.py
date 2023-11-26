import stripe
from config.settings import SECRET_TOKEN_STRIPE

def get_payment(obj):
    # Set your secret key. Remember to switch to your live secret key in production.
    # See your keys here: https://dashboard.stripe.com/apikeys
    print("**********************    **   ", obj.title)
    stripe.api_key = SECRET_TOKEN_STRIPE
    product = stripe.Product.create(name=obj.title)

    price = stripe.Price.create(
        currency="usd",
        custom_unit_amount={"enabled": True},
        product=product,
    )


    response = stripe.PaymentLink.create(line_items=[{"price": price, "quantity": 1}])

    return response.url
