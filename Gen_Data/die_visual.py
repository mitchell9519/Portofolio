from plotly.graph_objects import Bar , Layout
from plotly import offline
from die import Die


#create 2 d6
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
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualise results
x_values = list(range(2,max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title' : 'Result'}
y_axis_config = {'title' : 'Frequency of result'}

my_layout = Layout(title='Result of rolling d10 & d6 1000 times ', 
        xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data' : data, 'layout': my_layout}, filename= 'd6_d6.html')



