import pygal   
import json    

with open('data.json', 'r') as f:
    data = { str(key) : [float(item) for item in value] for key, value in \
            json.load(f).items()}
bar_chart = pygal.Bar()      
bar_chart.title = "Marks evaluation"   
bar_chart.x_labels = map(str, range(1,2,3))     
bar_chart.add("CS", data["CS"])    
bar_chart.add("Maths", data["Maths"])      
bar_chart.add("Additional", data["Additional"])      
bar_chart.render_to_file("graph.svg")        


#reference taken from pygal's documentation.
