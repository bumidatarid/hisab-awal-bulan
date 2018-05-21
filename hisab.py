#!/usr/bin/env python
'''
Script untuk menghitung hisab awal bulan.

Algoritma: jika ketika Matahari terbenam, bulan di atas
horizon & kemarin di bawah horizon, maka terjadi bulan baru.
Seharusnya sudah mengakomodasi algoritma Muhammadiyah.

Script memperhitungkan situasi jika ada kemungkinan rukyat
tidak berhasil mengamati hilal, yaitu jika ketinggian bulan
di bawah 3° saat matahari terbenam.

Script hanya menghitung untuk lokasi Jakarta. Untuk
penentuan bulan baru, seharusnya dilakukan untuk lokasi
lain di Indonesia.
'''
import ephem
from datetime import datetime, timedelta

sekarang = datetime(2000, 1, 1, 5, 0, 0)
selesai = datetime(2100, 12, 1, 5, 0, 0)

bulan = ephem.Moon()
matahari = ephem.Sun()

pengamat = ephem.Observer()
pengamat.lon = '106.816667'
pengamat.lat = '-6.2'
pengamat.elevation = 8

ketinggiankemarin = 0

while sekarang <= selesai:
    pengamat.date = sekarang
    terbenam = pengamat.next_setting(matahari)
    pengamat.date = terbenam
    bulan.compute(pengamat)

    ketinggian = float(bulan.alt) / 0.01745329252

    if ketinggian > 0 and ketinggiankemarin <= 0:
        if ketinggian > 2:
            print("%s-%s-%s: Masuk bulan baru. Ketinggian bulan: %s°" % (sekarang.year, sekarang.month, sekarang.day, ketinggian))
        else:
            print("%s-%s-%s: Muhammadiyah masuk bulan baru, pemerintah tergantung rukyat. Ketinggian bulan: %s°" % (sekarang.year, sekarang.month, sekarang.day, ketinggian))

    ketinggiankemarin = ketinggian
    sekarang += timedelta(days = 1)