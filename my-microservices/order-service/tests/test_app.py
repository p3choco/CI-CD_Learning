import pytest
from src.app import app

@pytest.fixture
def client():
    """
    Udostępnia klienta Flask do testów.
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_orders_empty(client):
    """
    Sprawdza, czy na starcie lista zamówień jest pusta.
    """
    response = client.get('/orders')
    assert response.status_code == 200
    assert response.json == []

def test_create_order(client):
    """
    Tworzy nowe zamówienie i sprawdza, czy jest zwracane w odpowiedzi.
    """
    new_order = {"user_id": 123, "status": "NEW", "amount": 99.99}
    response = client.post('/orders', json=new_order)
    assert response.status_code == 201
    created_order = response.json
    assert "order_id" in created_order
    assert created_order["user_id"] == 123
    assert created_order["status"] == "NEW"
    assert created_order["amount"] == 99.99

def test_get_order_by_id(client):
    """
    Po utworzeniu zamówienia sprawdzamy pobranie go po order_id.
    """
    # Najpierw stwórz zamówienie
    new_order = {"user_id": 777, "status": "NEW", "amount": 150}
    create_resp = client.post('/orders', json=new_order)
    order_id = create_resp.json["order_id"]

    # Następnie pobierz go po ID
    get_resp = client.get(f'/orders/{order_id}')
    assert get_resp.status_code == 200
    order_data = get_resp.json
    assert order_data["user_id"] == 777
    assert order_data["amount"] == 150

def test_order_not_found(client):
    """
    Zapytanie o nieistniejące zamówienie powinno dać błąd 404.
    """
    response = client.get('/orders/999999')
    assert response.status_code == 404
    assert response.json["error"] == "Order not found"
