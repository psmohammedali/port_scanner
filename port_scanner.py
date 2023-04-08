import termcolor
import text_formats
import socket


def take_input():
    multi_scan = False

    choice = int(input(termcolor.colored(text_formats.scan_options,"magenta")))
    if choice == 1:
        pass
    else:
        print("2")
        multi_scan = True
    
    if multi_scan == False:
        print("Enter the IPV4 Address in the requested Format(i.e. 255.255.255.255): ")
        ip_address = input()
    else:
        print("Enter the IPV4 Address in their requested Format(i.e. 255.255.255.255, 192.52.58.14) with comma Separated: ")
        ip_address = input()

    
    ip_address_list = ip_address.split(",")
    for idx,ip_add in enumerate(ip_address_list):
        ip_address_list[idx] = ip_add.strip()
    return ip_address_list



def create_connection(ip_address):
    print(termcolor.colored("SCANNING PORTS ON {}".format(ip_address),"red"))
    refused_conn = 0
    accepted_conn = 0
    
    for port in range(1,100):
        try:
            socket_obj = socket.socket()
            socket_obj.connect((ip_address,port))
            accepted_conn  += 1
            print(termcolor.colored("{0} OPEN --> {1}".format(port,ip_address),"green"))
            socket_obj.close()
        except:
            print(termcolor.colored("STATUS: Open-> {0} & Close-> {1}".format(accepted_conn,refused_conn),"blue"))
            refused_conn += 1
        
    
    print("SUMMARY")
    print(termcolor.colored("OPEN PORTS on {0} : {1}".format(ip_address,accepted_conn),"green"))
    print(termcolor.colored("CLOSE PORTS on {0} : {1}".format(ip_address,refused_conn),"red"))
    print("=============================================================")

    



if __name__ == "__main__":
    print(termcolor.colored(text_formats.name,"red"))
    ip_address = take_input()
    for ip in ip_address:
        create_connection(ip)