import aiohttp
import asyncio

from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/getJokes")
async def getJokes(req):
    try: 
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            jokes = []
            users = []
            for _ in range(3):
                jokeTask = asyncio.create_task(sendRequestsToJokes(jokes, session))
                userTask = asyncio.create_task(sendRequestsToRandomUser(users, session))
                jokes = await jokeTask
                users = await userTask
                jokesRes = await asyncio.gather(*jokes)
                usersRes = await asyncio.gather(*users)
                jokeJson_data = [await x.json() for x in jokesRes]
                userJson_data = [await x.json() for x in usersRes]
                print(jokeJson_data)
                print(userJson_data)
                task2 = asyncio.create_task(filterUser(jokeJson_data, session))
                task3 = asyncio.create_task(filterUser(userJson_data, session))
                service2_response = await task2
                service3_response = await task3

        return web.json_response({"Status Servis 01" : "OK"}, status=200)
    except Exception as e:
        return web.json_response({"Status Servis 01" : str(e)}, status=500)

#Send requests to https://official-joke-api.appspot.com/random_joke API
async def sendRequestsToJokes(jokes, session):
    for a in range(2):
        jokes.append(asyncio.create_task(session.get("https://official-joke-api.appspot.com/random_joke")))
        print("Sending request - ", a)
    return jokes

#Send requests to https://randomuser.me/api/ API
async def sendRequestsToRandomUser(jokes, session):
    for a in range(2):
        jokes.append(asyncio.create_task(session.get("https://official-joke-api.appspot.com/random_joke")))
        print("Sending request - ", a)
    return jokes

#Send requests to Servis_02 user
async def filterUser(user, session):
    for i in range(len(user)):
        async with session.post("http://localhost:8082/filterUser", json=user[i]) as resp:
            print("Sending... - ", i)
            service2_response = await resp.text()
    return service2_response

#Send requests to Servis_03 joke
async def filterJoke(joke, session):
    for i in range(len(joke)):
        async with session.post("http://localhost:8083/filterJoke", json=joke[i]) as resp:
            print("Sending... - ", i)
            service3_response = await resp.text()
    return service3_response

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8081)