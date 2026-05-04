from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)

import time
import counterfit_shims_serial

serial = counterfit_shims_serial.Serial('COM1')  # hoặc port đúng trong CounterFit

print("STARTING GPS...")

while True:
    line = serial.readline()

    if line:
        try:
            print("DATA:", line.decode('utf-8').strip())
        except:
            print("DATA:", line)

    time.sleep(0.5)