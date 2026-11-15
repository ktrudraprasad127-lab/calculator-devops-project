import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.parametrize("numbers, operation, expected", [
    ("10,20,30", "add", "60.0"),
    ("100,20,10", "subtract", "70.0"),
    ("2,3,4", "multiply", "24.0"),
    ("100,2,5", "divide", "10.0"),
])
def test_calculations(client, numbers, operation, expected):
    response = client.post("/", data={
        "numbers": numbers,
        "operation": operation
    })

    assert expected in response.get_data(as_text=True)


def test_division_by_zero(client):
    response = client.post("/", data={
        "numbers": "10,0",
        "operation": "divide"
    })

    assert "Cannot divide by zero" in response.get_data(as_text=True)
