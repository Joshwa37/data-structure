n=8
graphs=[[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]
dict={}
for i,j in graphs:
    if i in dict:
        dict[i].append(j)
    else:
        dict[i]=[j]
print(dict)
seen=set()
source=0
seen.add(source)
stack=[0]
while(stack):
    node=stack.pop()
    print(node)
    for i in dict.get(node,[]):
        if(i not in seen):
            seen.add(i)
            stack.append(i)

print(seen)