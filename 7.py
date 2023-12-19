import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
heart_disease=pd.read_csv('data7.csv')
print('columns in datasets')
for col in heart_disease.columns:
  print(col)
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator as MLE
model=BayesianModel([('age','trestbps'),('age','fbs'),('sex','trestbps'),('exang','trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),('heartdisease','restecg'),('heartdisease','thalach'),('heartdisease','chol')])
model.fit(heart_disease,estimator=MLE)
print(model.get_cpds('sex'))
from pgmpy.inference import VariableElimination
HeartDisease_infer = VariableElimination(model)
q = HeartDisease_infer.query(variables = ['heartdisease'],evidence = {'age':29,'sex' : 0,'fbs':1})
print(q)