import argparse
import socket
import dns.resolver

def resolve_domain(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"IP address for {domain}: {ip_address}")
    except socket.gaierror:
        print(f"Failed to resolve {domain}")

def resolve_ip(ip):
    try:
        domain = socket.gethostbyaddr(ip)[0]
        print(f"Domain name for {ip}: {domain}")
    except socket.herror:
        print(f"Failed to resolve {ip}")

def resolve_mx(domain):
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        if mx_records:
            print(f"MX Records for {domain}:")
            for mx in mx_records:
                print(mx.to_text())
        else:
            print(f"No MX records found for {domain}")
    except dns.resolver.NoAnswer:
        print(f"No MX records found for {domain}")

def resolve_ns(domain):
    try:
        ns_records = dns.resolver.resolve(domain, 'NS')
        if ns_records:
            print(f"NS Records for {domain}:")
            for ns in ns_records:
                print(ns.to_text())
        else:
            print(f"No NS records found for {domain}")
    except dns.resolver.NoAnswer:
        print(f"No NS records found for {domain}")

def resolve_txt(domain):
    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        if txt_records:
            print(f"TXT Records for {domain}:")
            for txt in txt_records:
                print(txt.to_text())
        else:
            print(f"No TXT records found for {domain}")
    except dns.resolver.NoAnswer:
        print(f"No TXT records found for {domain}")

def reverse_dns(ip):
    try:
        domain = socket.gethostbyaddr(ip)[0]
        print(f"Domain name for {ip}: {domain}")
    except socket.herror:
        print(f"Failed to resolve {ip}")

def main():
    parser = argparse.ArgumentParser(description='DNS Lookup Tool')
    parser.add_argument('lookup_type', choices=['domain', 'ip', 'mx', 'ns', 'txt', 'reverse'],
                        help='Type of lookup (domain, ip, mx, ns, txt, reverse)')
    parser.add_argument('query', help='Domain or IP address to query')
    args = parser.parse_args()

    if args.lookup_type == 'domain':
        resolve_domain(args.query)
    elif args.lookup_type == 'ip':
        resolve_ip(args.query)
    elif args.lookup_type == 'mx':
        resolve_mx(args.query)
    elif args.lookup_type == 'ns':
        resolve_ns(args.query)
    elif args.lookup_type == 'txt':
        resolve_txt(args.query)
    elif args.lookup_type == 'reverse':
        reverse_dns(args.query)

if __name__ == '__main__':
    main()
