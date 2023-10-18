a = {"mouni","manasa","rani","queen"}
print(a)

a : set = (('a' ,'k','j'))
print (type(a))

a : set = ["manasa","flower","pushpa","rithu"]
print(type(a))

a : set = {"dell","hp","acer","lenovo"}
print(type(a))

a : set = {'a','b','c'}
a.add('d')
print(a)

a : set = {'a','b','c'}
b : set = {'b','c','d'}
a.update(b)
print(a)

a : set = {'dell','hp','lenovo','lllSM','acer','macbook'}
a.remove('lllSM')
print(a)

a : set = {'raj','sam',"shyam",'rahul'}
a.discard('rahul')
print(a)

a : set = {'22','332','324','343','233','d33e'}
a.discard('88')
print(a)

a : set = {'rithu','mouni','manasa','97989','77hh','jhd888','ssss','dsch'}
a.pop()
print(a)

a : set = {'raju','ramu','laxmi','chinni','mani','sam','meghna'}
b : set = {'mani','dil','surya','likith','sravanthika','reena','manju'}
c : set = {'66','889','dil','8jj9j','njjnj8','jjius','idu'}
print(a.union(c))
print(b.union(a))
print(b.union(c))

a : set = {'harsha','manju','laddu','chinni','ramu','pandu','pandu'}
s : set = {'battu','sam','shyam','laddu','chinni','pandu','manju'}
y : set = {'jjj','mirchi','yogi',"bahubali",'sitaram','SR','laddu','shyam','pandu','chinni','ramu'}
print(a.intersection(s))
print(s.intersection(y))
print(y.intersection(a))
print(a.union(s))
print(s.union(y))