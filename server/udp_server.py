import socket
import random

host = "0.0.0.0"
port = 55552

loss_min = 0.10
loss_max = 0.30

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((host, port))

print(f"Servidor UPD iniciado em {host}:{port}.")

while True:
  data, addr = sock.recvfrom(2048)
 
  prob = random.uniform(loss_min, loss_max)

  if random.random() < prob:
    print("UDP DROP: ", addr, data)
    continue

  print("UDP Recv: ", addr, data)
  sock.sendto(b"Echo:" + data, addr)
