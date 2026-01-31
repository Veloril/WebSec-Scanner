from data import SECURITY_HEADERS


def check_security_headers(response):
    report = {
        "test": "Checking Security Headers",
        "status": "INFO",
        "findings": []
    }

    for header, info in SECURITY_HEADERS.items():
        if not response.headers.get(header):
            report["findings"].append({
                "header": header,
                "status": "MISSING",
                "owasp": info["owasp"],
                "description": info["description"],
                "recommendations": info["recommendation"]
            })

    return report
