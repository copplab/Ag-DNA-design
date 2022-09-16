import csv
import pandas as pd
import numpy as np
from statistics import mean, stdev
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, cross_val_score,StratifiedKFold
from dna_featuregenerator_all import create_feature_vectors
from balanced_class import balanced_subsample
from sklearn.metrics import f1_score,confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from modAL.models import ActiveLearner
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from dtreeviz.trees import *
from sklearn.calibration import CalibratedClassifierCV
import matplotlib.pyplot as plt

sequences = ['dark_green.txt','dark_red.txt','dark_vred.txt','dark_nir.txt','green_red.txt','green_vred.txt','green_nir.txt','red_vred.txt','red_nir.txt','vred_nir.txt']
for i in sequences:
    accuracy=[]
    for j in range(100):
        features=create_feature_vectors(i,i)
        X = features.drop('color', axis=1)
        y = features['color']
        xs,ys=balanced_subsample(X,y)
        svm = LinearSVC(penalty='l1', loss='squared_hinge', dual=False,random_state=0, tol=1e-5,max_iter=1000000, C=.1)
        clf = CalibratedClassifierCV(svm)
        clf.fit(xs, ys)
        scores = cross_val_score(clf, xs, ys, cv=10)
        b=(sum(scores)/len(scores))
        accuracy.append(b)
    acc_mean=mean(accuracy)
    acc_stdev=stdev(accuracy)
    print(i)
    print(acc_mean,acc_stdev)
