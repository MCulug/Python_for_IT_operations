import html2text
import requests
import win32com.client
import os
from urllib.request import urlretrieve

def callconfluence(titleName,author,KBtext,out_folder):
 AUTH = 'api.admin', 'somepass'
 CNFurl = 'https://sdlctest.ibtech.com.tr:444/confluence/rest/api/content'
 headers = {'Content-Type':'application/json;charset=utf-8'}
 #titleNameEncoded = titleName.encode(encoding='utf-8')
 #authorEncoded = author.encode(encoding='utf-8')
 #bodyEncoded = KBtext.encode(encoding='utf-8')
 payload_final = """{
    "type": "page",
    "title": "%s - %s",
    "ancestors": [
        {
            "id": 34537522
        }
    ],
    "space": {
        "key": "TS"
    },
    "body": {
        "storage": {
            "value": "%s",
            "representation": "storage"
        }
    }
}""" % (titleName,author,KBtext)
 
 
 print(payload_final)
 outpath = out_folder + "\\" + "request.txt" 
 f = open(outpath, "w")
 f.write(payload_final)
 f.close()
 #print(titleName)
 #CNFrequest = requests.post(CNFurl,data=test, verify=False, headers=headers, auth=(AUTH))
 #print(CNFrequest.content)

def start(indexnumber):
 KBurl = 'http://infraapps.finansbank.com.tr/appinfraportal/KnowledgeBase/Index/%d' %(indexnumber)
 KBrequestA = win32com.client.Dispatch('WinHTTP.WinHTTPRequest.5.1')
 KBrequestA.SetAutoLogonPolicy(0)
 KBrequestA.Open('GET', KBurl, False)
 KBrequestA.Send()
 KBresult = KBrequestA.responseText  
 
 if KBresult.find('<div>Tuba Erbas Kilic (Ibtech-Inf Application Infrastructure)</div>') != -1 or KBresult.find('<div>Kivanc Acar (Ibtech-Inf Application Infrastructure)</div>') != -1 or KBresult.find('<div>Gokhan Polat (Ibtech-Inf Application Infrastructure)</div>') != -1 or KBresult.find('<div>Ozgur Akbulut (Ibtech-Inf Application Infrastructure)</div>') != -1 or KBresult.find('<div>Selim Kisa (Ibtech-Inf Application Infrastructure)</div>') != -1 or KBresult.find('<div>Berk Cakir (Ibtech-Inf Application Infrastructure)</div>') != -1 or KBresult.find('<div>Tolga Unvermis (Ibtech-Inf Application Infrastructure)</div>') != -1 or KBresult.find('<div>Murat Ulker (Ibtech-Inf Application Infrastructure</div>') != -1 or KBresult.find('<div>Didem Fergana (Ibtech-Inf Application Infrastructure)</div>') != -1 or KBresult.find('<div>Ismail Engin (Ibtech-Inf Application Infrastructure)</div>') != -1 :
  matchedtitle = "panel-title"
  matcehdline = [line for line in KBresult.split('\n') if matchedtitle in line]
  parse = matcehdline[0].split('<b>'[0])
  parse2 = parse[2].split('>'[0])
  titleName = parse2[1]
  payload = KBresult.split('col-md-8">')[1]
  payload2 = payload.split('<div class="panel-footer">')[0]
  author = payload.split('col-md-4">')[1]
  author2 = author.split('(Ibtech-Inf Application Infrastructure)')[0]
  author = author2.split('<div>')[2]
  Appendtext = ""
  Appendtext2 = ""
  imagecount=0
  out_folder = r"C:\Users\T64743\Desktop\pythonfiles\%d" %(indexnumber)
  os.mkdir(out_folder)
  for line in payload2.splitlines() :
     if 'data:image/' in line:
      filelink = line.split('src="')[1]
      filelink2 = filelink.split('"></span>')[0]
      outpath = out_folder + "\\" + str(imagecount) + ".png"
      urlretrieve(filelink2, outpath)
      imagecount = imagecount + 1
  for line in payload2.splitlines() :
     if 'data:image/' not in line:
      Appendtext = Appendtext + line 
  KBtext = html2text.html2text(Appendtext)
  KBtext2=KBtext.replace('"',"'")
  KBtext3=KBtext2.replace('\\',"|")
  KBtext4=KBtext3.replace('&','')
  KBtext5=KBtext4.replace('<','')
  KBtext6=KBtext5.replace('/>','')
  for line in KBtext4.splitlines():
   Append = line + "<br/>"
   Appendtext2 = Appendtext2 + Append
  print(Appendtext2) 
  #a="".join(Appendtext.split())
  callconfluence(titleName,author,Appendtext2,out_folder)
 else:
    print ("Team member Not found at index %d" %indexnumber)

if __name__ == '__main__': 
 for x in range (8, 32):
  start(x)
#start(19)

