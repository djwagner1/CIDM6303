#Experiment with data types

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

x = {1:{'hi':62, 'lo':42, 'hum':0.48},
    2:{'hi':64, 'lo':48, 'hum':0.53},
    3:{'hi':79, 'lo':47, 'hum':0.46},
    4:{'hi':52, 'lo':24, 'hum':0.44},
    5:{'hi':46, 'lo':28, 'hum':0.4},
    6:{'hi':50, 'lo':28, 'hum':0.6},
    7:{'hi':58, 'lo':32, 'hum':0.58},
    8:{'hi':66, 'lo':37, 'hum':0.5},
    9:{'hi':71, 'lo':43, 'hum':0.48},
    10:{'hi':77, 'lo':46, 'hum':0.43},
    11:{'hi':78, 'lo':47, 'hum':0.41},
    12:{'hi':78, 'lo':48, 'hum':0.39},
    13:{'hi':76, 'lo':48, 'hum':0.39},
    14:{'hi':79, 'lo':49, 'hum':0.38},
    15:{'hi':77, 'lo':50, 'hum':0.4}}

#for w_id,w_info in x.items():
#    print("Daily readings",w_id)

 #   for key in w_info:
#        print(key + ":", w_info[key])

#Hi_temp_values = x.values(key='hi')
#Hi_values_list = list(Hi_temp_values)
#print(Hi_values_list)