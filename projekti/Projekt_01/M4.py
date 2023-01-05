import asyncio
import aiofiles

from aiohttp import web

routes = web.RouteTableDef()

print("M4 process activated!")

gatheredCode = []


@routes.post("/gatherData")
async def postGatherData(req):
    try:
        data = await req.json()

        gatheredCode.append(data)

        if len(gatheredCode) > 10:
            for g in gatheredCode:
                await saveFile(g["content"], g["username"])
            gatheredCode.clear()

        return web.json_response({"Status M4": len(gatheredCode)}, status=200)
    except Exception as e:
        return web.json_response({"Status M4": "ERROR", "response": str(e)}, status=500)


async def saveFile(text, filename):
    try:
        async with aiofiles.open("files/"+filename, mode='w', encoding='utf-8-sig') as f:
            await f.write(text)
    except Exception as e:
        print("Error while saving file: ", e)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8004)
