class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.get_dict={}
        for start,end in edges:
            if start not in self.get_dict:
                self.get_dict[start]=[end]
            else:
                self.get_dict[start].append(end)
        print(self.get_dict)

    def get_paths(self,start,end,path=[]):
        path+=[start]
        if(start==end):
            return path
        if(start not in self.get_dict):
            return []
        paths=[]
        for i in self.get_dict[start]:
            if i not in path:
                new_path=self.get_paths(i,end,path)
                for p in new_path:
                    paths.append(p)
        return paths
    
    def get_shortest_path(self,start,end):
        path=[]
        path+=[start]
        if(start==end):
            return path
        if(start not in self.get_dict):
            return []
        shortest_path=None
        for i in self.get_dict[start]:
            sp = self.get_shortest_path(i, end, path)
            if sp:
                if shortest_path is None or len(sp) < len(shortest_path):
                    shortest_path = sp
        return shortest_path



if __name__=='__main__':
    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]
    route_graph=Graph(routes)
    start = "Mumbai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))