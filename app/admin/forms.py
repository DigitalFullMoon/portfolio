from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField('Titre', validators=[DataRequired(), Length(min=5, max=200)])
    content = TextAreaField('Contenu', validators=[DataRequired()])
    published = BooleanField('Publier')
    submit = SubmitField('Enregistrer')