from aiohttp import web
import aiohttp
import asyncio

async def get(request):
    duljina = await idi_na_google()
    return web.json_response(data={"status": "OK", "lenght": duljina})

async def idi_na_google():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://google.com") as resp:
            return len(await resp.text())

app = web.Application()
app.add_routes([web.get("/service", get)])

web.run_app(app)