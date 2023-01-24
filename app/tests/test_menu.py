import json


router_menu = '/api/v1/menus/'
router_menu_id = 'api/v1/menus/{id}/'

# def test_get_empty_menu(client):
#     response = client.get(router_menu)
#     assert response.status_code == 200
#     assert response.json() == []

def test_get_menu_not_found(client):
    response = client.get(router_menu_id.format(id=5))
    assert response.status_code == 404
    assert response.json() == {'detail': 'menu not found'}

def test_get_menu_by_id(client):
    response = client.get(router_menu_id.format(id=1))
    assert response.status_code == 200
    assert response.json() == {
        'title': 'New menu',
        'description': 'New menu description',
        'id': '1',
        'submenus_count': 1,
        'dishes_count': 0
    }

def test_create_menu(client):
    test_data = {"title": "MenuTest", "description": "MenuTest description"}
    response = client.post(router_menu, content=json.dumps(test_data))
    assert response.status_code == 201
    assert response.json() == {
        'title': 'MenuTest',
        'description': 'MenuTest description',
        'id': '2',
        'submenus_count': 0,
        'dishes_count': 0
    }

def test_update_menu(client):
    response = client.patch(
        router_menu_id.format(id=1),
        json={
            'title': 'Updated menu',
            'description': 'Updated menu description'
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'title': 'Updated menu',
        'description': 'Updated menu description',
        'id': '1',
        'submenus_count': 1,
        'dishes_count': 0
    }

def test_update_menu_not_found(client):
    response = client.patch(
        router_menu_id.format(id=5),
        json={'title': 'My updated menu', 'description': 'My updated menu description'},
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'menu not found'}

def test_delete_menu(client):
    response = client.delete(router_menu_id.format(id=1))
    assert response.status_code == 200
    assert response.json() == {'message': 'The menu has been deleted'}

def test_delete_menu_not_found(client):
    response = client.delete(
        router_menu_id.format(id=1)
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'menu not found'}