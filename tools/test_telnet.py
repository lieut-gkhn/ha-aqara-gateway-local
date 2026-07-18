import asyncio
import telnetlib3

HOST = "192.168.1.15"
PORT = 23


async def read_until(reader, text):
    data = ""
    while text not in data:
        chunk = await reader.read(1)
        if not chunk:
            break
        data += chunk
    return data


async def main():
    print(f"Connecting to {HOST}:{PORT}")

    reader, writer = await telnetlib3.open_connection(
        HOST,
        PORT,
        shell=None,
        connect_minwait=0.2,
    )

    # Login ekranını bekle
    data = await read_until(reader, "login:")
    print(data)

    # Kullanıcı adı gönder
    writer.write("admin\n")
    await writer.drain()

    # Shell promptunu bekle
    data = await read_until(reader, "#")
    print(data)

    print("Login successful!")

    # Ses dosyasını çal
    writer.write("aplay /data/musics/music-scene/door_bell_1.wav\n")
    await writer.drain()

    # Çalması için biraz bekle
    await asyncio.sleep(3)

    writer.close()


asyncio.run(main())