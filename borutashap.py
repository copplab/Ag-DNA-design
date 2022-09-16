import csv
import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, cross_val_score,StratifiedKFold
from dna_featuregenerator import create_feature_vectors, plot_coefficients
from balanced_class import balanced_subsample
from sklearn.metrics import f1_score,confusion_matrix, accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from BorutaShap import BorutaShap, load_data
a=[]
og_oob_scores = []
fil_oob_scores = []

sequences = ['dark_green.txt','dark_red.txt','dark_vred.txt','dark_nir.txt','green_red.txt','green_vred.txt','green_nir.txt','red_vred.txt','red_nir.txt','vred_nir.txt']
#create data structure for SVM
for i in sequences:
    for j in range(10):
        features=create_feature_vectors(i)
        X = features.drop('color', axis=1)
        y = features['color']
        #Balance class through subsampling
        xs,ys=balanced_subsample(X,y)
        #Split into training and test
        rf = RandomForestClassifier(n_estimators = 100, max_features=None, oob_score=True, class_weight = 'balanced_subsample', verbose = 1, random_state = (24))
        X_train, X_test, y_train, y_test = train_test_split(xs, ys, test_size = 0.10, random_state = 25+j)
        rf.fit(X_train,y_train)
        og_oob_scores.append(rf.oob_score_)
        y_rf = rf.predict(X_test)
        print(confusion_matrix(y_test, y_rf))
        print(accuracy_score(y_test, y_rf))
        fs = BorutaShap(model=rf, importance_measure='shap', classification=True)
        fs.fit(xs, ys, n_trials=100, sample=False, train_or_test = 'train', normalize=True, verbose = 1)
        subset = fs.Subset()
        rff = RandomForestClassifier(n_estimators = 100, max_features=None, oob_score=True, class_weight = 'balanced_subsample', verbose = 1, random_state = (24))
        X_trainf, X_testf, y_trainf, y_testf = train_test_split(subset, ys, test_size = 0.10, random_state = 25+j)
        rff.fit(X_trainf,y_trainf)
        fil_oob_scores.append(rff.oob_score_)
        y_rff = rff.predict(X_testf)
        print(confusion_matrix(y_testf, y_rff))
        print(accuracy_score(y_testf, y_rff))
        name = f"{i}_{j+1}"
        fs.results_to_csv(filename= name)
    print(og_oob_scores)
    print(fil_oob_scores)
    og_oob_scores = []
    fil_oob_scores = []
