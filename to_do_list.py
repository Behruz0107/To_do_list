from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import json
import os



class project(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setMaximumSize(700,800)
		self.setMinimumSize(700,800)
		self.setGeometry(400,100,700,800)
		self.setStyleSheet(""" background-color: rbg(0,255,255);
			color: rbg(199,21,133);""")
		self.setWindowTitle('Vazifa')


		self.lb=QPushButton("Vazifa qo'shish",self)
		self.lb.setGeometry(120,140,400,80)
		self.lb.setFont(QFont('Poor Richard',24))
		self.lb.setStyleSheet(""" background-color: rgb(128,128,128);
						color: rgb(0,0,0);
						border-color: rgb(0,128,128);
						border-radius: 10px;
						border-style: solid;
						border-width:2px;
						font-size:30;
						font-family: SF PRO; """)

		self.lb.clicked.connect(self.add_work)




		self.lb1=QPushButton("Vazifalarni ko'rish",self)
		self.lb1.setGeometry(120,250,400,80)
		self.lb1.setFont(QFont('Poor Richard',24))
		self.lb1.setStyleSheet(""" background-color: rgb(128,128,128);
						color: rgb(0,0,0);
						border-color: rgb(0,128,128);
						border-radius: 10px;
						border-style: solid;
						border-width:2px;
						font-size:30;
						font-family: SF PRO; """)
		self.lb1.clicked.connect(self.see_work)



		self.lb2=QPushButton("Vazifani o'chirish",self)
		self.lb2.setGeometry(120,360,400,80)
		self.lb2.setFont(QFont('Poor Richard',24))
		self.lb2.setStyleSheet(""" background-color: rgb(128,128,128);
						color: rgb(0,0,0);
						border-color: rgb(0,128,128);
						border-radius: 10px;
						border-style: solid;
						border-width:2px;
						font-size:30;
						font-family: SF PRO; """)

		self.lb2.clicked.connect(self.del_w)


		self.lb3=QPushButton("Chiqish",self)
		self.lb3.setGeometry(120,470,400,80)
		self.lb3.setFont(QFont('Poor Richard',24))
		self.lb3.setStyleSheet(""" background-color: rgb(128,128,128);
						color: rgb(0,0,0);
						border-color: rgb(0,128,128);
						border-radius: 10px;
						border-style: solid;
						border-width:2px;
						font-size:30;
						font-family: SF PRO; """)

		self.lb3.clicked.connect(self.exit_click)

	def add_work(self):
		self.add_word=add_project()
		self.add_word.show()
		self.hide()

	def see_work(self):
		self.wl=watch_work()
		file="project.json"
		if not os.path.exists(file):
			return

		try:
			with open(file,"rt",encoding="utf-8")as f:
				data=json.load(f)
		except(FileNotFoundError,json.JSONDecodeError):
			data={}
		item_text=""
		for name,info in data.items():
			tavsif=info.get("description","")
			is_done=info.get("done","")

			status="✓" if is_done else " "

			item_text+=f"[{status}]  {name}- {tavsif}\n"
			self.wl.ln.setPlainText(item_text)


		self.wl.show()
		self.hide()



	def del_w(self):
		self.wk=WatchWorkWindow()
		self.wk.show()
		self.hide()

	def exit_click(self):
		self.close()


class add_project(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setMaximumSize(700,800)
		self.setMinimumSize(700,800)
		self.setGeometry(400,100,700,800)
		self.setStyleSheet(""" background-color: rbg(0,255,255);
			color: rbg(199,21,133);""")
		self.setWindowTitle('Vazifa')



		layout=QVBoxLayout()

		self.name=QTextEdit(self)
		layout.addWidget(self.name)
		self.name.setGeometry(30,90,640,60)
		self.name.setPlaceholderText('Vazifa nomi ....')
		self.name.setStyleSheet("""background-color: rgb(0,255,255);
						color: rgb(255,8,0);
						border-color: rgb(0,128,128);
						border-radius: 10px;
						border-style: solid;
						border-width:2px;
						font-size:20px;
						font-family: Arial; """)





		layout=QVBoxLayout()

		self.name1=QTextEdit(self)
		layout.addWidget(self.name1)
		self.name1.setGeometry(30,180,640,200)
		self.name1.setPlaceholderText('Vazifa tasnifi ....')
		self.name1.setStyleSheet("""background-color: rgb(0,255,255);
						color: rgb(255,8,0);
						border-color: rgb(0,128,128);
						border-radius: 10px;
						border-style: solid;
						border-width:2px;
						font-size:20px;
						font-family: Arial; """)


		self.name2=QTextEdit(self)
		layout.addWidget(self.name2)
		self.name2.setGeometry(30,400,640,60)
		self.name2.setPlaceholderText('Vazifa tasnifi ....')
		self.name2.setStyleSheet("""background-color: rgb(0,255,255);
						color: rgb(255,8,0);
						border-color: rgb(0,128,128);
						border-radius: 10px;
						border-style: solid;
						border-width:2px;
						font-size:20px;
						font-family: Arial; """)


		self.save_bt=QPushButton('Saqlash',self)
		self.save_bt.setGeometry(300,540,100,100)
		self.save_bt.setStyleSheet(""" background-color: rgb(0,225,255);
						color: rgb(255,8,0);
						border-color: rgb(0,128,128);
						border-radius: 10px;
						border-style: solid;
						border-width:2px;
						font-size:20px;""")

		self.save_bt.clicked.connect(self.save_f)


		self.menu_bt=QPushButton("Menu",self)
		self.menu_bt.setGeometry(300,650,100,80)
		self.menu_bt.setStyleSheet(""" background-color: rgb(0,225,255);
						color: rgb(255,8,0);
						border-color: rgb(0,128,128);
						border-radius: 10px;
						border-style: solid;
						border-width:2px;
						font-size:20px;""")

		self.menu_bt.clicked.connect(self.menu_click)


	def menu_click(self):
		self.menu=project()
		self.menu.show()
		self.hide()


	def save_f(self):
		vazifa=self.name.toPlainText().strip()
		vazifa1=self.name1.toPlainText().strip()
		vazifa2=self.name2.toPlainText().strip()
		if not vazifa or not vazifa1:
			print("Maydon bo'sh")
			return

		file="project.json"
		data={}
		try:
			with open(file,"rt",encoding="utf-8") as f:
				data=json.load(f)
		except(FileNotFoundError,json.JSONDecodeError):


			data={}

		data[vazifa]={
					"description":vazifa1,
					"done":vazifa2
				     }


		with open(file,"wt",encoding="utf-8") as f:
			json.dump(data,f,ensure_ascii=False,indent=4)
			print("Mufaqqiyatli  saqlandi")

		self.name.clear()
		self.name1.clear()

class watch_work(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setMaximumSize(700,800)
		self.setMinimumSize(700,800)
		self.setGeometry(400,100,700,800)
		self.setStyleSheet(""" background-color: rbg(0,255,255);
			color: rbg(199,21,133);""")
		self.setWindowTitle('Vazifa')


		layout=QVBoxLayout()

		self.ln=QTextEdit(self)
		layout.addWidget(self.ln)
		self.ln.setGeometry(30,20,640,700)
		self.ln.setStyleSheet("""background-color: rgb(0,255,255);
						color: rgb(255,8,0);
						border-color: rgb(0,128,128);
						border-radius: 10px;
						border-style: solid;
						border-width:2px;
						font-size:20px;
						font-family: Arial; """)

		self.bt=QPushButton("Menu",self)
		self.bt.setGeometry(300,740,100,50)
		self.bt.setStyleSheet(""" background-color: rgb(0,225,255);
						color: rgb(255,8,0);
						border-color: rgb(0,128,128);
						border-radius: 10px;
						border-style: solid;
						border-width:2px;
						font-size:18px;""")

		self.bt.clicked.connect(self.menu)

	def menu(self):
		self.exit=project()
		self.exit.show()
		self.hide()

class WatchWorkWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setMaximumSize(700,800)
		self.setMinimumSize(700,800)
		self.setGeometry(400,100,700,800)
		self.setStyleSheet(""" background-color: rgb(0,255,255);
			color: rgb(199,21,133);""")
		self.setWindowTitle('Vazifa')


        # Asosiy vidjet va pleymout
		central_widget = QWidget()
		self.setCentralWidget(central_widget)
		layout = QVBoxLayout(central_widget)

        # 1. Vazifalarni chiqarish uchun ro'yxat (QListWidget)
		self.list_widget = QListWidget()
		layout.addWidget(self.list_widget)

        # 2. O'chirish tugmasi
		self.delete_btn = QPushButton("Tanlangan vazifani o'chirish")
		self.delete_btn.setStyleSheet("background-color: #ff4d4d; color: white; font-weight: bold; padding: 8px;")
		self.delete_btn.clicked.connect(self.delete_selected_item)
		layout.addWidget(self.delete_btn)


		self.bt=QPushButton("Menu",self)
		self.bt.setStyleSheet(""" background-color: rgb(0,225,255);
						color: rgb(255,8,0);
						border-color: rgb(0,128,128);
						border-radius: 10px;
						border-style: solid;
						border-width:2px;
						font-size:18px;""")

		self.bt.clicked.connect(self.exit_m)
		layout.addWidget(self.bt)

        # Fayldagi vazifalarni yuklab ro'yxatga to'ldiramiz
		self.load_works()



	def load_works(self):
		file = "project.json"
		if not os.path.exists(file):
			return

		try:
			with open(file, "rt", encoding="utf-8") as f:
				data = json.load(f)
		except (FileNotFoundError, json.JSONDecodeError):
			data = {}

        # Har bir vazifani ro'yxatga qo'shamiz
		for name, info in data.items():
			tavsif = info.get("description", "")
			is_done = info.get("done", "")
			status = "✓" if is_done else " "
            # Ro'yxat elementiga matn yozamiz (masalan: [✓] Vazifa nomi - Tavsifi)
			item_text = f"[{status}]  {name} - {tavsif}"
			self.list_widget.addItem(item_text)

	def delete_selected_item(self):
		"""Ro'yxatdan tanlangan vazifani json fayldan va ekrandan o'chiradi"""
		selected_items = self.list_widget.selectedItems()
		if not selected_items:
			QMessageBox.warning(self, "Diqqat", "Iltimos, o'chirish uchun ro'yxatdan bitta vazifani tanlang!")
			return

        # Tanlangan element matnini olamiz
		item = selected_items[0]
		full_text = item.text() # Masalan: "[ ]  Bozor - Non sotib olish"
        # Matndan vazifa nomini ajratib olamiz (taxminiy formatga qarab)
        # Biz formatni: "[status]  NOMI - Tavsif" qilgan edik
		try:
            # Qavslarni tozalab, nomini ajratib olamiz
			clean_part = full_text.split("]")[1].strip() # "NOMI - Tavsif"
			vazifa_nomi = clean_part.split(" - ")[0]     # "NOMI"
		except IndexError:
            # Agar formatda muammo bo'lsa
			return

        # Tasdiqlash oynasi chiqaramiz
		reply = QMessageBox.question(
		self, "O'chirishni tasdiqlash",
		f"'{vazifa_nomi}' nomli vazifani o'chirmoqchimisiz?",
		QMessageBox.Yes | QMessageBox.No, QMessageBox.No
		)

		if reply == QMessageBox.Yes:
			file = "project.json"
			if os.path.exists(file):
				try:
					with open(file, "rt", encoding="utf-8") as f:
						data = json.load(f)
				except (FileNotFoundError, json.JSONDecodeError):
					data = {}

                # Agar lug'atda bo'lsa, o'chiramiz
				if vazifa_nomi in data:
					del data[vazifa_nomi]
                    # Faylga qayta yozamiz
					with open(file, "wt", encoding="utf-8") as f:
						json.dump(data, f, ensure_ascii=False, indent=4)

                    # Ekranda ham ro'yxatni yangilaymiz
					self.load_works()
					QMessageBox.information(self, "Muvaffaqiyat", "Vazifa muvaffaqiyatli o'chirildi!")
				else:
					QMessageBox.warning(self, "Xato", "Bunday vazifa JSON faylidan topilmadi.")




	def exit_m(self):
		self.exit=project()
		self.exit.show()
		self.hide()




if __name__=="__main__":
	os.system("clear")


	app=QApplication([])
	ilova=project()
	ilova.show()
	sys.exit(app.exec_())

