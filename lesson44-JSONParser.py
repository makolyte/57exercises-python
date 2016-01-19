import json
from pprint import pprint

jsonDaty = """
{
"products" :
    [
    {"name":"Widget", "price":25.00, "qty":5},
    {"name":"Thing", "price":15.00, "qty":5},
    {"name":"Doodad", "price":5.00, "qty":10}
    ]
}
"""

data = json.loads(jsonDaty)

for d in data["products"]:
    print d["name"]
    print d["price"]
    print d["qty"]