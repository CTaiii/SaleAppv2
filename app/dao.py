def get_categories():
    return [{
        "id": 1,
        "name": "Mobile"
    }, {
        "id": 2,
        "name": "Tablet"
    }]


def get_products(kw):
    products = [{
        "id": 1,
        "name": "IP15",
        "price": 20,
        "image": "https://cdn.dienthoaigiakho.vn/photos/1694577894457-iPhone15Pr-BL3.jpg",
        "category_id": 1
    },
        {
            "id": 2,
            "name": "IP14",
            "price": 15,
            "image": "https://cdn.dienthoaigiakho.vn/photos/1675237288530-600-600-ip14prm-old.jpg",
            "category_id": 1
        },
        {
            "id": 3,
            "name": "Mobile",
            "price": 20,
            "image": "https://cdn.dienthoaigiakho.vn/photos/1696922859873-iPhone-14-pl-128.jpg",
            "category_id": 1
        },
        {
            "id": 4,
            "name": "Mobile",
            "price": 20,
            "image": "https://cdn.dienthoaigiakho.vn/photos/1675237288530-600-600-ip14prm-old.jpg",
            "category_id": 1
        },
        {
            "id": 5,
            "name": "Mobile",
            "price": 20,
            "image": "https://cdn.dienthoaigiakho.vn/photos/1675237288530-600-600-ip14prm-old.jpg",
            "category_id": 1
        }
    ]
    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products
