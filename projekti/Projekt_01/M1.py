import aiohttp
import asyncio
import json

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
                session.post("http://localhost:8002/UsernameQuerry_w", json=response_data)))
            data.append(asyncio.create_task(
                session.post("http://localhost:8003/UsernameQuerry_d", json=response_data)))

            res = await asyncio.gather(*data)
            response = await res[0].json()
            response_data = response["response"]

            return web.json_response({"Status M1": "OK", "response": response_data}, status=200)
    except Exception as e:
        return web.json_response({"Status M1": "ERROR", "response": str(e)}, status=500)


async def send_to_wt(url, data):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.post(url, json=data) as resp:
            wt_resp = await resp.text()
    return wt_resp

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8001)
