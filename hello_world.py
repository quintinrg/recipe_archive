from flask import Flask, jsonify, request
import json
import uuid
app = Flask(__name__)

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


#Delete Route
#Update Route


#GETs single recipe, PUTs new name in recipe (edits name), DELETEs recipe
#
@app.route('/<id>', methods=['GET', 'DELETE', 'PUT'])
def single_recipe(id):
  if request.method == 'GET':  #displays single recipe - first one that matches 'id'
    return next(recipe for recipe in data if recipe['id'] == id)

  elif request.method == 'DELETE':
    # return "Deleted"
    for recipe in data:
      if id in recipe:
        del element['id']
    with open('data.json', 'w') as data_file:
      newdata = json.dump(data, data_file, indent=2)
      return jsonify(newdata)  #returns null

  elif request.method == 'PUT':
    body = request.get_json()
    return next(recipe for recipe in data if recipe['id'] == id)


#1 build frontend - React/TS

#2 use actual database - later

#3 docker deployed to digitalocean

#rethink db (noSQL)

if __name__ == '__main__':
  app.run()
