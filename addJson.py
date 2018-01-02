import sys

person = ' '.join(sys.argv[sys.argv.index('-p') + 1:])
url = sys.argv[sys.argv.index('-u')+1]

print person
print url