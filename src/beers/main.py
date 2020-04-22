from aiohttp import web
from . import queries
from . import model


async def get_beer(request):
    beer_id = request.match_info.get("beer_id", None)

    if beer_id:
        beer = queries.fetch("id", beer_id)
        if not beer:
            raise web.HTTPNotFound
        return web.json_response(beer)

    beers = queries.fetch()
    beers_list = model.to_list(beers)
    return web.json_response(beers_list)


async def add_beer(request):
    beer = await request.json()
    print(type(beer), beer)

    if not beer or not "name" in beer or not "graduation" in beer:
        raise web.HTTPBadRequest

    beer_exist = queries.fetch("name", beer["name"])
    if beer_exist:
        raise web.HTTPConflict

    queries.insert(beer)
    beers = queries.fetch()
    beers_list = model.to_list(beers)
    return web.json_response(beers_list)


# async def remove_beer(request):
#     beer_id = request.match_info.get("beer_id", None)
#
#     if not beer_id:
#         raise web.HTTPBadRequest
#
#     beer_to_remove = list(filter(lambda x: x["id"] == beer_id, BEERS))
#
#     if not beer_to_remove:
#         raise web.HTTPNotFound
#
#     BEERS.remove(beer_to_remove[0])
#
#     return web.json_response(BEERS)


def server():
    queries.create_table()
    app = web.Application()
    app.add_routes([
        web.get("/", get_beer),
        web.get("/{beer_id}", get_beer),
        web.post("/", add_beer),
        # web.delete("/{beer_id}", remove_beer),
    ])
    web.run_app(app)
