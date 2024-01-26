#Json files - like dict in studio
from plotly.graph_objs import Scattergeo , Layout
from plotly import offline
import json
import plotly.express as px

filename = 'Data\eq_data_1_day_m1.json'
with open(filename) as object_file:
    all_eq_data = json.load(object_file)


#done with auto sort also
# sort_json():
    # readable_file = 'data/readable_eq_file.json'
    # with open(readable_file)as f:
    #     json.dump(all_ed_data,f, indent=4)

## - gets num dicts
all_eq_dicts = all_eq_data['features']  
#print(len(all_eq_dicts))

mags,lons,lats,hover_texts =[],[],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

data = [{
    'type':'scattergeo',
        'lon':lons,
        'lat':lats,
        'text': hover_texts,
        'marker':{
            'size' : [5*mag for mag in mags],'color':mags,
                'colorscale' :'viridis',
                'reversescale' : True,
                'colorbar': {'title': 'Magnitude'}
                    
        },
    }]

my_layout = Layout(title = 'My_earthquakes')
fig = {'data':data , 'layout':my_layout}
offline.plot(fig, filename='global_eqs3.html')


#data = [Scattergeo(lon=lons , lat=lats)]

# fig = px.scatter_geo(lon=lons,lat=lats,
                     
#                      color=mags,
#                      color_discrete_map={'title' :'magnitude'},
#                      size = [5*mag for mag in mags],
#                      opacity = 0.8,
                     
                    
# )
                                   
                                
                     
fig.px.show()