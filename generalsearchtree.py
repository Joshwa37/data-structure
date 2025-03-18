class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_children(self,child):
        child.parent=self
        self.children.append(child)
    
    def level(self):
        count=0
        p=self.parent
        while(p):
            count+=1
            p=p.parent
        return  count
    
    def print(self):
        space=' ' * self.level()*3
        extra=space+"|__" if self.parent else ""
        print(extra+self.data)
        if(self.children):
            for child in self.children:
                child.print()
    
def build_product():
    root=TreeNode("Electronics")
    laptop=TreeNode("Laptop")
    laptop.add_children(TreeNode("Asus"))
    laptop.add_children(TreeNode("lenova"))
    laptop.add_children(TreeNode("acer"))

    root.add_children(laptop)
    root.print()

build_product()