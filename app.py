from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
with app.app_context():
    db.create_all()

@app.route('/')
def show_all_pets():
    """Shows a list of pets and availability"""
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Pet add form; handle adding"""
    form = AddPetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        # create new pet with user input and add to database
        new_pet = Pet(name=name,species=species,photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_pet_form.html", form=form)
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def view_pet(pet_id):
    """Renders a new page that displays the information about the pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)
    
        
        


        
    