from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd
model=pickle.load(open('static/new_classification_model.pkl','rb'))

def Transform_data(fr):
  df=pd.read_csv(r"static/ObesityDataSet_raw_and_data_sinthetic.csv")
  X=df.drop(['NObeyesdad'],axis=1)
  Y=df[['NObeyesdad']]
  numerical_cols=['Age', 'Height', 'Weight', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE']
  categorical_cols=['Gender', 'family_history_with_overweight', 'FAVC', 'CAEC', 'SMOKE','SCC', 'CALC', 'MTRANS']
  Gender_cat=['Male','Female']
  family_history_with_overweight_cat=['yes','no']
  FAVC_cat=['yes','no']
  CAEC_cat=[ 'Sometimes','no','Frequently','Always']
  SMOKE_cat=['yes','no']
  SCC_cat=['yes','no']
  CALC_cat=[ 'Sometimes','no','Frequently','Always']
  MTRANS_cat=['Public_Transportation','Automobile','Walking','Motorbike','Bike']
  num_pipeline=Pipeline(
      steps=[
     ('imputer',SimpleImputer(strategy='median')),
     ('scaler',StandardScaler())
     ]
  )
  cat_pipeline=Pipeline(
      steps=[
      ('imputer',SimpleImputer(strategy='most_frequent')),
      ('ordinalencoder',OrdinalEncoder(categories=[Gender_cat,family_history_with_overweight_cat,FAVC_cat,CAEC_cat,SMOKE_cat,SCC_cat,CALC_cat,MTRANS_cat])),
      ('scaler',StandardScaler())
      ]
  )
  preprocessor = ColumnTransformer([
  ('num_pipeline',num_pipeline,numerical_cols),
  ('cat_pipeline',cat_pipeline,categorical_cols)
  ])
  X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.30,random_state=30)
  X_train=pd.DataFrame(preprocessor.fit_transform(X_train),columns=preprocessor.get_feature_names_out())
  X_test=pd.DataFrame(preprocessor.transform(X_test),columns=preprocessor.get_feature_names_out())
  c = pd.DataFrame(preprocessor.transform(fr), columns=preprocessor.get_feature_names_out())
  return pd.DataFrame(c)