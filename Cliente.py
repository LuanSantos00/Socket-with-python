from socket import*

HOST = "127.0.0.1"
PORT = 2000

cliente = socket(AF_INET, SOCK_DGRAM)   #Cria socket do cliente

while 1:
    #Cliente envia os valores para o servidor
    X = input("Digite X: ")
    cliente.sendto(X.encode(), (HOST, PORT))
    
    Y = input("Digite Y: ")
    cliente.sendto(Y.encode(), (HOST, PORT))
    
    maior, enderecoServidor = cliente.recvfrom(2048)    #Cliente recebe o resultado da comparação

    print(maior.decode(), "\n")     #Imprime o resultado da comparação
    
cliente.close()
