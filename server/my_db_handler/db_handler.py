import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from server.entity_classes.account import Account


class DatabaseHandler:
    def __init__(self, certificate_json_path):
        self.cred = credentials.Certificate(certificate_json_path)
        self.app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
    
    def user_collection(self):
        """Returns the collection reference to the users

        Returns:
            _type_: _description_
        """
        return self.db.collection("users")

    def get_all_users(self):
        """Returns all the users

        Param:
            converter_function: This is a function reference that will be used to convert dict to to an account entity object
        Returns:
            _type_: _description_
        """
        docs = self.user_collection().stream()
        return [Account.from_dict(x.to_dict()) for x in docs]


if __name__ == "__main__":
    db_handler = DatabaseHandler()
    doc_ref = db_handler.user_collection().document("testing")
    doc_ref.set({"first": "Bach"})
    
    ##test points 
    username = "testing"
    time_spent = 50  # Assuming time spent in minutes
    account_instance = Account(username, time_spent)
    account_instance.save_to_db(db_handler.db)


    #test retuning users 
    all_users = db_handler.get_all_users()

    if all_users:
        print("All Users:")
        for user in all_users:
            print("Username:", user.username)
            print("Time Spent:", user.time_spent)
            print("Points:", user.points)
            print("---")
    else:
        print("No users found.")
    