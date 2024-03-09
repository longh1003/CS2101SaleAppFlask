import json

def load_catergory():
    with open('data/category.json', encoding='utf-8') as f:
        return json.load(f)
def load_product():
    with open('data/product.json', encoding='utf-8') as f:
        products = json.load(f)
        return products

if __name__ == '__main__':
    print(load_product())