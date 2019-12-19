import socket

HOST = '192.168.0.29'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msg = raw_input('Informe nome, cargo e salario\n')

#enviando mensagem ao servidor 
udp.sendto (msg, dest)

#recebe resposta do servidor
data, server = udp.recvfrom(1024)
print data

udp.close()
