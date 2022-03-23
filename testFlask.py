import json
from flask import Flask, Response
import requests
#from productInfo import Product

app = Flask(__name__)

@app.route("/")
def wellcome():
    mensaje = """
            BIENVENIDOS A LA DEMOSTRCION DEL USO DE UNA API 
                     TRATAMIENTO DE DATOS GRUPO 2
            Para esta demostracion se ha creado 5 funciones
            1.- SEARCH listar todos los productos basados en el parametros keyword que estamos enviando.
            2.- SEARCH LOW PRICE listar todos productos que tengan un valor menor al valor que estemos enviando en la URL.
            3.- SEARCH HIGHER PRICE listar los 3 productos mas caros con respecto al valor enviado en la URL.
            4.- SEARCH PRODUCT CONDITION listar todos los productos que se estan buscando en base a su condicion de uso.
            5.- SEARCH PARAMETER Usar clase Producto para organizar la informacion y devolver un diccionario armado desde esa clase.
    """
    return Response(mensaje, status=200, mimetype="text/plain")

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
    return Response(json.dumps(build_url_request("libros")), status=200, mimetype="application/json")

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
        title_dict = {"title": elemento.get("title"), "description": elemento.get("description"),
                      "price": elemento.get("price"), "currency": elemento.get("currency")}
        product_list.append(title_dict)

    return product_list

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)