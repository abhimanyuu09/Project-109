import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

#Finding The Mean
mean = sum(data) / len(data)
#Finding The Median
median = statistics.median(data)
#Finding The Mode
mode = statistics.mode(data)
print("Mea, Median, Mode are {},{} and {}".format(mean,meadian,mode))

#Finding The Standard Deviation
std_deviation = statistics.stdev(data)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

list_of_data_in_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_in_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_in_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("Standard deviation is {}".format(std_deviation))
print("{}% of data is within 1 standard deviation".format(len(list_of_data_in_1_std_deviation)*100.0/len(data)))
print("{}% of data is within 2 standard deviations".format(len(list_of_data_in_2_std_deviation)*100.0/len(data)))
print("{}% of data is within 3 standard deviations".format(len(list_of_data_ins_3_std_deviation)*100.0/len(data)))
