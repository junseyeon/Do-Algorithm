""" start_p = [1,1,1,2,4,6]
end_p = [2,3,4,5,6,7]
graph = [[0] * (7+1) for _ in range(7+1)]

for start, end in zip(start_p, end_p):
	print(start, end)
	graph[start][end] = 1
	graph[end][start] = 1
print(graph) """

graph = [[] for _ in range(10)]
print(graph)