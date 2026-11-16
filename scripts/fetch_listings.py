import os
import requests
from dotenv import load_dotenv

load_dotenv()
headers = {
    "x-api-key": f'{os.environ["ETSY_API_KEY"]}:{os.environ["ETSY_SHARED_SECRET"]}'
}
shop_id = os.environ["ETSY_SHOP_ID"]

r = requests.get(
    f"https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/active",
    headers=headers,
    params={"limit": 100},
    timeout=15,
)
print("Estado:", r.status_code)

for listing in r.json().get("results", []):
    price = listing["price"]["amount"] / listing["price"]["divisor"]
    print(
        listing["listing_id"],
        "|", listing["title"][:40],
        "| visitas:", listing["views"],
        "| favoritos:", listing["num_favorers"],
        "| precio:", price,
        "| auto-renovar:", listing["should_auto_renew"],
    )