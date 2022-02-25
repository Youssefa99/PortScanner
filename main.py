import socket
import threading
from queue import Queue

'''

PortScanning is illegal and should only be used in your network or if you have permission to use it on a network
This script is for educational purposes only and should not be used to access networks without connections

'''

target = "Target IP address"
queue = Queue()
open_ports = []


# connect to the port
def port_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        return True
    except:
        return False


# put ports range in queue
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


# thread worker function
def worker():
    while not queue.empty():
        port = queue.get()
        if port_scan(port):
            print("port {} is open".format(port))
            open_ports.append(port)


port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

# run 512 threads for execution speed
for i in range(512):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

# start threads activities
for thread in thread_list:
    thread.start()

# wait until all threads are finished before printing
for thread in thread_list:
    thread.join()

print("open ports are: ", open_ports)
