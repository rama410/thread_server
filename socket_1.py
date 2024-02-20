import socket

# Inisialisasi socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke alamat dan port tertentu
server_address = ('localhost', 8080)
server_socket.bind(server_address) #, server berjalan di localhost (127.0.0.1) dengan port 8080. bind()

# Mendengarkan koneksi
server_socket.listen(1) #listen() untuk memulai mendengarkan koneksi. Argumen 1 menunjukkan bahwa server akan mendengarkan maksimal satu koneksi pada saat tertentu

print('Server listening on', server_address)

while True:
    # Menunggu koneksi
    connection, client_address = server_socket.accept() #Dalam loop tak terbatas, server akan memanggil accept() untuk menerima koneksi dari klien. accept() akan mengembalikan objek socket baru (connection) untuk berinteraksi dengan klien yang telah terhubung. client_address berisi informasi alamat dan port klien yang terhubung.
    print('Connection from', client_address)
    
    try:
        # Menerima data dari klien
        data = connection.recv(1024)
        if data:
            print('Received:', data.decode('utf-8'))
            # Kirim balik ke klien
            connection.sendall(b'Server received: ' + data)
    finally:
        # Tutup koneksi
        connection.close() #Ketika koneksi telah didirikan, server menerima data dari klien menggunakan recv(). Data yang diterima kemudian dicetak di server. Server juga mengirimkan pesan balasan ke klien menggunakan sendall()

