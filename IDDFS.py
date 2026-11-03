def dls(graph, target, depth_limit):

    stack = [(0, 0)]      # (vertex, depth)
    vis = {0}
    res = []

    while stack:
        curr_ver, depth = stack.pop()
        res.append(curr_ver)

        if curr_ver == target:
            print("Element Found!")
            print("Traversal :", res)
            return True

        if depth < depth_limit:
            for neighbor in graph[curr_ver]:
                if neighbor not in vis:
                    vis.add(neighbor)
                    stack.append((neighbor, depth + 1))

    print("Traversal :", res)
    return False

# ---------------- Main Prog ------------------ #

ip = input("Enter Graph : ")
graph = eval(ip)

target = int(input("Enter Element to Search : "))
max_depth = int(input("Enter Maximum Depth : "))

found = False

for limit in range(max_depth + 1):

    print("\nDepth Limit =", limit)

    if dls(graph, target, limit):
        found = True
        break

if not found:
    print("\nElement Not Found within Maximum Depth.")

#{0:[1,2],1:[3],2:[4],3:[],4:[]}