from flask import Blueprint, render_template, url_for, request, flash

rom ep1.extensions import db
from ep1.models import Club

club_bp = Blueprint('clubs', _name_, template_folder='templates')

@crub_bp.route('/')
def index().
query = db.select(Club)
clubs = db.select(Club)
return render_template('clubs/index.html', title='Clubs Page')

@app.route('/players')
def all_players():
  players = db.session.scalars(db.select(Player)).all()
  return render_template('players/index.html',
                         title='Players Page',
                         players=players)

@app.route('/players/new', methods=['GET', 'POST'])
def new_player():
  clubs = db.session.scalars(db.select(Club)).all()
  if request.method == 'POST':
    name = request.form['name']
    position = request.form['position']
    nationality = request.form['nationality']
    goals = int(request.form['goals'])
    squad_no = int(request.form['squad_no'])
    img = request.form['img']
    club_id = int(request.form['club_id'])

    player = Player(name=name, position=position, nationality=nationality,
                    goals=goals, squad_no=squad_no, img=img, club_id=club_id)
    db.session.add(player)
    db.session.commit()
    flash('add new player successfully', 'success')
    return redirect(url_for('all_players'))

  return render_template('players/new_player.html',
                         title='New Player Page',
                         clubs=clubs)

@app.route('/players/search', methods=['POST'GET'])
def search_player():
  if request.method == 'POST':
    player_name = request.form['player_name']
    players = db.session.scalars(db.select(Player).where(Player.name.like(f'%{player_name}%'))).all()
    return render_template('players/search_player.html',
                           title='Search Player Page',
                           players=players)

@player_bp.route('/<int:id>/info')
def info_player(id):
    player = db.session.get(Player, id)
    return render_template('players/info_player.html',
                           title='Info Player Page',
                           player=player)

@player_bp.route('/<int:id>/update')
def u_player(id):
    player = db.session.get(Player, id)
    return render_template('players/info_player.html',
                           title='Info Player Page',
                           player=player)
                           @app.route('/clubs/<int:id>/update', methods=['GET','POST'])
def update_club(id):
  club = db.session.get(Club, id)
  if request.method == 'POST':
    name = request.form['name']
    stadium = request.form['stadium']
    year = int(request.form['year'])
    logo = request.form['logo']

    club.name = name
    club.stadium = stadium
    club.year = year
    club.logo = logo

    db.session.add(PLAYERS)
    db.session.commit()
  
    player.name = name
player.position = position
player.nationality = nationality
player.goals = goals
player.squad_no = squad_no
player.img = img
player.club_id = club_id

db.session.add(player)
db.session.commit()

flash('update player successfully', 'success')
return redirect(url_for('players.index'))

    