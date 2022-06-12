def error_serializer(error) -> dict:
    serialize_error = {
        "id": str(error["_id"]),
        "name": error["name"],
        "priority": error["priority"],
        "involved": error["involved"],
        "next_step": error["next_step"],
        "accept_date": error["accept_date"],
    }
    if error["update_date"] != None:
        serialize_error["update_date"] = error["update_date"]
    return serialize_error

def errors_serializer(errors) -> list:
    return [error_serializer(error) for error in errors]