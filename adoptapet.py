#Solution for simple flask app example from Codeacademy project - Adopt a Pet: https://www.codecademy.com/courses/learn-flask/projects/adopt-a-pet
#How to create different pages and routing into each page
#import Flask class from the flask module
from flask import Flask
#import pets dictionary from helper.py document
from helper import pets

app = Flask(__name__)

#create home page
@app.route('/')
def index():
  return '<h1>Adopt a Pet</h1><p>Browse through the links below to find your new furry friend:</p><ul><li><a href="/animals/dogs">Dogs</a></li> <li><a href="/animals/cats">Cats</a></li> <li><a href="/animals/rabbits">Rabbits</a></li></ul>'

  
#create pages for each animal
@app.route('/animals/<pet_type>')
def animals(pet_type):
  name = str()
  pet = pets[pet_type]
  html = '<ul>'
  for ind, info in enumerate(pet):
    name = info['name']
    html += f'<li><a href="/animals/{pet_type}/{ind}">' + name + '</a></li>'
  html += '</ul>'
  return html

#add contents into each page
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  html = '<ul>'
  html += f'<li>name:' + pet["name"] + '</li>'
 #html +=  pet["age"]
  html +=  f'<li>breed:' + pet["breed"] + '</li>'
  html +=  f'<li>description:' + pet["description"] + '</li>'
  url = pet['url']
  html += '<li>image:<img src="' + url + '"/></li>' 
  html += '</ul>'
  return html
