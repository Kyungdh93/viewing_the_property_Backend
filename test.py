import uvicorn
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


def main():
    RESTAPI_HOST = "0.0.0.0"
    RESTAPI_PORT = "8000"
    uvicorn.run(app, host=RESTAPI_HOST, port=RESTAPI_PORT, ssl_keyfile=None, ssl_certfile=None, log_config=None, access_log=False, proxy_headers=True, forwarded_allow_ips="*")


if __name__ == "__main__":
    main()
