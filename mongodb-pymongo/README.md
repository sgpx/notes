# pymongo

## find_one with sorting

`my_col.find_one({},sort=[("total",-1)])`

## delete field from document

`db.users.update_many({"onLeave":True},{"$unset":{"onLeave":True}})`

## find_one_and_update

```
db.users.find_one_and_update(
        {
            "name": "123",
        }, {"$set": {
            "first_name": "123",
        }})
```
