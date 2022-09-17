import csv
import numpy as np
from sklearn.svm import LinearSVC
from dna_featuregenerator import create_feature_vectors
from balanced_class import balanced_subsample
from sklearn.metrics import f1_score,confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.calibration import CalibratedClassifierCV
from itertools import product

test_sequences = ["file_name"]
sequences = ['dark_green.txt',
             'dark_red.txt',
             'dark_vred.txt',
             'dark_nir.txt',
             'green_red.txt',
             'green_vred.txt',
             'green_nir.txt',
             'red_vred.txt',
             'red_nir.txt',
             'vred_nir.txt']

classifiers=[]
df = pd.DataFrame()
for i in sequences:
    features=create_feature_vectors(i)
    for j in range(10):
        x1 = []
        y1 = []
        X = features.drop('color', axis=1)
        y = features['color']
        xs,ys=balanced_subsample(X,y)
        svm = LinearSVC(penalty='l1', loss='squared_hinge', dual=False,random_state=0, tol=1e-5,max_iter=1000000, C=.1)
        svm.fit(xs,ys)
        clf = CalibratedClassifierCV(svm)
        clf.fit(xs,ys)
        classifiers.append(clf)
print("done")

k=0
for i in sequences:
    x2 = []
    y2 = []
    x3 = []
    y3 = []
    seq=create_feature_vectors(test_sequences)
    seq = seq.drop('color', axis=1)

    for j in range(10):
        x1 = []
        y1 = []
        b=classifiers[k]
        a= b.predict_proba(seq)
        k+=1
        if (j==0):
            for l, m in a:
                x2.append(l)
                y2.append(m)
        else:
            for l, m in a:
                x1.append(l)
                y1.append(m)
            x2=np.add(x1,x2)
            y2=np.add(y1,y2)
    x2=(x2/10)
    y2=(y2/10)
    df[i] = x2.tolist()
    df[i+"2"] = y2.tolist()
df.to_csv(out, mode='a', header=False)
