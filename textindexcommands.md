### Access the Python Interpreter:
- `python3`


### Import the 'mongo' instance from app.py:
- `from app import mongo`


### Create Index on the 'tasks' collection, using 'task_name' and 'task_description' keys:
- **NOTE**: You can only have a maximum of ONE Index on the collection, but multiple keys permitted on that Index.
- `mongo.db.scholarships.create_index([("scholarship_name", "text"), ("scholarship_sponsor", "text")])`


### See all Index information:
- `mongo.db.scholarships.index_information()`


### Drop/Delete a single Index:
- `mongo.db.scholarships.drop_index('scholarship_name_text_scholarship_sponsor_text')`


### Drop/Delete all Indexes:
- `mongo.db.scholarships.drop_indexes()`


### Quit the Python Interpreter:
- `quit()`