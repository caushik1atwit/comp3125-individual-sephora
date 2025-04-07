import multiprocessing.pool
import requests
import multiprocessing
import math
from time import sleep

"""
After getting top 10 products:
cut -f1,2 -d',' products.csv  | sort -t',' -n  -k2  | tail
(404827,4300)
(469438,4800)
(432500,5300)
(39787544,5400)
(411885,8400)
(467208,10500)
(384060,11400)
(455936,14100)
(87985432,17500)
(61003,19800)
"""

product_ids = [
    (404827, 4300),
    (469438, 4800),
    (432500, 5300),
    (39787544, 5400),
    (411885, 8400),
    (467208, 10500),
    (384060, 11400),
    (455936, 14100),
    (87985432, 17500),
    (61003, 19800),
]


def get_reviews(pid: int, total_reviews: int):
    pages = math.ceil(total_reviews / 100)  # 3 pages: 0–99, 100–199, 200–298
    params = {
        "Filter": f"ProductId:p{pid}",
        "Sort": "Helpfulness:desc",
        "Limit": 100,
        "Offset": 0,
        "Include": "Products,Comments",
        "Stats": "Reviews",
        "passkey": "calXm2DyQVjcCy9agq85vmTJv5ELuuBCF2sdg4BnJzJus",  # The passkey can be easily obtained through inspecting network calls
        "apiversion": 5.4,
    }

    with open(f"p{pid}_reviews.json", "w") as f:
        for page in range(pages):
            params["Offset"] = page * 100
            url = "https://api.bazaarvoice.com/data/reviews.json"
            headers = {"accept": "application/json"}

            res = requests.get(url, headers=headers, params=params, timeout=10)

            if res.status_code == 200:
                f.write(res.text)
                f.write("\n")  # newline-delimited JSON
                print(f"Wrote batch {page + 1}")
            else:
                print(f"Failed to fetch batch {page + 1}: {res.status_code}")

            sleep(1)


if __name__ == "__main__":
    with multiprocessing.Pool(8) as pool:
        pool.starmap(get_reviews, product_ids)
