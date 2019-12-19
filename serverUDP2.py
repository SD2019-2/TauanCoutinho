import socket

HOST = '192.168.0.29'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

while True:
    #recebe mensagem do cliente
    msg, cliente = udp.recvfrom(1024)
    
    #separa dados da string enviada
    dados = msg.split()
    nome = dados[0]
    sexo = dados[1]
    idade = int(dados[2])

    if sexo == 'masculino':
        if idade >= 18:
            texto = '%s e maior de idade' % (nome)
        
        else:
            texto = '%s e menor de idade' % (nome)


    elif sexo == 'feminino':
        if idade >= 21:
            texto = '%s e maior de idade' % (nome)
        
        else:
            texto = '%s e menor de idade' % (nome)

    #envia resposta ao cliente
    udp.sendto(texto, cliente)    

udp.close()