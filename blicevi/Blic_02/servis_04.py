import aiosqlite

from aiohttp import web

routes = web.RouteTableDef()

temp_jokes_storage = []
temp_users_storage = []
numberOfRowsInTable = 0

@routes.post("/storeData")
async def storeData(request):
    req = await request.json()
    try:
        if "user" in req:
            temp_users_storage.append(req)
        else:
            temp_jokes_storage.append(req)
        if "user" in req:
            if temp_jokes_storage.count > 0:
                async with aiosqlite.connect("databse.db") as db:
                    user = temp_users_storage.pop()
                    joke = temp_jokes_storage.pop()
                    await db.execute("INSERT INTO userAndJoke (name,city,username,setup,punchline) VALUES (?,?,?,?,?)", 
                    (user["data"]["name"], user["data"]["city"], user["data"]["username"], joke["data"]["setup"], joke["data"]["punchline"]))
                    await db.commit()
                    cursor = db.execute('SELECT * FROM userAndJoke')
                    numberOfRowsInTable = len(cursor.fetchall())
        if numberOfRowsInTable > 0:
            return web.json_response({"status": "OK", "data": {"numberOfRowsInTable" : numberOfRowsInTable} }, status=200)
        else:
            return web.json_response({"status": "Failed", "message": "Joke not present" }, status=200)
    except Exception as e:
        return web.json_response({"Status S4" : str(e)}, status=500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8084)