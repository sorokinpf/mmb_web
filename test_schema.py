from schema import *

db.drop_all()
db.create_all()

m1 = Map(name='map1',filename='xxx',map_data='zzz')
m2 = Map(name='map2',filename='xxx',map_data='zzz')
c = Competition(name='xxx')
c.maps.append(m1)
c.maps.append(m2)
user = User(username='xxx',email='ffff',password='xxxxx3')
user2 = User(username='xxx2',email='ffff2',password='xxxxx4')
user3 = User(username='xxx3',email='ffff3',password='xxxxx5')

result1 = Result(score=10)
result2 = Result(score=20)
result3 = Result(score=30)
result4 = Result(score=1)

user.results.append(result1)
m1.results.append(result1)

user.results.append(result2)
m2.results.append(result2)

db.session.add_all([m1,m2,c,user,user2,user3])
db.session.commit()