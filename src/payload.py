from pydantic import BaseModel

class ShortRequest(BaseModel):
    url: str 

class LongRequest(BaseModel):
    short_url: str 

class ClickCountRequest(BaseModel):
    click_count: int

