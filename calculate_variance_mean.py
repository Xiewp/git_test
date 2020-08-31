import csv
import glob
import matplotlib.pyplot as plt
import numpy as np

I_nums = 40

# C20
C20_file = []
for C20_file_name in glob.glob('D://fjeport//RTG(Rubber Tire Gantry)//correct_data//test_0827//C20*.csv'):
    C20_file.append(C20_file_name)
# C23
C23_file = []
for C23_file_name in glob.glob('D://fjeport//RTG(Rubber Tire Gantry)//correct_data//test_0827//C23*.csv'):
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
    C20_stds = []
    C20_means = []
    if len(C20_deviation) <= I_nums:
        pass
    else:
        for C20_index in range(I_nums, len(C20_deviation)):
            C20_stds.append(np.std(C20_deviation[(C20_index-I_nums):C20_index]))
            C20_means.append(np.mean(C20_deviation[(C20_index - I_nums):C20_index]))
    plt.plot(range(I_nums, len(C20_deviation)), C20_stds, label='C20_stds', color='#FFA500')
    plt.plot(range(I_nums, len(C20_deviation)), C20_means, label='C20_means', color='#FF00FF')

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
    C23_stds = []
    C23_means = []
    if len(C23_deviation) <= I_nums:
        pass
    else:
        for C23_index in range(I_nums, len(C23_deviation)):
            C23_stds.append(np.std(C23_deviation[(C23_index - I_nums):C23_index]))
            C23_means.append(np.mean(C23_deviation[(C23_index - I_nums):C23_index]))
    plt.plot(range(I_nums, len(C23_deviation)), C23_stds, label='C23_stds', color='#00FF7F')
    plt.plot(range(I_nums, len(C23_deviation)), C23_means, label='C23_means', color='#A9A9A9')

    plt.ylim(-350, 350)
    plt.plot((0, len(C20_deviation)), [-100, -100], color='r')
    plt.plot((0, len(C20_deviation)), [100, 100], color='r')
    plt.legend()
    plt.title(C23_file[i].split('\\')[-1])
    plt.show()
print('finish {} csv files'.format(csv_nums*2))


def stable_error(trace_list, i_nums=40, std_threshold=30):
    trace_list = np.array(trace_list)
    if len(trace_list) <= i_nums:
        return 0
    else:
        trace_stds = np.std(trace_list[-i_nums:])
        trace_means = np.mean(trace_list[-i_nums:])
    if trace_stds > std_threshold:
        return 0
    else:
        return trace_means


tmp_out = []
for tmp in (range(len(C23_deviation))):
    tmp_out.append(stable_error(C23_deviation[:tmp]))
plt.plot(tmp_out)
plt.show()
