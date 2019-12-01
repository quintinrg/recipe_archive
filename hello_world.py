from flask import Flask, jsonify, request
import json
import uuid
from flask_cors import CORS
from deepmerge import always_merger

app = Flask(__name__)
CORS(app)
with open('data.json', 'r') as data_file:
  data = json.load(data_file)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return jsonify(data)

  elif request.method == 'POST':
    body = request.get_json()

    body['id'] = str(uuid.uuid4())
    data.append(body)
    with open('data.json', 'w') as data_file:
      json.dump(data, data_file, indent=2)
    return next(recipe for recipe in data if recipe['id'] == body['id'])


#GETs single recipe, PUTs new name in recipe (edits name), DELETEs recipe
#
@app.route('/<id>', methods=['GET', 'DELETE', 'PUT'])
def single_recipe(id):
  if request.method == 'GET':  #displays single recipe - first one that matches 'id'
    return next(recipe for recipe in data if recipe['id'] == id)

  elif request.method == 'DELETE':
    #return "Deleted"

    for ix, recipe in enumerate(data):
      if recipe['id'] == id:
        del data[ix]

    with open('data.json', 'w') as data_file:
      json.dump(data, data_file, indent=2)
    with open('data.json', 'r') as data_file:
      output = json.load(data_file)

    return jsonify(output)

  elif request.method == 'PUT':
    body = request.get_json()
    for ix, recipe in enumerate(data):
      if recipe['id'] == id:
        data[ix] = always_merger.merge(recipe, body)
    with open('data.json', 'w') as data_file:

      json.dump(data, data_file, indent=2)
    return jsonify(next(recipe for recipe in data if recipe['id'] == id))


#1 build frontend - React/TS

#2 use actual database - later

#3 docker deployed to digitalocean

#rethink db (noSQL)

if __name__ == '__main__':
  app.run()
