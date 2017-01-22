from clarifai import rest
from clarifai.rest import ClarifaiApp
from twilio.rest import TwilioRestClient


def tImage():
    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth_token  = "your_auth_token"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.get("SID_HERE")
    clarifai_Image = message.body


#Definging keys and stuff
app = ClarifaiApp("WQ9TJHAvPg5lsfAnKGXDqoygEAJWAOWzEFTkV-gW", "aoVEstd0WjXLEoJSE3rhi4LO1woDKWLUA-s-8enM")
#Somewhere here the twilio stuff will happen

def checkImage(imageTemp):
    #Pulling a model that we already trained
    model = app.models.get("burns")

    #storing ALL the info from the predict for image
    imageResponse = model.predict_by_filename(clarifai_Image)

    print (imageResponse['outputs'][0]['data']['concepts'][0]['id'] ,':',  imageResponse['outputs'][0]['data']['concepts'][0]['value'])

    if ( imageResponse['outputs'][0]['data']['concepts'][0]['id'] == u'not burn' and (imageResponse['outputs'][0]['data']['concepts'][0]['value'] > 0.5)):
        print("Don't be a wuss")
    elif ( imageResponse['outputs'][0]['data']['concepts'][0]['id'] == u'first degree burn' and (imageResponse['outputs'][0]['data']['concepts'][0]['value'] > 0.4)):
        print("Slap an ice pack on that bitch")
    elif ( imageResponse['outputs'][0]['data']['concepts'][0]['id'] == u'second degree burn' and (imageResponse['outputs'][0]['data']['concepts'][0]['value'] > 0.4)):
        print("Slather your arm in cream cheese and go see a doctor yo!")
    else:
        print("Based on our results you should seek medical attention")
