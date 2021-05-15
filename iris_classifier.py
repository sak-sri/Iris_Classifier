import numpy as np
import pandas as pd 
import random as rand
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
iris_df=pd.read_csv("F:\\myproject\\flaskr\\iris_ds.csv")
iris_df.columns=["sepal length","sepal width","petal length","petal width","class"]
dic={"Iris-setosa":1,"Iris-versicolor":2,"Iris-virginica":3}
iris_df["class"]=iris_df["class"].apply(lambda x:dic[x])
iris_df=iris_df.sample(len(iris_df))
iris_df=iris_df.reset_index(drop=True)
y=pd.DataFrame(iris_df["class"])
x=iris_df.drop("class",1)
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.40,random_state=4)
cv_x,test_x,cv_y,test_y=train_test_split(test_x,test_y,test_size=0.50,random_state=4)
c=[0.01,0.03,0.1,0.3,1,3,5,7]
scr=[]
mn=-100
for i in c:
    clf=LogisticRegression(C=i,solver="lbfgs",multi_class="multinomial",max_iter=300)
    clf.fit(train_x,train_y.to_numpy().ravel())
    sc=clf.score(cv_x,cv_y.to_numpy().ravel())
    scr.append(sc)
    if(mn<sc):
        mn=sc
        fin_clf=clf
        fin_c=i
print(fin_clf.score(test_x,test_y.to_numpy().ravel()))
Pkl_FileName="F:\\myproject\\flaskr\\model.pkl" 
with open(Pkl_FileName,'wb') as file:
    pickle.dump(fin_clf,file)   