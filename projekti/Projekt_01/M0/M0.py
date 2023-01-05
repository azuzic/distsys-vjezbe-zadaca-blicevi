import aiosqlite
import json

from aiohttp import web

routes = web.RouteTableDef()

print("M0 process activated!")


@routes.get("/GithubLinks")
async def getGithubLinks(req):
    print("M0 process called!")
    try:
        # Connect to the database
        conn = await aiosqlite.connect('/app/DB.db')
        cursor = await conn.cursor()

        # If the database is empty, populate it with test data
        if await isTableEmpty(cursor):
            await fillDatabase(conn, cursor)
            data = await fetchGithubLinks(cursor)
        else:
            data = await fetchGithubLinks(cursor)

        print("M0 process finished!")
        return web.json_response({"Status M0": "OK", "response": data}, status=200)
    except Exception as e:
        return web.json_response({"Status M0": "ERROR", "response": str(e)}, status=500)


async def isTableEmpty(cursor):
    try:
        # Execute a SELECT query to check if the database is empty
        await cursor.execute('SELECT * FROM github_links')
        results = await cursor.fetchall()
        return not results
    except Exception as e:
        print("Database error: ", e)


async def fillDatabase(conn, cursor):
    # Load json file
    with open('/app/data.json') as f:
        for line in f:
            l = json.loads(line)
            username = l["repo_name"].split('/')[0]
            filename = l["path"].split('/')[-1]
            ghlink = "https://github.com/" + l["repo_name"]
            content = l["content"]
            try:
                await cursor.execute('INSERT INTO github_links (username,ghlink,filename,content) VALUES (?,?,?,?)',
                                     (username, ghlink, filename, content))
                await conn.commit()

            except Exception as e:
                print("Database inset error: ", e)
    print("Populated database with test data!")


async def fetchGithubLinks(cursor):
    try:
        # Execute a SELECT query ORDERED by random with 100 LIMIT
        await cursor.execute('SELECT * FROM github_links ORDER BY random() LIMIT 100')

        # Extract column names and values to create a list of dictionaries
        column_names = [column[0] for column in cursor.description]
        rows = await cursor.fetchall()
        result = [dict(zip(column_names, row)) for row in rows]

        return result
    except Exception as e:
        print("Fetching error: ", e)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8000)
