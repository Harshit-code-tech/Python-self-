from statistics import mode
from statistics import median
from statistics import mean

# def calculate_mean(data):
#     mean=sum(data)/len(data)
#     return mean
# def calculate_median(data1):
#     data1.sort()
#     n=len(data1)
#     mid=n//2
#     if n%2==0:
#         median = (data1[mid-1]+ data1[mid])/2
#     else:
#         median = data1[mid]
#     return median

data_set=[10,15,525,123,52,30,30]
mean_result = mean(data_set)
print("mean :" ,mean_result)
mediam_Result = median(data_set)
print("Median :", mediam_Result)
mode_result=mode(data_set)
print("MOde: ",mode_result)