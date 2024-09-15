import socket
import requests

def GetLocalIP():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def GetPublicIP():
    response = requests.get('https://api.ipify.org?format=json')
    public_ip = response.json()['ip']
    return public_ip

def GetGeolocation(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    response.encoding = 'utf-8'
    data = response.json()
    return data

