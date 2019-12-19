
import socket
import os
import sys

host = '172.16.32.227'   # Endereco IP do Servidor
porta = 5000            # Porta do Servidor

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (host, porta)

tcp.bind(orig)
tcp.listen(1)

while True:
    conexao, cliente = tcp.accept()
    pid = os.fork()
    
    if pid == 0:
        #tcp.close()
        print('Conectado por', cliente)
        
        while True:
            msg = conexao.recv(1024)
            msg = msg.split()
            
            if not msg: 
                break
            
            n1 = float(msg[0])
            n2 = float(msg[1])
            n3 = float(msg[2])

            if (n1 + n2)/2 >= 7:
                resultado = 'aprovado'
        
            elif (n1 + n2)/2 >= 3 and (n1 + n2)/2 < 7:
                print ('analisando n3 ...')
                if (n1 + n2 + n3)/3 >= 5:
                    resultado = 'aprovado'
            
                else:
                    resultado = 'reprovado'
        
            else:
                resultado = 'reprovado'
        
            conexao.send(resultado.encode()) #envia resultado ao cliente conectado
        
        print('Finalizando conexao do cliente', cliente)
        conexao.close()
        sys.exit(0)
    
    else:
        conexao.close()
