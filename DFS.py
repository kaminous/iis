ip = input("i/p - ")

graph = eval(ip)

stack = [0]       
vis = {0}    
res = []  

while stack:
    curr_ver = stack.pop()  
    res.append(curr_ver)

    for neighbor in graph[curr_ver]:
        if neighbor not in vis:
            vis.add(neighbor)
            stack.append(neighbor) 

print("o/p -", res)