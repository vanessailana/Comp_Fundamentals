from sklearn import datasets 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 


iris=datasets.load_iris();

X=iris.data;
y=iris.target;

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)


dtree_model = DecisionTreeClassifier(max_depth = 2).fit(X_train, y_train) 
dtree_predictions = dtree_model.predict(X_test) 
 

cm=confusion_matrix(y_test,dtree_predictions)


print(cm)