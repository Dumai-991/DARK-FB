import os,sys



PERINTAH = """
cd $HOME
cd DARK-FB
mv data $HOME
mv results $HOME
cd
rm -rf DARK-FB
git clone https://github.com/Dumai-991/DARK-FB
cd $HOME
mv data DARK-FB
mv results DARK-FB
cd DARK-FB
"""

print(" |-->Tunggu Sebentar Sedang Update Script....")
os.system(PERINTAH)
print(' |')
print(' |')
print(' |-->Update Script Sudah Selesai...')
print(' |-->Silahkan Jalankan Perintah Ini : python main.py')
os.sys.exit()

