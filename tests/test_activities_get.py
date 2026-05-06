from src.app import activities


def test_get_activities_returns_initial_data(client, initial_activities):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200
    assert response.json() == initial_activities
    assert len(activities) == len(initial_activities)
