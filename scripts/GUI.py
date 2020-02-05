#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 30, 2019 01:06:36 AM GMT  platform: Darwin

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import GUI_support
from read import read_main

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = MainWindow (root)
    GUI_support.init(root, top)
    root.mainloop()

w = None
def create_MainWindow(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = MainWindow (w)
    GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_MainWindow():
    global w
    w.destroy()
    w = None

class MainWindow:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1737x1023+55+23")
        top.minsize(72, 15)
        top.maxsize(2000, 1500)
        top.resizable(1, 1)
        top.title("Autoread: Milton Court Theatre")
        top.configure(borderwidth="1")
        top.configure(background="#550000")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Master_Container = tk.Frame(top)
        self.Master_Container.place(relx=0.006, rely=0.01, relheight=0.958
                , relwidth=0.996)
        self.Master_Container.configure(relief='flat')
        self.Master_Container.configure(borderwidth="1")
        self.Master_Container.configure(background="#000000")
        self.Master_Container.configure(highlightbackground="#d9d9d9")
        self.Master_Container.configure(highlightcolor="black")

        def importAutoData():
            AxisArray = read_main()
            return AxisArray
        AxisArray = importAutoData()


        def importAxisNames():
            with open("axis_names.txt","r") as file:
                AxisNames = list(file.readlines())
            for line in AxisNames:
                AxisNames[AxisNames.index(line)] = line.replace("\n","")
                print(AxisNames)
            return AxisNames

        AxisNames = importAxisNames()

        self.MCC1 = tk.LabelFrame(self.Master_Container)
        self.MCC1.place(relx=0.006, rely=0.02, relheight=0.872, relwidth=0.98)
        self.MCC1.configure(relief='groove')
        self.MCC1.configure(foreground="#ffffff")
        self.MCC1.configure(text='''Milton Court Theatre''')
        self.MCC1.configure(background="#000066")
        self.MCC1.configure(highlightbackground="#d9d9d9")
        self.MCC1.configure(highlightcolor="black")

        self.TkStorage = list([]*len(AxisArray))
        AxisOffset = 1        #"""Choose the Axes to display here:"""
        AxisNumbers = [*range(1,36),*range(41,47),*range(91,94)]
        for Axis in AxisArray:
            AxisItem = 0
            AxisLabels = []
            #Labels per axis: 7
            AxisLabels.append(tk.Frame(self.MCC1))
            VertSpacing = 75
            if AxisOffset % 4 == 1:
                AxisLabels[AxisItem].place(x=10, y=17*((AxisOffset*4)-(AxisOffset * 3))+17, relheight=0.064 #rely=0.023
                        , width=400, bordermode='ignore')
            elif AxisOffset % 4 == 2:
                AxisLabels[AxisItem].place(x=430, y=17*((AxisOffset*4)-(AxisOffset * 3)), relheight=0.064 #rely=0.023
                        , width=400, bordermode='ignore')
            elif AxisOffset % 4 == 3:
                AxisLabels[AxisItem].place(x=850, y=17*((AxisOffset*4)-(AxisOffset * 3))-17, relheight=0.064 #rely=0.023
                        , width=400, bordermode='ignore')
            elif AxisOffset % 4 == 0:
                AxisLabels[AxisItem].place(x=1270, y=17*((AxisOffset*4)-(AxisOffset * 3))-(17*2), relheight=0.064 #rely=0.023
                        , width=400, bordermode='ignore')

            AxisLabels[AxisItem].configure(relief='flat')
            AxisLabels[AxisItem].configure(borderwidth="2")
            AxisLabels[AxisItem].configure(background="#d9d9d9")
            AxisLabels[AxisItem].configure(highlightbackground="#d9d9d9")
            AxisLabels[AxisItem].configure(highlightcolor="black")

            AxisItem += 1
            AxisLabels.append(tk.Label(AxisLabels[0]))
            AxisLabels[AxisItem].place(relx=0.0, rely=0.364, height=35, width=40)
            AxisLabels[AxisItem].configure(activebackground="#f9f9f9")
            AxisLabels[AxisItem].configure(activeforeground="black")
            AxisLabels[AxisItem].configure(background="#000000")
            AxisLabels[AxisItem].configure(font="-family {Arial} -size 30")
            AxisLabels[AxisItem].configure(foreground="#ffff00")
            AxisLabels[AxisItem].configure(highlightbackground="#d9d9d9")
            AxisLabels[AxisItem].configure(highlightcolor="black")
            AxisLabels[AxisItem].configure(text=str(AxisNumbers[AxisOffset-1]))

            AxisItem += 1
            AxisLabels.append(tk.Label(AxisLabels[0]))
            AxisLabels[AxisItem].place(relx=0.098, rely=0.364, height=35, width=140)
            AxisLabels[AxisItem].configure(activebackground="#f9f9f9")
            AxisLabels[AxisItem].configure(activeforeground="black")
            AxisLabels[AxisItem].configure(anchor='e')
            AxisLabels[AxisItem].configure(background="#ffffff")
            AxisLabels[AxisItem].configure(font="-family {Arial} -size 30")
            AxisLabels[AxisItem].configure(foreground="#000000")
            AxisLabels[AxisItem].configure(highlightbackground="#d9d9d9")
            AxisLabels[AxisItem].configure(highlightcolor="black")
            AxisLabels[AxisItem].configure(text=str(AxisArray[str(AxisNumbers[AxisOffset-1])][0]))

            AxisItem += 1
            AxisLabels.append(tk.Label(AxisLabels[0]))
            AxisLabels[AxisItem].place(relx=0.439, rely=0.364, height=35, width=159)
            AxisLabels[AxisItem].configure(activebackground="#000000")
            AxisLabels[AxisItem].configure(activeforeground="white")
            AxisLabels[AxisItem].configure(activeforeground="black")
            AxisLabels[AxisItem].configure(anchor='e')
            AxisLabels[AxisItem].configure(background="#000000")
            AxisLabels[AxisItem].configure(font="-family {Arial} -size 30")
            AxisLabels[AxisItem].configure(foreground="#ffffff")
            AxisLabels[AxisItem].configure(highlightbackground="#d9d9d9")
            AxisLabels[AxisItem].configure(highlightcolor="black")
            AxisLabels[AxisItem].configure(text='''0 mm/s''')

            AxisItem += 1
            AxisLabels.append(tk.Label(AxisLabels[0]))
            AxisLabels[AxisItem].place(relx=0.0, rely=0.0, height=20, width=410)
            AxisLabels[AxisItem].configure(activebackground="#f9f9f9")
            AxisLabels[AxisItem].configure(activeforeground="black")
            AxisLabels[AxisItem].configure(anchor='w')
            AxisLabels[AxisItem].configure(background="#bcbcbc")
            AxisLabels[AxisItem].configure(font="-family {Arial} -size 16 -weight bold")
            AxisLabels[AxisItem].configure(foreground="#000000")
            AxisLabels[AxisItem].configure(highlightbackground="#d9d9d9")
            AxisLabels[AxisItem].configure(highlightcolor="black")
            AxisLabels[AxisItem].configure(padx="25")
            AxisLabels[AxisItem].configure(text=AxisNames[AxisOffset-1])

            AxisItem += 1
            AxisLabels.append(tk.Label(AxisLabels[0]))
            AxisLabels[AxisItem].place(relx=0.829, rely=0.364, height=35, width=71)
            AxisLabels[AxisItem].configure(activebackground="#f9f9f9")
            AxisLabels[AxisItem].configure(activeforeground="black")
            AxisLabels[AxisItem].configure(anchor='se')
            AxisLabels[AxisItem].configure(background="#d9d9d9")
            AxisLabels[AxisItem].configure(font="-family {Arial} -size 24")
            AxisLabels[AxisItem].configure(foreground="#000000")
            AxisLabels[AxisItem].configure(highlightbackground="#d9d9d9")
            AxisLabels[AxisItem].configure(highlightcolor="black")
            AxisLabels[AxisItem].configure(text='''0s''')

            AxisOffset += 1

        self.Status = tk.LabelFrame(self.Master_Container)
        self.Status.place(relx=0.006, rely=0.898, relheight=0.087
                , relwidth=0.988)
        self.Status.configure(relief='groove')
        self.Status.configure(foreground="#ffffff")
        self.Status.configure(text='''Status''')
        self.Status.configure(background="#505050")
        self.Status.configure(highlightbackground="#d9d9d9")
        self.Status.configure(highlightcolor="black")

        self.Scrolledlistbox1 = ScrolledListBox(self.Status)
        self.Scrolledlistbox1.place(relx=0.006, rely=0.235, relheight=0.635
                , relwidth=0.989, bordermode='ignore')
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(font="TkDefaultFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.006, rely=0.968, height=22, width=1433)
        self.Label1.configure(background="#550000")
        self.Label1.configure(foreground="#aaaaaa")
        self.Label1.configure(text='''Developed by James Cooper for the Guildhall School of Music and Drama. Not working? Contact james@jcooper.tech. This system should not be relied upon for show or safety critical purposes. System provided as is, with no guarantee.''')


    def update_axes(self, AxesList=None, ):
        UpdateQuantArr = self.QuantifiedArray
        Axis35 = list(getSpecificAxisData(UpdateQuantArr, 35))
        self.AxisPosition_3.configure(text=str(Axis35[0])+"mm")

    def updater(self):
        self.QuantifiedArray = read_main()
        self.update_axes()
        root.after(1, MainWindow.updater(self))


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()
