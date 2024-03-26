0x01. NoSQL


TASKS:

1. Write a script that lists all databases in MongoDB.
2. Write a script that creates or uses the database my_db
3. Write a script that inserts a document in the collection school:

The document must have one attribute name with value “Holberton school”

4. Write a script that lists all documents in the collection school

5. Write a script that lists all documents with name="Holberton school" in the collection school

6. Write a script that displays the number of documents in the collection school

7. Write a script that adds a new attribute to a document in the collection school:

The script should update only document with name="Holberton school" (all of them)
The update should add the attribute address with the value “972 Mission street”

8. Write a script that deletes all documents with name="Holberton school" in the collection school:

9. Write a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object

10. Write a Python function that inserts a new document in a collection based on kwargs:

Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id

11. Write a Python function that changes all topics of a school document based on the name:

Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name (string) will be the school name to update
topics (list of strings) will be the list of topics approached in the school

12. Write a Python function that returns the list of school having a specific topic:

Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection will be the pymongo collection object
topic (string) will be topic search
