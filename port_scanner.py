import socket
# import threading

def get_open_ports(target, port_range, verbose=None):
    open_ports = []
    start, end = port_range
    
    def port_scan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((target, port))
            print(f"The port {port} is Open.")
            open_ports.append(port)
            s.close()
        except:
            print(f'The port {port} is Closed.')
    
    for i in range(start, (end+1)):
        port_scan(i)

    return(open_ports)