print('Enter TB or GB for the advertised unit:')
unit = input('>')

# Calculate the amount that the advertised capacity lies:
if unit == 'TB' or unit == 'tb':
    discrepancy = 1000**4 / 1024**4
elif unit == 'GB' or unit == 'gb':
    descrepancy = 1000*3 / 1024**3

print('Enter the advertise capacity:')
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)

# Calculate the real capacity, round it to the nearest hundredths,
# and convert it to a string so it can be concatenated with other strings::
real_capacity = str(round(advertised_capacity * discrepancy, 2))

print('The actual capacity is ' + real_capacity + ' ' + unit)

# The advertised capacity is always greater than the actual
# When calculating the discrepancy, the discrepancy is always less than 1
# When you multiply the advertised capacity by the discrepancy, you will get the actual capacity

# This is the difference between TB and TiB