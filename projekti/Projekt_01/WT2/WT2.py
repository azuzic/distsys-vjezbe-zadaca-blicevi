import aiohttp
import asyncio

from aiohttp import web

routes = web.RouteTableDef()

print("WT2 process activated!")


@routes.post("/UsernameD")
async def postUsernameD(req):
    print("WT2 process called!")
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            data = await req.json()

            # Sort the list by the 'username' key
            sorted_data = sorted(data, key=lambda x: x['username'])

            # Filter the list to keep only the dictionaries where the 'username' starts with 'd'
            filtered_data = [
                d for d in sorted_data if d['username'].startswith('t')]

            data = []
            for f in filtered_data:
                data.append(asyncio.create_task(
                    session.post("http://m4:8004/gatherData", json=f)))

            res = await asyncio.gather(*data)
            response = await res[0].json()

            print("WT2 process finished!")
            return web.json_response({"Status WT1": "OK", "response": response}, status=200)
    except Exception as e:
        return web.json_response({"Status WT2": "ERROR", "response": str(e)}, status=500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8003)
