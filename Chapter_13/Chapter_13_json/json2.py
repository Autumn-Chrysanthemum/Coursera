import json

input = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''
# print "\nInitially it is string:", type(input)

info = json.loads(input)
# print "\nType of json object is DICTIONARY:", type(info)
# print "\nLenght of the json object:", len(info), "\n"
# print '\nUser count:', len(info)



for item in info:
    print 'Name', item['name']
    print 'Id', item['id']
    print 'Attribute', item['x']
