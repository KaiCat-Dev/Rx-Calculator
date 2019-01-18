from tkinter import *


def hasil(arg=None):
	fre = lblen.get()
	jarak = lbljaraken.get()
	wat = lblwaten.get()
	kabel = lblkabelen.get()
	db = lbldben.get()

	fsl = int(fre) + int(jarak) + float(36.6)

	eigrp = int(wat) + int(kabel) + int(db)

	rx = int(kabel) + int(db)

	what.config(text=fsl)
	what_dua.config(text=eigrp)
	what_tiga.config(text=rx)

window = Tk()
window.geometry("400x400")
window.title("welcome")
frame = Frame(window, bd=5) .grid(row=0, column=0)

lbljudul = Label(frame, text="Rx Caclculation", relief="groove") 
lbljudul.grid(row=2, column=2)

lblfre = Label(frame, text="Frekuensi") 
lblfre.grid(row=3, column=2)

lblen = Entry(frame, textvariable="Frekuensi") 
lblen.grid(row=3, column=3)

lbljarak = Label(frame, text="Jarak Antena") 
lbljarak.grid(row=4, column=2)

lbljaraken = Entry(frame, textvariable="Jarak Antena") 
lbljaraken.grid(row=4, column=3)

lblwat = Label(frame, text="mWatt") 
lblwat.grid(row=5, column=2)

lblwaten = Entry(frame, textvariable="mWatt") 
lblwaten.grid(row=5, column=3)

lblkabel = Label(frame, text="Panjang Kabel") 
lblkabel.grid(row=6, column=2)

lblkabelen = Entry(frame, textvariable="Panjang Kabel") 
lblkabelen.grid(row=6, column=3)

lbldb = Label(frame, text="Antena Db") 
lbldb.grid(row=7, column=2)

lbldben = Entry(frame, textvariable="Antena Db") 
lbldben.grid(row=7, column=3)

jumlah = Button(frame, text="Jumlah", command=hasil) 
jumlah.grid(row=8, column=4)

whatlbl = Label(frame, text="Free Space Loss")
whatlbl.grid(row=10, column=3)

what = Label(frame, text="") 
what.grid(row=11, column=3)

lblwhat = Label(frame, text="Eigrp")
lblwhat.grid(row=12, column=3)

what_dua = Label(frame, text="") 
what_dua.grid(row=13, column=3)

lblwhatwhat = Label(frame, text="Rx Power")
lblwhatwhat.grid(row=14, column=3)

what_tiga = Label(frame, text="") 
what_tiga.grid(row=15, column=3)

#c = main(window)
window.mainloop()