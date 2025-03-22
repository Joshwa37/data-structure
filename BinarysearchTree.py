class Binary:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def add_child(self,data):
        if(self.data==data):
            return
        if(data<self.data):
            if self.left:
                self.left.add_child(data)
            else:
                self.left=Binary(data)
        
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=Binary(data)

    def in_order_trav(self):
        element=[]
        if(self.left):
            element+=self.left.in_order_trav()

        element.append(self.data)

        if(self.right):
            element+=self.right.in_order_trav()

        return element
    
    def pre_order_traversal(self):
        element=[]

        element.append(self.data)

        if(self.left):
            element+=self.left.pre_order_traversal()

        if(self.right):
            element+=self.right.pre_order_traversal()

        return element

    def post_order_traversal(self):
        element=[]

        if(self.left):
            element+=self.left.post_order_traversal()

        if(self.right):
            element+=self.right.post_order_traversal()

        element.append(self.data)

        return element
    
    def find_max(self):
        if(self.right):
            return self.right.find_max()
        else:
            return self.data
    
    def find_min(self):
        if(self.left):
            return self.left.find_min()
        else:
            return self.data
    
    def decending(self):

        element=[]

        if(self.right):
            element+=self.right.decending()

        if(self.left):
            element+=self.left.decending()

        element.append(self.data)

        return element
    
    def delete(self,val):
        if(val<self.data):
            if(self.left):
                self.left.delete(val)
        elif(val>self.data):
            if(self.right):
                self.right.delete(val)
                
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val=self.left.find_min()
            self.data=min_val
            self.right=self.right.delete(min_val)
        
        return self
            

    
def build_tree(element):
    root=Binary(element[0])

    for i in range(1,len(element)):
        root.add_child(element[i])

    return root

if __name__=="__main__":
    number=build_tree([15,12,7,14,27,20,23,88])

    print(number.in_order_trav())
    print(number.post_order_traversal())
    print(number.pre_order_traversal())
    print(number.find_max())
    print(number.find_min())
    number.delete(15)
    print(number.in_order_trav())




    


        
        
        


        


        