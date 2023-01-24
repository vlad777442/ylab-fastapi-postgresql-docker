
router_dish = '/api/v1/menus/1/submenus/1/dishes'
router_dish_id = 'api/v1/menus/1/submenus/1/dishes/{id}/'

def test_get_empty_dish(client):
    response = client.get(router_dish)
    assert response.status_code == 200
    assert response.json() == []

# def test_get_dish(client, dish_1):
#     response = client.get(
#         router_dish_id.format(id=1)
#     )
#     assert response.status_code == 200
#     assert response.json() == dict(dish_1)

def test_create_dish(client, db, submenu_1):
    response = client.post(
        router_dish,
        json={
            'title': 'My dish',
            'description': 'Dish description',
            'price': '13.99'
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        'title': 'My dish',
        'description': 'Dish description',
        'id': '1',
        'price': '13.99'
    }


def test_update_dish(client):
    response = client.patch(
        router_dish_id.format(id=1),
        json={
            'title': 'My updated dish',
            'description': 'Dish description',
            'price': '13.99'
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'title': 'My updated dish',
        'description': 'Dish description',
        'id': '1',
        'price': '13.99'
    }

def test_update_dish_not_found(client):
    response = client.patch(
        router_dish_id.format(id=5),
        json={
            'title': 'My updated dish',
            'description': 'Dish description',
            'price': '13.99'
        }
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'dish not found'}

def test_delete_dish(client):
    response = client.delete(
        router_dish_id.format(id=1)
    )
    assert response.status_code == 200
    assert response.json() == {'message': 'The dish has been deleted'}

def test_delete_dish_not_found(client):
    response = client.delete(
        router_dish_id.format(id=1)
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'dish not found'}