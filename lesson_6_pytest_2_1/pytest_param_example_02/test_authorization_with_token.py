import pytest

@pytest.fixture
def auth_headers(request):
    role = request.param

    headers = {
        "User": {
            "Authorization": "Bearer user_token"
        },
        "Admin": {
            "Authorization": "Bearer admin_token"
        },
        "Guest": {
            "Authorization": "Bearer guest_token"
        }
    }

    return headers[role]

@pytest.mark.parametrize(
    "auth_headers",
    ["User", "Admin", "Guest"],
    indirect=True
)

# добавил тест для вывода заголовков
def test_api_authorization(auth_headers):
    print(f"-> Заголовки запроса: {auth_headers}")

    assert "Authorization" in auth_headers