from flask import Flask
from helper import pets
app = Flask(__name__)








##homepage listing animal types
@app.route('/')
def index():
  return'''<h1>Adopt a pet<h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li><a href="/animals/dogs">Dogs</a></li>
    <li><a href='/animals/cats'>Cats</a></li>
    <li><a href='/animals/rabbits'>Rabbit</a></li>
  </ul>'''

@app.route('/animals/<pet_type>')  
def animals(pet_type):
  html = f'<h1>List of {pet_type}</h1>'
  html += '<ul>'
  for pet_id,name in enumerate(pets[pet_type]):
    html += f'<li>' 
    html += f"<a href='/animals/{pet_type}/{pet_id}'>" 
    html += f'{name["name"]}'
    html += '</a></li>'
  return f'{html}'

@app.route('/animals/<pet_type>/<int:pet_id>')  
def pet(pet_type,pet_id):
  pet = (pets[pet_type][pet_id])

  return f'''
  <h1><strong>{pet["name"]}</strong><h1>
            <div = "Description">
              <h2>About you furry friend.</h2>
                <ul>
                  <li>Age : {pet["age"]}</li>
                  <li>Breed: {pet["breed"]}</li>
                </ul>
            </div>
            <div = "media">
              <img src="{pet["url"]}" />

  <br><p>Description: {pet["description"]}</p>'''
