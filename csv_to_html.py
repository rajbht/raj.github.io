# Python program to convert 
# CSV to HTML Table
import pandas as pd

def csv_html(filename):
    # to read csv file named "samplee"
    a = pd.read_csv(filename)
    a.to_html(filename.replace("csv","htm"))
    html_file = a.to_html()

if __name__ == "__main__":    
    print("Building NY school rankings page ...")
    csv_html("NY_school_rankings.csv")
    print("done.")
    print("Building NJ school rankings page ...")
    csv_html("NJ_school_rankings.csv")
    print("done.")
    