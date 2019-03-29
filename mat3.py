import matplotlib.pyplot as p
from RandomWalk import RandomWalk
def draw_values():
    x_values = list(range(1, 1000)) # generator -> list
    y_values = [x ** 2 for x in x_values] # list comprehension

##    p.scatter(x_values,
##              y_values,
##              edgecolor='none',
####              c='red', 
##              s=10)
    p.scatter(x_values,
              y_values,
              edgecolor='none',
              c=y_values,
              cmap=p.cm.Blues,
              s=10)
    p.xlabel("Value x", fontsize=14)
    p.ylabel("Value y", fontsize=14)

    p.tick_params(axis='both',
                  which='major',
                  labelsize=14)
    p.axis([0, 1100, 0, 1100000])
##    p.show()
    p.savefig('squares_plot.png')

def draw_two():
    rw = RandomWalk()
    rw.fill_walk()
    p.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=p.cm.Reds, s=15)
    p.axes().get_xaxis().set_visible(False)
    p.axes().get_yaxis().set_visible(False)
    p.show()

def infinite_draw():
    while True:
        draw_two()
        answer = input("Do you want to show again?")
        if answer == '':
            break

infinite_draw() 
