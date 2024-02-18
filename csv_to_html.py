# Python program to convert 
# CSV to HTML Table
import pandas as pd

def csv_html(filename):
    # to read csv file named "samplee"
    a = pd.read_csv(filename)
    
    # to save as html file
    # named as "Table"
    a.to_html(filename.replace("csv","htm"))
    
    # assign it to a 
    # variable (string)
    html_file = a.to_html()


if __name__ == "__main__":
    csv_html("NY_school_rankings.csv")
    csv_html("NJ_school_rankings.csv")
    