import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_auc_score,auc,roc_curve
import joblib
import warnings
warnings.filterwarnings('ignore')

# Importing the file
df=pd.read_csv('HR_Employee_Attrition_Data.csv')

df=df.drop(['EmployeeCount','Over18','StandardHours'],axis=1)

df=df.drop(['EmployeeNumber','HourlyRate','PercentSalaryHike','PerformanceRating'],axis=1)

cat_index=df.select_dtypes(include='object').columns

dummy=pd.get_dummies(df[cat_index])

dummy=dummy.drop(['Attrition_No','OverTime_No','Gender_Female'],axis=1)

df1=pd.concat([df,dummy],axis=1)

df1=df1.drop(['Attrition','BusinessTravel','Department','EducationField','Gender','JobRole',
             'MaritalStatus','OverTime'],axis=1)

X=df1.drop('Attrition_Yes',axis=1)
y=df1['Attrition_Yes']


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

rfc=RandomForestClassifier()

rfc.fit(X_train,y_train)

file='emp_att_rate.pkl'

joblib.dump(rfc,file)
