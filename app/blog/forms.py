from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class CommentForm(FlaskForm):
    content = TextAreaField('Commentaire', validators=[DataRequired(), Length(min=10, max=2000)])
    submit = SubmitField('Publier')