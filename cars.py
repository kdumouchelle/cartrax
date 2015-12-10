__author__ = 'Kyle Dumouchelle'
# CPSC409 final, 12/09/2015

# controller

import sqlite3
from functools import wraps
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
from forms import AddMaintenanceForm

# configuration (remote)
app = Flask(__name__)
app.config.from_object("config")

# function used for connecting to databse
def connnect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('Login Required')
            return redirect(url_for('login'))
    return wrap

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
            request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Username and/or Password.'
        else:
            session['logged_in'] = True
            flash('Logged In')
            return redirect(url_for('main'))
    return render_template('login.html', error=error)

# Read maintenance items
@app.route('/main')
@login_required
def main():
    g.db = connnect_db()
    cur = g.db.execute('SELECT maintenance_type, date, odometer, item_id FROM items WHERE status=1')
    open = [dict(maintenance_type=row[0], date=row[1],odometer=row[2], item_id=row[3])
            for row in cur.fetchall()]
    cur = g.db.execute('SELECT maintenance_type, date, odometer, item_id FROM items WHERE status=0')
    closed = [dict(maintenance_type=row[0], date=row[1],odometer=row[2], item_id=row[3])
            for row in cur.fetchall()]
    g.db.close()
    return render_template(
        'main.html',form=AddMaintenanceForm(request.form),
        open_items=open, closed_items=closed)

# Reads maintenence items with specified parameters
@app.route('/search', methods=['POST'])
@login_required
def search():
    g.db = connnect_db()
    type = request.form['maintenance_type']
    start_miles = request.form['start_miles']
    end_miles = request.form['end_miles']
    cur = g.db.execute('SELECT maintenance_type, date, odometer, item_id FROM items WHERE status=1'
                       ' AND maintenance_type="'+str(type)+'" AND odometer BETWEEN "'+str(start_miles)+'" AND "'+str(end_miles)+'"')
    open = [dict(maintenance_type=row[0], date=row[1],odometer=row[2], item_id=row[3])
            for row in cur.fetchall()]
    cur = g.db.execute('SELECT maintenance_type, date, odometer, item_id FROM items WHERE status=0'
                       ' AND maintenance_type="'+str(type)+'" AND odometer BETWEEN "'+str(start_miles)+'" AND "'+str(end_miles)+'"')
    closed = [dict(maintenance_type=row[0], date=row[1],odometer=row[2], item_id=row[3])
            for row in cur.fetchall()]
    g.db.close()
    return render_template(
        'main.html',form=AddMaintenanceForm(request.form),
        open_items=open, closed_items=closed)



# Create maintenance item
@app.route('/add', methods=['POST'])
@login_required
def new_item():
    maintenance_type = request.form['maintenance_type']
    date = request.form['date']
    odometer = request.form['odometer']

    if not maintenance_type or not date or not odometer:
        flash("Fill out all fields and try again.")
        return redirect(url_for('main'))

    else:
        g.db = connnect_db()
        g.db.execute('INSERT INTO items (maintenance_type, date, odometer, status) '
                     'VALUES (?, ?, ?, 1)',
                     [maintenance_type, date, odometer])
        g.db.commit()
        g.db.close()
        flash('New maintenance item listed')
        return redirect(url_for('main'))

# Updates item as resolved
@app.route('/complete/<int:item_id>')
@login_required
def complete(item_id):
    g.db = connnect_db()
    g.db.execute('UPDATE items SET status = 0 WHERE item_id='+str(item_id))
    g.db.commit()
    g.db.close()
    flash('Maintenance item marked as completed')
    return redirect(url_for('main'))

# Deletes item
@app.route('/delete/<int:item_id>')
@login_required
def delete_entry(item_id):
    g.db = connnect_db()
    g.db.execute('DELETE FROM items WHERE item_id='+str(item_id))
    g.db.commit()
    g.db.close()
    flash('Maintenance item deleted')
    return redirect(url_for('main'))

@app.route('/logout')
def logout():
    # returns session key to default and returns to login page
    session.pop('logged_in', None)
    flash('Logged Out')
    return redirect(url_for('login'))