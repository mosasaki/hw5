def create_graph(network):
    """Create a graph of train lines

    Args:
        network(list): A list of dictionaries of lines and stations in the line
    Returns:
        graph(dictionary): A graph of train stations

    """

    graph = {}
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
        while i < len(network[line]['Stations']):
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
            data[current] += [end]
            return data[current]
        if current not in searched_list:
            searched_list.append(current)
            queue += graph[current]
            for station in graph[current]:
                if station not in data.keys():
                    data[station] = data[current] + [current]


def create_line_station_list(path_list, network):
    """Make a list of dictionary of station and the lines based on stations 
       included in path_list

    Args:
        path_list(list): A list of stations included in the shortest path
                         between the starting station and the goal station
        network(list): A list of dictionaries of lines and stations in lines

    Returns:
        path_with_lines(list): A list of dictionaries of stations and lines  
    """

    path_with_lines = []
    i = 0
   
    for station in path_list:
        st_dict = {'Station':station, 'Line':[]}
        path_with_lines.append(st_dict)
        
    while i < len(path_with_lines):
        j = 0
        while j < len(network):
            if path_with_lines[i]['Station'] in network[j]['Stations']:
                path_with_lines[i]['Line'].append(network[j]['Name'])
            j += 1
        i += 1

    return path_with_lines
        
               
def choose_line(path_with_lines):
    """ Choose one line for each stations in path_with_lines list

    Args:
        path_with_lines(list): A list of dictionaries of stations and lines 

    Returns:
        final_path(list): A list of dictionaries of station, line, and token
    """
    
    final_path = []
    i = 0
    end = len(path_with_lines) - 1
    token = 0
    while i < end:
        if len(path_with_lines[i]['Line']) == 1:
            path_with_lines[i]['token'] = token
            final_path.append(path_with_lines[i])
            i += 1
        else:
            
            for line in path_with_lines[i]['Line']:
                for next_line in path_with_lines[i + 1]['Line']:
                    if line == next_line:
                        new_dict = {'Station':path_with_lines[i]['Station'], 'Line':[line], 'token': token}
                        final_path.append(new_dict)
                        break
                break
            
            i += 1
            
    end_fin = len(final_path) 
    if len(path_with_lines[end]) == 1:
        final_path.append(path_with_lines[end])
    else:
        new_dict = {'Station': path_with_lines[end]['Station'], 'Line': final_path[end_fin - 1]['Line'], 'token': token}
        final_path.append(new_dict)
    i = 0
    while i < end_fin:
        if final_path[i]['Line'] != final_path[i + 1]['Line']:
            final_path[i]['token'] = 1
        i += 1
                  
    return final_path
    
