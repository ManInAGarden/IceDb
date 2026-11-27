# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

import gettext
_ = gettext.gettext

###########################################################################
## Class IceDBMain
###########################################################################

class IceDBMain ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"ICECREAM-Database"), pos = wx.DefaultPosition, size = wx.Size( 782,690 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_fileMenu = wx.Menu()
        self.m_menuItemOpenDb = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, _(u"Datenbank wechseln"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_fileMenu.Append( self.m_menuItemOpenDb )

        self.m_menuItemNewDb = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, _(u"Neue Datenbank anlegen"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_fileMenu.Append( self.m_menuItemNewDb )

        self.m_menuItem8 = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, _(u"Datenbank reparieren"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_fileMenu.Append( self.m_menuItem8 )

        self.m_fileMenu.AppendSeparator()

        self.m_menuItemExit = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, _(u"Beenden")+ u"\t" + u"CTRL+Q", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_fileMenu.Append( self.m_menuItemExit )

        self.m_menubar1.Append( self.m_fileMenu, _(u"Datei") )

        self.m_menuEdit = wx.Menu()
        self.m_menuIngredients = wx.MenuItem( self.m_menuEdit, wx.ID_ANY, _(u"Zutaten")+ u"\t" + u"CTRL+I", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuEdit.Append( self.m_menuIngredients )

        self.m_menuCatalogues = wx.MenuItem( self.m_menuEdit, wx.ID_ANY, _(u"Kataloge"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuEdit.Append( self.m_menuCatalogues )

        self.m_menubar1.Append( self.m_menuEdit, _(u"Bearbeiten") )

        self.m_aboutMenu = wx.Menu()
        self.m_helpMI = wx.MenuItem( self.m_aboutMenu, wx.ID_ANY, _(u"Hilfe"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_aboutMenu.Append( self.m_helpMI )

        self.m_aboutMI = wx.MenuItem( self.m_aboutMenu, wx.ID_ANY, _(u"Über"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_aboutMenu.Append( self.m_aboutMI )

        self.m_menubar1.Append( self.m_aboutMenu, _(u"Über IceDB") )

        self.SetMenuBar( self.m_menubar1 )

        self.m_mainWindowSB = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

        self.m_splitter2 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
        self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )

        self.m_panel1 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_recipesLC = wx.ListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
        bSizer2.Add( self.m_recipesLC, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_addRecipyBU = wx.Button( self.m_panel1, wx.ID_ANY, _(u"Hinzufügen"), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.BU_NOTEXT )

        self.m_addRecipyBU.SetBitmap( wx.Bitmap( u"ressources/Add-Row.png", wx.BITMAP_TYPE_ANY ) )
        bSizer3.Add( self.m_addRecipyBU, 0, 0, 5 )

        self.m_editRecipeBU = wx.Button( self.m_panel1, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.BU_NOTEXT )

        self.m_editRecipeBU.SetBitmap( wx.Bitmap( u"ressources/Edit.png", wx.BITMAP_TYPE_ANY ) )
        bSizer3.Add( self.m_editRecipeBU, 0, 0, 5 )

        self.m_deleteRecipeBU = wx.Button( self.m_panel1, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.BU_NOTEXT )

        self.m_deleteRecipeBU.SetBitmap( wx.Bitmap( u"ressources/Delete-Row.png", wx.BITMAP_TYPE_ANY ) )
        bSizer3.Add( self.m_deleteRecipeBU, 0, 0, 5 )


        bSizer2.Add( bSizer3, 0, wx.ALL|wx.EXPAND, 5 )


        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        self.m_panel2 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_recipeRT = wx.richtext.RichTextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB|wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
        bSizer4.Add( self.m_recipeRT, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_panel2.SetSizer( bSizer4 )
        self.m_panel2.Layout()
        bSizer4.Fit( self.m_panel2 )
        self.m_splitter2.SplitVertically( self.m_panel1, self.m_panel2, 0 )
        gbSizer1.Add( self.m_splitter2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


        gbSizer1.AddGrowableCol( 0 )
        gbSizer1.AddGrowableRow( 0 )

        self.SetSizer( gbSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.onRepairDB, id = self.m_menuItem8.GetId() )
        self.Bind( wx.EVT_MENU, self.quit, id = self.m_menuItemExit.GetId() )
        self.Bind( wx.EVT_MENU, self.OnMenuIngredients, id = self.m_menuIngredients.GetId() )
        self.m_recipesLC.Bind( wx.EVT_LEFT_DCLICK, self.onListDblClick )
        self.m_recipesLC.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onRecipeSelected )
        self.m_addRecipyBU.Bind( wx.EVT_BUTTON, self.addRecipe )
        self.m_editRecipeBU.Bind( wx.EVT_BUTTON, self.editRecipeButPressed )
        self.m_deleteRecipeBU.Bind( wx.EVT_BUTTON, self.deleteRecipe )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onRepairDB( self, event ):
        event.Skip()

    def quit( self, event ):
        event.Skip()

    def OnMenuIngredients( self, event ):
        event.Skip()

    def onListDblClick( self, event ):
        event.Skip()

    def onRecipeSelected( self, event ):
        event.Skip()

    def addRecipe( self, event ):
        event.Skip()

    def editRecipeButPressed( self, event ):
        event.Skip()

    def deleteRecipe( self, event ):
        event.Skip()

    def m_splitter2OnIdle( self, event ):
        self.m_splitter2.SetSashPosition( 0 )
        self.m_splitter2.Unbind( wx.EVT_IDLE )


###########################################################################
## Class gEditRecipeDialog
###########################################################################

class gEditRecipeDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Rezeptbearbeitung"), pos = wx.DefaultPosition, size = wx.Size( 493,688 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        gbSizer2 = wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"Titel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        gbSizer2.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"Zutaten"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        gbSizer2.Add( self.m_staticText2, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"Kurzbeschreibung"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        gbSizer2.Add( self.m_staticText3, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_descriptionTB = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_AUTO_URL|wx.TE_BESTWRAP|wx.TE_MULTILINE|wx.TE_RICH2 )
        gbSizer2.Add( self.m_descriptionTB, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, _(u"Zubereitung"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        gbSizer2.Add( self.m_staticText4, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_cookingDescriptionTB = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_BESTWRAP|wx.TE_MULTILINE|wx.TE_RICH2 )
        self.m_cookingDescriptionTB.SetMinSize( wx.Size( -1,200 ) )

        gbSizer2.Add( self.m_cookingDescriptionTB, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

        self.m_titleTB = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_titleTB, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_ingredientsLBCTRL = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        gbSizer2.Add( self.m_ingredientsLBCTRL, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_addIngredBU = wx.Button( self, wx.ID_ANY, _(u"Zutat hinzufügen"), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.BU_NOTEXT )

        self.m_addIngredBU.SetBitmap( wx.Bitmap( u"ressources/Add-Link.png", wx.BITMAP_TYPE_ANY ) )
        bSizer4.Add( self.m_addIngredBU, 0, wx.ALL, 5 )

        self.m_editIngredBU = wx.Button( self, wx.ID_ANY, _(u"Zutatdetails bearbeiten"), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.BU_NOTEXT )

        self.m_editIngredBU.SetBitmap( wx.Bitmap( u"ressources/Edit.png", wx.BITMAP_TYPE_ANY ) )
        bSizer4.Add( self.m_editIngredBU, 0, wx.ALL, 5 )

        self.m_removeIngredBU = wx.Button( self, wx.ID_ANY, _(u"Zutat entfernen"), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.BU_NOTEXT )

        self.m_removeIngredBU.SetBitmap( wx.Bitmap( u"ressources/Delete-Link.png", wx.BITMAP_TYPE_ANY ) )
        bSizer4.Add( self.m_removeIngredBU, 0, wx.ALL, 5 )


        gbSizer2.Add( bSizer4, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND, 5 )

        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
        self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
        m_sdbSizer1.Realize()

        gbSizer2.Add( m_sdbSizer1, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )


        gbSizer2.AddGrowableCol( 1 )
        gbSizer2.AddGrowableRow( 3 )
        gbSizer2.AddGrowableRow( 4 )

        self.SetSizer( gbSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_addIngredBU.Bind( wx.EVT_BUTTON, self.addIngreditientLink )
        self.m_editIngredBU.Bind( wx.EVT_BUTTON, self.editIngredientDetails )
        self.m_removeIngredBU.Bind( wx.EVT_BUTTON, self.removeIngreditientLink )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def addIngreditientLink( self, event ):
        event.Skip()

    def editIngredientDetails( self, event ):
        event.Skip()

    def removeIngreditientLink( self, event ):
        event.Skip()


###########################################################################
## Class gIngREecEditDialog
###########################################################################

class gIngREecEditDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Zutat für Rezept"), pos = wx.DefaultPosition, size = wx.Size( 428,135 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        gbSizer3 = wx.GridBagSizer( 0, 0 )
        gbSizer3.SetFlexibleDirection( wx.BOTH )
        gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"Zutat"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        gbSizer3.Add( self.m_staticText5, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        m_ingredCBCChoices = []
        self.m_ingredCBC = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_ingredCBCChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
        gbSizer3.Add( self.m_ingredCBC, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"Menge"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        gbSizer3.Add( self.m_staticText6, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_ammountSCD = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 5000, 0 )
        gbSizer3.Add( self.m_ammountSCD, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_unitTC = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        self.m_unitTC.SetMinSize( wx.Size( 50,-1 ) )

        gbSizer3.Add( self.m_unitTC, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        m_sdbSizer2 = wx.StdDialogButtonSizer()
        self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
        self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
        m_sdbSizer2.Realize()

        gbSizer3.Add( m_sdbSizer2, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 3 ), wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


        gbSizer3.AddGrowableCol( 1 )
        gbSizer3.AddGrowableRow( 2 )

        self.SetSizer( gbSizer3 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_ingredCBC.Bind( wx.EVT_COMBOBOX, self.onIngredientSelected )
        self.m_sdbSizer2OK.Bind( wx.EVT_BUTTON, self.okClicked )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onIngredientSelected( self, event ):
        event.Skip()

    def okClicked( self, event ):
        event.Skip()


###########################################################################
## Class gEditIngredientsDialog
###########################################################################

class gEditIngredientsDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Verfügbare Zutaten bearbeiten"), pos = wx.DefaultPosition, size = wx.Size( 938,460 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        gbSizer4 = wx.GridBagSizer( 0, 0 )
        gbSizer4.SetFlexibleDirection( wx.BOTH )
        gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_ingredientsLCTRL = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        gbSizer4.Add( self.m_ingredientsLCTRL, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_addRecipyBU = wx.Button( self, wx.ID_ANY, _(u"Hinzufügen"), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.BU_NOTEXT )

        self.m_addRecipyBU.SetBitmap( wx.Bitmap( u"ressources/Add-Row.png", wx.BITMAP_TYPE_ANY ) )
        bSizer3.Add( self.m_addRecipyBU, 0, 0, 5 )

        self.m_editIngredientBU = wx.Button( self, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.BU_NOTEXT )

        self.m_editIngredientBU.SetBitmap( wx.Bitmap( u"ressources/Edit.png", wx.BITMAP_TYPE_ANY ) )
        bSizer3.Add( self.m_editIngredientBU, 0, 0, 5 )

        self.m_deleteIngredientBU = wx.Button( self, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.BU_NOTEXT )

        self.m_deleteIngredientBU.SetBitmap( wx.Bitmap( u"ressources/Delete-Row.png", wx.BITMAP_TYPE_ANY ) )
        bSizer3.Add( self.m_deleteIngredientBU, 0, 0, 5 )


        gbSizer4.Add( bSizer3, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        m_sdbSizer3 = wx.StdDialogButtonSizer()
        self.m_sdbSizer3OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer3.AddButton( self.m_sdbSizer3OK )
        m_sdbSizer3.Realize()

        gbSizer4.Add( m_sdbSizer3, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )


        gbSizer4.AddGrowableCol( 0 )
        gbSizer4.AddGrowableRow( 0 )

        self.SetSizer( gbSizer4 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_ingredientsLCTRL.Bind( wx.EVT_LEFT_DCLICK, self.onIngListDblClick )
        self.m_addRecipyBU.Bind( wx.EVT_BUTTON, self.addIngredient )
        self.m_editIngredientBU.Bind( wx.EVT_BUTTON, self.editIngredient )
        self.m_deleteIngredientBU.Bind( wx.EVT_BUTTON, self.deleteIngredient )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onIngListDblClick( self, event ):
        event.Skip()

    def addIngredient( self, event ):
        event.Skip()

    def editIngredient( self, event ):
        event.Skip()

    def deleteIngredient( self, event ):
        event.Skip()


###########################################################################
## Class gEditIngredientDialog
###########################################################################

class gEditIngredientDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Zutat Bearbeiten"), pos = wx.DefaultPosition, size = wx.Size( 330,334 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        gbSizer5 = wx.GridBagSizer( 0, 0 )
        gbSizer5.SetFlexibleDirection( wx.BOTH )
        gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, _(u"Name"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        gbSizer5.Add( self.m_staticText7, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_nameTBC = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_nameTBC, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, _(u"Einheit"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        gbSizer5.Add( self.m_staticText8, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        m_unitCBChoices = []
        self.m_unitCB = wx.ComboBox( self, wx.ID_ANY, _(u"Combo!"), wx.DefaultPosition, wx.DefaultSize, m_unitCBChoices, 0 )
        gbSizer5.Add( self.m_unitCB, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, _(u"Zuckergehalt"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        gbSizer5.Add( self.m_staticText10, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_sugarSCD = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1, 0.000000, 1 )
        self.m_sugarSCD.SetDigits( 2 )
        gbSizer5.Add( self.m_sugarSCD, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, _(u"Fettgehalt"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        gbSizer5.Add( self.m_staticText11, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_fatSCD = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1, 0, 1 )
        self.m_fatSCD.SetDigits( 2 )
        gbSizer5.Add( self.m_fatSCD, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, _(u"Wasseranteil"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        gbSizer5.Add( self.m_staticText12, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_waterSCD = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1, 0, 1 )
        self.m_waterSCD.SetDigits( 2 )
        gbSizer5.Add( self.m_waterSCD, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, _(u"Kalorien/Einheit"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        gbSizer5.Add( self.m_staticText13, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_caloriesSCD = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 2.000000, 1 )
        self.m_caloriesSCD.SetDigits( 3 )
        gbSizer5.Add( self.m_caloriesSCD, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText131 = wx.StaticText( self, wx.ID_ANY, _(u"Einheitsgewicht/g"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText131.Wrap( -1 )

        gbSizer5.Add( self.m_staticText131, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_unitweightSDC = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0, 1 )
        self.m_unitweightSDC.SetDigits( 1 )
        gbSizer5.Add( self.m_unitweightSDC, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, _(u"Aktiv"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )

        gbSizer5.Add( self.m_staticText14, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_activeCB = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.CHK_2STATE )
        gbSizer5.Add( self.m_activeCB, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        m_sdbSizer4 = wx.StdDialogButtonSizer()
        self.m_sdbSizer4OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer4.AddButton( self.m_sdbSizer4OK )
        self.m_sdbSizer4Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer4.AddButton( self.m_sdbSizer4Cancel )
        m_sdbSizer4.Realize()

        gbSizer5.Add( m_sdbSizer4, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )


        gbSizer5.AddGrowableCol( 1 )
        gbSizer5.AddGrowableRow( 8 )

        self.SetSizer( gbSizer5 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


