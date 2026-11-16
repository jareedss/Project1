import os
import requests
from dotenv import load_dotenv

load_dotenv()
headers = {"x-api-key": f'{os.environ["ETSY_API_KEY"]}:{os.environ["ETSY_SHARED_SECRET"]}'}
listing_id = "4618426077"

r = requests.get(
    f"https://openapi.etsy.com/v3/application/listings/{listing_id}",
    headers=headers,
    timeout=15,
)
print(r.status_code)
print(r.json())