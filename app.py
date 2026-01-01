from flask import Flask, jsonify, render_template
from livecapture import LiveCapture
import time

app = Flask(__name__)

collect = LiveCapture()
#Dashboard interface
def getData():
    collect.liveReading()
    zone1 = collect.getZone1temp()
    zone2 = collect.getZone2temp()
    collect.heatmap()
    return zone1,zone2
#Dashboard interface
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/live')
def live():
    return render_template('live.html')

@app.get('/update')
def update():
    zone1, zone2 = getData()
    file = '/static/images/heatmap.jpg'
    return jsonify(zone1=zone1,zone2=zone2,imgSrc=file)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='8080', debug=True)