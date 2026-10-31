import socket
import selectors

# 1. El Reactor (Demultiplexor de eventos)
selector = selectors.DefaultSelector()


def accept_connection(server_socket):
    """Manejador de eventos para nuevas conexiones (Accept Handler)."""
    client_socket, address = server_socket.accept()
    print(f"📡 Cliente conectado desde: {address}")

    # Configurar el socket del cliente como no bloqueante
    client_socket.setblocking(False)

    # Registrar el cliente en el Reactor para escuchar eventos de LECTURA (READ)
    selector.register(client_socket, selectors.EVENT_READ, read_message)


def read_message(client_socket):
    """Manejador de eventos para leer datos (Read Handler)."""
    try:
        data = client_socket.recv(1024)
        if data:
            mensaje = data.decode(errors="replace").strip()
            print(f"📩 Mensaje recibido: {mensaje}")

            # Responder al cliente (Eco)
            client_socket.sendall(f"Eco: {mensaje}\n".encode())
        else:
            # Si no hay datos, el cliente cerró la conexión de forma limpia
            print("🔌 El cliente cerró la conexión.")
            cerrar_conexion(client_socket)

    except OSError:
        # Manejar desconexiones abruptas
        print("⚠️ Error de conexión con el cliente.")
        cerrar_conexion(client_socket)


def cerrar_conexion(client_socket):
    """Elimina el socket del reactor y lo cierra formalmente."""
    try:
        selector.unregister(client_socket)
    except KeyError:
        pass
    client_socket.close()


# 2. Configuración del Servidor (Inicio del Recurso)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 5000))
server.listen()
server.setblocking(False)

# Registrar el socket del servidor para aceptar conexiones
selector.register(server, selectors.EVENT_READ, accept_connection)
print("🚀 Servidor Reactor en marcha en 127.0.0.1:5000...")
# Para simplificar, este ejemplo solo recibe mensajes. Un servidor que también envíe respuestas debe gestionar escrituras parciales y eventos EVENT_WRITE.

# 3. El Bucle del Reactor (Event Loop)
try:
    while True:
        # select() bloquea de forma eficiente hasta que ocurra un evento de red
        events = selector.select(timeout=None)

        for key, mask in events:
            # key.data contiene la función manejadora (callback) asociada
            handler = key.data
            # key.fileobj contiene el socket real (servidor o cliente)
            handler(key.fileobj)

except KeyboardInterrupt:
    print("\n🛑 Servidor detenido por el usuario.")
finally:
    # Limpieza absoluta de recursos al apagar
    all_keys = list(selector.get_map().values())
    for key in all_keys:
        try:
            selector.unregister(key.fileobj)
        except KeyError:
            pass
        key.fileobj.close()
    selector.close()
    print("🧹 Recursos liberados correctamente.")

###Esta operación espera hasta que existan conexiones listas para realizar I/O. Luego, el bucle ejecuta los manejadores correspondientes.
