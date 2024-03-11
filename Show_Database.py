#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

insertMataKuliah = "INSERT INTO MATA_KULIAH (KODE_MATA_KULIAH, NAMA_MATA_KULIAH, WAKTU, RUANGAN) VALUES (%s, %s, %s, %s)"
valueMataKuliah = [
    ("MK111", "Praktik Pemrograman Python", "2024-03-11", "L2R3"),
    ("MK222", "Basis Data", "2024-03-11", "L2R2"),
    ("MK333", "Pemrograman Web", "2024-03-12", "L2R2"),
    ("MK444", "Wireless Communication", "2024-03-13", "L2R3"),
    ("MK555", "Analisis Sistem Informasi", "2024-03-13", "L2R2")    
]

insertDosen = "INSERT INTO DOSEN (NIP, NAMA_DOSEN, MATA_KULIAH_YANG_DIAJAR) VALUES (%s, %s, %s)"
valueDosen = [
    ("00890111", "Yusuf Fadilla Rachman", "MK111"),
    ("00890112", "Masbahah", "MK222"),
    ("00890113", "Masbahah", "MK333"),
    ("00890114", "Yusuf Fadilla Rachman", "MK444"),
    ("00890115", "Trisna Ari Roshinta", "MK555")
]

insertMahasiswa = "INSERT INTO MAHASISWA (NIM, NAMA_MAHASISWA, ALAMAT, MATA_KULIAH_YANG_DIIKUTI) VALUES (%s, %s, %s, %s)"
valueMahasiswa = [
    ("V3923001", "Heigel", "Magetan", "MK111"),
    ("V3923002", "Bunga", "Yogyakarta", "MK222"),
    ("V3923003", "Arul", "Surabaya", "MK333"),
    ("V3923004", "Raihan", "Surakarta", "MK444"),
    ("V3923005", "Salsa", "Malang", "MK555")
]

cursorObject.executemany(insertMataKuliah, valueMataKuliah)
cursorObject.executemany(insertDosen, valueDosen)
cursorObject.executemany(insertMahasiswa, valueMahasiswa)

dataBase.commit()

dataBase.close()

