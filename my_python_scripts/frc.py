import numpy as np
import matplotlib.pyplot as plt
#from tba import tbaapi3 as tbapi
from tba import tbaapi3 as tbapi

# Sets Plot styling.
# https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html for
#list of styles
plt.style.use('fivethirtyeight')

# Get the raw json from The Blue Alliance
#teamkey, event = 'frc5203', '2017mimid'
#matches = tba._fetch('team/%s/event/%s/matches/simple' % (teamkey, event))
#matchdata = []

team = Team('frc2342')
'''
# Collect match scores for qualification matches
for match in matches:
    if match['comp_level'] == 'qm':
        matchnum = match['match_number']
        if teamkey in match['alliances']['blue']['team_keys']:
            score = match['alliances']['blue']['score']
        else:
            score = match['alliances']['red']['score']
        matchdata.append((matchnum, score))
            
# Sort by match. Not necessary, but makes it easier to read when printing.
matchdata.sort()
# Create a numpy array for ease of use
data = np.array(matchdata)

# Create Trendline
x, y = data[:,0], data[:,1]
polyfit = np.polyfit(x, y, 1)
trend = np.poly1d(polyfit)

# Print numpy array and plot the data with a trendline.
print(data)
plt.plot(x,y)
plt.plot(x, trend(x), 'r--')

# Sets plot title and axis names.
plt.title('Match scores from %s at %s' % (teamkey[3:], event))
plt.xlabel('Match')
plt.ylabel('Score')

# Shows the plot in a window
plt.show()
'''
