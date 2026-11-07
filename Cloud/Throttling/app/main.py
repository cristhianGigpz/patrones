import time
from collections import defaultdict, deque
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

requests = defaultdict(deque)

LIMIT = 5
WINDOW = 10


@app.middleware("http")
async def throttle(request: Request, call_next):
    client = request.client.host if request.client else "unknown"
    now = time.monotonic()

    history = requests[client]

    while history and now - history[0] >= WINDOW:
        history.popleft()

    if len(history) >= LIMIT:
        retry_after = max(1, int(WINDOW - (now - history[0])) + 1)

        return JSONResponse(
            status_code=429,
            content={"detail": "Too Many Requests"},
            headers={"Retry-After": str(retry_after)},
        )

    history.append(now)

    return await call_next(request)


@app.get("/api/data")
def get_data():
    return {"message": "Solicitud procesada"}
