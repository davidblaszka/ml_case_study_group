import numpy as np
import pandas as pd

class CompanyDataClean():
    def __init__(self, df):
        self.df = df

    def define_churn(self):
        '''
        churn column made, churn = 1
        '''
        self.df['churn'] = (self.df["last_trip_date"] < "2014-06-01")*1

    def basic_clean(self):
        self.define_churn()
        self.df['phone'] = self.df['phone'].fillna('other') #changed null phone type to other
        self.df['rated_by_driver'] = (self.df['avg_rating_by_driver'].isnull() == False) * 1 #new column rated or not
        self.df['rated_by_passenger'] = (self.df['avg_rating_of_driver'].isnull() == False) * 1 #new column for rated or not
        self.df['luxury_car_user'] = self.df["luxury_car_user"].astype(int) #change luxury car to ints

    def ratings_binning_categories(self):
        self.basic_clean()
        self.df['avg_rating_of_driver']= self.df['avg_rating_of_driver'].fillna(0)  #filled missing valus with mean
        mean_driver_rating =self.df['avg_rating_of_driver'].mean()
        bins = [-1,0.001,mean_driver_rating, 4.999, 5.1] #since no 0 ratings (we think)
        bin_titles = ['unknown','bad', 'good','perfect']
        categories = pd.cut(self.df['avg_rating_of_driver'], bins, labels = bin_titles)
        self.df['driver_rating'] = pd.cut(self.df['avg_rating_of_driver'], bins, labels= bin_titles)

        self.df['avg_rating_by_driver']= self.df['avg_rating_by_driver'].fillna(0)  #filled missing valus with mean
        mean_passenger_rating =self.df['avg_rating_by_driver'].mean()
        bins = [-1,0.001,mean_passenger_rating, 4.999, 5.1] #since no 0 ratings (we think)
        bin_titles = ['unknown','bad', 'good','perfect']
        categories = pd.cut(self.df['avg_rating_by_driver'], bins, labels = bin_titles)
        self.df['passenger_rating'] = pd.cut(self.df['avg_rating_by_driver'], bins, labels= bin_titles)

        self.df["avg_rating_of_driver"]=self.df["avg_rating_of_driver"].replace(0,np.NaN)
        self.df["avg_rating_by_driver"]=self.df["avg_rating_by_driver"].replace(0,np.NaN)
        return self.df

    def dummies(self):
        self.ratings_binning_categories()
        city_dummies = pd.get_dummies(self.df['city'])
        city_dummies = city_dummies.drop("Winterfell", axis=1)
        self.df = pd.concat((self.df, city_dummies), axis=1)

        phone_dummies = pd.get_dummies(self.df['phone'])
        phone_dummies = phone_dummies.drop("other", axis=1)
        self.df = pd.concat((self.df, phone_dummies), axis=1)

        driver_rating_dummies = pd.get_dummies(self.df['driver_rating'])
        driver_rating_dummies = driver_rating_dummies.drop("unknown", axis=1)
        self.df = pd.concat((self.df, driver_rating_dummies), axis=1)

        passenger_rating_dummies = pd.get_dummies(self.df['passenger_rating'])
        passenger_rating_dummies = passenger_rating_dummies.drop("unknown", axis=1)
        self.df = pd.concat((self.df, passenger_rating_dummies), axis=1)
        return self.df

    def numerical_data(self):
        self.dummies()
        self.df = self.df.drop([
                'avg_rating_by_driver',
                'avg_rating_of_driver',
                'city',
                'last_trip_date',
                'phone',
                'signup_date',
                'driver_rating',
                'passenger_rating'],axis=1)
        return self.df
