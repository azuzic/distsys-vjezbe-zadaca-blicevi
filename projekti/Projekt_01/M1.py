import aiohttp
import asyncio

from aiohttp import web

routes = web.RouteTableDef()

print("M1 process activated!")


@routes.get("/Dictionary")
async def getDictionary(req):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            data = []
            data.append(asyncio.create_task(
                session.get("http://localhost:8000/GithubLinks")))
            res = await asyncio.gather(*data)
            response = await res[0].json()
            response_data = response["response"]

            data = []
            data.append(asyncio.create_task(
                session.post("http://localhost:8002/UsernameW", json=response_data)))
            data.append(asyncio.create_task(
                session.post("http://localhost:8003/UsernameD", json=response_data)))

            res = await asyncio.gather(*data)
            response1 = await res[0].json()
            response2 = await res[1].json()

            return web.json_response({"Status M1": "OK", "response": (response1, response2)}, status=200)
    except Exception as e:
        return web.json_response({"Status M1": "ERROR", "response": str(e)}, status=500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8001)
