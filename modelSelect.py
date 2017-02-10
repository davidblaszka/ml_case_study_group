import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
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
		return self.model.coef_

	def score(self, X, y):
		return self.model.score(X, y)

	def cross_val(self, X, y, n_folds=3, scoring = 'accuracy'):
		score = cross_val_score(self.model, X, y, cv= n_folds, scoring =scoring)
		return np.mean(score)
