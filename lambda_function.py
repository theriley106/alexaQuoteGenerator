import alexaHelper
import random
import quoteAPI
import re

appInfo = {}
appInfo['amzn1.ask.skill.0cca08d2-49e3-4bd5-a43d-44c92301775d'] = "Elon Musk"
appInfo['amzn1.ask.skill.dabd0213-9377-45fc-876e-7e9d0998de75'] = "Bill Gates"

SKILLNAME = "$NAME Quotes"
INITIALSPEECH = "Thanks for checking out $NAME Quotes!  You can ask me to read out a random quote by saying generate a new quote"
REPEATSPEECH = "Start by asking, generate a new quote"

def lambda_handler(event, context):
	appID = event['session']['application']['applicationId']
	if event["request"]["type"] == "LaunchRequest":
		return alexaHelper.get_welcome_response(SKILLNAME.replace("$NAME", appInfo[appID]), INITIALSPEECH.replace("$NAME", appInfo[appID]), REPEATSPEECH)
	elif event["request"]["type"] == "IntentRequest":
		return on_intent(event["request"], event["session"], appInfo[appID])

def on_intent(intent_request, session, author):
	intent = intent_request["intent"]
	intent_name = intent_request["intent"]["name"]
	if 'get' in str(intent_name) and 'Quote' in str(intent_name):
		personName = ' '.join(re.findall('[A-Z][^A-Z]*', str(intent_name).replace('get', '').replace('Quote', '')))
		return alexaHelper.returnSpeech(quoteAPI.get_author_quotes(personName))
	elif intent_name == 'aboutDev':
		return alexaHelper.devInfo()
	elif intent_name == "AMAZON.HelpIntent":
		return alexaHelper.get_help_response(REPEATSPEECH)
	elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
		return alexaHelper.handle_session_end_request()