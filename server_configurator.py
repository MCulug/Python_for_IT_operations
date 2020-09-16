#!/usr/bin/env python
import yaml

def main():
 CHOICE = input("Please select the operation  \n 1 - list servers: \n 2 - add server to list: \n 3 - set server configuration: \n 4 - remove server from list: ")
 options = {'1' : list_server, '2' : add_server,'3' : set_server,'4' : remove_server}
 options[CHOICE]()

def list_server():
    with open("test1.yaml") as f:
     list_doc = yaml.safe_load(f)
     for t in list_doc:
            print("Server Name:",t["NAME"],"| hostname:",t["hostname"],"| ip address:",t["ipaddr"],"\n")

def add_server():
    serv_name = input("Please give the server a name")
    serv_hostname = input("Please write server hostname")
    serv_ip = input("Please write server ip")
    new_yaml_data_dict = {'NAME': serv_name, 'hostname': serv_hostname, 'ipaddr': serv_ip}
    with open("test1.yaml") as f:
        list_doc = yaml.safe_load(f)
        list_doc.append(new_yaml_data_dict)

    with open("test1.yaml", "w") as f:
        yaml.safe_dump(list_doc, f)

def set_server():
    serv_name = input("Please write server name to make changes in config")
    new_host_name = input("Please write new host name")
    new_ip = input("Please write new ip addres")
    with open("test1.yaml") as f:
        list_doc = yaml.safe_load(f)

    for b in list_doc:
        if b["NAME"] == serv_name:
            b["hostname"] = new_host_name
            b["ipaddr"] = new_ip

    with open("test1.yaml", "w") as f:
        yaml.safe_dump(list_doc, f)

def remove_server():
    delete_serv = input("Please write server name to delete")
    with open("test1.yaml") as f:
        list_doc = yaml.safe_load(f)
        count = 0
        for sense in list_doc:
            if sense["NAME"] == delete_serv:
                print(count)
                del list_doc[count]
            else: count += 1
    #print(list_doc[1])
    # delete as if like an array element deletion
    with open("test1.yaml", "w") as f:
        yaml.safe_dump(list_doc, f)

def send_request_to_servers(request_xml):
    AUTH = 'admin', 'pass'  
    port = '9080'   #api port of server
    headers = {'Content-Type': 'text/xml;charset=UTF-8'}
    for c in list_doc:
        target_host = c["hostname"] + port
        sent = requests.post(target_host, data=request_xml, verify=False, headers=headers, auth=(AUTH))
        result = sent.content

if __name__ == "__main__":
    main()
