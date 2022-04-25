from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello":"World"}

def test_fetch_errors():
    response = client.get("/api/v1/errors")
    assert response.status_code == 200

def test_fetch_error_by_name_ok():
    response = client.get("/api/v1/errors/404 NOT FOUND")
    assert response.status_code == 200
    assert response.json()["name"] == "404 NOT FOUND"

def test_fetch_error_by_name_wrong():
    response = client.get("/api/v1/errors/1000")
    assert response.status_code == 404

def test_register_error_ok():
    response = client.post("/api/v1/errors", json={
        "name": "202 Bad",
        "priority": "Low",
        "involved": [
            "David Rimon",
            "Chen Ben Ezra",
            "Dor",
            "Laila"
        ],
        "next_step": "nothing to do",
        "accept_date": "2022-04-25"
    })
    assert response.status_code == 200
    
def test_register_error_wrong_json():
    response = client.post("/api/v1/errors", json={
        "name": "202 Bad",
        "priority": "Low",
        "involved": [
            "David Rimon",
            "Chen Ben Ezra",
            "Dor",
            "Laila"
        ],
        "next_step": "nothing to do"
    })
    assert response.status_code == 422

def test_register_error_already_exists():
    response = client.post("/api/v1/errors", json={
        "name": "200 OK",
        "priority": "Low",
        "involved": [
            "David Rimon",
            "Chen Ben Ezra",
            "Dor",
            "Laila"
        ],
        "next_step": "nothing to do",
        "accept_date": "2022-04-25"
    })
    assert response.status_code == 409
    assert response.json() == {"detail": "error called 200 OK already exists"}

def test_delete_error():
    response = client.delete("/api/v1/errors/200 OK")
    assert response.status_code == 200
    assert response.json() == {"error 200 OK": "removed successfully"}

def test_delete_error_not_exists():
    response = client.delete("/api/v1/errors/1000")
    assert response.status_code == 404
    assert response.json() == {"detail": "error called 1000 does not found"}

# def test_update_error():
#     response = client.put("/api/v1/errors/200 OK", json={
#         "name": "200 OK",
#         "priority": "Low",
#         "involved": [
#             "Guy",
#             "Dodo"
#         ],
#         "next_step": "Do not do nothing",
#         "update_date": "1994-11-24 10:10:00"
#     })
#     assert response.status_code == 200
#     assert response.json() == {"error 200 OK": "updated seccessfully"}