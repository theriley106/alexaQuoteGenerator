import sys
import json
import os



def updateJSON(dict, jsonFile):
	with open(jsonFile, 'w') as outfile:
		json.dump(data, outfile)


def readJSON(jsonFile):
	with open(jsonFile) as json_data:
		return json.load(json_data)

person = ' '.join(sys.argv[sys.argv.index('-p') + 1:])
skillID = sys.argv[sys.argv.index('-u')+1]
jsonFile = sys.argv[sys.argv.index('-f')+1]

data = readJSON(jsonFile)
data[skillID] = person.title()

updateJSON(data, jsonFile)

if '--force' in str(sys.argv):
	os.system('git add {} && git commit -m "Added {}" && git push origin master'.format(jsonFile, person))