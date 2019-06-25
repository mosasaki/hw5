def create_graph(network):
    """Create a graph of train lines

    Args:
        network(list): A list of dictionary 
    Returns:
        graph(dictionary): A graph of train stations

    """

    graph = {}
    '''
    for name in network:
        for station in Stations:
            print(station)
            graph[station] = []
            
    for name in network:
        end = len(Stations)
        for station in Stations:
            if station != Stations[0]
            graph[station].append(station - 1)
            if station != Stations[end - 1]
            graph[statiom].append(station - 1)
            
    '''
    line = 0
    i = 0
    while line < len(network):
        while i <len(network[line]['Stations']):
            graph[network[line]['Stations'][i]] = []
            i += 1
        i = 0
        line += 1

    line = 0
    i = 0
    while line < len(network):
        while i <len(network[line]['Stations']):
            if i != 0:
                graph[network[line]['Stations'][i]].append(network[line]['Stations'][i - 1])
            if i != len(network[line]['Stations']) - 1:
                graph[network[line]['Stations'][i]].append(network[line]['Stations'][i + 1])
            
            i += 1
        i = 0
        line += 1  

    return graph

def search_shortest_paths_bfs(graph, start, end):
    """search path between starting station to goal station

    Args:
        graph(dictionary): graph of train stations
        start(string): the name of the starting station
        end(string): the name of the gaol station

    Return:
        answer(list): a path between the starting station to gaol station
        
    """

    searched_list = []
    data = {start: []}
    queue = [start]

    while queue:
        current = queue.pop(0)
        if current == end:
            return data[current]
        if current not in searched_list:
            searched_list.append(current)
            queue += graph[current]
            for station in graph[current]:
                if station not in data.keys():
                    data[station] = data[current] + [current]
