"""Telnet client for Aqara Gateway."""

import asyncio

import telnetlib3


class AqaraTelnetClient:
    """Simple Telnet client."""

    def __init__(self, host: str):
        self.host = host
        self.port = 23

    async def execute(self, command: str) -> None:
        reader, writer = await telnetlib3.open_connection(
            self.host,
            self.port,
            shell=None,
            connect_minwait=0.2,
        )

        await self._read_until(reader, "login:")

        writer.write("admin\n")
        await writer.drain()

        await self._read_until(reader, "#")

        writer.write(command + "\n")
        await writer.drain()

        await asyncio.sleep(0.5)

        writer.close()

    async def _read_until(self, reader, text):
        data = ""

        while text not in data:
            chunk = await reader.read(1)
            if not chunk:
                break

            data += chunk

        return data