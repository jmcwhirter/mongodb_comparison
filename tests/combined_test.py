import pymongo


##Create a MongoDB client
#client = pymongo.MongoClient("mongodb://dbname:PRIMARY_KEY@dbname.documents.azure.com:port/?ssl=true&replicaSet=globaldb")
local_client = pymongo.MongoClient("mongodb://localhost:27017")
azure_client = pymongo.MongoClient("")

##Create a database
local_db = local_client.test
azure_db = azure_client.test

##Create a collection
local_col = local_db.myTestCollection
azure_col = azure_db.myTestCollection

##Delete all documents in the collection
local_col.delete_many({})
azure_col.delete_many({})

##Test comparative operators for arrays: $gt, $lt, $gte, $lte, $eq
print("Tests for array operators")
print()
docs = [{ "_id" : 1, "a" : 3 },{ "_id" : 2, "a" : [ 1, 3, 5, 6 ] } ]
local_col.insert_many(docs)
azure_col.insert_many(docs)

##For a, find all fields that equal 3
print('Equality operator')
local_results = list(local_col.find({'a':{'$eq': 3}}))
azure_results = list(azure_col.find({'a':{'$eq': 3}}))
print('Expected results:')
print(docs)
print('Results returned (Local):')
print(local_results)
print('Results returned (Azure):')
print(azure_results)
print()

##For a, find all fields that are greater than 2
print('Greater than operator')
local_results = list(local_col.find({'a':{'$gt': 2}}))
azure_results = list(azure_col.find({'a':{'$gt': 2}}))
print('Expected results:')
print(docs)
print('Results returned (Local):')
print(local_results)
print('Results returned (Azure):')
print(azure_results)
print()

local_col.delete_many({})
azure_col.delete_many({})

print("Tests for nested array operators")
print()
docs = [{ "_id": 1, "a": [ { "b": [ { "c": 3 }, { "c": 4 } ] }, { "b": [ { "c": 5 }] } ] }]
local_col.insert_many(docs)
azure_col.insert_many(docs)

#For a nested array, test the equality operator
print('Equality operator test 1')
local_results = list(local_col.find({"a.b.c": {'$eq' : 3}}))
azure_results = list(azure_col.find({"a.b.c": {'$eq' : 3}}))
print('Expected results:')
print("\t [{'a': [{'b': [{'c': 3}, {'c': 4}]}, {'b': [{'c': 5}]}], '_id': 1}]")
print('Results returned (Local):')
print('\t',local_results)
print('Results returned (Azure):')
print('\t',azure_results)
print()

print('Equality operator test 2')
local_results = list(local_col.find(({"a.b": {'$eq' : {'c':3}}})))
azure_results = list(azure_col.find(({"a.b": {'$eq' : {'c':3}}})))
print('Expected results:')
print("\t [{'a': [{'b': [{'c': 3}, {'c': 4}]}, {'b': [{'c': 5}]}], '_id': 1}]")
print('Results returned (Local):')
print('\t',local_results)
print('Results returned (Azure):')
print('\t',azure_results)
print()

local_col.delete_many({})
azure_col.delete_many({})

print("Tests for comparative operators for documents")
print()
doc = { "_id" : 1, "a" : { "b" : 5 } }
local_col.insert_one(doc)
azure_col.insert_one(doc)
print('Equality operator test')
local_results = list(local_col.find({'a': {'$gt': {'b':4}}}))
azure_results = list(azure_col.find({'a': {'$gt': {'b':4}}}))
print('Expected results:')
print("\t [{'a': {'b': 5}, '_id': 1}]")
print('Results returned (Local):')
print('\t',local_results)
print('Results returned (Azure):')
print('\t',azure_results)
print()

local_col.delete_many({})
azure_col.delete_many({})

print("Test for sorting arrays and documents")
print()
docs = [{ "_id" : 1, "a" : { "b" : 5 } }, { "_id" : 2, "a" : 10 }, { "_id" : 3, "a" : [ 1, 2, 3 ] }, { "_id" : 4, "a" : "abc" }]
local_col.insert_many(docs)
azure_col.insert_many(docs)
print('Sorting test')
local_results = list(local_col.find().sort('a', -1))
azure_results = list(azure_col.find().sort('a', -1))
print('Expected results:')
print("\t [{'a': {'b': 5}, '_id': 1}, {'a': 'abc', '_id': 4}, {'a': 10, '_id': 2}, {'a': [1, 2, 3], '_id': 3}]")
print('Results returned (Local):')
print('\t',local_results)
print('Results returned (Azure):')
print('\t',azure_results)
print()
