vertices_num = 7 
edges_num = 6

graph = [[0] * (vertices_num+1) for _ in range(vertices_num+1)]

visited = [False for _ in range(vertices_num + 1)] 

def dfs(vertex):
	for curr_v in range(1, vertices_num+1):
		if graph[vertex][curr_v] and not visited[curr_v]:
			print(curr_v)
			visited[curr_v] = True
			dfs(curr_v)

start_p = [1,1,1,2,4,6]
end_p = [2,3,4,5,6,7]

for start, end in zip(start_p, end_p):
	graph[start][end] = 1
	graph[end][start] = 1
   
root_vertex = 1
print(root_vertex)
visited[root_vertex] = True
dfs(root_vertex)