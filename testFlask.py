import json

from flask import Flask, Response, request

import requests
from productInfo import Product

app = Flask(__name__)

@app.route("/")
def wellcome():
    mensaje = """
            BIENVENIDOS A LA DEMOSTRCION DEL USO DE UNA API 
                     TRATAMIENTO DE DATOS GRUPO 2
            Para esta demostracion se ha creado 5 funciones que pueden ser ejecutadas a traves de http://127.0.0.1:5000
            1.- /search listar todos los productos basados en el parametros keyword que estamos enviando (Parameters: productName).
            2.- /searchLowerPrice listar todos productos que tengan un valor menor al valor que estemos enviando en la URL (Parameters: productName, productPrice).
            3.- /searchTop3HigherPrices listar los 3 productos mas caros con respecto al valor enviado en la URL (Parameters: productName, productPrice).
            4.- /searchProductCondition listar todos los productos que se estan buscando en base a su condicion de uso (Parameters: productName, productcondition).
    """
    return Response(mensaje, status=200, mimetype="text/plain")

@app.route("/search")
def search_method_keyword():
    # Mandar el keyword mediante el URL y anadirlo a la busqueda API (mostrar todos los productos)
    # se necesita parametro del tipo de producto

    productName = request.args.get("productName", "")

    return Response(json.dumps(build_url_request(productName)), status=200, mimetype="application/json")

@app.route("/searchLowerPrice")
def search_method_price():
    # Mandar todos productos que tengan un valor menor al valor que estemos mandando en la URL
    # se necesita parametro del tipo de producto y precio
    # RUDEL H
    productName = request.args.get("productName", "")
    productPrice = request.args.get("productPrice", "")

    productList = build_url_request(productName)
    productsFiltered = list(filter(lambda product: product["price"] <= float(productPrice), productList))

    return Response(json.dumps(productsFiltered[:1]), status=200, mimetype="application/json")

@app.route("/searchTop3HigherPrices")
def search_higher_price():
    # Mandar los 3 productos mas caros con respecto al valor dado en la URL
    # se necesita parametro del tipo de producto y precio
    # ERICK
    productName = request.args.get("productName", "")
    productPrice = request.args.get("productPrice", "")

    productList = build_url_request(productName)
    productsFiltered = list(filter(lambda product: product["price"] >= float(productPrice), productList))

    return Response(json.dumps(productsFiltered[:3]), status=200, mimetype="application/json")

@app.route("/searchProductCondition")
def search_item_condition():
    # Mandar todos los items que se estan buscando depende de su condicion de uso
    # se necesita parametro y la condicion del producto
    # CARLOS
    # URL: 127.0.0.1:5000/searchProductCondition?productName=ps4&productcondition=fair
    # Parametros: new/as_good_as_new/good/fair/has_given_it_all
    productName = request.args.get("productName", "")
    productcondition = request.args.get("productcondition", "")

    return Response(json.dumps(build_url_request(productName, productcondition)), status=200, mimetype="application/json")

def build_url_request(searchParameter, status=""):
    # Usar clase Producto para organizar la informacion y devolver un diccionario armado desde esa clase
    # FERNANDO
    if status == "":
        url = f"https://api.wallapop.com/api/v3/general/search?keywords={searchParameter}%20&category_ids=12900&filters_source=seo_landing&longitude=-3.69196&latitude=40.41956"
    else:
        url = f"https://api.wallapop.com/api/v3/general/search?keywords={searchParameter}&filters_source=quick_filters&latitude=40.418965&longitude=-3.711781&condition={status}"

    r = requests.get(url)
    product_list = [] #Creamos la lista vacía

    for elemento in r.json().get("search_objects"):

        product = Product(elemento.get("title"),elemento.get("price"),elemento.get("description"),elemento.get("currency"))
        product_list.append(product.to_dict())

    return product_list

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)