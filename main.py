from extractor import fetch_data
from transformer import transform_data
from loader import load_data

if __name__ == '__main__':

    # Extract
    fetch_data()

    #Transform
    finaldf = transform_data()

    #Load
    load_data(finaldf)