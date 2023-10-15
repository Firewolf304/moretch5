import osmnx
import shapely.geometry as geo
import astar
osmnx.config(use_cache=True, log_console=True)

def func(start: tuple, end : tuple):
    #start = 55.0600604, 82.9071446
    #end = 55.2600604, 82.9871446
    #point = geo.Point(start)
    getgraph = osmnx.graph_from_point(start, dist=1000, network_type='all')
    path = astar.alogs(graph=getgraph)
    path.aStar(start, end)
    #global getgraph
    #print(path)
    #mass = list( getgraph.edges )
    #sub = getgraph.edge_subgraph(mass[0:4])




    #shortest_route_map = osmnx.plot_graph(sub )
    #shortest_route_map
    #print(getgraph.edges)
    for i in getgraph.edges:
        print(f"{getgraph.nodes[i[0]]}, {getgraph.nodes[i[1]]}   - {i[2]} ")