import socket
import common_ports

def get_open_ports(target, port_range, Verbose=None):
    open_ports = []
    start, end = port_range
    
    if target[0].isdigit():
        ip = True
    else:
        ip = False
        
    try:
        for i in range(start, (end + 1)):
            port = i
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            s.close()
        
        if Verbose:
            if ip:
                url = socket.gethostbyaddr(target)[0]
                string = f"Open ports for {url} ({target})\nPORT     SERVICE\n"
            else:
                ip_address = str(socket.gethostbyname(target))
                string = f"Open ports for {target} ({ip_address})\nPORT     SERVICE\n"
            port_arr = []
            
            for port in open_ports:
                space_length = 9 - len(str(port))
                common_port = common_ports.ports_and_services
                port_arr.append(f"{port}{space_length * ' '}{common_port[port]}")
        
            return string + '\n'.join(port_arr)
        else: 
            return open_ports
        
    except socket.gaierror:
        if ip == True:
            return "Error: Invalid IP address"
        else:
            return "Error: Invalid hostname"
        
    
        