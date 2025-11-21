import json

# Load swagger/openapi JSON file
with open("swagger.json", "r") as f:
    swagger = json.load(f)

paths = swagger.get("paths", {})

allowed_methods = ["get", "post", "patch", "delete"]

for path, path_info in paths.items():
    for method, details in path_info.items():
        if method.lower() not in allowed_methods:
            continue

        # Try to get the requestBody schema for POST/PATCH
        payload = {}
        request_body = details.get("requestBody", {})
        if "content" in request_body:
            content = request_body.get("content", {})
            app_json = content.get("application/json", {})
            schema = app_json.get("schema", {})

            if "properties" in schema:
                for k, v in schema["properties"].items():
                    payload[k] = f"<{v.get('type', 'value')}>"
            elif schema.get("type") == "array":
                payload = ["<item>"]

        print(f"METHOD: {method.upper()}")
        print(f"URL: {path}")
        print(f"PAYLOAD EXAMPLE:\n{json.dumps(payload, indent=4)}\n")
