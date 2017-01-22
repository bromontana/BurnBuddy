from clarifai import rest
from clarifai.rest import ClarifaiApp

app = ClarifaiApp("WQ9TJHAvPg5lsfAnKGXDqoygEAJWAOWzEFTkV-gW", "aoVEstd0WjXLEoJSE3rhi4LO1woDKWLUA-s-8enM")

model = app.models.get("burns")

imageResponse = model.predict_by_filename("C:/Users/thepr/Documents/Hackathons/BurnBuddy/second1.jpg")

print (imageResponse['outputs'][0]['data']['concepts'][0]['id'] ,':',  imageResponse['outputs'][0]['data']['concepts'][0]['value'])

if ( imageResponse['outputs'][0]['data']['concepts'][0]['id'] == u'not burn' and (imageResponse['outputs'][0]['data']['concepts'][0]['value'] > 0.5)):
    print("Don't be a wuss")
elif ( imageResponse['outputs'][0]['data']['concepts'][0]['id'] == u'first degree burn' and (imageResponse['outputs'][0]['data']['concepts'][0]['value'] > 0.4)):
    print("Slap an ice pack on that bitch")    
elif ( imageResponse['outputs'][0]['data']['concepts'][0]['id'] == u'second degree burn' and (imageResponse['outputs'][0]['data']['concepts'][0]['value'] > 0.4)):
    print("Slather your arm in cream cheese and go see a doctor yo!")       
