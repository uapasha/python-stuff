class Parent (object):

	def implicit(self):
		print "PARENT implicit()"
	
	def override(self):
		print "PARENT override()"
		
	def altered(self):
		print "PARENT altered()"
	
class Child (Parent):
	
	def override(self):
		print "CHILD override()"
	
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFRER PARENT altered()"

dad = Parent()
son = Child()

#dad.implicit()
#son.implicit()

#dad.override()
#son.override()

#dad.altered()
#son.altered()


class Other(object):
	
	def override(self):
		print "OTHER override()"
	
	def implicit(self):
		print "OTHER implicit()"
	
	def altered(self):
		print "OTHER altered()"
		
class Some(object):

	def __init__(self):
		self.other = Other()
		
	def implicit(self):
		self.other.implicit()
	
	def override(self):
		print "SOME override()"
	
	def altered(self):
		print("SOME BEFORE altered()")
		self.other.altered()
		print("SOME AFTER altered()")

some = Some()

some.implicit()
some.override()
some.altered()	