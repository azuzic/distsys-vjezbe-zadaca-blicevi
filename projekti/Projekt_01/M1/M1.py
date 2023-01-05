import aiohttp
import asyncio

from aiohttp import web

routes = web.RouteTableDef()

print("M1 process activated!")


@routes.get("/Dictionary")
async def getDictionary(req):
    print("M1 process called!")
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            data = []

            data.append(asyncio.create_task(
                session.get("http://m0:8000/GithubLinks")))

            res = await asyncio.gather(*data)  # Wait for tasks to complete
            response = await res[0].json()  # Await the result of the task
            response_data = response["response"]
            data = []
            data.append(asyncio.create_task(
                session.post("http://wt1:8002/UsernameW", json=response_data)))
            data.append(asyncio.create_task(
                session.post("http://wt2:8003/UsernameD", json=response_data)))

            res = await asyncio.gather(*data)  # Wait for tasks to complete
            response1 = await res[0].json()  # Await the result of the task
            response2 = await res[1].json()  # Await the result of the task

            print("M1 process finished!")
            return web.json_response({"Status M1": "OK", "response": (response1, response2)}, status=200)
    except Exception as e:
        return web.json_response({"Status M1": "ERROR", "response": str(e)}, status=500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8001)
