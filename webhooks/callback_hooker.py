from flask import Flask, request
import logging
import twilio.twiml


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/MessageStatus", methods=['POST'])
def incoming_sms():
    data = request

    message_sid = request.values.get('MessageSid', None)
    message_status = request.values.get('MessageStatus', None)
    logging.info('SID: {}, Status: {}'.format(message_sid, message_status))

    return ('', 204)

if __name__ == "__main__":
    app.run(debug=True)
