def bfs(graph,start_node):
   visited = []
   queue = [start_node]

   while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print(f"exploring node:{current_node}") 
            visited.append(current_node)
        for neighbor in graph.get(current_node,[]):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
            return visited

print("---Build Your Graph---")
student_graph = {}

num_edges =int (input("how many edges connection does graph have?"))
print("enter each edge serparated by a space(e.g,A,B):")
for i in range (num_edges):
    u,v = input(f"Edge {i+1}:").split()
    if u not in student_graph:
        student_graph[u] = []
    if v not in student_graph:
        student_graph[v] = []

    student_graph[u].append(v)
    student_graph[v].append(u)

start = input ("enter the starting node for bfs:")
print(f"\nYour graph dictionary:{student_graph}")
print("starting bfs tarversal")
bfs (student_graph,start)