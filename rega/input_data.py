import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import pymysql
import datetime
import time
from tkinter import messagebox


root = Tk()
class WindowDraggable():

        def __init__(self, label):
                self.label = label
                label.bind('<ButtonPress-1>', self.StartMove)
                label.bind('<ButtonRelease-1>', self.StopMove)
                label.bind('<B1-Motion>', self.OnMotion)

        def StartMove(self, event):
                self.x = event.x
                self.y = event.y

        def StopMove(self, event):
                self.x = None
                self.y = None

        def OnMotion(self,event):
                x = (event.x_root - self.x - self.label.winfo_rootx() + self.label.winfo_rootx())
                y = (event.y_root - self.y - self.label.winfo_rooty() + self.label.winfo_rooty())
                root.geometry("+%s+%s" % (x, y))
                
judul_kolom = ("Kode Barang","Nama Barang","Tanggal Beli","Jumlah Beli","Tanggal Terjual","Jumlah Terjual")
class Petugas:
        def __init__(self, parent):
                self.parent = parent
                self.parent.protocol("WM_DELETE_WINDOWS", self.keluar)
                lebar=650
                tinggi=500
                setTengahX = (self.parent.winfo_screenwidth()-lebar)//2
                setTengahY = (self.parent.winfo_screenheight()-tinggi)//2
                self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
                self.parent.overrideredirect(1)
                self.aturKomponen()
                # self.auto()
                
        def keluar(self,event=None):
                self.parent.destroy()
                
        def OnDoubleClick(self, event):
                # self.entKodeBarang.config(state="normal")
                self.entKodeBarang.delete(0, END)
                self.entNamaBarang.delete(0, END)
                self.entHariBeli.delete(0, END)
                self.entJumlahBeli.delete(0, END)
                self.entHariJual.delete(0, END)
                self.entJumlahJual.delete(0, END)
            
                it = self.trvTabel.selection()[0]
                ck = self.trvTabel.item(it,"values")[0]
                self.entKodeBarang.insert(END,ck)
                
                cKodeBarang = self.entKodeBarang.get()
                con = pymysql.connect(db="db_rega", user="root", passwd="", host="localhost", port=3306,autocommit=True)
                cur = con.cursor()
                sql = "SELECT nama_barang, tanggal_beli, jumlah_beli, tanggal_terjual, jumlah_terjual  FROM penjualan_barang WHERE kode_barang = %s"
                cur.execute(sql,cKodeBarang)
                data = cur.fetchone()

                
                # self.entKodeBarang.insert(END, data[0])
                self.entNamaBarang.insert(END, data[0])
                
                #TGL Beli
                self.entHariBeli.insert(END, data[1])
                cTglBeli = self.entHariBeli.get()
                
                pecahTahunBeli = str(cTglBeli[0]+cTglBeli[1]+cTglBeli[2]+cTglBeli[3])
                pecahBulanBeli = str(cTglBeli[5]+cTglBeli[6])
                pecahHariBeli = str(cTglBeli[8]+cTglBeli[9])
        
                self.entHariBeli.delete(0, END)
                self.entBulanBeli.delete(0, END)
                self.entTahunBeli.delete(0, END)
                self.entHariBeli.insert(END, pecahHariBeli)
                self.entBulanBeli.insert(END, pecahBulanBeli)
                self.entTahunBeli.insert(END, pecahTahunBeli)
                
                self.entJumlahBeli.insert(END, data[2])

                #TGL Jual
                self.entHariJual.insert(END, data[3])
                cTglJual = self.entHariJual.get()
                
                pecahTahunJual = str(cTglJual[0]+cTglJual[1]+cTglJual[2]+cTglJual[3])
                pecahBulanJual = str(cTglJual[5]+cTglJual[6])
                pecahHariJual = str(cTglJual[8]+cTglJual[9])
        
                self.entHariJual.delete(0, END)
                self.entBulanJual.delete(0, END)
                self.entTahunJual.delete(0, END)
                self.entHariJual.insert(END, pecahHariJual)
                self.entBulanJual.insert(END, pecahBulanJual)
                self.entTahunJual.insert(END, pecahTahunJual)

                self.entJumlahJual.insert(END, data[4])

                self.entKodeBarang.config(state="disable")
                self.btnSave.config(state="disable")
                self.btnUpdate.config(state="normal")
                self.btnDelete.config(state="normal")
                
        def aturKomponen(self):
                frameWin = Frame(self.parent, bg="#666")
                frameWin.pack(fill=X,side=TOP)
                WindowDraggable(frameWin)
                Label(frameWin, text='REGA',bg="#666",fg="white").pack(side=LEFT,padx=20)
                buttonx = Button(frameWin, text="X",fg="white", bg="#FA8072", width=6, height=2,bd=0,\
                                 activebackground="#FB8072",activeforeground="white", command=self.onClose, relief=FLAT)
                buttonx.pack(side=RIGHT)
                mainFrame = Frame(self.parent)
                mainFrame.pack(side=TOP,fill=X)
                btnFrame = Frame(self.parent)
                btnFrame.pack(side=TOP, fill=X)
                tabelFrame = Frame(self.parent)
                tabelFrame.pack( expand=YES, side=TOP,fill=Y)
       
                Label(mainFrame, text='  ').grid(row=0, column=0)
                Label(btnFrame, text='  ').grid(row=1, column=0)

                Label(mainFrame, text='Kode Barang').grid(row=1, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=1, column=1, sticky=W,pady=5,padx=10)
                self.entKodeBarang = Entry(mainFrame, width=20)
                self.entKodeBarang.grid(row=1, column=2,sticky=W)


                Label(mainFrame, text="Nama Barang").grid(row=2, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=2, column=1, sticky=W,pady=5,padx=10)
                self.entNamaBarang = Entry(mainFrame, width=30)
                self.entNamaBarang.grid(row=2, column=2,sticky=W)

                Label(mainFrame, text="Tanggal Beli").grid(row=3, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=3, column=1, sticky=W,pady=5,padx=10)

                #tgl Beli
                tglBeli = Frame(mainFrame)
                tglBeli.grid(row=3,column=2,sticky=W)
                self.entHariBeli = Entry(tglBeli, width=5)
                self.entHariBeli.grid(row=1, column=0,sticky=W)
                self.entBulanBeli = Entry(tglBeli, width=5)
                self.entBulanBeli.grid(row=1, column=1,sticky=W,padx=2)
                self.entTahunBeli = Entry(tglBeli, width=10)
                self.entTahunBeli.grid(row=1, column=2,sticky=W,padx=2)
                Label(tglBeli, text='(dd/mm/yyyy)').grid(row=1, column=3, sticky=E,padx=5)
                
                
                Label(mainFrame, text="Jumlah Beli").grid(row=4, column=0, sticky=NW,padx=20)
                Label(mainFrame, text=':').grid(row=4, column=1, sticky=NW,padx=10,pady=6)
                self.entJumlahBeli = Entry(mainFrame, width=30)
                self.entJumlahBeli.grid(row=4, column=2,sticky=W)

                Label(mainFrame, text="Tanggal Terjual").grid(row=5, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=3, column=1, sticky=W,pady=5,padx=10)

                #tgl Jual
                tglJual = Frame(mainFrame)
                tglJual.grid(row=5,column=2,sticky=W)
                self.entHariJual = Entry(tglJual, width=5)
                self.entHariJual.grid(row=1, column=0,sticky=W)
                self.entBulanJual = Entry(tglJual, width=5)
                self.entBulanJual.grid(row=1, column=1,sticky=W,padx=2)
                self.entTahunJual = Entry(tglJual, width=10)
                self.entTahunJual.grid(row=1, column=2,sticky=W,padx=2)
                Label(tglJual, text='(dd/mm/yyyy)').grid(row=1, column=3, sticky=E,padx=5)

                Label(mainFrame, text="Jumlah Terjual").grid(row=6, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=6, column=1, sticky=W,pady=5,padx=10)
                self.entJumlahJual = Entry(mainFrame, width=30)
                self.entJumlahJual.grid(row=6, column=2,sticky=W)


                self.btnSave = Button(
                        btnFrame, text='Save', command=self.onSave, width=10,
                        relief=FLAT, bd=2, bg="#666", fg="white",activebackground="#444",activeforeground="white" 
                )
                self.btnSave.grid(row=0, column=1,padx=5)

                self.btnUpdate = Button(
                        btnFrame, text='Update', command=self.onUpdate,state="disable", width=10,
                        relief=FLAT, bd=2, bg="#666", fg="white",activebackground="#444",activeforeground="white"
                )
                self.btnUpdate.grid(row=0,column=2,pady=10, padx=5)
                
                self.btnClear = Button(
                        btnFrame, text='Clear', command=self.onClear, width=10,
                        relief=FLAT, bd=2, bg="#666", fg="white",activebackground="#444",activeforeground="white"
                )
                self.btnClear.grid(row=0,column=3,pady=10, padx=5)

                self.btnDelete = Button(
                        btnFrame, text='Delete',
                        command=self.onDelete,state="disable", width=10,
                        relief=FLAT, bd=2, bg="#FC6042", fg="white",activebackground="#444",activeforeground="white"
                )
                self.btnDelete.grid(row=0,column=4,pady=10, padx=5)


                self.fr_data = Frame(tabelFrame, bd=10)
                self.fr_data.pack(fill=BOTH, expand=YES)
                self.trvTabel = ttk.Treeview(self.fr_data, columns=judul_kolom,show='headings')
                self.trvTabel.bind("<Double-1>", self.OnDoubleClick)
                sbVer = Scrollbar(self.fr_data, orient='vertical',command=self.trvTabel.yview)
                sbVer.pack(side=RIGHT, fill=Y)
                
                self.trvTabel.pack(side=TOP, fill=BOTH)
                self.trvTabel.configure(yscrollcommand=sbVer.set)
                self.table()
                
        def table(self):        
                con = pymysql.connect(db="db_rega", user="root", passwd="", host="localhost", port=3306,autocommit=True)
                cur = con.cursor()
                cur.execute("SELECT * FROM penjualan_barang")
                data_table = cur.fetchall()

                for kolom in judul_kolom:
                    self.trvTabel.heading(kolom,text=kolom)

                self.trvTabel.column("Kode Barang", width=100,anchor="w")
                self.trvTabel.column("Nama Barang", width=100,anchor="w")
                self.trvTabel.column("Tanggal Beli", width=100,anchor="w")
                self.trvTabel.column("Jumlah Beli", width=100,anchor="w")
                self.trvTabel.column("Tanggal Terjual", width=100,anchor="w")
                self.trvTabel.column("Jumlah Terjual", width=100,anchor="w")
            

                i=0
                for dat in data_table:
                    if(i%2):
                        baris="genap"
                    else:
                        baris="ganjil"
                    self.trvTabel.insert('', 'end', values=dat, tags=baris)
                    i+=1

                self.trvTabel.tag_configure("ganjil", background="#FFFFFF")
                self.trvTabel.tag_configure("genap", background="whitesmoke")
                cur.close()
                con.close()        
                       

        # def auto(self):
        #         con = pymysql.connect(db='db_rega', user='root', passwd='', host='localhost', port=3306,autocommit=True)
        #         cur = con.cursor()
        #         cuv = con.cursor()
        #         sqlkode = "SELECT max(kode_barang) FROM penjualan_barang"
        #         sql = "SELECT kode_barang FROM penjualan_barang"
        #         cur.execute(sqlkode)
        #         cuv.execute(sql)
        #         maxkode = cur.fetchone()
                
        #         if cuv.rowcount> 0:      
        #             autohit = int(maxkode[0])+1
        #             hits = "000"+str(autohit)
        #             if len(hits) == 4:
        #                 self.entKodeBarang.insert(0, hits)
        #                 self.entNamaBarang.focus_set()
        #             elif len(hits) == 5:
        #                 hit = "00"+str(autohit)
        #                 self.entKodeBarang.insert(0, hit)
        #                 self.entNamaBarang.focus_set()
        #             elif len(hits) == 6:
        #                 hit = "0"+str(autohit)
        #                 self.entKodeBarang.insert(0, hit)
        #                 self.entNamaBarang.focus_set()
        #             elif len(hits) == 7:
        #                 hit = ""+str(autohit)
        #                 self.entKodeBarang.insert(0, hit)
        #                 self.entNamaBarang.focus_set()
                    
        #             else:
        #                 messagebox.showwarning(title="Peringatan", \
        #                             message="maaf lebar data hanya sampai 4 digit")
                        
        #         else:
        #             hit = "0001"
        #             self.entKodeBarang.insert(0, hit)
        #             self.entNamaBarang.focus_set()
                    
        #         self.entKodeBarang.config(state="normal")

        def onClose(self, event=None):
                self.parent.destroy()


        def onDelete(self):
                con = pymysql.connect(db='db_rega', user='root', passwd='', host='localhost', port=3306,autocommit=True)
                cur = con.cursor()
                self.entKodeBarang.config(state="normal")
                cKodeBarang = self.entKodeBarang.get()
                sql = "DELETE FROM penjualan_barang WHERE kode_barang =%s"
                cur.execute(sql,cKodeBarang)
                self.onClear()
                messagebox.showinfo(title="Informasi", \
                                    message="Data sudah di hapus.")
                
                cur.close()
                con.close()


        def onClear(self):
                self.btnSave.config(state="normal")
                self.btnUpdate.config(state="disable")
                self.btnDelete.config(state="disable")
                self.entKodeBarang.config(state="normal")
                self.entKodeBarang.delete(0, END)
                self.entNamaBarang.delete(0, END)
                self.entHariBeli.delete(0, END)
                self.entBulanBeli.delete(0, END)
                self.entTahunBeli.delete(0, END)
                self.entJumlahBeli.delete(0, END)
                self.entBulanJual.delete(0, END)
                self.entTahunJual.delete(0, END)
                self.entHariJual.delete(0, END)
                self.entJumlahJual.delete(0, END)
                self.trvTabel.delete(*self.trvTabel.get_children())
                self.fr_data.after(0, self.table())
        
                # self.auto()
                self.entNamaBarang.focus_set()

                        
        def onSave(self):
        
                con = pymysql.connect(db='db_rega', user='root', passwd='', host='localhost', port=3306,autocommit=True)
 
                cKodeBarang = self.entKodeBarang.get()
                cNamaBarang = self.entNamaBarang.get()

                ####
                cHariBeli = self.entHariBeli.get()
                cBulanBeli = self.entBulanBeli.get()
                cTahunBeli = self.entTahunBeli.get()
                dTanggalBeli = datetime.date(int(cTahunBeli),int(cBulanBeli),int(cHariBeli))
                cJumlahBeli = self.entJumlahBeli.get()
                cHariJual = self.entHariJual.get()
                cBulanJual = self.entBulanJual.get()
                cTahunJual = self.entTahunJual.get()
                dTanggalJual = datetime.date(int(cTahunJual),int(cBulanJual),int(cHariBeli))
                cJumlahJual = self.entJumlahJual.get()
                if len(cHariBeli) == 0 and len(cBulanBeli) == 0 and len(cTahunBeli):
                        messagebox.showwarning(title="Peringatan",message="Tanggal Beli Tidak boleh kosong")    
                elif len(cHariJual) == 0 and len(cBulanJual) == 0 and len(cTahunJual):
                        messagebox.showwarning(title="Peringatan",message="Tanggal Terjual Tidak boleh kosong")
                else:
                        
                        cur = con.cursor()
                        sql = "INSERT INTO penjualan_barang (kode_barang,nama_barang, tanggal_beli, jumlah_beli,tanggal_terjual,jumlah_terjual)"+\
                              "VALUES(%s,%s,%s,%s,%s,%s)"
                        cur.execute(sql,(cKodeBarang,cNamaBarang,dTanggalBeli,cJumlahBeli,dTanggalJual,cJumlahJual))
                        self.onClear()
                        messagebox.showinfo(title="Informasi", \
                                            message="Data sudah di tersimpan.")
                        
                        cur.close()
                        con.close()
                
        def onUpdate(self):
                cKodeBarang = self.entKodeBarang.get()
                
                if len(cKodeBarang) == 0:
                        messagebox.showwarning(title="Peringatan",message="Kode kosong.")
                        self.entKodeBarang.focus_set()

                else:
                        con = pymysql.connect(db='db_rega', user='root', passwd='', host="localhost",\
                                      port=3306, autocommit=True)
                        cur = con.cursor()
                        cKodeBarang = self.entKodeBarang.get()
                        cNamaBarang = self.entNamaBarang.get()

                        ####
                        cHariBeli = self.entHariBeli.get()
                        cBulanBeli = self.entBulanBeli.get()
                        cTahunBeli = self.entTahunBeli.get()
                        dTanggalBeli = datetime.date(int(cTahunBeli),int(cBulanBeli),int(cHariBeli))
                        cJumlahBeli = self.entJumlahBeli.get()
                        cHariJual = self.entHariJual.get()
                        cBulanJual = self.entBulanJual.get()
                        cTahunJual = self.entTahunJual.get()
                        dTanggalJual = datetime.date(int(cTahunJual),int(cBulanJual),int(cHariJual))
                        cJumlahJual = self.entJumlahJual.get()
                        
                        sql = "UPDATE penjualan_barang SET nama_barang=%s, tanggal_beli=%s, jumlah_beli=%s,tanggal_terjual=%s,jumlah_terjual=%s WHERE kode_barang =%s"
                        cur.execute(sql,(cNamaBarang,dTanggalBeli,cJumlahBeli,dTanggalJual,cJumlahJual,cKodeBarang))
                        self.onClear()
                        messagebox.showinfo(title="Informasi", \
                                    message="Data sudah di terupdate.")

                        cur.close()
                        con.close()   
                     

def main():
    Petugas(root)
    root.mainloop()
main()