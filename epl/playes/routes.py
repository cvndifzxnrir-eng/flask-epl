from flsak import blueprit, render_template

core_db()'core',__name__,template_folder=template')

from flask import Blueprint, render_template

core_bp = Blueprint('core', _name_, template_folder='templates')

@core_bp.route('/')
def index():
    return render_template('core/index.html', title='Home Page')

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

@app.route('/players/search', methods=['POST'])
def search_player():
  if request.method == 'POST':
    player_name = request.form['player_name']
    players = db.session.scalars(db.select(Player).where(Player.name.like(f'%{player_name}%'))).all()
    return render_template('players/search_player.html',
                           title='Search Player Page',
                           players=players)