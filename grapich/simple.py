from bokeh.plotting import figure,output_file, show
import numpy as np


def f(x):
    return np.sin(x)




if __name__ == "__main__":
    output_file('simple_graphic.html')
    fig = figure()

    total_vars = int(input("How many values you want to graphic:"))
    #x = list(range(total_vars))
    x = np.linspace(-4,4,total_vars)
    y = f(x)

    

    
    fig.line(x,y, line_width=2)

    show(fig)

