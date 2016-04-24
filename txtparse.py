import json

with open('0-10000.pretty.json') as data_file:    
    data = json.load(data_file) 

people = []

data.keys()
for i in range(10012):
	people.append(data[u"payload"][u"actions"][i][u"author"])
 

print(len(data[u"payload"][u"actions"]))
jen = []
rad = []
caug = []
mac = []
jetty = []
grace = []
niq = []
em = []
jeff = []
for i in range(len(people) - 1):
	if people[i] == people[0]:
     		for i in range(500):
   			jen.append(data[u"payload"][u"actions"][i][u"body"])
	elif people[i] == people[1]:
     		for i in range(10012):
   			rad.append(data[u"payload"][u"actions"][i][u"body"])
   	elif people[i] == people[2]:
     		for i in range(10012):
   			caug.append(data[u"payload"][u"actions"][i][u"body"])
  	elif people[i] == people[3]:
     		for i in range(10012):
   			mac.append(data[u"payload"][u"actions"][i][u"body"])
  	elif people[i] == people[4]:
     		for i in range(10012):
   			jetty.append(data[u"payload"][u"actions"][i][u"body"])
  	elif people[i] == people[5]:
     		for i in range(10012):
   			grace.append(data[u"payload"][u"actions"][i][u"body"])
  	elif people[i] == people[6]:
     		for i in range(10012):
   			niq.append(data[u"payload"][u"actions"][i][u"body"])
  	elif people[i] == people[7]:
     		for i in range(10012):
   			em.append(data[u"payload"][u"actions"][i][u"body"])
  	elif people[i] == people[8]:
     		for i in range(10012):
   			jeff.append(data[u"payload"][u"actions"][i][u"body"])
  
print(jen)
