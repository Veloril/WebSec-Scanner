from data import HTTP_METHODS

def check_http_methods(client):
    report = {
        "module": "HTTP Methods Discovery",
        "status": "INFO",
        "allowed_methods": []
    }

    for method in HTTP_METHODS:
        response = client.request(method, "/")

        if response.status_code < 400:
            report["allowed_methods"].append(method)

    return report
