from core import SecurityScanner


def main():
    print("=== WebSec Scanner v1.0 ===")
    target = input("Enter target URL (e.g., https://example.com): ").strip()

    if not target.startswith(('https://', 'http://')):
        print("Error: URL must start with http:// o r https://")
        return

    try:
        scanner = SecurityScanner(target)
        print(f"\nStarting security scan for: {target}")

        print("[1/3] Analyzing Security Headers...")
        scanner.check_security_headers()

        print("[2/3] Discovering Allowed HTTP Methods...")
        scanner.check_http_methods()

        print("[3/3] Verifying SSL/TLS Certificate..")
        scanner.check_certificate()

        scanner.save_report()
        print("\nScan completed successfully.")

    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
    except Exception as e:
        print(f"\nError occurred: {e}")

if __name__ == "__main__":
    main()