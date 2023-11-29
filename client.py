import socket
import json
import argparse

def main():
    # Parsing arguments for command line.
    parse_data = argparse.ArgumentParser()
    parse_data.add_argument("intel_server_addr", help= "Address where intel server resides")
    parse_data.add_argument("intel_server_port", help= "Address where intel server accepts queries")
    parse_data.add_argument("domain", help="The domain that is the subject of the query.")
    parse_data.add_argument("service", help="May be one of the following: \"IPV4_ADDR\", \"IPV6_ADDR\", \"TLS_CERT\", \"HOSTING_AS\", or \"ORGANIZATION\".")
    args = parse_data.parse_args()

    data = {
        "domain": args.domain,
        "command":args.service
    }
    json_string = json.dumps(data)

    # Create a socket and establish a connection
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (str(args.intel_server_addr), int(args.intel_server_port))
    client_socket.connect(server_address)


    # Send, recieve and close the connection
    client_socket.send(json_string.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    client_socket.close()
    print(response)


if __name__ == "__main__": 
    main()
