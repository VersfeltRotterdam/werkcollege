import osmnx as ox
import numpy as np
import pandas as pd
import folium
import folium.plugins as plugins

from utils.downloader import _get_graph_from_dbfs, _get_paths_from_dbfs

def _plot_all_locations(color = "red", size = 5):
    G = _get_graph_from_dbfs()
    gdf_nodes = ox.graph_to_gdfs(G)[0]
    mask = pd.isnull(gdf_nodes["amenity"])
    location_nodes = gdf_nodes.loc[~mask]
    return _plot_nodes_folium(G, gdf_nodes = location_nodes, graph_map = None, tiles="cartodbpositron", zoom=1, fit_bounds=True, node_color = color, node_size = size)

def _plot_route(solution):
    G = _get_graph_from_dbfs()
    paths = _get_paths_from_dbfs()
        
    route = []
    route += paths[0, solution[0]][:-1].tolist()
    for i in range(1, len(solution)):
        route += paths[solution[i-1], solution[i]][:-1].tolist()
    route += paths[solution[len(solution)-1], 0].tolist()
    
    route_map = ox.plot_route_folium(G, route, route_color='#3484F0', opacity=1)
    return _plot_route_markers_folium(G, route_map, solution)
    
def _plot_route_markers_folium(G, route_map, solution):
    required_nodes = [44409833] + [node for (node, data) in G.nodes(data = True) if 'amenity' in data and data['amenity'] == data['amenity']]
    gdf_nodes = ox.graph_to_gdfs(G)[0]
    nodes = gdf_nodes.loc[np.isin(gdf_nodes.index, required_nodes)]
    # set name of timmerhuis
    nodes.loc[44409833, 'name'] = "Timmerhuis"
    nodes.loc[44409833, 'amenity'] = "None"

    indices = list(pd.read_parquet("/dbfs/FileStore/demo_optimalisatie/Rotterdam_pois_distances.parquet").index)
    sequence = [(indices[solution[i]], i+1) for i in range(len(solution))]
    
    for key,value in sequence:
        nodes.loc[key, "sequence"] = int(value)
    nodes.loc[44409833, 'sequence'] = 0
    
    for i in range(0,len(nodes)):
        folium.Marker(
            location=[nodes.iloc[i]['y'], nodes.iloc[i]['x']], popup=None,
            icon=plugins.BeautifyIcon(
                             icon="arrow-down", icon_shape="marker",
                             number=nodes.iloc[i]['sequence'],
                             border_color= "#757575",
                             background_color="#FFFFFF"
                         )
        ).add_to(route_map)

    return route_map
    
def _plot_nodes_folium(G, graph_map, gdf_nodes, tiles, zoom, fit_bounds, node_color='red', node_size = 5):      
    # get centroid
    x, y = gdf_nodes.unary_union.centroid.xy
    centroid = (y[0], x[0])

    if graph_map is None:
        graph_map = folium.Map(location=centroid, zoom_start=zoom, tiles=tiles)
        
    # if fit_bounds is True, fit the map to the bounds of the route by passing
    # list of lat-lng points as [southwest, northeast]
    if fit_bounds and isinstance(graph_map, folium.Map):
        tb = gdf_nodes.total_bounds
        graph_map.fit_bounds([(tb[1], tb[0]), (tb[3], tb[2])])
    

    gdf_nodes['nc'] = node_color

    nodes_group = folium.map.FeatureGroup()

    # add nodes to the container individually
    for y, x, nc, amenity, name in zip(gdf_nodes['y'], gdf_nodes['x'], gdf_nodes['nc'], gdf_nodes['amenity'], gdf_nodes['name']):
        nodes_group.add_child(
            folium.vector_layers.CircleMarker(
            [y, x],
            radius= node_size,
            color=None,
            fill=True,
            fill_color=nc,
            fill_opacity=1,
            tooltip = f"{name}: {amenity}"
            )
        )
    graph_map.add_child(nodes_group)

    return graph_map