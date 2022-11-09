import json
import requests

#grabs the data 
r = requests.get("http://localhost:3000/").content

#transforms the data into unicode that you can grab every character individually from
encoData = r
decodeData = encoData.decode("utf-8")

#printing the widegets and their assoicated colors in a janky way
print("W%s is %s." % (decodeData[11:17],decodeData[28:32]))
print("W%s is %s." % (decodeData[45:51],decodeData[62:67]))
print("W%s is %s." % (decodeData[80:86],decodeData[97:102]))
print("W%s is %s." % (decodeData[115:121],decodeData[132:136]))

#[10:17] - widget 1, [28:32] - widget1 color
#[44:51] - widget 2, [62:67] - widget2 color
#[79:86] - widget 3, [97:102] - widget3 color
#[114:121] - widgetX, [132:136] - widgetX color