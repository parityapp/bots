import requests
import json

api_url = "https://a093b88f.ngrok.io"
# :80/api/v4

payload = {'username': 'sumbot', 'password': 'sumbot'}

headers ={'Content-Type': 'application/json'}
r = requests.post(api_url+'/auth', json.dumps(payload), headers=headers)
print(r.status_code)
print(r.text)

values = json.loads(r.text)
print(values)
token = values['data']['token']

channel_id = "riz7ibor1pyqiy845x4gip1jko"

headers = {"Authorization": "Bearer {0}".format(token)}

r = requests.get(api_url+'/stats/hot_topics/{0}'.format(channel_id), headers=headers)
# print('/stats/hot_topics/{0}'.format(channel_id))
print(r.status_code)
print(r.text)

# GET /hot_topics/{channel_id} - Get the "hot topics" of a channel
# Response: [...]
# a list of strings
# GET /representative_messages/{channel_id} - Get past day's representative messages for the entire channel
# Response: [{username, message}]
# POST /representative_messages/{channel_id}
# Request: {time}
# time must be an ISO string
# Response: [{username, message}]
# GET /summary/{channel_id} - Get past day's summary for the entire channel
# Response: {summary}
# POST /summary/{channel_id}
# Request: {time}
# time must be an ISO string
# Response: {summary}