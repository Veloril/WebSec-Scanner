import ssl
import socket
import re
from datetime import datetime


def get_certificate_expiry(url):
    context = ssl.create_default_context()

    try:
        match = re.search(r'^https?://([^/]+)', url)
        hostname = match.group(1)
        with socket.create_connection((hostname, 443), timeout=3) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

                expiry_str = cert['notAfter']
                expiry_date = datetime.strptime(expiry_str, '%b %d %H:%M:%S %Y %Z')

                days_left = (expiry_date - datetime.utcnow()).days
                return days_left

    except Exception as e:
        return f"Error: {e}"