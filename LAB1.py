import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
    def push(self, node,cost):
        heapq.heappush(self.queue, (cost, node))
    def pop(self):
        return heapq.heappop(self.queue)[1]
    def is_empty(self):
        return len(self.queue) == 0

def createGraph_Heuristic(File):
    graph={}
    heuristic={}
    with open(File,"r") as f:
        for line in f:
            tokens =line.split()
            sourceCity =tokens[0]
            heuristicValue =int(tokens[1])
            heuristic[sourceCity] =heuristicValue
            destinationCities ={}
            for i in range(2, len(tokens), 2):
                destinationCity =tokens[i]
                distance =int(tokens[i+1])
                destinationCities[destinationCity] =distance
            graph[sourceCity] =destinationCities
    return graph, heuristic


def astar(graph, heuristic, start, end):
    pq =PriorityQueue()
    pq.push(start, 0)
    path ={start: None}
    dist ={start: 0}
    expanded =[]
    while not pq.is_empty():
        current =pq.pop()
        if current==end:
            break
        expanded.append(current)
        for neighbor,distance in graph[current].items():
            newCost =dist[current]+distance
            if neighbor not in dist or newCost < dist[neighbor]:
                dist[neighbor] =newCost
                priority =newCost+heuristic[neighbor]
                pq.push(neighbor, priority)
                path[neighbor] =current
    finalPath =[]
    node=end
    while node is not None:
        finalPath.append(node)
        node=path[node]
    finalPath.reverse()
    print(f"Path from {start} to {end}:\n{finalPath}")
    print(f'Total distance-{dist[end]}','km')
    print(f'Expanded nodes: {expanded}')

if __name__ == '__main__':
    graph,heuristic = createGraph_Heuristic('INPUT FILE.txt')
    astar(graph,heuristic, 'Arad', 'Bucharest')