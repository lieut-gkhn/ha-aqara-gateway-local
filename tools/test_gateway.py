import sys
from pathlib import Path

# Projenin kök dizinini Python path'ine ekle
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import asyncio

from aqara_core.gateway import AqaraGateway


async def main():
    gw = AqaraGateway("192.168.1.15")

    await gw.play_sound(
        "/data/musics/music-scene/door_bell_1.wav"
    )


asyncio.run(main())