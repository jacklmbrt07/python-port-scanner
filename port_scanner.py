import socket

def get_open_ports(target, port_range, verbose=None):
    open_ports = []

    start, end = port_range
    
    for i in range(start, (end+1)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = i
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"The port {port} is Open.")
            open_ports.append(port)
        else:
            print(f'The port {port} is Closed.')
        s.close()

    return(open_ports)