#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Practica realizada por Juan Antonio Pagés López y Fernando San José Domínguez

import main_controller
import wx


class Mainframe(wx.Frame):

    '''Genera la ventana principal e inicializa las variables globales'''

    def __init__(self, *args, **kwds):
        self.tam = 0
        self.obs = 0
        self.score = 0
        self.moves = 0
        self.tiles = ""
        self.mode = 1
        # begin wxGlade: W.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((929, 831))

        # Tool Bar
        self.frame_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.frame_toolbar)
        self.frame_toolbar.AddTool(100, "New_Tab_Tool", wx.Bitmap("Imagenes\\newfile.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                   wx.ITEM_NORMAL, "", "")
        self.frame_toolbar.AddSeparator()
        self.frame_toolbar.AddTool(101, "Open_Fich_Tool", wx.Bitmap("Imagenes\\openfile.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                   wx.ITEM_NORMAL, "", "")
        self.frame_toolbar.AddSeparator()
        self.frame_toolbar.AddTool(102, "Save_Fich_Tool", wx.Bitmap("Imagenes\\savefile.png", wx.BITMAP_TYPE_ANY),
                                   wx.Bitmap("Imagenes\\savefile.png", wx.BITMAP_TYPE_ANY), wx.ITEM_NORMAL, "", "")
        self.frame_toolbar.AddSeparator()
        self.frame_toolbar.AddTool(103, "Avanzar_10", wx.Bitmap("Imagenes\\+10.png", wx.BITMAP_TYPE_ANY),
                                   wx.NullBitmap,
                                   wx.ITEM_NORMAL, "", "")
        # Tool Bar end
        self.box_select_modes = wx.RadioBox(self, wx.ID_ANY, "Modo:", choices=["Alfabetico", "Nivel", "1024", "2048"],
                                            majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.tablero = wx.Panel(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TOOL, self.new_tab, id=100)                          # Genero popup para crear nuevo tablero
        self.Bind(wx.EVT_TOOL, self.open_fich, id=101)                        # Genero popup para abrir tablero
        self.Bind(wx.EVT_TOOL, self.save_fich, id=102)                        # Genero popup para guardar tablero
        self.Bind(wx.EVT_TOOL, self.avanza_10, id=103)
        self.Bind(wx.EVT_RADIOBOX, self.select_mode, self.box_select_modes)   # Permite seleccionar el modo
        self.Bind(wx.EVT_CHAR_HOOK, self.on_key_press)                        # Detecta movimiento de teclas

        self.tablero.SetFocus()
        self.Center()
        # end wxGlade

        '''Inicializa el tablero'''

    def tablero_inicial(self):
        print(len(self.tiles))
        main_controller.cambiar_modo(self.mode, self.tiles)                         # Permite cambiar de modo
        main_controller.imprimirTab(len(self.tiles), 1, self.tiles)                 # Genera el tablero
        tablero_sizer = wx.GridSizer(len(self.tiles), len(self.tiles), 10, 10)
        for i in range(len(self.tiles)):                                            # Genera el tablero con las Imagenes
            for j in range(len(self.tiles)):
                imagen = self.set_imagen(i, j)
                tablero_sizer.Add(imagen, 1, wx.EXPAND, 10)
        self.tablero.SetSizer(tablero_sizer)
        self.Layout()
        print(tablero_sizer.GetCols())
        self.tablero.SetFocus()
        self.label_1.SetLabel("MOVIMIENTOS: " + str(self.moves))                    # Actualiza movimientos en GUI
        self.label_2.SetLabel(u"PUNTUACIÓN: " + str(self.score))                    # Actualiza puntuacion en GUI

    def __set_properties(self):
        # begin wxGlade: W.__set_properties
        self.SetTitle("Juego 2048")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("Imagenes\\Bloque.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.frame_toolbar.SetToolBitmapSize((5, 5))
        self.frame_toolbar.Realize()
        self.box_select_modes.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: W.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.box_select_modes, 2, wx.ALL | wx.EXPAND, 3)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, "MOVIMIENTOS: " + str(self.moves), style=wx.ALIGN_LEFT)
        self.label_1.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_2.Add(self.label_1, 1, wx.ALL | wx.EXPAND, 0)
        self.label_2 = wx.StaticText(self, wx.ID_ANY, u"PUNTUACIÓN: " + str(self.score))
        self.label_2.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_2.Add(self.label_2, 1, wx.ALL | wx.EXPAND, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY,
                                "\nTECLAS DE CONTROL:\n\n W ---> Subir\n S ---> Bajar\n D ---> Derecha\n A ---> Izquierda")
        label_3.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_2.Add(label_3, 1, wx.ALL | wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.ALL | wx.EXPAND, 1)
        sizer_1.Add(self.tablero, 2, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    '''Genera las Imagenes para el tablero'''

    def set_imagen(self, i, j):

        if self.tiles[j][i].getValor() == "*":
            nombre_imagen = "Bloque.png"
        elif self.tiles[j][i].getValor() == " ":
            nombre_imagen = "Vacio.png"
        else:
            nombre_imagen = str(self.mode - 1) + "-" + str(self.tiles[j][i].getValor()) + ".png"

        print(nombre_imagen)

        imagen = wx.Image(("Imagenes\\" + nombre_imagen), wx.BITMAP_TYPE_ANY)

        imagenbitmap = wx.StaticBitmap(self.tablero, wx.ID_ANY, wx.BitmapFromImage(imagen))

        return imagenbitmap

    '''Genera los 10 movimientos aleatorios'''

    def avanza_10(self, event):

        for i in range(10):

            numero_rand = main_controller.randInt(4)                             # Genera un numero aleatorio de 0-3

            if numero_rand == 0:
                a, self.score = main_controller.subir(self.tam, self.tiles, self.score)  # Mueve hacia arriba
                main_controller.addCelda(self.tam, self.tiles)
                self.moves += 1
            elif numero_rand == 1:
                a, self.score = main_controller.bajar(self.tam, self.tiles, self.score)  # Mueve hacia abajo
                main_controller.addCelda(self.tam, self.tiles)
                self.moves += 1
            elif numero_rand == 2:
                a, self.score = main_controller.izquierda(self.tam, self.tiles, self.score)  # Mueve hacia la izquierda
                main_controller.addCelda(self.tam, self.tiles)
                self.moves += 1
            elif numero_rand == 3:
                a, self.score = main_controller.derecha(self.tam, self.tiles, self.score)  # Mueve hacia la derecha
                main_controller.addCelda(self.tam, self.tiles)
                self.moves += 1

            self.tablero_inicial()
            self.Layout()
            main_controller.imprimirTab(self.tam, self.mode, self.tiles)                    # Imprime el tablero

    '''Genera los movimientos'''

    def on_key_press(self, event):

        keycode = event.GetKeyCode()
        print(keycode)
        if keycode == 87:
            a, self.score = main_controller.subir(self.tam, self.tiles, self.score)  # Mueve hacia arriba
            main_controller.addCelda(self.tam, self.tiles)
            self.moves += 1
        elif keycode == 83:
            a, self.score = main_controller.bajar(self.tam, self.tiles, self.score)  # Mueve hacia abajo
            main_controller.addCelda(self.tam, self.tiles)
            self.moves += 1
        elif keycode == 65:
            a, self.score = main_controller.izquierda(self.tam, self.tiles, self.score)  # Mueve hacia la izquierda
            main_controller.addCelda(self.tam, self.tiles)
            self.moves += 1
        elif keycode == 68:
            a, self.score = main_controller.derecha(self.tam, self.tiles, self.score)  # Mueve hacia la derecha
            main_controller.addCelda(self.tam, self.tiles)
            self.moves += 1
        self.tablero_inicial()
        self.Layout()
        main_controller.imprimirTab(self.tam, self.mode, self.tiles)

    '''Genera un popup para crear un nuevo tablero'''

    def new_tab(self, event):  # wxGlade: W.<event_handler>

        self.tablero_nuevo = wx.Dialog(self)
        self.spin_ctrl_1 = wx.SpinCtrl(self.tablero_nuevo, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_2 = wx.SpinCtrl(self.tablero_nuevo, wx.ID_ANY, "0", min=0, max=100)
        button_1 = wx.Button(self.tablero_nuevo, wx.ID_ANY, "Aceptar")
        button_2 = wx.Button(self.tablero_nuevo, wx.ID_ANY, "Cancelar")
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_2 = wx.GridSizer(2, 2, 0, 0)
        label_3 = wx.StaticText(self.tablero_nuevo, wx.ID_ANY, "Dimensiones:")
        grid_sizer_2.Add(label_3, 1, wx.ALIGN_CENTER | wx.LEFT | wx.TOP, 5)
        grid_sizer_2.Add(self.spin_ctrl_1, 0, wx.ALIGN_CENTER | wx.RIGHT, 10)
        label_4 = wx.StaticText(self.tablero_nuevo, wx.ID_ANY, "Nº Obstáculos:")
        grid_sizer_2.Add(label_4, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.LEFT, 0)
        grid_sizer_2.Add(self.spin_ctrl_2, 0, wx.ALIGN_CENTER | wx.RIGHT, 10)
        sizer_5.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        sizer_6.Add(button_1, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_6.Add(button_2, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_5.Add(sizer_6, 1, wx.ALIGN_CENTER, 0)
        self.tablero_nuevo.SetSizer(sizer_5)
        self.tablero_nuevo.Layout()
        self.tablero_nuevo.Centre()
        self.tablero_nuevo.Bind(wx.EVT_BUTTON, self.accept_new_tab, button_1)
        self.tablero_nuevo.Bind(wx.EVT_BUTTON, self.cancel_new_tab, button_2)
        self.tablero_nuevo.Show()

    '''Genera un nuevo tablero'''

    def accept_new_tab(self, event):  # wxGlade: New_Tab.<event_handler>
        self.tam = self.spin_ctrl_1.GetValue()
        self.obs = self.spin_ctrl_2.GetValue()
        self.tiles = main_controller.initCelda(self.tam, self.obs)
        main_controller.imprimirTab(self.tam, 1, self.tiles)
        self.tablero_inicial()
        self.tablero_nuevo.Destroy()

    '''Destruye el popup new_tab'''

    def cancel_new_tab(self, event):  # wxGlade: New_Tab.<event_handler>
        self.Destroy()

    '''Permite Abrir una partida guardada'''

    def open_fich(self, event):  # wxGlade: W.<event_handler>
        fileDialog = wx.FileDialog(self, message="Elige una ruta", defaultFile="", style=wx.FD_OPEN)
        if fileDialog.ShowModal() == wx.ID_OK:
            path = fileDialog.GetPath()
            self.tiles, self.moves, self.score, self.tam = main_controller.load(path)
            self.tablero_inicial()
            fileDialog.Destroy()

    '''Permite Guardar la partida'''

    def save_fich(self, event):  # wxGlade: W.<event_handler>
        filedialog = wx.FileDialog(self, message="Elige una ruta", defaultFile="", style=wx.FD_SAVE)
        if filedialog.ShowModal() == wx.ID_OK:
            path = filedialog.GetPath()
            main_controller.save(self.tam, self.tiles, path, self.
                                 moves, self.score)
            filedialog.Destroy()

    '''Permite cambiar de modo'''

    def select_mode(self, event):  # wxGlade: W.<event_handler>
        self.tablero.SetSizer(None, True)
        modo = self.box_select_modes.GetSelection()
        self.mode = modo + 1
        self.tablero_inicial()
        self.Layout()

# end of class W


class MyApp(wx.App):

    def OnInit(self):
        self.frame = Mainframe(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
