from flask import Flask, render_template, send_file, make_response, request
import sqlite3
import time
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import sys

# setup path to import db
sys.path.insert(0, '..')
import db

# setup db connection
db = db.Database('../database.db')

app = Flask(__name__)

def get_local_time(seconds):
    return time.ctime(seconds)


def get_most_recent_reading():
    query = "SELECT * FROM soil_readings ORDER BY timestamp DESC LIMIT 1;"
    rows = db.query(query)
    return rows[0]


def get_historical_data(num_samples):
    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM soil_readings ORDER BY timestamp DESC LIMIT " + str(num_samples))
    data = cursor.fetchall()
    dates = []
    measurements = []
    
    for row in reversed(data):
        dates.append(row[1])
        measurements.append(row[2])
    
    conn.close()
        
    return dates, measurements

def get_count():
    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()
    
    for row in cursor.execute("select COUNT(mean) from soil_readings"):
        return row[0]

# main route
@app.route('/')
def index():
    reading = get_most_recent_reading()
    
    template_data = {
        'time': get_local_time(reading[1]),
        'mean': reading[2]
    }
    
    return render_template('index.html', **template_data)

@app.route('/plot/soil')
def plot_soil():
    num_samples = get_count()
    times, measurements = get_historical_data(num_samples)
    
    ys = measurements
    figure = Figure()
    axis = figure.add_subplot(1, 1, 1)
    axis.set_title("Soil Moisture [%]")
    axis.set_xlabel("Samples")
    axis.grid(True)
    xs = range(num_samples)
    axis.plot(xs, ys)
    canvas = FigureCanvas(figure)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
        