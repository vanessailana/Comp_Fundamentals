import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler 
import matplotlib.pyplot as  plt
from sklearn.decomposition import PCA 
import seaborn as sns 
from sklearn.datasets import load_breast_cancer 
#orthoganl transformated of correlation to uncorrelated
#unsupervised learned interrelations
#examine interrelations

cancer = load_breast_cancer() 

df = pd.DataFrame(cancer['data'], columns = cancer['feature_names'])


print(df)


scalar=StandardScaler();
scalar.fit(df)

scaled_data=scalar.transform(df)

pca=PCA(n_components=2)
pca.fit(scaled_data)
x_pca=pca.transform(scaled_data)

plt.scatter(x_pca[:,0], x_pca[:, 1], c = cancer['target'], cmap ='plasma')
plt.xlabel("First Principal Component")

plt.ylabel("Second Principal Component")

plt.show();


#unsupervised learning technicque to learn interrealtions among variables

PCA.components;

#interrelations among a heat map

df_comp = pd.DataFrame(pca.components_, columns = cancer['feature_names']) 

plt.figre(figsize=(14,6))

sns.heatmap(df_comp)

sns.show();