from aiohttp import web
from . import create_table

BEERS = [
  {"id": "aaa-111", "name": "Amstel", "graduation": 4.5},
  {"id": "bbb-222", "name": "Mahoo", "graduation": 3.5},
  {"id": "ccc-333", "name": "Coronita", "graduation": 5.5},
  {"id": "ddd-444", "name": "Heineken", "graduation": 3.0}
]


async def get_beer(request):
  beer_id = request.match_info.get("beer_id", None)

  if beer_id:
    beer = list(filter(lambda x: x["id"] == beer_id, BEERS))
    if not beer:
      raise web.HTTPNotFound
    return web.json_response(beer[0])

  return web.json_response(BEERS)


async def add_beer(request):
  beer = await request.json()

  if not beer or not beer["id"] or not beer["name"] or not beer["graduation"]:
    raise web.HTTPBadRequest

  beer_exist = list(filter(lambda x: x["name"] == beer["name"], BEERS))
  if beer_exist:
    raise web.HTTPConflict

  BEERS.append(beer)

  return web.json_response(BEERS)


async def remove_beer(request):
  beer_id = request.match_info.get("beer_id", None)

  if not beer_id:
    raise web.HTTPBadRequest

  beer_to_remove = list(filter(lambda x: x["id"] == beer_id, BEERS))

  if not beer_to_remove:
    raise web.HTTPNotFound

  BEERS.remove(beer_to_remove[0])

  return web.json_response(BEERS)


def server():
  create_table.beers()
  app = web.Application()
  app.add_routes([
    web.get("/", get_beer),
    web.get("/{beer_id}", get_beer),
    web.post("/", add_beer),
    web.delete("/{beer_id}", remove_beer),
  ])
  web.run_app(app)
