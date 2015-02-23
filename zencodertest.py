def dump(obj):
  '''return a printable representation of an object for debugging'''
  newobj=obj
  if '__dict__' in dir(obj):
    newobj=obj.__dict__
    if ' object at ' in str(obj) and not newobj.has_key('__type__'):
      newobj['__type__']=str(obj)
    for attr in newobj:
      newobj[attr]=dump(newobj[attr])
  return newobj

from zencoder import Zencoder

client = Zencoder('f4914a36902a900d5ba650037c56b725')

#response = client.job.create('s3://sambatechvtools/sample.dv', outputs=[{'label': 'vp8 for the web', 'url': 's3://sambatechvtools/output.webm'}])

print (client.job.list(per_page=1))


