from fitparse import FitFile
import matplotlib.pyplot as plt

# for record in fitfile.get_messages('record'):
#
#     # Go through all the data entries in this record
#     for record_data in record:
#
#         # Print the records name and value (and units if it has any)
#         if record_data.units:
#             print( record_data.name, record_data.value, record_data.units)
#         else:
#             print(record_data.name, record_data.value)
#     print

fitfile = FitFile('data_garmin_csv\8015057612_ACTIVITY.fit')
speed, heart_rate = [], []
for record in fitfile.get_messages('record'):
    # Go through all the data entries in this record
    for record_data in record:
        # Print the records name and value (and units if it has any)
        if record_data.name == 'speed':
            speed.append(record_data.value)
        if record_data.name == 'heart_rate':
            heart_rate.append(record_data.value)
# Plot grafik
min_len = min(len(speed), len(heart_rate))
plt.plot(speed[:min_len], heart_rate[:min_len])
plt.ylabel('heart_rate')
plt.xlabel('speed')
plt.show()

