import threading
import time


def test():
    for j in range(5):
        print('test {}'.format(j))
        time.sleep(1)


thread = threading.Thread(target=test)
thread.start()
for i in range(5):
    print("main {}".format(i))
    time.sleep(1)
