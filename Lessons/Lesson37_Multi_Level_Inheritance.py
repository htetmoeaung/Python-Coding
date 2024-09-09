# multi-level inheritance = when a derived (child) class inherits
#                           another derived (child) class

class GrandParents:
    alive = True

class Parents(GrandParents):
    def work(self):
        print('We work in supermarket')

class child(Parents):
    def study(self):
        print('Studying in Highschool')

child = child()
print(child.alive)
child.work()
child.study()