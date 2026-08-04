import pytest


@pytest.mark.parametrize(
    "api",
    ["User", "Admin", "Guest"],
    indirect=True
)
def test_api_authorization(api):
    response = api.get_profile()

    assert response["status_code"] == 200
    assert "Authorization" in response["headers"]

    print(response["headers"])