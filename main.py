import wx
import Login
# import renderer

class panelDashb(Login.panelDua): #subClass bs menggunakan event
	def __init__(self, parent): #parent container yg memuat gui diatasnya
		Login.panelDua.__init__(self, parent) #memanggil construktor
		self.SetSize(parent.GetSize())
		self.Row=0


class MyGui(Login.MyFrame1): #subClass bs menggunakan event
	def __init__(self, parent): #parent container yg memuat gui diatasnya
		Login.MyFrame1.__init__(self, parent) #memanggil construktor
		self.panelDua = panelDashb(parent=self)
		self.panelDua.Hide()
		self.Row=0		
		# self.AddButtonEditDelete()
		# self.tabel()

	def m_button_simpanOnButtonClick( self, event ):
		username = self.inputUsername.GetValue()
		password = self.inputPassword.GetValue()

		print('Username:', username)
		print('Password:', password)

		if username == 'a' and password == 'a':
			wx.MessageBox('Login berhasil', 'Pesan', wx.OK | wx.ICON_INFORMATION)
			print('Berhasil')
			self.panelLogin.Hide()
			self.panelDua.Show()
		else:
			wx.MessageBox('Login gagal', 'Pesan', wx.OK | wx.ICON_ERROR)
			print('Gagal')


	def tambahButton(self, event):
		data 			= []
		nama 			= self.nama.GetValue()
		informasi 		= self.informasi.GetValue()
		jenisHama 		= self.jenisHama.GetValue()
		penangananHama 	= self.penangananHama.GetValue()
		if nama == '' or informasi == '' or jenisHama == '' or penangananHama == '':
			wx.MessageBox('Masih ada inputan kosong', 'Error', wx.OK | wx.ICON_ERROR)
		else: 
			wx.MessageBox('Berhasil disimpan', 'Succes', wx.OK | wx.ICON_INFORMATION)
			data.append(nama)
			data.append(informasi)
			data.append(jenisHama)
			data.append(penangananHama)
			for x in range (len(data)):
				self.tabel.SetCellValue(self.Row,x,data[x])
			self.Row+=1

	def select(self, event):
		data = []
		col  = event.GetCol()
		row  = event.GetRow()
		print('====')
		print('col: ', col)
		print('row: ', row)
		if col == 4:
			wx.MessageBox(self.data[0], 'Edit Form')
			for x in range(len(data)):
				self.tabel.GetCellValue(self.Col,x,data[x])

		elif col == 5:
			wx.MessageBox('Hapus', 'Hapus Form')




	def AddButtonEditDelete(self):		
		imgEdit = wx.Bitmap("edit.PNG", wx.BITMAP_TYPE_PNG)
		imgDelete = wx.Bitmap("delete.PNG", wx.BITMAP_TYPE_PNG)
		colEdit = 5
		colDelete = 6
		self.rdEdit = renderer.MyImageRenderer(imgEdit)
		self.rdDelete = renderer.MyImageRenderer(imgDelete)
		for row in range (self.tabel.GetNumberRows()):
			self.tabel.SetCellRenderer(row, colEdit, self.rdEdit)
			self.tabel.SetRowSize(row, imgEdit.GetHeight() + 4)
			self.tabel.SetColSize(colEdit, imgEdit.GetWidth() + 4)

			self.tabel.SetCellRenderer(row, colDelete, self.rdDelete)
			self.tabel.SetRowSize(row, imgDelete.GetHeight() + 4)
			self.tabel.SetColSize(colDelete, imgDelete.GetWidth() + 4)


	def MyFrame1OnSize(self, event ):
		self.panelLogin.SetSize(self.GetSize())
		self.panelDua.SetSize(self.GetSize())


app = wx.App()
frame = MyGui(parent=None) #frame paling tinggi hierakhinya pd komponen gui yg lain
frame.Show()
app.MainLoop() 