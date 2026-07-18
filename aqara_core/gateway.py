from .telnet_client import AqaraTelnetClient


class AqaraGateway:

    def __init__(self, host):
        self.client = AqaraTelnetClient(host)

    async def play_sound(self, filename):

        await self.client.execute(
            f"aplay {filename}"
        )