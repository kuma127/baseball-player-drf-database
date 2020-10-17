from aiohttp import web
import aiohttp

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    print("cliend data")

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            await ws.send_str(msg.data)
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print("ws connection closed with exception %s" % ws.exception())
    
    print("websocket connection closed")

    return ws

app = web.Application()
app.add_routes(
    [
        web.get("/ws", websocket_handler)
    ]
)

web.run_app(app, port=8088)