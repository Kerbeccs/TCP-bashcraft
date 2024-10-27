
import socket
import sys

def connect_to_server(host='127.0.0.1', port=8080):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(10)  
    
    try:
        print(f"Connecting to server at {host}:{port}...")
        client_socket.connect((host, port))
        print("Connected!")

        message = "Hello from client!"
        print(f"Sending: {message}")
        client_socket.sendall(message.encode('utf-8'))

      
        data = client_socket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")

    except ConnectionRefusedError:
        print("Connection failed. Make sure the server is running.")
    except socket.timeout:
        print("Connection timed out.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
    finally:
        try:
            client_socket.shutdown(socket.SHUT_RDWR)
        except:
            pass
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    connect_to_server()