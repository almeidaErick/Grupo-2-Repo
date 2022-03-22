import requests
class Product:

    def __init__(self, product, price):
        self.product = product
        self.price = price

    def __str__(self):
        search = input("Ingrese el objeto que esta buscando")
        url = f"https://api.wallapop.com/api/v3/general/search?keywords={search}%20&category_ids=12900&filters_source=seo_landing&longitude=-3.69196&latitude=40.41956"
        datos = requests.get(url)
        lista = []
        for elementos in datos.json().get("search_objects"):
            dic = {'Title': elementos.get("title"), 'Description': elementos.get("description"),
                   'Distance': elementos.get("distance"), 'Currency': elementos.get('currency'),
                   'Price': elementos.get("price")}
            lista.append(dic)
        return str(lista)

    def to_dict(self):
        # complete this
        # JORGE
        return