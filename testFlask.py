import json
from flask import Flask, Response,request
import requests
from productInfo import Product

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Anadir mensaje de bienvenida que se pueda observar en postman y/o navegador
    # no se necesita parametro
    # LUIS
    return "QUE MAS VE"

@app.route("/search")
def search_method_keyword():
    # Mandar el keyword mediante el URL y anadirlo a la busqueda API (mostrar todos los productos)
    # se necesita parametro del tipo de producto
    # DANI
    return Response(json.dumps(build_url_request("libros")), status=200, mimetype="application/json")

@app.route("/searchLowerPrice")
def search_method_price():
    # Mandar todos productos que tengan un valor menor al valor que estemos mandando en la URL
    # se necesita parametro del tipo de producto y precio
    # RUDEL
    return Response(json.dumps(build_url_request("libros")), status=200, mimetype="application/json")

@app.route("/searchTop3HigherPrices")
def search_higher_price():
    # Mandar los 3 productos mas caros con respecto al valor dado en la URL
    # se necesita parametro del tipo de producto y precio
    # ERICK
    return Response(json.dumps(build_url_request("libros")), status=200, mimetype="application/json")

@app.route("/searchProductCondition")
def search_item_condition():
    # Mandar todos los items que se estan buscando depende de su condicion de uso
    # se necesita parametro y la condicion del producto
    # CARLOS
    # URL: 127.0.0.1:5000/searchProductCondition?productName=ps4&productcondition=fair
    # Parametros: new/as_good_as_new/good/fair/has_given_it_all
    productName = request.args.get("productName", "")
    productcondition = request.args.get("productcondition", "")

    return Response(json.dumps(build_url_request(productName,productcondition)), status=200, mimetype="application/json")

def build_url_request(searchParameter, status=""):
    # Usar clase Producto para organizar la informacion y devolver un diccionario armado desde esa clase
    # FERNANDO
    if status == "":
        url = f"https://api.wallapop.com/api/v3/general/search?keywords={searchParameter}%20&category_ids=12900&filters_source=seo_landing&longitude=-3.69196&latitude=40.41956"
    else:
        url = f"https://api.wallapop.com/api/v3/general/search?keywords={searchParameter}&filters_source=quick_filters&latitude=40.418965&longitude=-3.711781&condition={status}"

    r = requests.get(url)
    product_list = []

    for elemento in r.json().get("search_objects"):
        product=Product(elemento.get("title"),elemento.get("price"),elemento.get("description"),elemento.get("currency"))
        product_list.append(product.to_dict())

    return product_list

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)