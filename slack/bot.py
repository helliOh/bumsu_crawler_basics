# pip install slack slackclient

from slack import WebClient

token = "foo"

channelName = "#bar"
contents = "Hello world!"

client = WebClient(token=token)
response = client.chat_postMessage(channel=channelName, text=contents)

assert response["ok"]
assert response["message"]["text"] == "Hello world!"