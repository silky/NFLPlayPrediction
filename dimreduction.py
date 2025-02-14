#Load games
from __future__ import division
import numpy as np
from sklearn.decomposition import PCA

def pca(features,num_comp):
    pca = PCA(n_components = num_comp)
    pca.fit(features)
    red_features = pca.transform(features)
    print(pca.explained_variance_ratio_) 
    return (red_features,pca)