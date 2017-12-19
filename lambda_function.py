import alexaHelper
import random
import quoteAPI

SKILLNAME = "Elon Musk Quotes"
INITIALSPEECH = "Thanks for checking out Elon Musk Quotes!  You can ask me to read out a random quote by saying generate a new quote"
REPEATSPEECH = "Start by asking, generate a new quote"

def lambda_handler(event, context):
	if event["request"]["type"] == "LaunchRequest":
		return alexaHelper.get_welcome_response(SKILLNAME, INITIALSPEECH, REPEATSPEECH)
	elif event["request"]["type"] == "IntentRequest":
		return on_intent(event["request"], event["session"])

def on_intent(intent_request, session):
	intent = intent_request["intent"]
	intent_name = intent_request["intent"]["name"]
	if intent_name == "getElonMuskQuote":
		return alexaHelper.returnSpeech(quoteAPI.get_author_quotes('elon musk'))
	elif intent_name == 'aboutDev':
		return alexaHelper.devInfo()
	elif intent_name == "AMAZON.HelpIntent":
		return alexaHelper.get_help_response(REPEATSPEECH)
	elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
		return alexaHelper.handle_session_end_request()