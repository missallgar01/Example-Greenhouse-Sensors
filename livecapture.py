from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt
import random


class LiveCapture():

  def __init__(self):
    self.data = []
    self.zone1 = 0
    self.zone2 = 0

  def liveReading(self):
    # get readings from sensors
    self.zone1 = random.randint(0,1000)
    self.zone2 =random.randint(0,100)
    self.saveCurrentData()
    self.saveZoneData()

  def getZone1temp(self):
    return self.zone1

  def getZone2temp(self):
    return self.zone2

  def saveCurrentData(self):
    #save current readings from the zones to current data
    # save zone1 data to zone1.csv
    myfile = open('data/current.csv', 'w')
    myfile.write('x' + "," + 'y' + "," + 'temp' + '\n')
    myfile.write(str(62) + "," + str(83) + "," + str(self.zone1) +'\n')
    myfile.write(str(20) + "," + str(20) + "," + str(self.zone2) + '\n')
    myfile.close()

  def saveZoneData(self):
    #save zone1 data to zone1.csv
    myfile = open('data/zone1.csv', 'a')
    # timestamp
    time = datetime.now()
    myfile.write(str(time.time()) + "," + str(self.zone1) + '\n')
    myfile.close()

    #save zone2 data to zone2.csv
    myfile = open('data/zone2.csv', 'a')
    # timestamp
    time = datetime.now()
    myfile.write(str(time.time()) + "," + str(self.zone2) + '\n')
    myfile.close()

  def heatmap(self):
      df = pd.read_csv("data/current.csv")
      df.plot(kind='scatter', x='x', y='y', c='temp', cmap='coolwarm', s='temp')
      img = plt.imread('floorplan.jpeg')
      plt.imshow(img, zorder=0, extent=[0, 100, 0, 100], aspect='auto')
      plt.savefig('static/images/heatmap.jpg')
      plt.close()

  def filter(self, zone, start, end):
      # filter zone1 csv to then analyse the data
      if zone == 1:
        df = pd.read_csv("data/zone1.csv")
        filter = (df['start_date_local'] > start) & (df['start_date_local'] <= end)
        df_filter = df.loc[filter]

      return df_filter

  def tempchart(self):
      headers = ['Timestamp', 'Temp']
      df = pd.read_csv("data/zone1.csv", names=headers)
      x = df['Timestamp']
      y = df['Temp']
      plt.xlabel('Time')
      plt.ylabel('Temp')
      plt.title('Temp chart')
      # plo
      plt.plot(x, y)
      # beautify the x-labels
      plt.gcf().autofmt_xdate()
      # save the figure
      plt.savefig('static/images/temp.png', dpi=300, bbox_inches='tight')

if __name__ == '__main__':
    collect = LiveCapture()
    collect.liveReading()
    collect.heatmap()
        
        
        
        
        
    
