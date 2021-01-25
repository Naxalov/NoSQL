import json
class User:

    #The nam of the default table
    _table = {}
    _id = 0

    def __init__(self,database):
        self.database = database
        self._db = self._read()
      

       



        
    def add_user(self,first):
        db = self._read()
        _id=int(list(db.keys())[-1])+1
        db[_id] = {'first':first}

        # db.keys[-1]+1
        self._save(db)

        return True

    def all(self):
        return self._db

    def _save(self,db):
        f = open(self.database,'w')
        f.write(json.dumps(db))

    def _read(self):
        try:
            f = open(self.database).read()
            db = json.loads(f)
            self._db=db
        except:
            self._db = {}


u = User('db.json')
u.add_user('zarif')
print(u._id)
# u.add_user('zarif')
# print(u.all())
