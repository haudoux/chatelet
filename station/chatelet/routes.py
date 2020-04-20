from flask import Blueprint, render_template, url_for
from datetime import datetime
import requests
import json

chatelet = Blueprint('chatelet',__name__)


@chatelet.route('/')
def render():
    return render_template('chatelet.html.jinja')

@chatelet.route('/<string:molecule>/<string:dateDebut>/<string:dateFin>', methods=['GET'])
def getMolecule(molecule, dateDebut, dateFin):
    data = loadJson(molecule, dateDebut, dateFin)
    return str(data)
    #print(data)
    

def loadJson(molecule,dateDebut, dateFin):
    secondDebut = datetime.fromisoformat(dateDebut)
    secondFin = datetime.fromisoformat(dateFin)
    #second = second.utcnow()
    data = {}
    lastMolecules = 0
    with open('static/ressources/qualite-de-lair-mesuree-dans-la-station-chatelet.json') as json_file:
        items = json.load(json_file)
        2019-10-31
        for item in items:
            itemTime = datetime.fromisoformat(item['fields']['dateheure']).replace(tzinfo=None)
            if itemTime > secondDebut and itemTime < secondFin:
                if molecule in item['fields']:
                    lastMolecules = item['fields'][molecule]
            #print(itemTime)
                    data[str(itemTime.strftime('%x %X'))] = lastMolecules
    return json.dumps(data)