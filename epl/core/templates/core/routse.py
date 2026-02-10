from flask import Blueprint, render_template

core_bp = Blueprint('core', _name_, template_folder='templates')

@core_bp.route('/')
def index():
    return render_template('core/index.html', title='Home Page')
@app.route('/clubs')
def all_clubs():
  clubs = db.session.scalars(db.select(Club)).all()
  return render_template('clubs/index.html',
                         title='Clubs Page',
                         clubs=clubs)

@app.route('/clubs/new', methods=['GET', 'POST'])
def new_club():
  if request.method == 'POST':
    name = request.form['name']
    stadium = request.form['stadium']
    year = int(request.form['year'])
    logo = request.form['logo']

    club = Club(name=name, stadium=stadium, year=year, logo=logo)
    db.session.add(club)
    db.session.commit()
    flash('add new club successfully', 'success')
    return redirect(url_for('all_clubs'))
  
  return render_template('clubs/new_club.html',
                         title='New Club Page')

@app.route('/clubs/search', methods=['GET', 'POST'])
def search_club():
  if request.method == 'POST':
    club_name = request.form['club_name']
    clubs = db.session.scalars(db.select(Club).where(Club.name.like(f'%{club_name}%'))).all()
    return render_template('clubs/search_club.html',
                          title='Search Club Page',
                          clubs=clubs)
  
@app.route('/clubs/<int:id>/info')
def info_club(id):
  club = db.session.get(Club, id)
  return render_template('clubs/info_club.html',
                         title='Info Club Page',
                         club=club)

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

    db.session.add(club)
    db.session.commit()

    flash('update club successfully', 'success')
    return redirect(url_for('all_clubs'))
  
  return render_template('clubs/update_club.html',
                         title='Update Club Page',
                         club=club)
