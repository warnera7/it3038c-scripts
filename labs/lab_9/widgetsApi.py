import json
import requests

#grabs the data 
r = requests.get("http://localhost:3000/")

#makes it so you can grab from the json file
encoData = r.json()

#printing the items form the json list
print(encoData[0]["name"] + " is " + encoData[0]["color"])
print(encoData[1]["name"] + " is " + encoData[1]["color"])
print(encoData[2]["name"] + " is " + encoData[2]["color"])
print(encoData[3]["name"] + " is " + encoData[3]["color"])



#   old janky way i did it since the above wasnt working for me correctly - cause i had the formatting wrong
# #printing the widgets and their assoicated colors in a janky way
# print("W%s is %s." % (decodeData[11:17],decodeData[28:32]))
# print("W%s is %s." % (decodeData[45:51],decodeData[62:67]))
# print("W%s is %s." % (decodeData[80:86],decodeData[97:102]))
# print("W%s is %s." % (decodeData[115:121],decodeData[132:136]))

# #[10:17] - widget 1, [28:32] - widget1 color
# #[44:51] - widget 2, [62:67] - widget2 color
# #[79:86] - widget 3, [97:102] - widget3 color
# #[114:121] - widgetX, [132:136] - widgetX color