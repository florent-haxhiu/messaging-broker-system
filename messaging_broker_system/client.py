from websockets.sync.client import connect

from messaging_broker_system.models import MessageRequest


def hello():
    uri = "ws://localhost:5678"
    req = MessageRequest(conversation_id="convo-id", message="Hello World", destination=uri)
    with connect(uri) as websocket:
        websocket.send(req.model_dump_json())
        message = websocket.recv()
        print(f"Received: {message}")


hello()
