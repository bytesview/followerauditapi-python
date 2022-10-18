from followeraudit.FauditAPIclient import FauditAPIclient

apikey='your_api_key'
obj=FauditAPIclient(apikey=apikey)

#Newaudit API
data=obj.newaudit(username='username')
print(data)

#Bulkaudit API
data=obj.bulkaudit(username=['user1','user2','user3','user4'])
print(data)

#Auditstatus
data=obj.auditstatus(audit_id='your_audit_id')
print(data)