from fitparse import FitFile
import matplotlib.pyplot as plt


def plot_grafik(x, y, x_value, y_value):
    #min datas in record mdr
    mdr = min(len(x), len(y))
    plt.plot(x[:mdr], y[:mdr])
    plt.ylabel(f', {y_value}')
    plt.xlabel(f', {x_value}')
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

flag = True
for record in fitfile.get_messages('record'):
    for record_data in record:
        match record_data.name:
            case '':
                if flag:
                    activity_type.append(record_data.value)
            case 'altitude':
                altitude.append(record_data.value)
                if flag:
                    altitude_unit = record_data.unit
            case 'cadence':
                cadence.append(record_data.value)
                if flag:
                    cadence_unit = record_data.unit
            case 'distance':
                distance.append(record_data.value)
                if flag:
                    distance_unit = record_data.unit
            case 'edenhanced_altitude':
                enhanced_altitude.append(record_data.value)
                if flag:
                    enhanced_altitude_unit = record_data.unit
            case 'enhanced_speed':
                enhanced_speed.append(record_data.value)
                if flag:
                    enhanced_speed_unit = record_data.unit
            case 'fractional_cadence':
                fractional_cadence.append(record_data.value)
                if flag:
                    fractional_cadence_unit = record_data.unit
            case 'heart_rate':
                heart_rate.append(record_data.value)
                if flag:
                    heart_rate_unit = record_data.unit
            case 'position_lat':
                position_lat.append(record_data.value)
            case 'position_long':
                position_long.append(record_data.value)
            case 'speed':
                speed.append(record_data.value)
                if flag:
                    speed_unit = record_data.unit
            case 'stance_time':
                stance_time.append(record_data.value)
                if flag:
                    stance_time_unit = record_data.unit
            case 'stance_time_balance':
                stance_time_balance.append(record_data.value)
                if flag:
                    stance_time_balance_unit = record_data.unit
            case 'stance_time_percent':
                stance_time_percent.append(record_data.value)
            case 'step_length':
                step_length.append(record_data.value)
                if flag:
                    step_length_unit = record_data.unit
            case 'temperature':
                temperature.append(record_data.value)
                if flag:
                    temperatureunit = record_data.unit
            case 'timestamp':
                timestamp.append(record_data.value)
                if flag:
                    timestamp_unit = record_data.unit
            case 'vertical_oscillation':
                vertical_oscillation.append(record_data.value)
                if flag:
                    vertical_oscillation_unit = record_data.unit
            case 'vertical_ratio':
                vertical_ratio.append(record_data.value)
                if flag:
                    vertical_ratio_unit = record_data.unit
        flag = False

# Plot grafik
plot_grafik(distance, heart_rate, distance_unit, heart_rate_unit)


