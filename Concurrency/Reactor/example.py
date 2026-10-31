import asyncio


async def process_client(client_id):
    print(f"Cliente {client_id}: conectado")

    await asyncio.sleep(2)

    print(f"Cliente {client_id}: finalizado")


async def main():
    await asyncio.gather(process_client(1), process_client(2), process_client(3))


asyncio.run(main())
