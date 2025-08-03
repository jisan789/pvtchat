from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import json
import asyncio
from flask import Flask, jsonify

app = Flask(__name__)

# Telegram credentials
api_id = 28345038
api_hash = '6c438bbc256629655ca14d4f74de0541'
string_session = '1BVtsOHEBu7Ps0EP0Sf__DVSXwT5fI5EAW_XNszWyjecxwwtpq2FPkIBxs-6oxsnquDhS8txn2RLSlPtJhv124hKlLZ1Qfeg46sOzmWtcFb4s17ANgysjABnx6VNFcBrzzEqpP0TqRhOSH2BwnyniyaW7cvjcvBsW1JJiQUXddxqqb9DeamEcPB9KNsjf9gLIeWRJ9aLg14Lj5j81tWd3ylh7E2r-R4WutrcBs3ed-Bl5V6_laWPnoy8IiTE0rRdZ5guAO8JOLdn3dwyGAu1NbYru6_NrloqSx9Shod9gtr8pQk5le_KHCWhtqfUrQqClqnQo2axKolIOk3gTHFoDZOGJvJ2eiPM='

TARGET_USERNAME = 'GoldTraderJisan'

@app.route('/')
def get_messages():
    messages_data = []

    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    with TelegramClient(StringSession(string_session), api_id, api_hash) as client:
        entity = client.get_entity(TARGET_USERNAME)
        for message in client.iter_messages(entity, limit=150):
            messages_data.append({
                "id": message.id,
                "from": message.sender_id,
                "message": message.text
            })

    return jsonify(messages_data)
