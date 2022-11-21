import aiohttp
import asyncio

from aiohttp import web

routes = web.RouteTableDef()

@routes.post("/filterUser")
async def filterUser(req):
    try:
        json_data = await req.json()
        filteredUser = {}
        filteredUser["data"]["user"]["name"] = json_data["results"][0]["name"]["first"]
        filteredUser["data"]["user"]["city"] = json_data["results"][0]["location"]["city"]
        filteredUser["data"]["user"]["username"] = json_data["results"][0]["login"]["username"]
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            task = asyncio.create_task(session.post("http://localhost:8084/storeData", filteredUser))

        return web.json_response({"status": "OK"}, status=200)
    except Exception as e:
        return web.json_response({"Status S2" : str(e)}, status=500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8082)