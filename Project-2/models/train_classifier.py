import sys
import numpy as np
import pandas as pd
import sqlite3
import sqlalchemy
from sqlalchemy import create_engine
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import make_multilabel_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.base import BaseEstimator, TransformerMixin
import pickle

nltk.download(['punkt', 'wordnet','averaged_perceptron_tagger'])

class StartingVerbExtractor(BaseEstimator, TransformerMixin):

    def starting_verb(self, text):
        sentence_list = nltk.sent_tokenize(text)
        for sentence in sentence_list:
            pos_tags = nltk.pos_tag(tokenize(sentence))
            first_word, first_tag = pos_tags[0]
            if first_tag in ['VB', 'VBP'] or first_word == 'RT':
                return True
        return False

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_tagged = pd.Series(X).apply(self.starting_verb)
        return pd.DataFrame(X_tagged)

def load_data(database_filepath):
    '''
    Loads the data from the SQLite database saved from process_data.py and returns messages (X) and categorical logical matrix (Y)
    
    INPUTS:
        database_filepath ---> database to load
        
    OUTPUTS:
        X ---> Pandas series of messages
        Y ---> Pandas datagrame of logical categories
    '''
    engine = create_engine(f'sqlite:///{database_filepath}')
    df = pd.read_sql_table("categorized_messages", con=engine)
    X = df['message'] #message
    Y = df.iloc[:,4:] #numeric categories
    category_names = Y.columns
    return X,Y,category_names

def tokenize(text):
    '''
    Clean and tokenize function referenced from section 4.3 of this course
    
    INPUTS:
        text ---> text to tokenize
        
    OUTPUTS:
        clean_tokens ---> clean tokens
    '''
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    
    clean_tokens=[]
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)
        
    return clean_tokens

def build_model():
    '''
    Builds parallel/serial model pipeline and executes a grid search over number of estimators
    '''
    pipeline = Pipeline([
        ('features', FeatureUnion([

            ('text_pipeline', Pipeline([
                ('vect', CountVectorizer(tokenizer=tokenize)),
                ('tfidf', TfidfTransformer())
            ])),

            ('starting_verb', StartingVerbExtractor())
        ])),

        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])
    parameters = {
        'clf__estimator__n_estimators' : [10,20]
    }
    cv = GridSearchCV(pipeline,param_grid=parameters)
    return cv

def evaluate_model(model, X_test, y_test, category_names):
    '''
    Prints precision, recall, f1-score and support for all categories
    '''
    y_pred = model.predict(X_test)
    y_pred_df = pd.DataFrame(y_pred)
    for i in np.arange(1,len(y_test.columns)):
        print(category_names[i],'\n',classification_report(y_test.iloc[:,i],y_pred_df.iloc[:,i]),'\n')

def save_model(model, model_filepath):
    '''
    Saves the model into a serialized pickle file
    '''
    pickle.dump(model, open(model_filepath, 'wb'))

def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
