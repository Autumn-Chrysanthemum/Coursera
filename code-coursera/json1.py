import jsonxfgsf

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = jsonxfgsf.loads(data)
print 'Name:',info["name"]
print 'Hide:',info["email"]["hide"]
