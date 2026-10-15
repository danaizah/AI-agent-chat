from ninja import NinjaAPI, Schema

api = NinjaAPI()


class TestOut(Schema):
    status: str


@api.get("/health", response=TestOut)
def health(request) -> dict:
    return {"status": "ok"}
