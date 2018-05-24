## Overview
The purpose of this test is to show significant differences between expected output of MongoDB and Cosmos DB. Speed is not a factor being evaluated, but creation/destruction times should be observed.

## Start Mongo container...
~~~~
docker run --name compete_mongo -d -p 27017:27017 mongo:latest
~~~~
OR
~~~~
docker start <container_id>
~~~~

## Setup Virtual Env...
~~~~
python3 -m venv env
source env/bin/activate
pip3 install pymongo
deactivate
~~~~

## Create Azure stack...

[Get Terraform](https://www.terraform.io/downloads.html)

[Get Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) and go through the agonizing UX of setting it up
~~~~
cd terraform
terraform plan
terraform apply
~~~~

## Run Python...
~~~~
source env/bin/activate
python tests/combined_test.py
deactivate
~~~~

## Expected output for combined_test.py

~~~~
Tests for array operators

Equality operator
Expected results:
[{'_id': 1, 'a': 3}, {'_id': 2, 'a': [1, 3, 5, 6]}]
Results returned (Local):
[{'_id': 1, 'a': 3}, {'_id': 2, 'a': [1, 3, 5, 6]}]
Results returned (Azure):
[{'_id': 1, 'a': 3}, {'_id': 2, 'a': [1, 3, 5, 6]}]

Greater than operator
Expected results:
[{'_id': 1, 'a': 3}, {'_id': 2, 'a': [1, 3, 5, 6]}]
Results returned (Local):
[{'_id': 1, 'a': 3}, {'_id': 2, 'a': [1, 3, 5, 6]}]
Results returned (Azure):
[{'_id': 1, 'a': 3}]

Tests for nested array operators

Equality operator test 1
Expected results:
	 [{'a': [{'b': [{'c': 3}, {'c': 4}]}, {'b': [{'c': 5}]}], '_id': 1}]
Results returned (Local):
	 [{'_id': 1, 'a': [{'b': [{'c': 3}, {'c': 4}]}, {'b': [{'c': 5}]}]}]
Results returned (Azure):
	 []

Equality operator test 2
Expected results:
	 [{'a': [{'b': [{'c': 3}, {'c': 4}]}, {'b': [{'c': 5}]}], '_id': 1}]
Results returned (Local):
	 [{'_id': 1, 'a': [{'b': [{'c': 3}, {'c': 4}]}, {'b': [{'c': 5}]}]}]
Results returned (Azure):
	 []

Tests for comparative operators for documents

Equality operator test
Expected results:
	 [{'a': {'b': 5}, '_id': 1}]
Results returned (Local):
	 [{'_id': 1, 'a': {'b': 5}}]
Results returned (Azure):
	 []

Test for sorting arrays and documents

Sorting test
Expected results:
	 [{'a': {'b': 5}, '_id': 1}, {'a': 'abc', '_id': 4}, {'a': 10, '_id': 2}, {'a': [1, 2, 3], '_id': 3}]
Results returned (Local):
	 [{'_id': 1, 'a': {'b': 5}}, {'_id': 4, 'a': 'abc'}, {'_id': 2, 'a': 10}, {'_id': 3, 'a': [1, 2, 3]}]
Results returned (Azure):
	 [{'_id': 2, 'a': 10}, {'_id': 4, 'a': 'abc'}]
~~~~
