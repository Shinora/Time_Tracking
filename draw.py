import matplotlib
import pandas
import os

def table():
    for file in os.listdir("data/time"):
        with open("data/time/"+file, mode="r") as drawfile:
            df = pandas.read_csv(drawfile)
            print(df)
    
    for file in os.listdir("data/questions"):
        with open("data/questions/"+file, mode="r") as drawfile:
            df = pandas.read_csv(drawfile)
            print(df)


if __name__ == "__main__":
    table()