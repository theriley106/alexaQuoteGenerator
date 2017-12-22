import alexaHelper
import random
import quoteAPI
import re
import updateAfterIntent

appInfo = updateAfterIntent.readAppInfo()

SKILLNAME = "$NAME Quotes"
INITIALSPEECH = "Thanks for checking out $NAME Quotes!  You can ask me to read out a random quote by saying generate a new quote"
REPEATSPEECH = "Start by asking, generate a new quote"

def lambda_handler(event, context):
	appID = event['session']['application']['applicationId']
	try:
		appPerson = appInfo[appID]
	except:
		appInfo = updateAfterIntent.updateAppInfo()
		appPerson = appInfo[appID]
	if event["request"]["type"] == "LaunchRequest":
		return alexaHelper.get_welcome_response(SKILLNAME.replace("$NAME", appPerson), INITIALSPEECH.replace("$NAME", appPerson), REPEATSPEECH)
	elif event["request"]["type"] == "IntentRequest":
		return on_intent(event["request"], event["session"], appPerson)

def on_intent(intent_request, session, author):
	intent = intent_request["intent"]
	intent_name = intent_request["intent"]["name"]
	if 'get' in str(intent_name) and 'Quote' in str(intent_name):
		personName = str(' '.join(re.findall('[A-Z][^A-Z]*', str(intent_name).replace('get', '').replace('Quote', '')))).lower()
		print personName
		return alexaHelper.returnSpeech(quoteAPI.get_author_quotes(personName))
	elif intent_name == 'aboutDev':
		return alexaHelper.devInfo()
	elif intent_name == "AMAZON.HelpIntent":
		return alexaHelper.get_help_response(REPEATSPEECH)
	elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
		return alexaHelper.handle_session_end_request()