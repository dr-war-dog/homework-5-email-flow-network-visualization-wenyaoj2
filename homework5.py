import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import datetime
new_item = []
class network_visualization:
    global new_item
    def __init__(self,file):
        self.df = pd.DataFrame.from_csv(file)
    def get_df(self):
        return self.df

    def choose_time(self,df,start_year,start_month,start_day,end_year,end_month,end_day):
        global new_item
        start=datetime.date(start_year,start_month,start_day)
        end=datetime.date(end_year,end_month,end_day)
        for index,row in df.iterrows():
            date = datetime.datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.000Z').date()
            if date>=start and date<=end:
                new_item.append(row)
        new_item = pd.DataFrame(new_item)
    def directed_graph(self,title):
        G = nx.from_pandas_edgelist(new_item,source="sender",target="receiver",create_using=nx.DiGraph())
        plt.title(title)
        nx.draw(G,with_labels=True)
        plt.show()
    def graph(self,title):
        G = nx.from_pandas_edgelist(new_item,"sender","receiver")
        plt.title(title)
        nx.draw(G,with_labels=True)
        plt.show()
    def find_id(self,df,start_id,end_id):
        global new_item
        for index,row in df.iterrows():
            if start_id<=index and end_id>=index:

                new_item.append(row)

        new_item = pd.DataFrame(new_item)

def main():
    df = network_visualization("D:/pycharm/IS590/DATAset/enricos-email-flows/personal.csv")
    data = df.get_df()
    df.choose_time(data,2006,2,22,2006,3,21)
    df.directed_graph("directed graph of email 2006.2.22-2006.3.21")
    # df.find_id(data,10,20)
    # df.graph("simple graph of email id 10- id 20")
main()
