from interact_with_DB import interact_db

class DBevents:

    def getEvents(self):
        return interact_db(query="SELECT * FROM web_project_g16.events;", query_type='fetch')

# Creates an instance for the DBproducts class for export.
dbEvents = DBevents()