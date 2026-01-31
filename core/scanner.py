from modules import check_security_headers, check_http_methods, get_certificate_expiry, HttpClient
from datetime import datetime
import json
import os

class SecurityScanner:
    def __init__(self, url):
        self.url = url
        self.results = []
        self.client = HttpClient(base_url=self.url)

    def check_security_headers(self):
        response = self.client.get("/")
        report = check_security_headers(response)
        self.results.append(report)
        return report

    def check_http_methods(self):
        report = check_http_methods(self.client)
        self.results.append(report)
        return report

    def check_certificate(self):
        result = get_certificate_expiry(self.url)
        if isinstance(result, int):
            report = {
                "test": "TLS Certificate Validity",
                "status": "INFO",
                "findings": f"TLS certificate expires in {result} days."
            }
        else:
            report = {
                "test": "TLS Certificate Validity",
                "status": "ERROR",
                "findings": f"Could not check certificate: {result}"
            }
        self.results.append(report)
        return report

    def save_report(self, filename=None):
        report_dir = "reports"

        if not os.path.exists(report_dir):
            os.makedirs(report_dir)

        if not filename:
            timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
            clean_url = self.url.replace("https://", "").replace("http://", "").replace("/", "-")
            filename = f"report_{clean_url}_{timestamp}.json"

        filepath = os.path.join(report_dir, filename)

        full_report = {
            "target": self.url,
            "scan_time": datetime.now().isoformat(),
            "results": self.results
        }

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(full_report, f, indent=4, ensure_ascii=False)
            print(f"Report saved to {filepath}")
        except Exception as e:
            print(f"Error saving report: {e}")