class HashTable:
    def __init__(self):
        self.MAX=100
        self.lis=[[] for i in range(self.MAX)]


    def get_key(self,key):
        h=0
        for i in key:
            h+=ord(i)
        h=h%self.MAX
        return h


    def create_hash(self,key,value):
        hash=self.get_key(key)
        found=False
        for idx,element in enumerate(self.lis[hash]):
            if(len(element)==2 and element[0]==key):
                self.lis[hash][idx]=(key,value)
                found=True
                break
        if not found:
            self.lis[hash].append((key,value))

    def delete(self,key):
        hash=self.get_key(key)
        for idx,element in enumerate(self.lis[hash]):
            if(len(element)==2 and element[0]==key):
                del self.lis[hash][idx]
            else:
                print("Not Found")
            
    def get_val(self,key):
        hash=self.get_key(key)
        for idx,element in enumerate(self.lis[hash]):
            if(len(element)==2 and element[0]==key):
                return element[1]
            else:
                return "Not Found"
    

letter=[["march 22",66],["march 22",56],["march 28",156],["march 23",89],["jun 23",90]]
t=HashTable()
for i in letter:
    t.create_hash(i[0],i[1])
    
q=t.get_val("march 22")
print(q)





