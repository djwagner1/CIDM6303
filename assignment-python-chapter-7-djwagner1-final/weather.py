#code below
import statistics

#Find the max high temp and the avg temp for list of values
hi_temp = [62,64,79,52,46,50,58,66,71,77,78,78,76,79,77]
max_hi = max(hi_temp)
avg_hi = int(sum(hi_temp)/len(hi_temp))

#Find the minimum low temp and average low temp for list

low_temp=[42,48,47,24,28,28,32,37,43,46,48,47,48,49,50]
min_low = min(low_temp)
avg_low= int(sum(low_temp)/len(low_temp))


#Find the average humidity
humid = [.48,.53,.46,.44,.4,.6,.58,.5,.48,.43,.41,.39,.39,.38,.4]
avg_hum = sum(humid)/len(humid)

# Print the required output for the assignment
print(f"Weather forecast for the next 15 days: The average high will be {avg_hi} and the average\n")
print(f"low will be {avg_low}. The highest temperature will be {max_hi}. The lowest temperature\n")
print(f"will be {min_low}. The average humidity will be {avg_hum:.2f}.")