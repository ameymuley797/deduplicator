import pandas as pd
import numpy as np
import extdata
from fuzzywuzzy import fuzz
from itertools import product
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.metrics import accuracy_score

class deduplication:
     def __init__(self):
         self.le = LabelEncoder()

     def label_encoding(self, X, columns_to_be_encoded):
         for i in columns_to_be_encoded:
            X[i] = self.le.fit_transform(X[i])
         return X

     def processing(self, df):
         """
         extracts relevant features and processes the data and
         thus, returns the input and output dataframes
         :param df: training and testing datasets
         :return: input and output dataframes
         """
         df['id'] = df.index
         full_name_df = pd.DataFrame(list(product(df.id.tolist(), df.id.tolist())), columns=['id', "id_"])
         full_name_df['combined_labels'] = full_name_df[['id', 'id_']].values.tolist()
         full_name_df['combined_labels'] = full_name_df['combined_labels'].apply(lambda x: sorted(x))
         full_name_df['combined_labels'] = full_name_df['combined_labels'].astype(str)
         full_name_df = full_name_df.drop_duplicates(subset=['combined_labels'])
         full_name_df.drop(columns=['combined_labels'], inplace=True)
         full_name_df = full_name_df[full_name_df['id'] != full_name_df['id_']]
         df1 = pd.merge(full_name_df, df, how='left', on='id')
         dict = {'id': 'id_', 'ln': 'ln_', 'dob': 'dob_', 'gn': 'gn_', 'fn': 'fn_', 'label': 'label_'}
         df2 = pd.merge(full_name_df, df.rename(columns=dict), how='left', on='id_')
         overall_df = pd.concat([df1, df2], axis=1)
         overall_df = overall_df.loc[:, ~overall_df.columns.duplicated()]
         overall_df['fn_sr'] = overall_df.apply(lambda x: fuzz.ratio(x['fn'], x["fn_"]) / 100, axis=1)
         overall_df['ln_sr'] = overall_df.apply(lambda x: fuzz.ratio(x['ln'], x["ln_"]) / 100, axis=1)
         overall_df['dob_flag'] = (np.where(overall_df['dob'] == overall_df['dob_'], 1, 0))
         overall_df['gn_flag'] = (np.where(overall_df['gn'] == overall_df['gn_'], 1, 0))
         overall_df['target'] = (np.where(overall_df['label'] == overall_df['label_'], 1, 0))
         X = overall_df.drop(
             columns=['ln', 'ln_', 'fn', 'fn_', 'dob', 'dob_', 'gn', 'gn_', 'label',
                      'label_', 'target'])
         y = overall_df['target']
         return X, y

     def main(self):
         train = pd.read_csv(extdata.training)
         test = pd.read_csv(extdata.test)

         X_train, y_train = self.processing(train)
         X_test, y_test = self.processing(test)

         clf = tree.DecisionTreeClassifier()
         model = clf.fit(X_train, y_train)

         print('Model accuracy: ', accuracy_score(y_test, model.predict(X_test)))

         X_test['y_predict'] = model.predict(X_test)
         X_test['y_actual'] = list(y_test)

         test['id'] = test.index
         output = pd.merge(test, X_test['id'].drop_duplicates(), how='inner', on='id')
         output.drop(columns=['id'], inplace=True)
         output.to_csv('output.csv')
         return X_test








