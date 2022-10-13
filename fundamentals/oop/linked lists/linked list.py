class SLNode:
    def __init__(self,value):
        self.value=value
        self.head=None
class SList:
    def __init__(self):
        self.head=None
    def add_to_front(self,val):
        new_node=SLNode(val)
        current_head=self.head
        new_node.next=current_head
        self.head=new_node
        return self
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next 	# set the runner to its neighbor
        return self	# once the loop is done, return self to allow for chaining
	

list1=SList()
list1.add_to_front(1)
list1.add_to_front(2)
list1.add_to_front(3)
list1.add_to_front(4)
list1.add_to_front(9)
list1.add_to_front(6)
list1.print_values()
