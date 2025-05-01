#This is my first project on this IDLE. I am working on Pandas.
#Use "#" when commenting out a single line.
#Use (""") if you are describing functions,classes or modules.
#Installing Libraries.
    #Steps:(Windows or MacBook):
            #Close IDLE if already open
            #Win+R or type cmd >>(windows)/cmd+space or type terminal >>(Mac).
            #type:pip install name_of_library e.g pandas.>>(Windows)
            #type:pip3 install name_of_library e.g pandas. >>(Mac)
            #Reopen IDLE and type: import pandas as pd.
#Working with projects:
    #Windows or Mackbook:
        #File > New(BOTH) or Ctrl+N>>(Windows) and cmd+N>>(Mac) (.py)file names.
        #File > Save(Both) or Ctrl+S>>(Windows) and cmd+S>>(Mac)
        #Run>Run Module or F5 (Both) to run files.
        #Shell > Restart shell (Both) to restart your shell.

#Begin by importation of pandas as pd.

import pandas as pd
pd.set_option('display.max_columns',None)#This tells panda not to hide any columns, no matter how many they are

#Creating a dataframe.(Let's use a dictioanary to create one)
data={
    'name':['Lewis','Joy','Ian','Karen','Lance','Nzilani','Barbara'],
    'location':['Mumbi','Chamos','Wendani','All-soaps','Hurmbuger','Wendani','Sukari'],
    'age':[21,22,20,21,22,21,23],
    'score':[88.0,87.0,86.0,85.0,84.0,83.0,82.0]
    }
row_labels=[101,102,103,104,105,106,107]

df=pd.DataFrame(data=data, index=row_labels)
df

df2=pd.DataFrame(data=data, index=row_labels, columns=['score','age','location','name'])
df2                 

#Creating df using a list of dictionaries
d=[{'x':1,'y':2,'z':100},
   {'x':2,'y':3,'z':100},
   {'x':3,'y':4,'z':100}
   ]
df3=pd.DataFrame(d)

#Creating df using a list of list
d2=[[1,2,100],
    [2,3,100],
    [3,4,100]
    ]
df4=pd.DataFrame(d2,columns=['x','y','z'])

#Saving my candiidate data frame to a CSV file
df.to_csv('data.csv')
df_=pd.read_csv('data.csv',index_col=0)

#Modification of labels
#importing numpy as np to do the array modification
#.arange() function generates a NumPy array of evenly spaced values within a given interval
import numpy as np
df_.index=np.arange(10,17)
df_.index

#Modification of the column data types using the .astype() function
df_1=df_.astype(dtype={'age':np.int32,'score':np.float32})
df_1

#Modification of data in a data frame
#this modifies the first 5 items in the columnn 'score' using the supplied list.
df_.iloc[0:5,df_.columns.get_loc('score')]=[98.0,99.0,97.0,95.0,96.0]

#This modifys the values of the remaining columns with 0.0
df_.iloc[5:7,df_.columns.get_loc('score')]=100
                                            
#Inserting and deleting data in our data frame(ROW data)
#A)Inserting data
    #We start by creating a new object series.
new_series=pd.Series(data=['Liz', 'Embakasi', 22, 91.0],
                     index=df_.columns, name=17)

    #We now add this object into our df using the .concat() function call
df_ = pd.concat([df_, new_series.to_frame().T], ignore_index=False)

#B)Removing a row from a df
    #We use the .drop() function
df2_=df_.drop(labels = [17])

#Inserting and deleting columns.
   # Inserting a column at a specific position
df_.insert(loc=1, column='County', value=['Kirinyaga','Embu','Nyamira','Nyeri',
                                          'Muranga','Makueni','Eldoret','TaitaTaveta'])
    #Adding a column at the end of the dataframe
df_['js-score']=np.array([71.0,72.0,74.0,75.0,76.0,77.0,78.0,79.0])
    #OR Alternatively
#df_['js-score']= [71.0,72.0,74.0,75.0,76.0,77.0,78.0,79.0]

    #Adding a constant value
df_['academic_status']='Active'

    #Loopin/adding a value based on the values of another column
df_['Age_group']=df_['age'].apply(lambda x: 'teen' if x < 20 else 'adult')

#You can do arithmetic operations on pandaSeries and DataFrames
    #df_['score']+df_['js-score']
    #df_['score']/100
#You can also use arithmetic operation to add a new column to your DataFrame
    #Let's add a new column known as 'total'print)
df_['total']=0.4*df_['score']+0.3*df_['js-score']

#Applying NumPy and SciPy to pandaSeries and DataFrame
#score_=df_.iloc[:,4:6]
score_=df_[['score','js-score']] #either of the two creates the variable score
weights=[0.4,0.3]
weighted_avg=np.average(score_.to_numpy(),axis=1, weights=weights)
    
#Filtering data in Pandas
    #Expressions used
#NOT(~)
    #AND(&)
    #OR(|)
    #XOR(^)'''
filter_=(df_['score']>97.0) & (df_['js-score']<78.0)
    
#Determining Data Statistics
#You can get basic statistics for numerical columns using the call function .describe()
#df_.describe()

#WORKING WITH TIME SERIES
#We will first start by creating a list with data values, which will be hourly temperatues
#given in degrees celcius
temp_c = [ 8.0,  7.1,  6.8,  6.4,  6.0,  5.4,  4.8,  5.0,
           9.1, 12.8, 15.3, 19.1, 21.2, 22.1, 22.4, 23.1,
           21.0, 17.9, 15.5, 14.4, 11.9, 11.0, 10.2,  9.1]
#The next step is to create a sequence of dates and times.
#We use the function pd.date_range()
dt = pd.date_range(start='2019-10-27 00:00:00.0', periods=24,
                   freq='h')
#We can now create a data frame usung the above variables
temp = pd.DataFrame(data={'temp_c': temp_c}, index=dt)

#PLOTTING WITH PANDAS DATA FRAME
#We have to import matploylib library
import matplotlib.pyplot as plt

#We use pandas.DataFrame.plot() to plot
#We use plt.show() to show
temp.plot()
# plt.show()>>This is now run in the shell to display the plotted graph

