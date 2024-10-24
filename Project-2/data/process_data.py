import sys
import pandas as pd
import sqlite3
import sqlalchemy
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    '''
    Load and combine the two input dataframes
    INPUTS:
        messages_filepath ---> a .csv file formatted as the messages data set
        categories_filepath ---> a .csv file formatted as the categories data set
        
    OUTPUTS:
        df ---> a combined Pandas dataframe
    '''
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, how ='outer', on =['id'])
    return df


def clean_data(df):
    '''
    Splits the categories into separate logical category columns and removes duplicate records
    
    INPUTS:
        df ---> merged Pandas dataframe
        
    OUTPUTS:
        df ---> cleaned Pandas dataframe
    '''
    categories = df['categories'].str.split(';', expand=True)
    row = categories.iloc[0,:]
    category_colnames = list(row.str.slice(0,-2))
    categories.columns = category_colnames
    for column in categories:
        categories[column] = categories[column].str.slice(-1,)
        categories[column] = categories[column].astype(int)
    categories.drop(categories[categories.related > 1]].index, inplace=True)
    df.drop('categories',axis=1,inplace=True)
    df = pd.concat([df,categories],axis=1)
    df.drop_duplicates(inplace=True)
    return df


def save_data(df, database_filename):
    '''
    Saves the clean dataset into an sqlite database
    
    INPUTS:
        df ---> merged Pandas dataframe
        database_filename ---> save path for database
        
    OUTPUTS:
    '''
    engine = create_engine(f'sqlite:///{database_filename}')
    df.to_sql('categorized_messages', engine, index=False,if_exists='replace')  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
