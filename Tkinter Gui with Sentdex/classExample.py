class Listnode:
	def __init__(self, x):
		self.val = x
		self.next = None
# without parenthesis:###### a指向了Listnode类

a = Listnode
print(a)

a.val = 1
print(a.val)

Listnode.val = 2
print(a.val)

b = Listnode
b.val = 3
print(a.val)

# with parenthesis:######

c = Listnode(4)  # c为ListNode类的一个实例化对象，而非一个类，修改c.val不能修改其余的
print(c)
print(Listnode.val)
print(c.val)

c.val = 5
print(c.val)
print(Listnode.val)



#https://blog.csdn.net/lrs1353281004/article/details/81612390