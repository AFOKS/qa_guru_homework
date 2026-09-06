success_auth = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "refresh": {
            "type": "string"
        },
        "access": {
            "type": "string"
        }
    },
    "required": [
        "refresh",
        "access"
    ]
}


wrong_credentials_auth = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "detail": {
            "type": "string"
        }
    },
    "required": [
        "detail"
    ]
}


missing_password_auth = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "password": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
    "required": [
        "password"
    ]
}


unsupported_media_type = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "detail": {
            "type": "string"
        }
    },
    "required": [
        "detail"
    ]
}

missing_username_auth = {
    "type": "object",
    "properties": {
        "username": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
    "required": ["username"]
}


missing_username_password_auth = {
    "type": "object",
    "properties": {
        "username": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "password": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
    "required": ["username", "password"]
}