from uber_rides.session import Session
from uber_rides.client import UberRidesClient

session = Session(server_token="2pWDz82lm8GvniDsrxaGYTRZtxjM0iB5uepR-itY")
client = UberRidesClient(session)

#Get a list of available products

response = client.get_products(37.77, -122.41)
products = response.json.get('products')

#Get price and time estimates

response = client.get_price_estimates(
    start_latitude=37.770,
    start_longitude=-122.411,
    end_latitude=37.791,
    end_longitude=-122.405,
    seat_count=2
)

estimate = response.json.get('prices')

#Authorize a rider for your application

from uber_rides.auth import AuthorizationCodeGrant
auth_flow = AuthorizationCodeGrant(
    "neWKQtl-Fr3TKZeStdPdu2rkPMM0QH6p",
    "all_trips delivery history history_lite places profile request request_receipt ride_widgets",
    "q1DvUHO1KPj-GsqvxIm0qtPsnmUrqjyFBKMB-COU",
    "http://127.0.0.1/"
)
auth_url = auth_flow.get_authorization_url()
print(auth_url)

