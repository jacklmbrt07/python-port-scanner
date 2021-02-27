import socket
# import threading

def get_open_ports(target, port_range, Verbose=None):
    open_ports = []
    start, end = port_range
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname) 
       
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
        
    if Verbose:
        #Open ports for scanme.nmap.org (45.33.32.156)
        # PORT     SERVICE
        # 22       ssh
        # 80       http
        string = f"Open ports for {target} ({ip_address})\nPORT     SERVICE\n"
        # {portnumber}{9 - portnumberlength * ' '}{service}
        port_arr = []
        
        return string + '\n'.join(port_arr)
    else: 
        return(str(open_ports))
        