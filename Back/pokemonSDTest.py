import asyncio
import websockets

# Identifiant du combat (remplace par le vrai ID du match en cours)
BATTLE_ID = "battle-gen9unratedrandombattle-2320193384"

async def listen_showdown():
    uri = "wss://sim3.psim.us/showdown/websocket"
    
    async with websockets.connect(uri) as ws:
        print(f"✅ Connecté au serveur Showdown")

        # Rejoindre le combat
        await ws.send(f"|/join {BATTLE_ID}")
        print(f"📡 Suivi du combat {BATTLE_ID}...")

        while True:
            msg = await ws.recv()
            if msg:
                print(f"🔹 {msg}")  # Affichage brut des événements du combat

# Lancer le bot
asyncio.run(listen_showdown())