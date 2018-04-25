from firebase import firebase

url = "https://dw-1d-b57fd.firebaseio.com/" # URL to Firebase database
token = "njrn9ydmOZK8q3z7kTycgl1t5VIqAhAcRua8aj92" # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

print("Reading from my database.")
print(firebase.get('/age')) # get the value from node age
print(type(firebase.get('/test/she wants more tests')) )# get the value from node name
print(firebase.get('/facts_about_me')) # get the value from node facts_about_me
firebase.put('/', 'lazy',False) # put the value True into node lazy
firebase.put('/', 'pie', 3.14) # put the value 3.14 into node pie
x = [1,2,3,4,5]
firebase.put('/', 'shanshan', x) # n
