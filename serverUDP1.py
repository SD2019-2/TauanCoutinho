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
    cargo = dados[1]
    salario = float(dados[2])

    #altera valores do salario
    if cargo == 'operador':
        salario += salario * 0.2

    elif cargo == 'programador':
        salario += salario * 0.18

    #formata string de resposta
    texto = '%s %f' % (nome, salario)

    print cliente
    print nome, salario

    #envia resposta ao cliente
    udp.sendto(texto, cliente)    

udp.close()