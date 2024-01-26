from plotly.graph_objects import Bar, Layout
from plotly import offline

import plotly.express as px
from die import Die


die_1 = Die()
die_2 = Die()

#make rolls , store result
results = []

for roll_num in range(10_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)



#analyse results

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
x_values = list(range(2,max_result+1))

for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

fig = px.bar(x=x_values, y=frequencies,title="Roles")
fig.update_layout(
    title="Plot Title",
    xaxis_title="Results",
    yaxis_title="Frequency",
    legend_title="Legend Title",
    
    )
fig.show()