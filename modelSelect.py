import numpy as np 
import pandas as pd 
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

class ModelSelect(object):
	def __init__(self, model, name_of_model):
		'''
		input: 
			- model - is sklearn model class
			- name_of_model - name of model
		'''
		p_scaled = Pipeline([('scaler', StandardScaler()),
                   (name_of_model, model)])

		self.model = p_scaled

	def fit(self, X, y):
		'''
		Input:
			- X - dataframe
			- y - dataframe of dependent var
		'''
		self.model.fit(X,y)

	def predict(self, X):
		'''
		input:
			- X: dataframe 
		returns:
			- model predict: dataframe for model predictions
		'''
		return self.model.predict(X)

	def predict_proba(self, X):
		'''
		input:
			- X: dataframe 
		returns:
			- model predict probs: dataframe for model predictions probs
		'''
		return self.model.predict_proba(X)

	def coeff(self):
		pass

	def score(self, y_test):
		pass