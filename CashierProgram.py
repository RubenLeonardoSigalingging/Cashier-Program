#!/usr/bin/env python3


import tabulate
from tabulate import tabulate
from os import system
system("clear")


print("-----------------------")
print("-----PROGRAM KASIR-----")
print("-----------------------")
print("\n")
print("MENU MAKANAN")
print(tabulate([["Kode","Nama","Harga"],["","",""],["AG","Ayam Goreng","Rp. 25.000"],["NG","Nasi Goreng","Rp. 24.000"],["MG","Mie Goreng","Rp. 22.000"],["KG","Kwetiaw Goreng","Rp. 18.000"],["TG","Telur Goreng","Rp. 15.000"]]))


print("\n")
print("MENU MINUMAN")
print(tabulate([["Kode","Nama","Harga"],["","",""],["JA","Jus Alpukat","Rp. 8.000"],["JM","Jus Mangga","Rp. 10.000"],["JP","Jus Pepaya","Rp. 9.000"],["JM","Jus Melon","Rp. 11.000"],["JJ","Jus Jambu","Rp. 12.000"]]))


tanya=str(input("[!] Pilih Menu Makanan dan Minuman: "))
if tanya=="ag" or "AG":
	from os import system
	from pyfiglet import figlet_format
	system("clear")
	system("chmod 777 CashierProgram.py")
	tema=figlet_format("AyamGoreng",font="slant")
	print(tema)
	print("")
	print("[!] Anda Akan Membeli Ayam Goreng!")
	print("[!] Harga Ayam Goreng: Rp. 25.000 / Porsi")
	jumlah=int(input("[!] Mau Beli Berapa? "))
	print("")
	print(f"[!] Anda Membeli Ayam Goreng {jumlah} Porsi!")
	total=25000*jumlah
	print(f"[!] Total Belanja Anda: {total}")
	print("")
	total_bayar=int(input("[!] Total Bayar Anda: "))
	total_pembayaran=total_bayar-total
	print("")
	print(f"[!] Uang Kembalian: {total_pembayaran}")
	print("[!] Terima Kasih Telah Mampir!")
