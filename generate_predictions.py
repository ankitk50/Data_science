# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 13:09:25 2018

@author: opuser1
"""
import pickle
import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=1)

df=pd.read_excel('Complete_Das.xlsx','Combined')
df_test=df=pd.read_excel('corning.xlsx','test_set')#High:1, Medium+Low:0,NA:-1

loc='test6'
train_test_param=['NoFC','FR','RL','TtG']

def save_model(model_param):
    dump_file=open(loc+'/dump_model.obj','wb')
    X=df[model_param]
    Y=df['EoO'] #target parameter
    #model fitting, training
    
    clf=rf.fit(X, Y)
    train_accuracy=clf.score(X, Y)
    print "Train Accuracy:",train_accuracy
    pickle.dump(clf,dump_file)

def predictions(pred):
    submission=pd.DataFrame({
            "Patent Number":df['PatNo'],
            "Extent of Overlap":pred
            })
    submission.to_csv(loc+'/Classified_patents.csv',index=False)

def generate_predictions_from_saved_model():
    model=open(loc+'/dump_model.obj','rb')
    clf=pickle.load(model)
    X3_test = df_test[train_test_param]
    Y3_test = df_test['EoO']
    Y3test_pred = clf.predict(X3_test)
    predictions(Y3test_pred)
    print metrics.classification_report(Y3_test,Y3test_pred)


def one_model_one_prediction():
    X=df[train_test_param]
    Y=df['EoO'] #target parameter
    
    #model fitting, training
    
    clf=rf.fit(X, Y)
    train_accuracy=clf.score(X, Y)
    print "Train Accuracy:",train_accuracy
    #testing
        
    X3_test = df_test[train_test_param]
    Y3_test = df_test['EoO']
    Y3test_pred = rf.predict(X3_test)
    predictions(Y3test_pred)
    test_accuracy=rf.score(X3_test, Y3_test)
    print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(test_accuracy))
    print metrics.classification_report(Y3_test,Y3test_pred)
    
if __name__=="__main__":
    #save_model(train_test_param)
    generate_predictions_from_saved_model()