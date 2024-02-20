import socket
import threading
# mengimplementasikan server yang dapat melayani banyak klien 
# secara bersamaan dengan menggunakan threading
def handle_client(client_socket):
    # Kode untuk menangani permintaan klien dan mengirim respons
    message = "Selanjutnya, panggil metode penerimaan objek yang dikembalikan. Metode ini menunggu sampai klien terhubung ke port yang Anda tentukan, dan kemudian mengembalikan objek koneksi yang mewakili koneksi ke klien itu."
    send_sever = message + "\r\n"
    client_socket.sendall(send_sever.encode('utf-8'))
    
    # Terima balasan dari server
    data = client_socket.recv(1024)
    print('Received:', data.decode('utf-8'))

        # client_socket.close()
def main():
    # Set up a socket and bind it to a specific address and port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8080))
    server.listen(5)  # Allow up to 5 client connections

    print("Server listening on port 8080...")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")

        # Buat thread baru untuk menangani klien
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
        

if __name__ == "__main__":
    main()