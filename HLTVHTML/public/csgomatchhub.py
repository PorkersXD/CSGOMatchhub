from flask import Flask, render_template, request
from flask_table import Table, Col
import sqlite3

my_list = []
app = Flask(__name__)
DATABASE = 'db/matchinfo.db'
conn = sqlite3.connect(DATABASE)
c = conn.cursor()

# Or, more likely, load items from your database with something like
event = c.execute('SELECT Event FROM Matches WHERE ID = 1')
maps = c.execute('SELECT maps FROM Matches')
T1name = c.execute('SELECT T1name FROM Matches')
T1result = c.execute('SELECT T1result FROM Matches')
T2name = c.execute('SELECT T2name FROM Matches')
T2result = c.execute('SELECT T2result FROM Matches')

conn.commit()

my_list = [event, maps, T1name, T1result, T2name, T2result]
print(my_list)

#@app.route('/index')
#def index():
    
   # return render_template('index.html', my_list = my_list)  # make a list and pass it to our template variable named my_list


#app.run(debug=True)