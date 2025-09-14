import socket

host = "127.0.0.1"
port = 55552

timeout = 1.0
retries = 3

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.settimeout(timeout)

print(f"Conectado ao servidor.")

try:
  while True:
    msg = input("Cliente: ")
    if not msg:
      continue

  attempts = 0
  while attempts <= retries:
    attempts += 1
    sock.sendto(msg.encode(), (host, port))

except Exception as e:
  print("Erro: ", e)
finally:
  sock.close()
  
