import csv
import glob
import matplotlib.pyplot as plt
import numpy as np

# C20
C20_file = []
for C20_file_name in glob.glob('D://fjeport//RTG(Rubber Tire Gantry)//correct_data//test_0819//C20*.csv'):
    C20_file.append(C20_file_name)
# C23
C23_file = []
for C23_file_name in glob.glob('D://fjeport//RTG(Rubber Tire Gantry)//correct_data//test_0819//C23*.csv'):
    C23_file.append(C23_file_name)

assert len(C20_file) == len(C23_file)
csv_nums = len(C20_file)

for i in range(csv_nums):

    C20_angle = []
    C20_deviation = []
    with open(C20_file[i]) as C20_f:
        C20_f_csv = csv.reader(C20_f)
        for C20_row in C20_f_csv:
            C20_angle.append(C20_row[0])
            C20_deviation.append(C20_row[1])
        C20_angle = np.array(C20_angle, dtype='float')
        C20_deviation = np.array(C20_deviation, dtype='float')
        print('{}    contains {} points'.format(C20_file[i], C20_f_csv.line_num))
        plt.plot(range(len(C20_deviation)), C20_deviation, label='C20', color='b')

    C23_angle = []
    C23_deviation = []
    with open(C23_file[i]) as C23_f:
        C23_f_csv = csv.reader(C23_f)
        for C23_row in C23_f_csv:
            C23_angle.append(C23_row[0])
            C23_deviation.append(C23_row[1])
        C23_angle = np.array(C23_angle, dtype='float')
        C23_deviation = np.array(C23_deviation, dtype='float')
        print('{}    contains {} points'.format(C23_file[i], C23_f_csv.line_num))
        plt.plot(range(len(C23_deviation)), C23_deviation, label='C23', color='g')

    plt.ylim(-350, 350)
    plt.plot((0, len(C20_deviation)), [-100, -100], color='r')
    plt.plot((0, len(C20_deviation)), [100, 100], color='r')
    plt.legend()
    plt.show()
print('finish {} csv files'.format(csv_nums*2))
