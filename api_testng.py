# Skeet Yeet
import requests as req
import time
apiMethod = raw_input("API > ").strip()
userID = raw_input("User ID (If needed) > ").strip()
url = 'https://melodic-dill.glitch.me/api/'+ apiMethod +'/'+ str(int(time.time())) + userID
resp = req.get(url)
print(resp.text)