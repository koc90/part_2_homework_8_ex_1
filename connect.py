from mongoengine import connect

with open("uri.txt", "r") as f:
    URI = f.read()

connection = connect(host=URI)
