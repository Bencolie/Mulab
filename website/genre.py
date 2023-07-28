from website import get_genres, get_tracks, download, db
from flask import Blueprint,render_template,request,flash,send_file
from .models import Genres,Tracks


genre = Blueprint('genre',__name__)

@genre.route('/music_genre',methods=['GET','POST'])
def music_genre():
    if request.method == 'POST':
        # We need to link each dict of tracks to its categories!!!
        value = request.form.get('getTheseTracks')
        values = value.split(',')
        current_genre = Genres.query.filter_by(name=values[1]).first()
        tracks = current_genre.tracks
        if not tracks:
            track = get_tracks(values[0])
            for k in range(2,len(track)):
                if '(' in track[k]['track_name']:
                    name_update = track[k]['track_name'].split('(',1)
                    track[k]['track_name'] = name_update[0]
                    music_track = Tracks(name = track[k]['track_name'],dlink = track[k]['track_url'],genre_id=current_genre.id)
                else:
                    music_track = Tracks(name = track[k]['track_name'],dlink = track[k]['track_url'],genre_id=current_genre.id)
                db.session.add(music_track)
            db.session.commit()
        categories = Genres.query.all()
    else:
        cat = Genres.query.filter_by(name='Cinematic').first()
        if not cat:
            categories = get_genres('https://www.ashamaluevmusic.com/')
            # manage elements in categories
            for i in range(8,43):
                del categories[i]
            for k in range(1,len(categories)):
                music_genre = Genres(name=categories[k]['cat_name'],link=categories[k]['cat_url'])
                db.session.add(music_genre)
            db.session.commit()
        else:
            categories = Genres.query.all()
        tracks=None
    return render_template('genre.html',categories=categories,tracks=tracks)

@genre.route('/music_download',methods=['POST'])
def music_dowload():
    url = request.form.get('downloadThisTrack')
    file = download(url)
    # mimetype='audio/mpeg'
    return send_file(file, as_attachment=True,mimetype='audio/mpeg')

