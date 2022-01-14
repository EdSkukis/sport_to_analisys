from fitparse import FitFile
import matplotlib.pyplot as plt


def plot_grafik(x, y, x_value, y_value):
    #min datas in record mdr
    mdr = min(len(x), len(y))
    plt.plot(x[:mdr], y[:mdr])
    plt.ylabel(f'{y_value}')
    plt.xlabel(f'{x_value}')
    plt.show()


fitfile = FitFile('data_garmin_fit\8015057612_ACTIVITY.fit')

# record structur:
altitude, cadence, distance, enhanced_altitude, enhanced_speed, \
fractional_cadence, heart_rate, position_lat, position_long, speed, stance_time, \
stance_time_balance, stance_time_percent, step_length, temperature, timestamp, \
vertical_oscillation, vertical_ratio \
    = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

activity_type, altitude_unit, cadence_unit, distance_unit, enhanced_altitude_unit, enhanced_speed_unit, \
fractional_cadence_unit, heart_rate_unit, position_lat_unit, position_long_unit, speed_unit, stance_time_unit, \
stance_time_balance_unit, stance_time_percent_unit, step_length_unit, temperature_unit, timestamp_unit, \
vertical_oscillation_unit, vertical_ratio_unit \
    = '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''

flag = 0
for record in fitfile.get_messages('record'):
    flag += 1
    for record_data in record:
        match record_data.name:
            case '':
                if flag < 2:
                    activity_type.append(record_data.value)
            case 'altitude':
                altitude.append(record_data.value)
                if flag < 2:
                    altitude_unit = record_data.units
            case 'cadence':
                cadence.append(record_data.value)
                if flag < 2:
                    cadence_unit = record_data.units
            case 'distance':
                distance.append(record_data.value)
                if flag < 2:
                    distance_unit = record_data.units
            case 'edenhanced_altitude':
                enhanced_altitude.append(record_data.value)
                if flag < 2:
                    enhanced_altitude_unit = record_data.units
            case 'enhanced_speed':
                enhanced_speed.append(record_data.value)
                if flag < 2:
                    enhanced_speed_unit = record_data.units
            case 'fractional_cadence':
                fractional_cadence.append(record_data.value)
                if flag < 2:
                    fractional_cadence_unit = record_data.units
            case 'heart_rate':
                heart_rate.append(record_data.value)
                if flag < 2:
                    heart_rate_unit = record_data.units
            case 'position_lat':
                position_lat.append(record_data.value)
            case 'position_long':
                position_long.append(record_data.value)
            case 'speed':
                speed.append(record_data.value)
                if flag < 2:
                    speed_unit = record_data.units
            case 'stance_time':
                stance_time.append(record_data.value)
                if flag < 2:
                    stance_time_unit = record_data.units
            case 'stance_time_balance':
                stance_time_balance.append(record_data.value)
                if flag < 2:
                    stance_time_balance_unit = record_data.units
            case 'stance_time_percent':
                stance_time_percent.append(record_data.value)
            case 'step_length':
                step_length.append(record_data.value)
                if flag < 2:
                    step_length_unit = record_data.units
            case 'temperature':
                temperature.append(record_data.value)
                if flag < 2:
                    temperatureunit = record_data.units
            case 'timestamp':
                timestamp.append(record_data.value)
                if flag < 2:
                    timestamp_unit = record_data.units
            case 'vertical_oscillation':
                vertical_oscillation.append(record_data.value)
                if flag < 2:
                    vertical_oscillation_unit = record_data.units
            case 'vertical_ratio':
                vertical_ratio.append(record_data.value)
                if flag < 2:
                    vertical_ratio_unit = record_data.units


# Plot grafik
plot_grafik(distance, heart_rate, distance_unit, heart_rate_unit)

