# Servidor UDP com Simulação de Perda de Pacotes

Este é um servidor UDP simples implementado em Python que simula perda de pacotes.
Foi desenvolvido com fins didáticos, para mostrar como o protocolo UDP se comporta quando mensagens são descartadas, já que o UDP não garante entrega, ordem ou integridade dos dados.

## Como funciona

O cliente envia mensagens ao servidor via UDP.

O servidor recebe os datagramas e responde com um eco.

Para simular perda de pacotes, o servidor ignora algumas mensagens em vez de responder todas.

Assim, você pode observar como o UDP lida com a ausência de confirmações.


## Tecnologias

Python 3

Módulo socket (biblioteca padrão)


Como executar

1. Inicie o servidor:
```
python3 servidor_udp.py
```
Ele ficará ouvindo na porta configurada.


2. Inicie o cliente:
```
python3 cliente_udp.py
```

3. Envie mensagens e observe que algumas respostas não chegam, simulando pacotes perdidos.



## Observações importantes

O UDP (User Datagram Protocol) é um protocolo não orientado à conexão:

Não há garantia de entrega.

Os pacotes podem ser perdidos, duplicados ou chegar fora de ordem.


Este projeto ajuda a visualizar esses comportamentos na prática.


## Exemplo de execução

Cliente:
```
Enviado: Olá
Recebido: Eco: Olá
Enviado: Teste 1
(nenhuma resposta — pacote perdido)
Enviado: Teste 2
Recebido: Eco: Teste 2
```
Servidor:
```
[UDP] Ouvindo em 0.0.0.0:55555
Recebido: Olá de ('127.0.0.1', 48812)
-> Eco enviado
Recebido: Teste 1 de ('127.0.0.1', 48812)
-> Pacote descartado
Recebido: Teste 2 de ('127.0.0.1', 48812)
-> Eco enviado
```

---


# UDP Packet Loss Simulation Server

This is a simple UDP server implemented in Python that simulates packet loss.
It was developed for didactic purposes, to demonstrate how UDP behaves when messages are dropped, since UDP does not guarantee delivery, order, or integrity.

## How it works

The client sends messages to the server over UDP.

The server receives the datagrams and replies with an echo.

To simulate packet loss, the server ignores some messages instead of replying to all of them.

This allows you to see how UDP handles missing confirmations.


## Technologies

Python 3

socket module (standard library)


How to run

1. Start the server:
```
python3 server_udp.py
```
It will start listening on the configured port.


2. Start the client:
```
python3 client_udp.py
```

3. Send messages and observe that some replies are missing, simulating dropped packets.



## Important notes

UDP (User Datagram Protocol) is a connectionless protocol:

There is no guarantee of delivery.

Packets may be lost, duplicated, or arrive out of order.


This project helps visualize these behaviors in practice.


## Example output

Client:
```
Send: Hello
Recv: Echo: Hello
Send: Test 1
(no reply — packet dropped)
Send: Test 2
Recv: Echo: Test 2
```
Server:
```
[UDP] Listening on 0.0.0.0:55555
Received: Hello from ('127.0.0.1', 48812)
-> Echo sent
Received: Test 1 from ('127.0.0.1', 48812)
-> Packet dropped
Received: Test 2 from ('127.0.0.1', 48812)
-> Echo sent
```
