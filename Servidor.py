from socket import*

HOST = "127.0.0.1"
PORT = 2000

servidor = socket(AF_INET, SOCK_DGRAM)      #Cria socket do servidor
servidor.bind((HOST, PORT))     #Conecta o socket ao endereço

print("Servidor pronto!")

while 1:
    #Servidor recebe os valores e o endereço do cliente
    X, enderecoCliente = servidor.recvfrom(2048)
    X = float(X)
    
    Y, enderecoCliente = servidor.recvfrom(2048)
    Y = float(Y)

    #Verifica qual o maior
    if X > Y:
        maior = "O maior é X"
    elif Y > X:
        maior = "O maior é Y"
    else:
        maior = "X e Y são iguais"

    #Servidor envia o resultado da comparação para o cliente
    servidor.sendto(maior.encode(), enderecoCliente)
