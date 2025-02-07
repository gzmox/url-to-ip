import socket

def url_to_ip(url):
    try:
        hostname = url.replace('http://', '').replace('https://', '').split('/')[0]
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return "Invalid URL or unable to resolve."

url = input("Enter the URL: ")
ip = url_to_ip(url)
print(f"IP address of {url} is: {ip}")
