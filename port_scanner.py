import socket
import threading

def get_open_ports(target, port_range, verbose=None):
    open_ports = []

    start, end = port_range
    
    def port_scan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            result = s.connect((target, port))
            print(f"The port {port} is Open.")
            if result:
                open_ports.append(port)
            result.close()
        except:
            print(f'The port {port} is Closed.')
        
    
    for i in range(start, (end+1)):
        t = threading.Thread(target=port_scan, kwargs={'port':i})
        t.start()

    return(open_ports)