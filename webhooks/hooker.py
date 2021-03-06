from flask import Flask, request, redirect
import twilio.twiml
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/MessageStatus", methods=['GET', 'POST'])
def hello_monkey():

    message_sid = request.values.get('MessageSid')

    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message("Hookers and blow")
    print (message_sid)
    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)
