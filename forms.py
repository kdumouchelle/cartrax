__author__ = 'Kyle Dumouchelle'
#CPSC409, 12/9/2015

from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired

class AddMaintenanceForm(Form):
    item_id = IntegerField()
    maintenance_type = SelectField('Maintenance Type', validators=[DataRequired()],choices=
                    [('Tires','Tires'),('Brakes','Brakes'),('Headlights','Headlights'),('Battery','Battery'),
                     ('Engine Oil','Engine Oil'),('Coolant','Coolant'),('Timing Belt','Timing Belt'),
                     ('Air Filter','Air Filter'),('Battery','Battery'),('Spark Plug','Spark Plug')])
    date = DateField('Date (mm/dd/yyyy)', validators=[DataRequired()], format='%m/%d/%Y')
    odometer = IntegerField('Odometer',validators=[DataRequired()])
    start_miles = IntegerField('Start Miles', validators=[DataRequired()])
    end_miles = IntegerField('End Miles', validators=[DataRequired()])
