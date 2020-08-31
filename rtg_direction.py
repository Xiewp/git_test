import csv
import glob
import matplotlib.pyplot as plt
import numpy as np

camera_head = 'C20'          # the direction of travel
gantry_crane_length = 100    # define of the length for gantry crane
scaling_ratio = 0.002        # scalting ratio for data
point_interval = 5
C20_path = 'D://fjeport//RTG(Rubber Tire Gantry)//correct_data//test_0827//C20*C20.csv'
C23_path = 'D://fjeport//RTG(Rubber Tire Gantry)//correct_data//test_0827//C23*C20.csv'

C20_files = []
for C20_file_name in glob.glob(C20_path):
    C20_files.append(C20_file_name)
C23_files = []
for C23_file_name in glob.glob(C23_path):
    C23_files.append(C23_file_name)
csv_pair_nums = len(C20_files)

assert len(C20_files) == len(C23_files), \
    'the numbers of C20 csv are not equal to the numbers of C23 csv'

for i in range(csv_pair_nums):

    C20_angle = []
    C20_deviation = []
    with open(C20_files[i]) as C20_f:
        C20_f_csv = csv.reader(C20_f)
        for C20_row in C20_f_csv:
            C20_angle.append(C20_row[0])
            C20_deviation.append(C20_row[1])
        C20_angle = np.array(C20_angle, dtype='float')
        C20_deviation = np.array(C20_deviation, dtype='float')

    C23_angle = []
    C23_deviation = []
    with open(C23_files[i]) as C23_f:
        C23_f_csv = csv.reader(C23_f)
        for C23_row in C23_f_csv:
            C23_angle.append(C23_row[0])
            C23_deviation.append(C23_row[1])
        C23_angle = np.array(C23_angle, dtype='float')
        C23_deviation = np.array(C23_deviation, dtype='float')

    C20_deviation = C20_deviation*scaling_ratio
    C23_deviation = C23_deviation*scaling_ratio

    if camera_head == 'C20':
        head_deviation = C20_deviation
        back_deviation = C23_deviation
    elif camera_head == 'C23':
        head_deviation = C23_deviation
        back_deviation = C20_deviation
    else:
        raise ('please input the correct camera : C20 or C23.')

    points = len(head_deviation)
    for point in range(points):
        delta_y = head_deviation[point]-back_deviation[point]
        x_dev = np.sqrt(gantry_crane_length**2 - (delta_y)**2)
        x1 = -x_dev/2
        x2 = x_dev/2
        if point % 1 == 0:
            plt.arrow(x1+point*point_interval, back_deviation[point], x_dev, delta_y, width=0.01,
                      head_width=0.2, head_length=20, shape="full", fc='blue',
                      ec='green', overhang=0)
    plt.ylim(-2, 2)
    plt.title(C20_files[i].split('\\')[-1] + '\n' + C23_files[i].split('\\')[-1])
    plt.xlim(-gantry_crane_length, points*point_interval+gantry_crane_length)
    plt.plot((-gantry_crane_length, points*point_interval+gantry_crane_length), [0, 0], color='red')
    plt.show()
print('finish {} csv files'.format(csv_pair_nums*2))


