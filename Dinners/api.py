"""
This functions as the api for external services to access my dinner suggestions.
This is a very simple implementation as a means to learn about building microservices witrh Docker.
"""

from flask import Flask
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)

dinner_suggestions = ['Spag Bol',
                      'Fish Tacos',
                      'Homemade Pizza',
                      'Pesto Pasta',
                      'Red Curry',
                      'Green Curry',
                      'Saussies and Mash',
                      'Chicken salad',
                      'Burgers and Chips',
                      'Egg Noodle Soup',
                      ]


class Dinner(Resource):

    def get(self):
        return {
            'dinner': random.choice(dinner_suggestions)
        }

    # Below methods are future plans for when I fill out the API/HTML for user interaction.
    def add_dinner(self, new_dinner):
        dinner_suggestions.append(new_dinner)

        return "Dinner suggestion was succesfully added."

    def remove_dinner(self, old_dinner):
        if (old_dinner in dinner_suggestions):
            dinner_suggestions.remvove(old_dinner)
            return [True, "Dinner suggestion was succesfully removed."]
        else:
            return [False, "Dinner suggestion to remove is not a current suggestion."]

    def update_dinner(self, old_dinner, new_dinner):
        if (remove_dinner(old_dinner)[0]):
            add_dinner(new_dinner)
            return "Dinner suggestion was succesfully updated."
        else:
            return "Dinner suggestion to update is not a current suggestion."

api.add_resource(Dinner, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)