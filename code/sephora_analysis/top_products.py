from bs4 import BeautifulSoup
import requests
import csv


products = []


# In case we need to get ingredients as well.
def split_ingredients(text):
    result = []
    current = []
    depth = 0

    for char in text:
        if char == "(":
            depth += 1
            current.append(char)
        elif char == ")":
            depth -= 1
            current.append(char)
        elif char in [",", ".", ":"] and depth == 0:
            # Only split if we're outside of parentheses
            item = "".join(current).strip()
            if item:
                result.append(item)
            current = []
        else:
            current.append(char)

    # Add any remaining text
    if current:
        item = "".join(current).strip()
        if item:
            result.append(item)

    return result


def parse_count(s: str):
    if s.endswith("K"):
        return int(float(s[:-1]) * 1_000)
    elif s.endswith("M"):
        return int(float(s[:-1]) * 1_000_000)
    elif s.endswith("B"):
        return int(float(s[:-1]) * 1_000_000_000)
    else:
        return int(s)


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
}

# Scrape the first top 100 pages
for i in range(1, 100):
    res = requests.get(
        url=f"https://www.sephora.com/shop/makeup-cosmetics?currentPage={i}",
        headers=headers,
        timeout=10,
    )

    soup = BeautifulSoup(res.content, "html.parser")
    t = soup.find_all("div", {"class": "css-11ifn8v e15t7owz0"})
    for a in t:
        link_tag = a.find("a")
        product_id = (
            link_tag["href"].split(":")[1].replace("p", "")
            if link_tag and link_tag.has_attr("href")
            else -1
        )

        review_span = a.find("span", {"class": "css-qbbayi", "data-at": "review_count"})
        review_count = review_span.text.strip() if review_span else str(-1)

        brand_span = a.find("span", class_="css-1e2863e")
        product_brand = brand_span.text.strip() if brand_span else "N/A"

        name_span = a.find("span", class_="css-1ma869u")
        product_name = name_span.text.strip() if name_span else "N/A"

        products.append(
            (product_id, parse_count(review_count), product_brand, product_name)
        )


with open("products.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["pid", "reviews", "brand", "product_name"])
    writer.writerows(products)
