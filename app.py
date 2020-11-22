
from flask import render_template, Flask, jsonify, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.secret_key = 'example'

def regs(form, field):
    print(field.data)
    if field.data == 'eww':
        raise ValidationError('Error dont say eww')

class OurForm(FlaskForm):
    inp1 = StringField('String', validators=[DataRequired(), regs])
    subm = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = OurForm()
    if form.validate_on_submit():
        print("SINCE VALID, MAGSEND BACK NG SOMETHING TO SHOW PROGRESSBAR")
        print("THEN MAY GAGAWING FUNCTION MGA 10 SECONDS")
        print('THEN IREDIRECT ANG CLIENT SA SUCCESS PAGE')
    return render_template('home.html', form=form)

@app.route('/success')
def succ():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)