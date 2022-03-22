import requests
class Product:
    def __init__(self, product, price,search):
        self.product = product
        self.price = price

    def __str__(self):
        url=f"https://api.wallapop.com/api/v3/general/search?keywords={self.search}%20&category_ids=12900&filters_source=seo_landing&longitude=-3.69196&latitude=40.41956&order_by=closest"
        datos = requests.get(url)
        lista=[]
        for elementos in datos.json().get("search_objects"):
            diccionario = {"Title": elementos.get("title")+"\n", "Description": elementos.get("description")+"\n",
                    "Distance": elementos.get("distance")+"\n", "Currency": elementos.get("currency")+"\n",
                    "Price": elementos.get("price")+"\n\n"
                    }
            lista.append(diccionario)

        return str(lista)

    def to_dict(self):
        # complete this
        # JORGE
        return