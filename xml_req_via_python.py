import requests
import time
#same file must be created on odm everyday

def do_xml_req (target_host,xml_value)
 headers = {'Content-Type': 'application/xml'}
 myauth = 'admin', 'admin'
 payload="""<?xml version="1.0" encoding="UTF-8"?>
<env:Envelope xmlns:env="http://schemas.xmlsoap.org/soap/envelope/">
<env:Body>
         <mytag>%s</mytag>
</env:Body>
</env:Envelope>""" % xml_value
 logfile = open("mylog.txt","a+")
 time_start = str(time.strftime("%d %B %Y %H:%M:%S"))
 upload_resp=str(requests.post(target_host, data=payload, verify=False, headers=headers, auth=(myauth)).text)
 time_end = str(time.strftime("%d %B %Y %H:%M:%S"))
 logfile.write("\n operation started at "+time+" \n operation finished at "+time+" \n Response : "+upload_resp+"\n")
 logfile.close()

do_xml_req('https://some_server_address_1','some_xml_value')
do_xml_req('https://some_server_address_2','some_xml_value')
