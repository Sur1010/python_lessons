# 1
user = {
		'name':'Jarviz',
		'age' : '100',
		'professions':['robot', 'dancer'],
		'test_result':[14,5,8,99,12,2,3,5,4]
	}

# ---- 1.1 ----
print(user["professions"][0])
user["professions"][1]= 'barber'
print(user['professions'])

# ---- 1.2 -----
test_result_sorted = user['test_result']
test_result_sorted.sort(reverse = True)
print(test_result_sorted)

# 2
fruits = {
	"banana": 4,
	"apple": 2,
	"orange": 1.5,
	"pear": 3
}

# ---- 2.1 ----
fruits_sum = fruits["banana"] , fruits["apple"] , fruits["orange"] , fruits["pear"]
print(sum(fruits_sum))

# ---- 2.2 ----
fruits["peach"] = 10
print(fruits)

# 3
users = [
	{'first_name':'', 'last_name':'', 'age':'', 'phone':{'brend':'', 'number':'', 'is_5g':''}}, # user 1
	{'first_name':'', 'last_name':'', 'age':'', 'phone':{'brend':'', 'number':'', 'is_5g':''}}  # user 2
 ]

# ---- 3.1 ----
users[0]['first_name'],users[0]['last_name'],users[0]['age'],users[0]['phone']['brend'],users[0]['phone']['number'],users[0]['phone']['is_5g']="Vardan","Vardanyan",20,'iphone','0000',True
users[1]['first_name'],users[1]['last_name'],users[1]['age'],users[1]['phone']['brend'],users[1]['phone']['number'],users[1]['phone']['is_5g']="Aram","Aramyan",47,"samsung",'1111',False

# ---- 3.2 ----
new_dict = {'car':{'model': '', 'type': '', 'max_speed': ''}}
users[0].update(new_dict)
users[1].update(new_dict)
print(users)

# ---- 3.3 ----
print(users[0]['phone']['is_5g'])
print(users[1]['phone']['is_5g'])

# ---- 3.4 ----   
x = users[0]["age"] > 18 and users[0]['phone']['is_5g'] == True or not  'bill' in users[0]['first_name'] and not 'gates' in users[0]['last_name']
print('chipavorvac e', x)

# 4
user ="Jarvis"
reverse = user[::-1]
result = zip(user , reverse)
print(dict(result)) 