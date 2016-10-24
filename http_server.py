import socket
import os


def main() -> None:
    #server_sock = make_server_socket('0.0.0.0', 8000)
    server_sock = inherit_server_socket_from(0)
    while True:
        client_sock, _ = server_sock.accept()
        handle_client(client_sock)


def handle_client(client_sock: socket.socket) -> None:
    request = client_sock.recv(65535)
    client_sock.send(make_response('Server process ID: {}\n'.format(os.getpid())))
    client_sock.close()


def make_response(content: str):
    content_len = bytes('{}'.format(len(content)), 'ascii')
    return b'HTTP/1.0 200 OK\r\n' + \
           b'Content-Type: text/plain\r\n' + \
           b'Content-Length: ' + content_len + b'\r\n\r\n' + \
           bytes(content, 'ascii')


def make_server_socket(host: str, port: int) -> socket.socket:
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((host, port))
    server_sock.listen(65535)
    return server_sock


def inherit_server_socket_from(fd: int) -> socket.socket:
    return socket.fromfd(fd, socket.AF_INET, socket.SOCK_STREAM)


if __name__ == '__main__':
    main()
