import socket
import time
import random

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000
NUM_CLIENTES_SIMULTANEOS = 3


def iniciar_simulacion_clientes():
    sockets_clientes = []

    print(
        f"🤖 Conectando {NUM_CLIENTES_SIMULTANEOS} clientes simulados al servidor Reactor..."
    )

    try:
        # 1. Crear y conectar todos los clientes simultáneamente
        for i in range(NUM_CLIENTES_SIMULTANEOS):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((SERVER_HOST, SERVER_PORT))
            sockets_clientes.append(sock)
            print(f"✅ Cliente #{i + 1} conectado exitosamente.")

        print("\n💬 Comenzando el envío de mensajes alternados...\n")

        # Lista de mensajes aleatorios que enviarán los clientes
        mensajes_ejemplo = [
            "Hola desde el cliente",
            "¿Cómo va ese patrón Reactor?",
            "Enviando ráfaga de datos...",
            "Probando asincronía en un solo hilo",
            "Mensaje final de prueba",
        ]

        # 2. Enviar mensajes alternando entre los clientes abiertos
        for ronda in range(4):  # Haremos 4 rondas de mensajes
            for idx, sock in enumerate(sockets_clientes):
                cliente_id = idx + 1
                msg = f"[Cliente {cliente_id}] {random.choice(mensajes_ejemplo)} (Ronda {ronda + 1})"

                # Enviar mensaje al servidor
                sock.sendall(msg.encode())
                print(f"📤 {msg}")

                # Recibir la respuesta (Eco) del servidor Reactor
                respuesta = sock.recv(1024).decode()
                print(f"📥 Respuesta recibida: {respuesta.strip()}")

                # Pequeña pausa aleatoria para simular comportamiento humano
                time.sleep(random.uniform(0.3, 0.7))

    except ConnectionRefusedError:
        print(
            "❌ Error: No se pudo conectar. ¿Asegúrate de que el servidor Reactor está corriendo?"
        )

    finally:
        # 3. Cerrar formalmente todas las conexiones abiertas
        print("\n🔌 Cerrando todas las conexiones de los clientes...")
        for sock in sockets_clientes:
            sock.close()
        print("🧹 Clientes desconectados correctamente.")


if __name__ == "__main__":
    iniciar_simulacion_clientes()
