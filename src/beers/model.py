def beer(id=None, name=None, graduation=None):
    return dict(id=id, name=name, graduation=float(graduation))


def to_list(beers):
    return list(map(lambda tpl: beer(*tpl), beers))
