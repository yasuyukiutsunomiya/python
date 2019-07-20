import numpy as np
import matplotlib.pyplot as plt

def osaka_oppai(x):
    e = np.e
    y_1 = ((np.sqrt((np.absolute(1 - x) + 1 - x) / 2) + (1 / 4)) * np.exp(-(1 - x) ** 2))
    y_2_1 = (1 / 40)
    y_2_2 = (np.absolute(1 - 2 ** 4 * (5 * x - 3) ** 4))
    y_2_3 = (np.absolute(1 - 2 ** 9 * (5 * x - 3) ** 4))
    y_2_4 = (2 - 528 * (5 * x - 3) ** 4)
    y_2 = (y_2_1 * (y_2_2 + y_2_3 + y_2_4))
    y = y_1 + y_2

    return y

def plot_oppai(x, y):
    plt.title('oppai_function')
    plt.axes().set_aspect('equal', 'datalim')
    plt.plot(x, y, 'black')
    plt.show()

def main():
    x = np.arange(-2, 3 + 0.01, 0.01)
    y = osaka_oppai(x)
    plot_oppai(x, y)

if __name__ == '__main__':
    main()



import numpy as np
import matplotlib.pyplot as plt

def oppai_function(x):
    l1 = np.sqrt( ( np.absolute( 1 – x ) + 1 – x ) / 2 ) + ( 1 / 4 )
    l = l1 * np.exp( – (1 – x ) ** 2)
    z1 = np.absolute( 1 – 2 ** 4 * ( 5 * x – 3) ** 4 )
    z2 = np.absolute( 1 – 2 ** 9 * ( 5 * x – 3) ** 4)
    z3 = 2 – 528 * (5 * x -3)**4
    r = 1/40 * ( z1 + z2 + z3 )
    y = l + r
    return y

x = np.arange(-1.5,2,0.01)
y = oppai_function(x)
plt.xlim(-1,2)
plt.ylim(-0.1,1.5)
plt.grid()
plt.plot(x,y)
plt.show()




    
