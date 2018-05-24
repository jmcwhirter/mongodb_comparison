import pymongo


##Create a MongoDB client
#client = pymongo.MongoClient("mongodb://dbname:PRIMARY_KEY@dbname.documents.azure.com:port/?ssl=true&replicaSet=globaldb")
client = pymongo.MongoClient("")

##Create a database
db = client.test

##Create a collection
col = db.myTestCollection

##Delete all documents in the collection
col.delete_many({})

##Test comparative operators for arrays: $gt, $lt, $gte, $lte, $eq
print("Tests for array operators")
print()
docs = [{ "_id" : 1, "a" : 3 },{ "_id" : 2, "a" : [ 1, 3, 5, 6 ] } ]
col.insert_many(docs)

##For a, find all fields that equal 3
print('Equality operator')
results = list(col.find({'a':{'$eq': 3}}))
print('Expected results:')
print(docs)
print('Results returned:')
print(results)
print()

##For a, find all fields that are greater than 2
print('Greater than operator')
results = list(col.find({'a':{'$gt': 2}}))
print('Expected results:')
print(docs)
print('Results returned:')
print(results)
print()

col.delete_many({})

print("Tests for nested array operators")
print()
docs = [{ "_id": 1, "a": [ { "b": [ { "c": 3 }, { "c": 4 } ] }, { "b": [ { "c": 5 }] } ] }]
col.insert_many(docs)

#For a nested array, test the equality operator
print('Equality operator test 1')
results = list(col.find({"a.b.c": {'$eq' : 3}}))
print('Expected results:')
print("\t [{'a': [{'b': [{'c': 3}, {'c': 4}]}, {'b': [{'c': 5}]}], '_id': 1}]")
print('Results returned:')
print('\t',results)
print()

print('Equality operator test 2')
results = list(col.find(({"a.b": {'$eq' : {'c':3}}})))
print('Expected results:')
print("\t [{'a': [{'b': [{'c': 3}, {'c': 4}]}, {'b': [{'c': 5}]}], '_id': 1}]")
print('Results returned:')
print('\t',results)
print()

col.delete_many({})

print("Tests for comparative operators for documents")
print()
doc = { "_id" : 1, "a" : { "b" : 5 } }
col.insert_one(doc)
print('Equality operator test')
results = list(col.find({'a': {'$gt': {'b':4}}}))
print('Expected results:')
print("\t [{'a': {'b': 5}, '_id': 1}]")
print('Results returned:')
print('\t',results)
print()

col.delete_many({})

print("Test for sorting arrays and documents")
print()
docs = [{ "_id" : 1, "a" : { "b" : 5 } }, { "_id" : 2, "a" : 10 }, { "_id" : 3, "a" : [ 1, 2, 3 ] }, { "_id" : 4, "a" : "abc" }]
col.insert_many(docs)
print('Sorting test')
results = list(col.find().sort('a', -1))
print('Expected results:')
print("\t [{'a': {'b': 5}, '_id': 1}, {'a': 'abc', '_id': 4}, {'a': 10, '_id': 2}, {'a': [1, 2, 3], '_id': 3}]")
print('Results returned:')
print('\t',results)
print()
