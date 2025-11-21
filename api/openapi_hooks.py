# api/openapi_hooks.py

def limit_methods_hook(endpoints, generator, request, public):
    """
    Keep only GET, POST, PATCH, DELETE endpoints in the OpenAPI/Swagger schema.
    """
    allowed = ['get', 'post', 'patch', 'delete']
    filtered = []

    for path, path_regex, method, callback in endpoints:
        if method.lower() in allowed:
            filtered.append((path, path_regex, method, callback))

    return filtered
