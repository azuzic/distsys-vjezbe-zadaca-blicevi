import aiohttp

from aiohttp import web

routes = web.RouteTableDef()

print("WT2 process activated!")


@routes.post("/UsernameQuerry_d")
async def postUsernameQuerry_d(req):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            data = await req.json()

            # Sort the list by the 'username' key
            sorted_data = sorted(data, key=lambda x: x['repo_name'])

            # Filter the list to keep only the dictionaries where the 'username' starts with 'd'
            filtered_data = [
                d for d in sorted_data if d['repo_name'].startswith('d')]

            return web.json_response({"Status WT2": "OK", "response": filtered_data}, status=200)
    except Exception as e:
        return web.json_response({"Status WT2": "ERROR", "response": str(e)}, status=500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8003)
