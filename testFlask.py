import json
from flask import Flask, Response
import requests
from productInfo import Product

app = Flask(__name__)

@app.route("/")
def hello_world():
    search = "libros"
    url = f"https://api.wallapop.com/api/v3/general/search?keywords={search}%20&category_ids=12900&filters_source=seo_landing&longitude=-3.69196&latitude=40.41956&order_by=closest"
    r = requests.get(url)
    title_dict = {}

    for elemento in r.json().get("search_objects"):
        title_dict[elemento.get("title")] = elemento.get("price")

    return Response(json.dumps(title_dict), status=200, mimetype="application/json")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)