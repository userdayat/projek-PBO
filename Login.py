# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class panelDua
###########################################################################

class panelDua ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 601,416 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.SetBackgroundColour( wx.Colour( 0, 128, 128 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"PAKAR TANI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )
		self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer3.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		fgSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		fgSizer3.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Nama Tanaman", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.nama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.nama, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Informasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer3.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.informasi = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.informasi, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Jenis Hama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.jenisHama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.jenisHama, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Penanganan Hama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer3.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.penangananHama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.penangananHama, 0, wx.ALL, 5 )


		fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tambahData = wx.Button( self, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.tambahData.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_OTHER ) )
		fgSizer3.Add( self.tambahData, 0, wx.ALL, 5 )


		bSizer3.Add( fgSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.tabel = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel.CreateGrid( 5, 6 )
		self.tabel.EnableEditing( True )
		self.tabel.EnableGridLines( True )
		self.tabel.EnableDragGridSize( False )
		self.tabel.SetMargins( 0, 0 )

		# Columns
		self.tabel.EnableDragColMove( False )
		self.tabel.EnableDragColSize( True )
		self.tabel.SetColLabelSize( 30 )
		self.tabel.SetColLabelValue( 0, u"Nama" )
		self.tabel.SetColLabelValue( 1, u"Informasi" )
		self.tabel.SetColLabelValue( 2, u"Hama" )
		self.tabel.SetColLabelValue( 3, u"Penanganan" )
		self.tabel.SetColLabelValue( 4, u"Aksi" )
		self.tabel.SetColLabelValue( 5, u"Aksi" )
		self.tabel.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel.EnableDragRowSize( True )
		self.tabel.SetRowLabelSize( 80 )
		self.tabel.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer4.Add( self.tabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.panelDashboardOnSize )
		self.tambahData.Bind( wx.EVT_BUTTON, self.tambahButton )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def panelDashboardOnSize( self, event ):
		event.Skip()

	def tambahButton( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pertanian", pos = wx.DefaultPosition, size = wx.Size( 525,449 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.panelLogin = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panelLogin.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.panelLogin.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.panelLogin.SetBackgroundColour( wx.Colour( 64, 128, 128 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( self.panelLogin, wx.ID_ANY, u"PAKAR TANI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )
		self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer3.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText12 = wx.StaticText( self.panelLogin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		fgSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self.panelLogin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		fgSizer3.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self.panelLogin, wx.ID_ANY, u"Nama Tanaman", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.nama = wx.TextCtrl( self.panelLogin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.nama, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self.panelLogin, wx.ID_ANY, u"Informasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer3.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.informasi = wx.TextCtrl( self.panelLogin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.informasi, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self.panelLogin, wx.ID_ANY, u"Jenis Hama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.jenisHama = wx.TextCtrl( self.panelLogin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.jenisHama, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self.panelLogin, wx.ID_ANY, u"Penanganan Hama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer3.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.penangananHama = wx.TextCtrl( self.panelLogin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.penangananHama, 0, wx.ALL, 5 )


		fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tambahData = wx.Button( self.panelLogin, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.tambahData.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_OTHER ) )
		fgSizer3.Add( self.tambahData, 0, wx.ALL, 5 )


		bSizer3.Add( fgSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.tabel = wx.grid.Grid( self.panelLogin, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel.CreateGrid( 5, 6 )
		self.tabel.EnableEditing( True )
		self.tabel.EnableGridLines( True )
		self.tabel.EnableDragGridSize( False )
		self.tabel.SetMargins( 0, 0 )

		# Columns
		self.tabel.EnableDragColMove( False )
		self.tabel.EnableDragColSize( True )
		self.tabel.SetColLabelSize( 30 )
		self.tabel.SetColLabelValue( 0, u"Nama" )
		self.tabel.SetColLabelValue( 1, u"Informasi" )
		self.tabel.SetColLabelValue( 2, u"Hama" )
		self.tabel.SetColLabelValue( 3, u"Penanganan" )
		self.tabel.SetColLabelValue( 4, u"Aksi" )
		self.tabel.SetColLabelValue( 5, u"Aksi" )
		self.tabel.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel.EnableDragRowSize( True )
		self.tabel.SetRowLabelSize( 80 )
		self.tabel.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer4.Add( self.tabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.panelLogin.SetSizer( bSizer3 )
		self.panelLogin.Layout()
		bSizer3.Fit( self.panelLogin )
		bSizer1.Add( self.panelLogin, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.MyFrame1OnSize )
		self.tambahData.Bind( wx.EVT_BUTTON, self.tambahButton )
		self.tabel.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.select )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def MyFrame1OnSize( self, event ):
		event.Skip()

	def tambahButton( self, event ):
		event.Skip()

	def select( self, event ):
		event.Skip()


###########################################################################
## Class panelDashboard
###########################################################################

class panelDashboard ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,493 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.Colour( 64, 128, 128 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"PAKAR TANI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )
		self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer3.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		fgSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		fgSizer3.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Nama Tanaman", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.nama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.nama, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Informasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer3.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.informasi = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.informasi, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Jenis Hama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.jenisHama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.jenisHama, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Penanganan Hama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer3.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.penangananHama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.penangananHama, 0, wx.ALL, 5 )


		fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tambahData = wx.Button( self, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.tambahData.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_OTHER ) )
		fgSizer3.Add( self.tambahData, 0, wx.ALL, 5 )


		bSizer3.Add( fgSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.tabel = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel.CreateGrid( 5, 6 )
		self.tabel.EnableEditing( True )
		self.tabel.EnableGridLines( True )
		self.tabel.EnableDragGridSize( False )
		self.tabel.SetMargins( 0, 0 )

		# Columns
		self.tabel.EnableDragColMove( False )
		self.tabel.EnableDragColSize( True )
		self.tabel.SetColLabelSize( 30 )
		self.tabel.SetColLabelValue( 0, u"Nama" )
		self.tabel.SetColLabelValue( 1, u"Informasi" )
		self.tabel.SetColLabelValue( 2, u"Hama" )
		self.tabel.SetColLabelValue( 3, u"Penanganan" )
		self.tabel.SetColLabelValue( 4, u"Aksi" )
		self.tabel.SetColLabelValue( 5, u"Aksi" )
		self.tabel.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel.EnableDragRowSize( True )
		self.tabel.SetRowLabelSize( 80 )
		self.tabel.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer4.Add( self.tabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		# Connect Events
		self.tambahData.Bind( wx.EVT_BUTTON, self.tambahData )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tambahData( self, event ):
		event.Skip()


