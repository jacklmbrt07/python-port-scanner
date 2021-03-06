# This entrypoint file to be used in development. Start by reading README.md
import port_scanner
from unittest import main

# # Called with URL
# ports = port_scanner.get_open_ports("209.216.230.240", [440, 445])
# print("Open ports:", ports)
# expected 443 open

# # Called with ip address
# ports = port_scanner.get_open_ports("104.26.10.78", [8079, 8090])
# print("Open ports:", ports)

# # Verbose called with ip address and no host name returned -- single open port
# ports = port_scanner.get_open_ports("104.26.10.78", [440, 450], False)
# print(ports + '\n')

# # Verbose called with ip address and valid host name returned -- single open port
# ports = port_scanner.get_open_ports("137.74.187.104", [440, 450], True)
# print(ports + '\n')

# # Verbose called with host name -- multiple ports returned
# ports = port_scanner.get_open_ports("398ywdfkajskj23", [20, 80], True)
# print(ports + '\n')

# ports = port_scanner.get_open_ports("ljsdflkjasdf", [22, 42], False)
# print(ports)
# ports = port_scanner.get_open_ports("104.26.10.78", [440, 450], True)
# print(ports)
# expected = "Open ports for hackthissite.org (137.74.187.104)\nPORT     SERVICE\n443      https"


# err = port_scanner.get_open_ports("scanme.nmap", [22, 42], False)
# print(err)
# expected = "Error: Invalid hostname"

# # Run unit tests automatically
main(module='test_module', exit=False)