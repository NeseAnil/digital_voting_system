from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
from PIL import ImageTk,Image 

conn = sqlite3.connect("C:/Users/Anil/Documents/GUI_tkinter/project/db.db", timeout=10)
c = conn.cursor()

date = datetime.datetime.now().date()

class Application:


	def __init__(self, master, *args, **kwargs):
		
		self.master = master
		self.left = Frame(master, width=1920, height=1080)
		self.left.pack(side=LEFT)
		
		self.right = Frame(master, width=0, height=0)
		self.right.pack(side=LEFT)

		self.my=ImageTk.PhotoImage(Image.open("img3.jpg"))
		self.label=Label(image=self.my)
		self.label.pack()


		self.heading = Label(self.left, text="Welcome to Digital Voting ! ", font=("Comic Sans MS",70),fg="brown")
		self.heading.place(x=150, y=50)

		self.heading = Label(self.left, text="Login as", font=("Comic Sans MS",60),fg="blue")
		self.heading.place(x=430, y=250)	
		
		self.upd=Button(master,text="Admin",font=("Comic Sans MS",18),bg="green",width="12",command=self.loginad)	
		self.upd.place(x=600,y=400)

		self.view=Button(master,text="Voter",font=("Comic Sans MS",18),bg="green",width="12",command=self.loginvo)
		self.view.place(x=600,y=475)

		self.view=Button(master,text="Candidate",font=("Comic Sans MS",18),bg="green",width="12",command=self.loginca)
		self.view.place(x=600,y=550)

		self.view=Button(master,text="Result",font=("Comic Sans MS",18),bg="orange",width="12",command=self.winnerone)
		self.view.place(x=600,y=700)

		self.heading = Label(self.left, text="Check out for results --> ", font=("Comic Sans MS",30),fg="brown")
		self.heading.place(x=80, y=700)




	def voterAdding(self, *args, **kwargs):

		screen1=Toplevel()
		screen1.geometry("1000x1000")
		screen1.title("ONLINE VOTING SYSTEM - VOTER")
		self.heading = Label(screen1, text="Add to the database", font=("Comic Sans MS",40), fg='brown')

		self.heading.place(x=280,y=10)

		self.name_l = Label(screen1, text="Enter voter Name", font=("Comic Sans MS",18))
		self.name_l.place(x=30, y=130)

		self.id_l = Label(screen1, text="Enter voter id", font=("Comic Sans MS",18))
		self.id_l.place(x=30, y=180)

		#self.cid_l = Label(screen1, text="Enter candidate to vote for", font=("Comic Sans MS",18))
		#self.cid_l.place(x=30, y=230)

		self.city_l = Label(screen1, text="Enter voter city", font=("Comic Sans MS",18))
		self.city_l.place(x=30, y=230)

		self.age_l = Label(screen1, text="Enter age", font=("Comic Sans MS",18))
		self.age_l.place(x=30, y=280)


		self.cid_p = Label(screen1, text="Password", font=("Comic Sans MS",18))
		self.cid_p.place(x=30, y=330)


		self.name_e = Entry(screen1, width=25, font=("Comic Sans MS",18))
		self.name_e.place(x=380, y=130)

		self.id_e = Entry(screen1, width=25, font=("Comic Sans MS",18))
		self.id_e.place(x=380, y=180)

		#self.cid_e = Entry(screen1, width=25, font=("Comic Sans MS",18))
		#self.cid_e.place(x=380, y=230)

		self.city_e = Entry(screen1, width=25, font=("Comic Sans MS",18))
		self.city_e.place(x=380, y=230)

		self.age_e = Entry(screen1, width=25, font=("Comic Sans MS",18))
		self.age_e.place(x=380, y=280)

		self.cid_pe = Entry(screen1, width=25, font=("Comic Sans MS",18))
		self.cid_pe.place(x=380, y=330)

		

		self.btn_add = Button(screen1, text="  Add To Database", font=("Comic Sans MS",16),width=25, height=1, bg='steelblue', fg='white', command=self.get_itemsV)
		self.btn_add.place(x=470, y=450)

		self.btn_clear = Button(screen1, text="Clear All Fields", font=("Comic Sans MS",16),width=18, height=1, bg='green', fg='white', command=self.clear_allV)
		self.btn_clear.place(x=280, y=450)

		#self.master.bind('<Return>', self.get_itemsV)
		#self.master.bind('<Up>', self.clear_allV)

	def get_itemsV(self, *args, **kwargs):
	
		self.name = self.name_e.get()
		self.id = self.id_e.get()
		self.city= self.city_e.get()
		self.age = self.age_e.get()
		self.pas=self.cid_pe.get()
	   

		if self.name == '' or self.id == '' or self.city== '' or self.age=='':
			tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")
		else:
			if int(self.age) <18 or int(self.age) >120:
				tkinter.messagebox.showinfo("error","invalid User-(Age should be between 18 and 120)")
			else:
				self.k="didntcaste"		
				sql = "INSERT INTO voters (name,status, voterID, city, age,password) VALUES(?,?,?,?,?,?)"
				c.execute(sql, (self.name,self.k,self.id,self.city, self.age,self.pas))
				conn.commit()
				tkinter.messagebox.showinfo("Success", "Successfully added to the database")

	def clear_allV(self, *args, **kwargs):
		self.name_e.delete(0, END)
		self.id_e.delete(0, END)
		self.city_e.delete(0, END)
		self.age_e.delete(0, END)
		

	def candidateAdding(self, *args, **kwargs):
		#print("hi2")
		#result = c.execute("SELECT Max(candidatesID) from candidates")
		#for r in result:
			#candidateID= r[0]
		screen2=Toplevel()
		screen2.geometry("1000x1000")
		screen2.title("ONLINE VOTING SYSTEM - CANDIDATE")

		self.heading = Label(screen2, text="Add to the database", font=("Comic Sans MS",40), fg='brown')
		self.heading.place(x=280, y=10)

		self.name_l = Label(screen2, text="Enter candidate Name", font=("Comic Sans MS",18))
		self.name_l.place(x=30, y=130)

		self.id_l = Label(screen2, text="Enter candidate id", font=("Comic Sans MS",18))
		self.id_l.place(x=30, y=180)

		self.sym_l = Label(screen2, text="Enter symbol", font=("Comic Sans MS",18))
		self.sym_l.place(x=30, y=230)

		self.city_l = Label(screen2, text="Enter candidate city", font=("Comic Sans MS",18))
		self.city_l.place(x=30, y=280)

		self.age_l = Label(screen2, text="Enter age", font=("Comic Sans MS",18))
		self.age_l.place(x=30, y=330)

		self.name_e = Entry(screen2, width=25, font=("Comic Sans MS",18))
		self.name_e.place(x=380, y=130)

		self.id_e = Entry(screen2, width=25, font=("Comic Sans MS",18))
		self.id_e.place(x=380, y=180)

		self.sym_e = Entry(screen2, width=25, font=("Comic Sans MS",18))
		self.sym_e.place(x=380, y=230)

		self.city_e = Entry(screen2, width=25, font=("Comic Sans MS",18))
		self.city_e.place(x=380, y=280)

		self.age_e = Entry(screen2, width=25, font=("Comic Sans MS",18))
		self.age_e.place(x=380, y=330)

		self.btn_add = Button(screen2, text="Add To Database",font=("Comic Sans MS",16), width=25, height=1, bg='steelblue', fg='white', command=self.get_itemsC)
		self.btn_add.place(x=470, y=450)

		self.btn_clear = Button(screen2, text="Clear All Fields",font=("Comic Sans MS",16), width=18, height=1, bg='green', fg='white', command=self.clear_allC)
		self.btn_clear.place(x=280, y=450)

		#self.tBox = Text(screen2, width=60, height=18)
		#self.tBox.place(x=750, y=70)
		#self.tBox.insert(END, "ID has reached upto: " + str(candidateID))

		self.master.bind('<Return>', self.get_itemsC)
		self.master.bind('<Up>', self.clear_allC)

	def get_itemsC(self, *args, **kwargs):

		self.name = self.name_e.get()
		self.id = self.id_e.get()
		self.symbol = self.sym_e.get()
		self.city= self.city_e.get()
		self.age = self.age_e.get()

		if self.name == '' or self.id == '' or self.symbol == '' or self.city== '' or self.age== '':
			tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")
		#else:
											#if int(self.age) <18 or int(self.age) >120:
												#tkinter.messagebox.showinfo("error","invalid User-(Age should be between 18 and 120)")
		
		else:
			try:
				sql = "INSERT INTO candidates (candidatesID,name,city,age,symbol) VALUES(?,?,?,?,?)"
				c.execute(sql, (self.id, self.name, self.city, self.age, self.symbol))
				conn.commit()
				tkinter.messagebox.showinfo("Success", "Successfully added to the database")
			except:
				tkinter.messagebox.showinfo("error!", "Candidate id should be > 0")


	def clear_allC(self, *args, **kwargs):

		self.name_e.delete(0, END)
		self.id_e.delete(0, END)
		self.sym_e.delete(0, END)
		self.city_e.delete(0, END)
		self.age_e.delete(0, END)

	def updating(self, *args, **kwargs):

		#result = c.execute("SELECT Max(voterID) from voters")
		#for r in result:
			#id = r[0]
		self.screen3=Toplevel()
		self.screen3.geometry("1000x1000")
		self.screen3.title("ONLINE VOTING SYSTEM - UPDATION")

		self.heading = Label(self.screen3, text="Update the database", font=("Comic Sans MS",40), fg='steelblue')
		self.heading.place(x=350, y=0)


		self.id_le = Label(self.screen3, text="Enter Id", font=("Comic Sans MS",18))
		self.id_le.place(x=0, y=70)

		self.id_leb = Entry(self.screen3, font=("Comic Sans MS",18) ,width=10)
		self.id_leb.place(x=380, y=70)

		self.btn_search = Button(self.screen3, text="Search", width=15, height=2, bg='orange', command=self.search)
		self.btn_search.place(x=550, y=70)
		# labels  for the window
		self.name_l = Label(self.screen3, text="Enter voter Name", font=("Comic Sans MS",18))
		self.name_l.place(x=0, y=120)

		self.id_l = Label(self.screen3, text="Enter voters id", font=("Comic Sans MS",18))
		self.id_l.place(x=0, y=170)

		self.cid_l = Label(self.screen3, text="Enter votedID ", font=("Comic Sans MS",18))
		self.cid_l.place(x=0, y=220)

		self.city_l = Label(self.screen3, text="Enter city", font=("Comic Sans MS",18))
		self.city_l.place(x=0, y=270)

		self.age_l = Label(self.screen3, text="Enter age", font=("Comic Sans MS",18))
		self.age_l.place(x=0, y=320)

		self.name_e = Entry(self.screen3, width=25, font=("Comic Sans MS",18))
		self.name_e.place(x=380, y=120)

		self.id_e = Entry(self.screen3, width=25, font=("Comic Sans MS",18))
		self.id_e.place(x=380, y=170)

		self.cid_e = Entry(self.screen3, width=25, font=("Comic Sans MS",18))
		self.cid_e.place(x=380, y=220)

		self.city_e = Entry(self.screen3, width=25, font=("Comic Sans MS",18))
		self.city_e.place(x=380, y=270)

		self.age_e = Entry(self.screen3, width=25, font=("Comic Sans MS",18))
		self.age_e.place(x=380, y=320)

		

	def search(self, *args, **kwargs):
		d = self.id_leb.get()
		sql = "SELECT * FROM voters WHERE voterID=?"
		aa = c.execute(sql,(d,))
		
		conn.commit()
		for r in aa:
			print("hhhhhhhhhhh")
			self.n1 = r[0] #name
			self.n2 = r[1] #votedTO
			self.n3 = r[2] #voterId
			self.n4 = r[3] #city
			self.n5 = r[4] #age
			

		# insert into the entries to update
		self.name_e.delete(0, END)
		self.name_e.insert(0, str(self.n1))
		# print(self.n1)
		# print(self.n2)
		# print(self.n3)
		# print(self.n4)

		self.id_e.delete(0, END)
		self.id_e.insert(0, str(self.n3))

		self.cid_e.delete(0, END)
		self.cid_e.insert(0, str(self.n2))

		self.city_e.delete(0, END)
		self.city_e.insert(0, str(self.n4))

		self.age_e.delete(0, END)
		self.age_e.insert(0, str(self.n5))

		

		self.btn_add = Button(self.screen3, text="Update Database", width=25, height=2, bg='steelblue', fg='white', command=self.update)
		self.btn_add.place(x=520, y=520)

		self.btn_clear = Button(self.screen3, text="Clear All Fields", width=18, height=2, bg='lightgreen', fg='white',command=self.clear_allU)
		self.btn_clear.place(x=350, y=520)

	def update(self, *args, **kwargs):
		try:
			self.u1 = self.name_e.get()
			self.u2 = self.id_e.get()
			self.u3 = self.cid_e.get()
			self.u4 = self.city_e.get()
			self.u5 = self.age_e.get()
			

			query = "UPDATE voters SET name=?, voterID=?, city=?, votedTo=?, age=? WHERE voterID=?"
			c.execute(query, (self.u1, self.u2, self.u4, self.u3, self.u5, self.id_leb.get()))
			conn.commit()
			tkinter.messagebox.showinfo("Success", "Successfully Updated database")
			
			self.name_e.delete(0, END)
			self.id_e.delete(0, END)
			self.cid_e.delete(0, END)
			self.city_e.delete(0, END)
			self.age_e.delete(0, END)

			self.btn_add.destroy()
			self.btn_clear.destroy()
		except Exception as e:
			print(e)
			tkinter.messagebox.showinfo("Oopsss!!!","Change of stocks is mandatory.")
		# get all the updated values
		

	def clear_allU(self, *args, **kwargs):
		#delete all 
		self.name_e.delete(0, END)
		self.id_e.delete(0, END)
		self.cid_e.delete(0, END)
		self.city_e.delete(0, END)
		self.age_e.delete(0, END)
		

		self.btn_add.destroy()
		self.btn_clear.destroy()

		self.name = self.u1
		self.id = self.u2

		# insert into the transaction
		sql2 = "INSERT INTO Updated_info (voter_name, id, date) VALUES (?, ?, ?)"
		c.execute(sql2, (self.name,self.id, date))
		conn.commit()

	def viewInfo(self, *args, **kwargs):
		self.screen4=Toplevel()
		self.screen4.geometry("1920x1080")
		self.screen4.title("ONLINE VOTING SYSTEM - view information")

		self.heading = Label(self.screen4, text="Candidates Info", font=("Comic Sans MS",60), fg='brown')
		self.heading.place(x=450, y=0)

		self.querry="SELECT * from candidates"#wish to display entire table
		self.res=c.execute(self.querry)
		
		self.length=30
		self.breadth=130
		for r in self.res:
			
				#Label(self.screen4,text="Candidate_ID:"+str(r[1]),font=("Comic Sans MS",18,"bold"),fg='green').place(x=self.length,y=self.breadth+50)
				  
				Label(self.screen4,text=" "+str(r[0])+"  "+" Symbol-"+str(r[4]),font=("Comic Sans MS",18),fg='blue').place(x=self.length,y=self.breadth)
		
				#Label(self.screen4,text="Candidate_city:"+str(r[2]),font=("Comic Sans MS",18),fg='blue').place(x=self.length,y=self.breadth+150)
				
				#Label(self.screen4,text="Candidate_age:"+str(r[3]),font=("Comic Sans MS",18),fg='blue').place(x=self.length,y=self.breadth+200)
				
				#Label(self.screen4,text="Candidate_symbol:"+str(r[4]),font=("Comic Sans MS",18),fg='blue').place(x=self.length,y=self.breadth+250)
				self.breadth=self.breadth+50
				#print("hi")
		conn.commit()
		#self.btnToWin=Button(self.screen4,text="Know The Winner",font=("Comic Sans MS",15),bg="green",width="40",height=2,command=self.whoIsWinner)
		#self.btnToWin.place(x=450,y=500)

	def whoIsWinner(self, *args, **kwargs):
		self.screen5=Toplevel()
		self.screen5.geometry("1920x1080")
		self.screen5.title("who is the winner ?")

		self.heading = Label(self.screen5, text="Voting Result", font=("Comic Sans MS",80), fg='brown')
		self.heading.place(x=400, y=100)

		self.querry="select max(vt) as vt2 from (Select vote as vt,max(ans) as ans1 from (SELECT votedTo as vote, count(votedTo) as ans FROM voters as grps GROUP by votedTo))"
		
		self.result=c.execute(self.querry)
		
		for r in self.result:
			print(r[0])
		self.ans=(r[0])
		print(self.ans)

		querryN="SELECT name FROM candidates WHERE candidatesID=?"
		self.aaja = c.execute(querryN,(self.ans,))
		for l in self.aaja:
			self.aaaa = l[0]
		self.winner=Label(self.screen5,text="winner is "+str(self.aaaa),font=("Comic Sans MS",80,"bold"),fg='green')
		self.winner.place(x=330,y=400)

	def admin(self,*args, **kwargs):

		self.screen6=Toplevel()
		self.screen6.geometry("1920x1080")
		self.screen6.title("ONLINE VOTING SYSTEM - VOTER")
		
		
		self.heading = Label(self.screen6, text="    Admin", font=("Comic Sans MS",90),fg="brown")
		self.heading.place(x=310, y=10)

		self.date_l = Label(self.screen6, text=" Date: " + str(date), font=("Comic Sans MS",20), fg='blue')
		self.date_l.place(x=1200, y=17)
		 
		self.vadd=Button(self.screen6,text="Add Voter",font=("Comic Sans MS",18),bg="green",fg="yellow",width="17",command=self.voterAdding)
		self.vadd.place(x=500,y=250)

		self.cadd=Button(self.screen6,text="Add  Candidate",font=("Comic Sans MS",18),bg="green",fg="yellow",width="17",command=self.candidateAdding)
		self.cadd.place(x=500,y=325)
		
		self.upd=Button(self.screen6,text="Update Voter",font=("Comic Sans MS",18),bg="green",fg="yellow",width="17",command=self.updating)
		self.upd.place(x=500,y=400)

		self.upd=Button(self.screen6,text="Update candidate",font=("Comic Sans MS",18),bg="green",fg="yellow",width="17",command=self.updatingC)
		self.upd.place(x=500,y=475)

		self.view=Button(self.screen6,text="Candidates Info",font=("Comic Sans MS",18),bg="green",fg="yellow",width="17",command=self.candidate)
		self.view.place(x=500,y=550)

		#self.view=Button(self.screen6,text="Know The Winner",font=("Comic Sans MS",18),bg="green",width="20",command=self.whoIsWinner)
		#self.view.place(x=500,y=625)

		self.view=Button(self.screen6,text="Exit",font=("Comic Sans MS",18),bg="red",width="6",command=self.screen6.quit)
		self.view.place(x=1400,y=725)

	def updatingC(self, *args, **kwargs):

		self.screen8=Toplevel()
		self.screen8.geometry("1920x1080")
		self.screen8.title("ONLINE VOTING SYSTEM - UPDATION")

		self.heading = Label(self.screen8, text="Update the database(Candidate)", font=("Comic Sans MS",40), fg='steelblue')
		self.heading.place(x=350, y=0)
		self.id_cid = Label(self.screen8, text="Enter Id", font=("Comic Sans MS",18))
		self.id_cid.place(x=0, y=70)
		self.btn_searchc = Button(self.screen8, text="Search", width=15, height=2, bg='orange', command=self.searchc)
		self.btn_searchc.place(x=550, y=70)
		self.id_lebc = Entry(self.screen8, width=15, font=("Comic Sans MS",18))
		self.id_lebc.place(x=170, y=70)
		
		

		self.name_cname = Label(self.screen8, text="Enter candidate ", font=("Comic Sans MS",18))
		self.name_cname.place(x=0, y=120)

		self.name_cname = Label(self.screen8, text="Enter candidateID ", font=("Comic Sans MS",18))
		self.name_cname.place(x=0, y=170)
		
		self.id_csym = Label(self.screen8, text="Enter Symbol", font=("Comic Sans MS",18))
		self.id_csym.place(x=0, y=230)

		self.cid_cc = Label(self.screen8, text="Enter Candidate City ", font=("Comic Sans MS",18))
		self.cid_cc.place(x=0, y=280)

		self.city_cage = Label(self.screen8, text="Enter age", font=("Comic Sans MS",18))
		self.city_cage.place(x=0, y=320)



		self.cname_e = Entry(self.screen8, width=25, font=("Comic Sans MS",18))
		self.cname_e.place(x=380, y=120)

		self.cide = Entry(self.screen8, width=25, font=("Comic Sans MS",18))
		self.cide.place(x=380, y=170)

		self.csyme = Entry(self.screen8, width=25, font=("Comic Sans MS",18))
		self.csyme.place(x=380, y=220)

		self.cid_cce = Entry(self.screen8, width=25, font=("Comic Sans MS",18))
		self.cid_cce.place(x=380, y=270)

		self.city_cagee = Entry(self.screen8, width=25, font=("Comic Sans MS",18))
		self.city_cagee.place(x=380, y=320)


	def searchc(self, *args, **kwargs):
		dd = self.id_lebc.get()
		sql2 = "SELECT * FROM candidates WHERE candidatesID=?"
		aaa = c.execute(sql2,(dd,))
		conn.commit()
		
		for r in aaa:
			self.n1 = r[1] #name
			self.n2 = r[2] #city
			self.n3 = r[3] #age
			self.n4 = r[4] #symbol
			self.n5 = r[0] #cid

			#print(self.r[0])
			#print(self.r[1])
			#print(self.r[2])
			#print(self.r[3])
			#print(self.r[4])
			

		# insert into the entries to update
		self.cname_e.delete(0, END)
		self.cname_e.insert(0, str(self.n1))	

		self.csyme.delete(0, END)
		self.csyme.insert(0, str(self.n4))

		self.cid_cce.delete(0, END)
		self.cid_cce.insert(0, str(self.n2))

		self.city_cagee.delete(0, END)
		self.city_cagee.insert(0, str(self.n3))

		self.cide.delete(0, END)
		self.cide.insert(0, str(self.n5))

		

		self.btn_add = Button(self.screen8, text="Update Database", width=25, height=2, bg='steelblue', fg='white', command=self.updatec)
		self.btn_add.place(x=520, y=520)

		self.btn_clear = Button(self.screen8, text="Clear All Fields", width=18, height=2, bg='lightgreen', fg='white')
		self.btn_clear.place(x=350, y=520)
	
	def updatec(self, *args, **kwargs):
		try:
			self.u1 = self.cname_e.get()
			self.u2 = self.csyme.get()
			self.u3 = self.cid_cce.get()
			self.u4 = self.city_cagee.get()
			self.u5 = self.cide.get()

			
			

			query = "UPDATE candidates SET name=?, candidatesID=?, symbol=?, age=?,city=? WHERE candidatesID=?"
			c.execute(query, (self.u1, self.u5, self.u2, self.u4, self.u3, self.id_lebc.get()))
			conn.commit()
			tkinter.messagebox.showinfo("Success", "Successfully Updated database")
			
			self.cname_e.delete(0, END)
			self.csyme.delete(0, END)
			self.cid_cce.delete(0, END)
			self.city_cagee.delete(0, END)
			self.cide.delete(0, END)

			self.btn_add.destroy()
			self.btn_clear.destroy()
		except Exception as e:
			print(e)
			tkinter.messagebox.showinfo("Oopsss!!! something went wrong")


	def votercaste(self, *args, **kwargs):

		self.screen9=Toplevel()
		self.screen9.geometry("1920x1080")
		self.screen9.title("ONLINE VOTING SYSTEM -Casting Vote")

		self.heading = Label(self.screen9, text="Caste Vote", font=("Comic Sans MS",40), fg='brown')
		self.heading.place(x=280,y=10)
		
		self.querry="SELECT * from candidates"#wish to display entire table
		self.res=c.execute(self.querry)
		
		self.length=30
		self.breadth=130
		for r in self.res:
			
				Label(self.screen9,text=" "+str(r[0])+"   "+" - " +str(r[1]) +"                    "+ "Symbol:"+str(r[4]),font=("Comic Sans MS",18),fg='blue').place(x=self.length,y=self.breadth)
				self.breadth=self.breadth+50
				
		conn.commit()


		
		self.heading = Label(self.screen9, text=" Enter Candidate ID", font=("Comic Sans MS",20), fg='brown')
		self.heading.place(x=50,y=500)

		self.cid_mm = Entry(self.screen9, width=25, font=("Comic Sans MS",20))
		self.cid_mm.place(x=380, y=500)

		

		self.btn_clear = Button(self.screen9, text="Caste Vote", width=18, height=1, bg='green',font=("Comic Sans MS",20), fg='black',command=self.votercaste22)
		self.btn_clear.place(x=400, y=580)

		#self.btn_clear = Button(self.screen9, text=" Results ", width=18, height=2, bg='green', fg='black',command=self.winnerone)
		#self.btn_clear.place(x=600, y=580)






	def votercaste22(self, *args, **kwargs):

		self.lk = self.cid_mm.get()

		if self.lk == "":
			tkinter.messagebox.showinfo("Error", "Please Fill  the Entry.")

		else:
			#flag=0
			result=c.execute('select candidatesID from candidates')
			for r in result:
				if(int(r[0])==self.lk):
					flag=1
					sql = "INSERT INTO  votedinfo (candidateid) VALUES(?)"
					c.execute(sql, (self.lk,))
					conn.commit()
					tkinter.messagebox.showinfo("Success", "Successfully Voted - Thank you :)")
			#if flag==0:
				#tkinter.messagebox.showinfo("error!", "candidate is not present")




	def winnerone(self, *args, **kwargs):
		self.screen10=Toplevel()
		self.screen10.geometry("1920x1080")
		self.screen10.title("who is the winner ?")

		self.heading = Label(self.screen10, text="Voting Result !!!", font=("Comic Sans MS",80), fg='brown')
		self.heading.place(x=400, y=100)

		self.querry="select max(vt) as vt2 from (Select vote as vt,max(ans) as ans1 from (SELECT candidateid as vote, count(candidateid) as ans FROM votedinfo as grps GROUP by candidateid))"
		
		self.result=c.execute(self.querry)
		
		for r in self.result:
			print(r[0])
		self.ans=(r[0])
		print(self.ans)

		querryN="SELECT name FROM candidates WHERE candidatesID=?"
		self.aaja = c.execute(querryN,(self.ans,))
		for l in self.aaja:
			self.aaaa = l[0]
		self.winner=Label(self.screen10,text="Winner is "+str(self.aaaa),font=("Comic Sans MS",80,"bold"),fg='green')
		self.winner.place(x=330,y=400)

		self.winner2=Label(self.screen10,text="Symbol : Sword",font=("Comic Sans MS",40,"bold"),fg='green')
		self.winner2.place(x=600,y=550)




	def candidate(self, *args, **kwargs):
		self.screen11=Toplevel()
		self.screen11.geometry("1920x1080")
		self.screen11.title("ONLINE VOTING SYSTEM -Casting Vote")

		self.heading = Label(self.screen11, text=" Candidate Information ", font=("Comic Sans MS",40), fg='brown')
		self.heading.place(x=280,y=10)
		
		self.querry="SELECT * from candidates"#wish to display entire table
		self.res=c.execute(self.querry)
		
		self.length=30
		self.breadth=200
		for r in self.res:
			
				Label(self.screen11,text=" "+str(r[0])+"   "+" - " +str(r[1]) +"                    "+ "Symbol:"+str(r[4]),font=("Comic Sans MS",18),fg='blue').place(x=self.length,y=self.breadth)
				self.breadth=self.breadth+50
				
		conn.commit()


	def loginad(self, *args, **kwargs):	

		self.screen12=Toplevel()
		self.screen12.geometry("1920x1080")
		self.screen12.title("ONLINE VOTING SYSTEM - Login Admin")


		self.heading = Label(self.screen12, text=" Login Admin", font=("Comic Sans MS",70), fg='brown')
		self.heading.place(x=280,y=10)

		self.sym_l = Label(self.screen12, text="Enter Admin id", font=("Comic Sans MS",23))
		self.sym_l.place(x=30, y=230)

		self.city_l = Label(self.screen12, text="Enter Password", font=("Comic Sans MS",23))
		self.city_l.place(x=30, y=350)

		self.city_e = Entry(self.screen12, width=25, font=("Comic Sans MS",23))
		self.city_e.place(x=380, y=230)

		self.age_e = Entry(self.screen12, width=25, font=("Comic Sans MS",23))		
		self.age_e.place(x=380, y=350)


		self.btn_clear = Button(self.screen12, text="Continue", width=14, height=1,font=("Comic Sans MS",18), bg='green',command=self.continue1)
		self.btn_clear.place(x=450, y=520)



	def continue1(self, *args, **kwargs):

		self.id=self.city_e.get()
		self.passw=self.age_e.get()


		sql="SELECT * FROM admin where id=? and password=?"
		result=c.execute(sql,(self.id,self.passw, ))
		conn.commit()

		a=[]
		for self.r in result:
			self.getid=self.r[0]
			a.append(self.getid)
			print(a)
		if self.id == ''or self.passw == '':

			tkinter.messagebox.showinfo("Error", "Please fill the entries")
			
		else:

			if(len(a)>0):
			
				self.admin()

			else:
			
				tkinter.messagebox.showinfo("Error", "INVALID ID OR PASSWORD")


	def loginvo(self, *args, **kwargs):	

		self.screen13=Toplevel()
		self.screen13.geometry("1920x1080")
		self.screen13.title("ONLINE VOTING SYSTEM - Login voter")


		self.heading = Label(self.screen13, text=" Login Voter", font=("Comic Sans MS",70), fg='brown')
		self.heading.place(x=280,y=10)

		self.sym_l = Label(self.screen13, text="Enter Voter id", font=("Comic Sans MS",23))
		self.sym_l.place(x=30, y=230)

		self.city_l = Label(self.screen13, text="Enter Password", font=("Comic Sans MS",23))
		self.city_l.place(x=30, y=350)

		self.city_e = Entry(self.screen13, width=25, font=("Comic Sans MS",23))
		self.city_e.place(x=380, y=230)

		self.age_e = Entry(self.screen13, width=25, font=("Comic Sans MS",23))		
		self.age_e.place(x=380, y=350)


		self.btn_clear = Button(self.screen13, text="Continue", width=14, height=1,font=("Comic Sans MS",18), bg='green',command=self.continue2)
		self.btn_clear.place(x=450, y=520)



	def continue2(self, *args, **kwargs):

		self.id=self.city_e.get()
		self.passw=self.age_e.get()


		sql="SELECT * FROM voters where voterID=? and password=?"
		result=c.execute(sql,(self.id,self.passw, ))
		conn.commit()

		a=[]
		for self.r in result:
			self.getid=self.r[0]
			self.statuss=self.r[1]
			print(self.statuss)
			a.append(self.getid)
			print(a)


		if self.id == ''or self.passw == '':

				tkinter.messagebox.showinfo("Error", "Please fill the entries")
			

		else:

				if(len(a)>0):

					self.statuss="casted"

					sql = "update voters set status = ? where voterID = ? and password = ?"
					c.execute(sql, (self.statuss,self.id,self.passw, ))

					conn.commit()

					self.votercaste()

				else:
					tkinter.messagebox.showinfo("Error", "Vote has been Casted")
					
			
	def loginca(self, *args, **kwargs):	

		self.screen14=Toplevel()
		self.screen14.geometry("1920x1080")
		self.screen14.title("ONLINE VOTING SYSTEM - Login Candidate")


		self.heading = Label(self.screen14, text=" Login Candidate", font=("Comic Sans MS",70), fg='brown')
		self.heading.place(x=280,y=10)

		self.sym_l = Label(self.screen14, text="Enter Candidate id", font=("Comic Sans MS",23))
		self.sym_l.place(x=30, y=230)

		self.city_l = Label(self.screen14, text="Enter Password", font=("Comic Sans MS",23))
		self.city_l.place(x=30, y=350)

		self.city_e = Entry(self.screen14, width=25, font=("Comic Sans MS",23))
		self.city_e.place(x=380, y=230)

		self.age_e = Entry(self.screen14, width=25, font=("Comic Sans MS",23))		
		self.age_e.place(x=380, y=350)


		self.btn_clear = Button(self.screen14, text="Continue", width=14, height=1,font=("Comic Sans MS",18), bg='green',command=self.continue3)
		self.btn_clear.place(x=450, y=520)
	
	def continue3(self, *args, **kwargs):

		self.id=self.city_e.get()
		self.passw=self.age_e.get()


		sql="SELECT * FROM candidates where candidatesID=? and password=?"
		result=c.execute(sql,(self.id,self.passw, ))
		conn.commit()

		a=[]
		for self.r in result:
			self.getid=self.r[0]
			a.append(self.getid)
			print(a)
		if self.id == ''or self.passw == '':

			tkinter.messagebox.showinfo("Error", "Please fill the entries")
			

		else:

			if(len(a)>0):
			
				self.candidate()

			else:
			
				tkinter.messagebox.showinfo("Error", "INVALID ID OR PASSWORD")



root = Tk()
b = Application(root)

root.geometry("1920x1080+0+0")
root.title("ONLINE VOTING")
root.mainloop()




