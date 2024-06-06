import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import seaborn as sns

def regression_plot(filename, xlabel, ylabel):
    df = pd.read_csv(filename)
    sns.set(rc={'figure.figsize': (12,6)})
    sns.regplot(x=df[xlabel], y=df[ylabel])
    plt.show()

if __name__ == '__main__':
    regression_plot('data/tempRainYearly.csv', 'Temp', 'Main')
