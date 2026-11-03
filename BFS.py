ip = input("i/p - ")

graph = eval(ip)

qu = [0]       
vis = {0}    
res = []  

while qu:
    curr_ver = qu.pop(0)  
    res.append(curr_ver)

    for neighbor in graph[curr_ver]:
        if neighbor not in vis:
            vis.add(neighbor)
            qu.append(neighbor) 

print("o/p -", res)