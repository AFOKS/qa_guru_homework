success_registration = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "username": {
            "type": "string"
        },
        "firstName": {
            "type": "string"
        },
        "lastName": {
            "type": "string"
        },
        "email": {
            "type": "string"
        },
        "remoteAddr": {
            "type": "string"
        }
    },
    "required": [
        "id",
        "username",
        "firstName",
        "lastName",
        "email",
        "remoteAddr"
    ]
}


registration_error = {
    "type": "object",
    "additionalProperties": True
}