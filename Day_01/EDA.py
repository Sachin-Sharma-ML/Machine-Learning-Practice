# EDA UNIVARIATE 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
var = pd.read_csv("C:\\Users\\sharm\\Desktop\\machine learnig\\train.csv")
var

# Categorical data
### a count plot
sns.countplot(x='Survived',data=var)	
var['Survived'].value_counts()
sns.countplot(x='Pclass',data=var)
var['Pclass'].value_counts()
sns.countplot(x='Sex',data=var)
var['Sex'].value_counts()
sns.countplot(x='Embarked',data=var)
var['Embarked'].value_counts()
# piechart
var['Sex'].value_counts().plot(kind='pie',autopct='%.2f')
var['Survived'].value_counts().plot(kind='pie',autopct='%.2f')
var['Embarked'].value_counts().plot(kind='pie',autopct='%.2f')
# numerical data
## Histogram
plt.hist(var['Age'],bins=55)
## displot |Histplot
sns.distplot(var['Age'])
sns.histplot(var['Age'])
# Box plot
sns.boxplot(var['Age'])
var['Age'].min()
var['Age'].max()
var['Age'].mean()
var['Age'].skew()

