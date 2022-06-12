def updated_error_serializer(error) -> dict:
    serialize_updated_error = {}
    if error["name"] != None:
        serialize_updated_error["name"] = error["name"]
    if error["priority"] != None:
        serialize_updated_error["priority"] = error["priority"]
    if error["involved"] != None:
        serialize_updated_error["involved"] = error["involved"]
    if error["next_step"] != None:
        serialize_updated_error["next_step"] = error["next_step"]
    if error["update_date"] != None:
        serialize_updated_error["update_date"] = error["update_date"]
    return serialize_updated_error

def updated_errors_serializer(errors) -> list:
    return [updated_error_serializer(error) for error in errors]