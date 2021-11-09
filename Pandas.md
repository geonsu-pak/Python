## Series
    import pandas as pd
    a = [1, 7, 2]
    myvar = pd.Series(a)
    print(myvar)
> index value    
> 0     1       
> 1     7    
> 2     2    
### Create your own labels:
    import pandas as pd
    a = [1, 7, 2]
    myvar = pd.Series(a, index = ["x", "y", "z"])
> x     1       
> y     7    
> z     2 
### Create a simple Pandas Series from a dictionary:
    import pandas as pd
    calories = {"day1": 420, "day2": 380, "day3": 390}
    myvar = pd.Series(calories)

## DataFrames = Datasets in Pandas
    import pandas as pd
    data = {
         # two Series
         "calories": [420, 380, 390],
         "duration": [50, 40, 45]
    }
    df = pd.DataFrame(data)
### Locate Row
    #refer to the row index:
    print(df.loc[0])
> calories    420    
> duration     50
    #use a list of indexes:
    print(df.loc[[0, 1]])    
>    calories  duration    
> 0       420        50    
> 1       380        40

## Load Files Into a DataFrame
    import pandas as pd
    df = pd.read_csv('data.csv')
    df.info()
### Remove Rows that contain empty(=NULL) cells
    import pandas as pd
    df = pd.read_csv('data.csv')
    new_df = df.dropna() # return a new DataFrame
### Change the original DataFrame, use the inplace = True
    df.dropna(inplace = True)
### Replace NULL values with the number 130:
    df.fillna(130, inplace=True)
### Replace Only For a Specified Columns
    df["Calories"].fillna(130, inplace = True)
    x = df["Calories"].mean()
    df["Calories"].fillna(x, inplace = True)  
### Remove rows with a NULL value in the "Date" column:
    df.dropna(subset=['Date'], inplace = True)
### Set "Duration" = 45 in row 7:
    df.loc[7, 'Duration'] = 45
### Loop through all values in the "Duration" column.
    # If the value is higher than 120, set it to 120:
    for x in df.index:
        if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120
### Delete rows where "Duration" is higher than 120:
    for x in df.index:
    if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
### Remove all duplicates:
    df.duplicated() # check
    df.drop_duplicates(inplace = True)
    
## Plotting
    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.read_csv('data.csv')
    df.plot()
    plt.show()
### Scatter
    df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
    plt.show()
