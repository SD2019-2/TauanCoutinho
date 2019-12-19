import socket

host = '172.16.32.227'
porta = 5000

sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (host, porta)

sok.connect(destino)    #conecta com o servidor através do endereço

msg = input('Informe as 3 notas\n')

sok.send(msg.encode())   #envia a msg ao servidor

data = sok.recv(1024)   #recebe resposta do servidor

data = data.decode()

print (data)

sok.close()
