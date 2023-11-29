import socket
import json

# Internal library
from serverfunctions import getIPv4,getIPv6,getSSL,get_org, get_asn


# Server Init
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(( '127.0.0.1', 5555))
server_socket.listen(5)
print("Listening on 127.0.0.1:5555")


while True:
    try:
        client_socket, client_address = server_socket.accept()
        data = client_socket.recv(1024)

        try:  
            dataJSON = json.loads(data.decode('utf-8'))
            server = dataJSON['domain']
            command = dataJSON['command']
        
            match(command):
                case "IPV4_ADDR":
                    response = getIPv4(server)
                case "IPV6_ADDR":
                    response = getIPv6(server)
                case "TLS_CERT":
                    response = str(getSSL(server))
                case "ORGANIZATION":
                    response = get_org(server)
                case "HOSTING_AS":
                    response = get_asn(server)
                case _:
                    response = "Invalid command"
        except Exception as e:
            response = str(e)

        client_socket.send(response.encode('utf-8'))    

    # Expected termination
    except KeyboardInterrupt:
        print("Shutting down server...")
        break

