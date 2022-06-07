import csv
import requests

CSV_URL = 'https://data.primariatm.ro/datastore/dump/a9b00faa-82a1-4ea0-aa11-ddd6edad7ca7?bom=True'

with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)

import requests
URL = 'https://data.primariatm.ro/datastore/dump/a9b00faa-82a1-4ea0-aa11-ddd6edad7ca7?bom=True'
response = requests.get(URL)
open('fisier.csv', 'wb').write(response.content)

from tkinter import ttk
import tkinter as tk

# crearea , configurarea tabelului si introducerea datelor
window = tk.Tk()
window.resizable(width=2, height=2)

treev = ttk.Treeview(window, selectmode='browse')

treev.pack(side='right')

# crearea scrollbarului
verscrlbar = ttk.Scrollbar(window,
                           orient="vertical",
                           command=treev.yview)
horscrlbar = ttk.Scrollbar(window,
                           orient="horizontal",
                           command=treev.xview)

verscrlbar.pack(side='right', fill='x')
horscrlbar.pack(side='left', fill='y')

# configurarea scrollbarului
treev.configure(xscrollcommand=verscrlbar.set)
treev.configure(yscrollcommand=horscrlbar.set)

# definirea numarului coloanelor
treev["columns"] = ("1", "2", "3","4","5","6","7","8","9","10","11")

# titlul
treev['show'] = 'headings'

# definirea latimii si a pozitiei textului
treev.column("1", width=400, anchor='c')
treev.column("2", width=90, anchor='se')
treev.column("3", width=90, anchor='se')
treev.column("4", width=90, anchor='se')
treev.column("5", width=90, anchor='se')
treev.column("6", width=90, anchor='se')
treev.column("7", width=90, anchor='se')
treev.column("8", width=90, anchor='se')
treev.column("9", width=90, anchor='se')
treev.column("10", width=90, anchor='se')
treev.column("11", width=90, anchor='se')




# introducerea titlurilor in coloanele respective

treev.heading("1", text="Cultura si culte")
treev.heading("2", text="2019")
treev.heading("3", text="2018")
treev.heading("4", text="2017")
treev.heading("5", text="2016")
treev.heading("6", text="2015")
treev.heading("7", text="2014")
treev.heading("8", text="2013")
treev.heading("9", text="2012")
treev.heading("10", text="2011")
treev.heading("11", text="2010")





# introducerea datelor in coloanele construite

treev.insert("", 'end', text="L1",
             values=("Capacitatea pt concerte", "2205", "2423",'2584','2589','2589','2688','2602','2908','2736','2786'))
treev.insert("", 'end', text="L2",
             values=("Nr angajati biblioteci", "255", "259",'261','274','226','226','218','221','232','0'))
treev.insert("", 'end', text="L3",
             values=("Nr colectii detinute de biblioteci","4085335", "4078630",'4222969','4439595','4421175','4494511','4336179','4310700','4041146','0'))
treev.insert("", 'end', text="L4",
             values=("Nr de biblioteci", "76", "82",'82','82','84','88','90','84','79','95'))
treev.insert("", 'end', text="L5",
             values=("Nr biblioteci publice", "1", "1",'1','1','1','1','1','1','1','1'))
treev.insert("", 'end', text="L6",
             values=("Nr de vizitatori muzee", "247204", "181935",'155855','144922','171777','173284','174760','161385','45401','74676'))
treev.insert("", 'end', text="L7",
             values=("Nr muzee", "9", "8",'9','9','9','9','9','10','11','11'))
treev.insert("", 'end', text="L8",
             values=("Nr personal muzee", "159", "143",'164','154','152','124','123','129','141','0'))
treev.insert("", 'end', text="L10",
             values=("Nr personal angajat din institutiile si companiile de spectacole", "826", "799",'792','788','788','776','741','743','762','0'))
treev.insert("", 'end', text="L11",
             values=("Nr spectatori in evenimente cultural/sociale cu vizibilitate internationala", "168108", "237553",'267113','253550','234265','228987','232132','191051','145245','115088'))
treev.insert("", 'end', text="L12",
             values=("Nr utilizatori activi in biblioteci", "80170", "85667",'93436','89764','90894','85777','82319','78114','76091','0'))
treev.insert("", 'end', text="L13",
             values=("Nr salilor de spectacole sau concerte", "0", "0",'8','8','8','8','8','7','7','8'))

# Calling mainloop
window.mainloop()



