# WebSec Scanner

Lightweight modular web security scanner focused on detecting common
**OWASP Top 10** security misconfigurations in web applications.

**This project is designed as an educational and defensive security tool,
demonstrating practical web security analysis rather than exploitation.**

---

## Features

Currently implemented modules:

- **Security Headers Analysis**
  - Detection of missing security headers.
  - Detailed descriptions of risks and remediation recommendations.

- **HTTP Methods Discovery**
  - Detection of enabled HTTP methods.

- **SSL/TLS certificate Verification**
  - Check certificate validity and expiration dates.

---

##  Project Philosophy

The scanner follows these principles:

- Defensive security only
- No exploitation or brute-force techniques
- Focus on misconfigurations and best practices
- Modular and extensible architecture
- Clear, structured findings suitable for reporting

---

### Dependencies
- Python 3.10+
- requests

### Installation
```bash
git clone https://github.com/veloril/websec-scanner.git
```
```bash
pip install -r requirements.txt
```
```bash
python main.py
```
## Project Structure

```text
websec-scanner/
├── modules/
│   ├── certificate.py
│   ├── http_headers.py
│   ├── http_methods.py
│   ├── http_client.py
│   └── __init__.py
├── data/
│   ├── http_methods.py
│   ├── security_headers.py
│   └── __init__.py
├── сore/
│   ├── scanner.py
│   └── __init__.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
