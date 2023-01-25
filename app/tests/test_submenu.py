
router_submenu = '/api/v1/menus/1/submenus/'
router_submenu_id = 'api/v1/menus/1/submenus/{id}/'

def test_get_empty_submenu(client):
    response = client.get(router_submenu)
    assert response.status_code == 200
    assert response.json() == []

# def test_get_submenu(client, submenu_1):
#     response = client.get(router_submenu_id.format(id=1))
#     assert response.status_code == 200
#     assert response.json() == (dict(submenu_1))

def test_get_submenu_not_found(client):
    response = client.get(router_submenu_id.format(id=1))
    assert response.status_code == 404
    assert response.json() == {'detail': 'submenu not found'}

# def test_create_submenu(client, submenu_1, db):
#     response = client.post(
#         router_submenu,
#         json={'title': 'My submenu', 'description': 'My submenu description'},
#     )
#     assert response.status_code == 201
#     assert response.json() == {
#         'title': 'My submenu',
#         'description': 'My submenu description',
#         'id': '2',
#         'dishes_count': 0,
#     }
def test_create_submenu1(client):
    response = client.post(
        "/api/v1/menus/2/submenus",
        json={"title": "My submenu 2", "description": "My submenu description 2", "dishes_count": 0},
    )
    assert response.json() == {
        "id": "2",
        "title": "My submenu 2",
        "description": "My submenu description 2",
        "dishes_count": 0,
    }

def test_update_submenu(client, db):
    response = client.patch(
        router_submenu_id.format(id=2),
        json={'title': 'My updated submenu', 'description': 'My updated submenu description'},
    )
    assert response.status_code == 200
    assert response.json() == {
        'title': 'My updated submenu',
        'description': 'My updated submenu description',
        'id': '2',
        'dishes_count': 0
    }

def test_update_submenu_not_found(client):
    response = client.patch(
        router_submenu_id.format(id=5),
        json={'title': 'My updated submenu', 'description': 'My updated submenu description'},
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'submenu not found'}

def test_delete_submenu(client, db):
    resp = client.delete(
        router_submenu_id.format(id=2)
    )
    assert resp.status_code == 200
    assert resp.json() == {'message': 'The submenu has been deleted'}

def test_delete_submenu_not_found(client):
    resp = client.delete(
        router_submenu_id.format(id=2)
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'submenu not found'}
