#!/usr/bin/env python3
"""
FinalCTF Security Testing Tool
Author: Your Name
Course: CYB-3633
Description:
    Lightweight automated security-testing tool for SQLi, XSS,
    and access-control validation on intentionally vulnerable web apps.
"""

import requests
import argparse
import sys


def banner():
    print(r"""
  ______ _           _ _   _____ _______ _____ 
 |  ____| |         | | | / ____|__   __/ ____|
 | |__  | | ___  ___| | |/ /       | | | (___  
 |  __| | |/ _ \/ __| | | |        | |  \___ \ 
 | |    | |  __/ (__| | | \____    | |  ____) |
 |_|    |_|\___|\___|_|_|\_____|   |_| |_____/ 

    FinalCTF — Automated Web Security Testing
    """)


def test_sqli(url):
    payload = "' OR 1=1--"
    full_url = url + payload

    print(f"[+] Testing SQL Injection at: {full_url}")
    try:
        r = requests.get(full_url, timeout=5)
    except Exception as e:
        print(f"[!] Request error: {e}")
        return

    indicators = ["SQL", "sql", "database", "syntax", "error"]

    if any(i in r.text for i in indicators):
        print("[!] Possible SQL Injection vulnerability detected!")
    else:
        print("[+] No SQLi detected based on response.")


def test_xss(url):
    payload = "<script>alert('XSS')</script>"
    print(f"[+] Testing XSS at: {url}")

    try:
        r = requests.get(url, params={"q": payload}, timeout=5)
    except Exception as e:
        print(f"[!] Request error: {e}")
        return

    if payload in r.text:
        print("[!] Reflected XSS vulnerability detected!")
    else:
        print("[+] No reflected XSS detected.")


def test_admin_access(url):
    print(f"[+] Checking admin access at: {url}")

    try:
        r = requests.get(url, timeout=5)
    except Exception as e:
        print(f"[!] Request error: {e}")
        return

    if r.status_code == 200:
        print("[!] Admin page is publicly accessible! HIGH RISK.")
    else:
        print("[+] Access appears to be restricted.")


def main():
    banner()
    parser = argparse.ArgumentParser(description="FinalCTF Web Security Testing Tool")

    parser.add_argument("--sqli", help="Test SQL Injection on an endpoint (ex: /dvwa/sqli/?id=)", type=str)
    parser.add_argument("--xss", help="Test Reflected XSS via query parameters", type=str)
    parser.add_argument("--admin", help="Test if admin page is publicly accessible", type=str)

    args = parser.parse_args()

    if not (args.sqli or args.xss or args.admin):
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.sqli:
        test_sqli(args.sqli)
    if args.xss:
        test_xss(args.xss)
    if args.admin:
        test_admin_access(args.admin)


if __name__ == "__main__":
    main()
