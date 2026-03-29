from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# TEAM TESTS

def test_create_team():
    response = client.post("/teams/", json={
        "name": "Lakers",
        "city": "Los Angeles",
        "coach": "JJ Redick",
        "wins": 0,
        "losses": 0
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Lakers"
    assert data["city"] == "Los Angeles"

def test_get_teams():
    response = client.get("/teams/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_team_by_id():
    # сначала создаём команду
    create = client.post("/teams/", json={
        "name": "Bulls",
        "city": "Chicago",
        "coach": "Billy Donovan",
        "wins": 0,
        "losses": 0
    })
    team_id = create.json()["id"]

    response = client.get(f"/teams/{team_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Bulls"

def test_get_team_not_found():
    response = client.get("/teams/99999")
    assert response.status_code == 404

def test_update_team():
    create = client.post("/teams/", json={
        "name": "Nets",
        "city": "Brooklyn",
        "coach": "Jordi Fernandez",
        "wins": 0,
        "losses": 0
    })
    team_id = create.json()["id"]

    response = client.patch(f"/teams/{team_id}", json={
        "name": "Nets",
        "city": "Brooklyn",
        "coach": "Jordi Fernandez",
        "wins": 10,
        "losses": 5
    })
    assert response.status_code == 200
    assert response.json()["wins"] == 10

def test_delete_team():
    create = client.post("/teams/", json={
        "name": "Hornets",
        "city": "Charlotte",
        "coach": "Charles Lee",
        "wins": 0,
        "losses": 0
    })
    team_id = create.json()["id"]

    response = client.delete(f"/teams/{team_id}")
    assert response.status_code == 200

    # проверяем что удалилась
    response = client.get(f"/teams/{team_id}")
    assert response.status_code == 404


# PLAYER TESTS

def test_create_player():
    # сначала создаём команду
    team = client.post("/teams/", json={
        "name": "Warriors",
        "city": "San Francisco",
        "coach": "Steve Kerr",
        "wins": 0,
        "losses": 0
    })
    team_id = team.json()["id"]

    response = client.post("/players/", json={
        "name": "Stephen",
        "surname": "Curry",
        "avg_pts": 24.5,
        "avg_assists": 6.3,
        "avg_reb": 4.5,
        "team_id": team_id
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Stephen"
    assert data["surname"] == "Curry"

def test_get_players():
    response = client.get("/players/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_player_by_id():
    create = client.post("/players/", json={
        "name": "LeBron",
        "surname": "James",
        "avg_pts": 25.0,
        "avg_assists": 7.0,
        "avg_reb": 7.5,
        "team_id": None
    })
    player_id = create.json()["id"]

    response = client.get(f"/players/{player_id}")
    assert response.status_code == 200
    assert response.json()["surname"] == "James"

def test_get_player_not_found():
    response = client.get("/players/99999")
    assert response.status_code == 404

def test_update_player():
    create = client.post("/players/", json={
        "name": "Kevin",
        "surname": "Durant",
        "avg_pts": 27.0,
        "avg_assists": 5.0,
        "avg_reb": 6.0,
        "team_id": None
    })
    player_id = create.json()["id"]

    response = client.patch(f"/players/{player_id}", json={
        "name": "Kevin",
        "surname": "Durant",
        "avg_pts": 29.0,
        "avg_assists": 5.0,
        "avg_reb": 6.0,
        "team_id": None
    })
    assert response.status_code == 200
    assert response.json()["avg_pts"] == 29.0

def test_delete_player():
    create = client.post("/players/", json={
        "name": "James",
        "surname": "Harden",
        "avg_pts": 22.0,
        "avg_assists": 8.0,
        "avg_reb": 5.0,
        "team_id": None
    })
    player_id = create.json()["id"]

    response = client.delete(f"/players/{player_id}")
    assert response.status_code == 200

    response = client.get(f"/players/{player_id}")
    assert response.status_code == 404

def test_update_team_not_found():
    response = client.patch("/teams/99999", json={
        "name": "Test",
        "city": "Test",
        "coach": "Test",
        "wins": 0,
        "losses": 0
    })
    assert response.status_code == 404

def test_delete_team_not_found():
    response = client.delete("/teams/99999")
    assert response.status_code == 404

def test_update_player_not_found():
    response = client.patch("/players/99999", json={
        "name": "Test",
        "surname": "Test",
        "avg_pts": 0.0,
        "avg_assists": 0.0,
        "avg_reb": 0.0,
        "team_id": None
    })
    assert response.status_code == 404

def test_delete_player_not_found():
    response = client.delete("/players/99999")
    assert response.status_code == 404

def test_create_player_with_invalid_team():
    response = client.post("/players/", json={
        "name": "Test",
        "surname": "Player",
        "avg_pts": 0.0,
        "avg_assists": 0.0,
        "avg_reb": 0.0,
        "team_id": 99999
    })
    assert response.status_code == 404