import csv
import urllib.request
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()#Asks for input file
with open(file_path, newline='') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        urllib.request.urlretrieve(URL_in_Csv, Downlad_file_name) # (url,download file as), You can read a url and download it as another name in the CSV 

       