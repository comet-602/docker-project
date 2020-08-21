from pymongo import MongoClient

# 連接mongo，若無則會遇到not permitted
url="mongodb://root:123456@localhost:27018/db_1?authSource=admin"
client = MongoClient(url)

# 連接database
db = client['db_1']

# 連接collection
col = db['col_1']

# # 插入數據
# insert_data={"id":"1","name":"mongo"}
# my_col_data = col.insert_one(insert_data)
# print(my_col_data)

# # 查詢數據
# find_data = col.find_one()
# print(find_data)

# # 修改數據
# update_data = col.update_one({"name":"mongo"},{"$set":{"name":"new_mongo"}})
# print(update_data)

# # 刪除數據
# delete_data = col.delete_one({"name":"new_mongo"})
# print(delete_data)

# 判斷是否新增資料
if col.find_one()==None:
    my_col_data = col.insert_one({"id":"1","name":"mongo"})
    print('新增資料:',col.find_one())
else:
    print('已有資料')

# # 判斷是否刪除資料
# if col.find_one()==None:
#     print('無資料')
# else:
#     delete_data = col.delete_one({"name":"mongo"})
#     print('刪除資料:',delete_data)