"""Import acme Product to use in acme report and Import random
for random numbers
"""
from acme import Product
from random import sample, randint, uniform

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """Making random products"""
    products = []
    for x in range(num_products):
        product = Product(name=f"{sample(ADJECTIVES, 1)} {sample(NOUNS, 1)}",
                          price=randint(5, 100), weight=randint(5, 100),
                          flammability=uniform(0.0, 2.5))
        products.append(product)
    return products


def inventory_report(products):
    """Generating the Inventoy Report"""
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    names = len(products)    

    cost = []
    for x in range(30):
        cost.append(products[x].price)
    
    weight = []
    for x in range(30):
        weight.append(products[x].weight)

    fire = []
    for x in range(30):
        fire.append(products[x].flammability)

    print(f"Unique name = {names}")
    print(f"Average Price: {sum(cost)/30}")
    print(f"Avg weight: {sum(weight)/30}")
    print(f"avg fire {sum(fire)/30}")


if __name__ == '__main__':
    inventory_report(generate_products())
