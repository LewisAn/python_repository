from Die import Die
import pygal

die_one = Die()
die_two = Die(10)

results = []
for roll_num in range(50000):
    result = die_one.roll() + die_two.roll()
    results.append(result)

#print(results)

frequencies = []
for value in range(2, 17):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()
hist.title = "Results of rolling 6-side die and 10-side die"

hist.x_labels = ['2','3','4','5','6''7','8','9','10','11','12','13','14','15','16']
hist.y_labels = "Frequency of Results"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visible_2.svg')


