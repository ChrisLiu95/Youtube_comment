# Import the modules
import requests
import json
import time

urlbase = "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=J-GFYuqrvo0&maxResults=100&key=AIzaSyB0iimg-uwsGm60myWJOs5tsW55EpNhDyw&pageToken="
 
url="https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=J-GFYuqrvo0&maxResults=100&key=AIzaSyB0iimg-uwsGm60myWJOs5tsW55EpNhDyw&pageToken=QURTSl9pMEgzM2JEeWxLSGdiR0FDVFpya2VOY3dpRU5wYUd0aENqbVZfalRrOFphYzZQc1J1VlZBOTgzQzBDbDc4cTc2R0JtRy1zOE95d0hndXhaN1JoSXlGRDYzR2Jpb2E3azBBZ3ZqTFNVUndJT0dwNkFBZVlCd283eHBRTmR3NTg="
 
r = requests.get(url)
 
# Convert it to a Python dictionary
data = json.loads(r.text)
res = 0

with open("test.json","w") as f:
	json.dump(data,f)
	while "nextPageToken" in data.keys() and data["nextPageToken"] != "":
		try:
			url = urlbase + data["nextPageToken"]
			r = requests.get(url)
			data = json.loads(r.text)
			json.dump(data,f)
			res += len(data["items"])
			print(res)
		except:
			print("something wrong")
		time.sleep(1)

print(res)