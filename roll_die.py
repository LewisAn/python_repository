from Die import Die
import pygal

die_one = Die() # 骰子1
die_two = Die(12) # 骰子2

results = []
for roll_num in range(5000):
    result = die_one.roll() + die_two.roll()
    results.append(result)

frequencies = [] # 最后需要被可视化的数据
for value in range(2, 19):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()
hist.title = "Results of rolling 6-side die"

hist.x_labels = []
for i in range(2, 19):
    hist.x_labels.append(str(i))
    
hist.y_labels = "结果"

hist.add('6-side dice and 10-side dice', frequencies)
hist.render_to_file('die_visible_4.svg')


