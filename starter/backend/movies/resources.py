from flask import jsonify
from flask.views import MethodView

movies = {
    "123": {"title": "Top Gun: Maverick", "description": "Fighter planes"},
    "456": {"title": "Sonic the Hedgehog", "description": "Blue Sega character"},
    "789": {"title": "A Quiet Place", "description": "Scary monsters"},
    "101": {"title": "Di Den Noi Co Gio", "description": "Chinese movie"},
}


class Movies(MethodView):
    def get(self, movie_id):
        if movie_id is None:
            return jsonify({"movies": [dict({"title": movie["title"]}, **{"id": i}) for i,
                                       movie in movies.items()]})
        else:
            return jsonify({"movie": movies[str(movie_id)]})
