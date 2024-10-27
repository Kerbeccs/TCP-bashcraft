
import socket
import threading
import time

class TCPServer:
    def __init__(self, host='127.0.0.1', port=8080):
        self.host = host
        self.port = port
        self.server_socket = None
        self.is_running = False
        self.clients = set()
        self._lock = threading.Lock()

    def start(self):
        """Start the TCP server"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            self.is_running = True
            print(f"TCP Server started on {self.host}:{self.port}")

            while self.is_running:
                try:
                    client_socket, client_address = self.server_socket.accept()
                    with self._lock:
                        self.clients.add(client_socket)
                    client_thread = threading.Thread(
                        target=self._handle_client,
                        args=(client_socket, client_address)
                    )
                    client_thread.daemon = True
                    client_thread.start()
                except socket.error:
                    if self.is_running:  
                        print("Socket accept error")
                        time.sleep(0.1)  

        except Exception as e:
            print(f"Server error: {e}")
        finally:
            self.stop()

    def _handle_client(self, client_socket, client_address):
        """Handle individual client connections"""
        print(f"New connection from {client_address}")
        try:
            while self.is_running:
                try:
                    data = client_socket.recv(1024).decode('utf-8')
                    if not data:
                        break
                    
                    print(f"Received from {client_address}: {data}")
                    response = f"Server received: {data}"
                    client_socket.sendall(response.encode('utf-8'))
                    
                except socket.error:
                    break
                
        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
        finally:
            with self._lock:
                self.clients.remove(client_socket)
            try:
                client_socket.shutdown(socket.SHUT_RDWR)
            except:
                pass
            client_socket.close()
            print(f"Connection closed with {client_address}")

    def stop(self):
        """Stop the TCP server and clean up connections"""
        print("Stopping TCP server...")
        self.is_running = False
        
      
        with self._lock:
            for client_socket in self.clients:
                try:
                    client_socket.shutdown(socket.SHUT_RDWR)
                except:
                    pass
                client_socket.close()
            self.clients.clear()
        
      
        if self.server_socket:
            try:
                self.server_socket.shutdown(socket.SHUT_RDWR)
            except:
                pass
            self.server_socket.close()
            self.server_socket = None
        
        print("TCP server stopped")


if __name__ == "__main__":
    server = TCPServer()
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()