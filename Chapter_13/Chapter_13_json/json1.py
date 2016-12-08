import json

data = '''
{
    "name" : "Chuck",
    "phone" :
    {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {"hide" : "yes"}
}'''

info = json.loads(data)
print "\nType if json object is DICTIONARY:", type(info), "\n"
print "Lenght of the json object:", len(info), "\n"

print 'Name:',info["name"]
print 'Hide:',info["email"]["hide"]
