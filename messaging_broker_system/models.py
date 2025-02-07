from pydantic import BaseModel

class MessageRequest(BaseModel):
    conversation_id: str
    message: str
    destination: str
