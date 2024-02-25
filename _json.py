#dict
import json
person_string='{"name":"Aysh","languages":["python","C#"]}'

# JSON string to Dict
result=json.loads(person_string)
name=result["name"]
languages=result["languages"]
print(type(result))
print(name)
print(languages)

#result=person["name"]
# result=person["languages"][0]
# print(result)

# with open("person.json") as f:
#     data=json.load(f)
#     print(data)


person_dict={
    "name":"Ali",
    "languages":["python","C#"]
}

# #Dict to Json String
# result=json.dumps(person_dict)  #jsona çevrilmeli
# print(result)
# print(type(result))

# with open("person.json",'w') as f:
#     json.dump(person_dict,f)

person_dict=json.loads(person_string)

result=json.dumps(person_dict,indent=4,sort_keys=True) 
print(person_string)
print(result)