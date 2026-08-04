import pytest


class FakeAPI:

    def __init__(self, role):
        self.headers = {
            "User": {
                "Authorization": "Bearer user_token"
            },
            "Admin": {
                "Authorization": "Bearer admin_token"
            },
            "Guest": {
                "Authorization": "Bearer guest_token"
            }
        }[role]

    def get_profile(self):
        return {
            "status_code": 200,
            "headers": self.headers
        }


@pytest.fixture
def api(request):
    return FakeAPI(request.param)