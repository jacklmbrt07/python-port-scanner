import socket
import common_ports
# import threading

def get_open_ports(target, port_range, Verbose=None):
    open_ports = []
    start, end = port_range
    ip_address = socket.gethostbyname(target) 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
       
    def port_scan(port):
        try:
            s.connect((target, port))
            print(f"The port {port} is Open.")
            open_ports.append(port)
        except:
            print(f'The port {port} is Closed.')
        finally:
            s.close()
            return
    
    for i in range(start, (end+1)):
        port = i
        port_scan(port)
        
    if Verbose:
        string = f"Open ports for {target} ({ip_address})\nPORT     SERVICE\n"
        port_arr = []
        
        for port in open_ports:
            space_length = 9 - len(str(port))
            common_port = common_ports.ports_and_services
            port_arr.append(f"{port}{space_length * ' '}{common_port[port]}")
        
        return string + '\n'.join(port_arr)
    else: 
        return(str(open_ports))
        