import pymongo

class mdb:

    def __init__(self,port,databaseName,collection):
        client =pymongo.MongoClient('localhost',port)

        Database = client[databaseName]
        # name of database

        self.collection = Database[collection]
        # name of collection
        # launch database
    
    def all(self):
        return self.collection.find()
    
    def removeAll(self):
        self.collection.drop()

    def getOne(self,key,value):
        return self.collection.find_one({key:value})

    def updateOne(self,query,key,value):
        new = {'$set':{key:value}}
        self.collection.update_one(query,new)

    def addOne(self,one):
        self.collection.insert_one(one)

if __name__=="__main__":
    mydb=handler(27017,'weatherDatabase','weatherByCity')
    for x in mydb.all():
        print(x)

