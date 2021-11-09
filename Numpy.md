## Converting Data Type on Existing Arrays
    rr = numpy.array([1.1, 2.1, 3.1])
    newarr = arr.astype(int)

## Reshape From 1-D to 2-D
    arr = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    newarr = arr.reshape(4, 3)
    
## Flattening the arrays
    arr = numpy.array([[1, 2, 3], [4, 5, 6]])
    newarr = arr.reshape(-1)
    
## Joining NumPy Arrays
    arr1 = numpy.array([1, 2, 3])
    arr2 = numpy.array([4, 5, 6])
    arr = numpy.concatenate((arr1, arr2))
> [1,2,3,4,5,6]
> 
### Join two 2-D arrays along rows (axis=1):
    arr1 = numpy.array([[1, 2], [3, 4]])
    arr2 = numpy.array([[5, 6], [7, 8]])
    arr = numpy.concatenate((arr1, arr2), axis=1)
> [[1 2 5 6]
 [3 4 7 8]]
 
 ### Joining Arrays Using Stack Functions
    arr1 = numpy.array([1, 2, 3])
    arr2 = numpy.array([4, 5, 6])
    arr = numpy.stack((arr1, arr2), axis=1)
> [[1 4]
 [2 5]
 [3 6]]    
 
    arr = numpy.stack((arr1, arr2), axis=0)
> [[1 2 3]
 [4 5 6]]
 
## Stacking Along Rows
    arr1 = numpy.array([1, 2, 3])
    arr2 = numpy.array([4, 5, 6])
    arr = numpy.vstack((arr1, arr2))
> [1,2,3,4,5,6]
## Stacking Along Columns
    arr1 = numpy.array([1, 2, 3])
    arr2 = numpy.array([4, 5, 6])
    arr = numpy.vstack((arr1, arr2))
> [[1 2 3]
 [4 5 6]]
 
 ## Find the indexes where the value is 4:
    arr = numpy.array([1, 2, 3, 4, 5, 4, 4])
    x = numpy.where(arr == 4)
## Find the indexes where the values are even:
    arr = numpy.array([1, 2, 3, 4, 5, 6, 7, 8])
    x = numpy.where(arr%2 == 1)
## Sort the array:
    arr = numpy.array([3, 2, 0, 1])
    numpy.sort(arr)
## Create an array from the elements on index 0 and 2:
    arr = numpy.array([41, 42, 43, 44])
    x = [True, False, True, False]
    newarr = arr[x]
