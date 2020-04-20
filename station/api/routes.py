from flask import Blueprint, request
from extensions import mysql

api = Blueprint('api',__name__)


@api.route('/console/<string:command>', methods=['GET'])
def manageConsole(command):  
    toReturn = ''
    if command == 0:
        toReturn = getQuestion(1)
    elif command != 0:
        toReturn = getActionFromCommand(str(command))
    else :
        toReturn = 'Commande inconnue'
    return toReturn

def getActionFromCommand(command):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT resultat FROM consolecommande WHERE commande=%s''',([command]))
    rv = cur.fetchone()
    return str(rv[0])

def getQuestion(id):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT question FROM consolequestion WHERE idconsole=%s''',(str(id)))
    rv = cur.fetchone()
    return str(rv[0])