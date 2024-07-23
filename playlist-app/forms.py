"""Forms for playlist app."""

from wtforms import SelectField, StringField, TextAreaField,SubmitField,validators
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name= StringField('Playlist Name', validators=[validators.DataRequired(),validators.Length(max=50)])
    description = TextAreaField('Description', validators=[validators.Optional(), validators.Length(max=200)])
    submit = SubmitField('Add Playlist')

class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField('Title', validators=[validators.DataRequired(), validators.Length(max=100)])
    artist = StringField('Artist', validators=[validators.DataRequired(), validators.Length(max=50)])
    submit = SubmitField('Add song')

# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
    submit = SubmitField('Add Song')