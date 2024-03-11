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

TBL_MATA_KULIAH = """CREATE TABLE MATA_KULIAH(
                    KODE_MATA_KULIAH VARCHAR(10) NOT NULL PRIMARY KEY,
                    NAMA_MATA_KULIAH VARCHAR(50) NOT NULL,
                    WAKTU DATE,
                    RUANGAN VARCHAR(10)
                    )"""

TBL_MAHASISWA = """CREATE TABLE MAHASISWA(
                    NIM VARCHAR(10) NOT NULL PRIMARY KEY,
                    NAMA_MAHASISWA VARCHAR(30) NOT NULL,
                    ALAMAT VARCHAR(255),
                    MATA_KULIAH_YANG_DIIKUTI VARCHAR(10),
                    FOREIGN KEY (MATA_KULIAH_YANG_DIIKUTI) REFERENCES MATA_KULIAH(KODE_MATA_KULIAH)
                    )"""

TBL_DOSEN = """CREATE TABLE DOSEN(
                NIP VARCHAR(20) NOT NULL PRIMARY KEY,
                NAMA_DOSEN VARCHAR(50) NOT NULL,
                MATA_KULIAH_YANG_DIAJAR VARCHAR(50),
                FOREIGN KEY (MATA_KULIAH_YANG_DIAJAR) REFERENCES MATA_KULIAH(KODE_MATA_KULIAH)
                )"""

cursorObject.execute(TBL_MATA_KULIAH)
cursorObject.execute(TBL_MAHASISWA)
cursorObject.execute(TBL_DOSEN)

dataBase.close()

