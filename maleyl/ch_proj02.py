# 	$Id: ch_proj02.py,v 1.3 2017/03/13 12:34:13 larry Exp larry $

# IMPORTS
from Tkinter import *
import tkMessageBox
import six
import sys
import pytest
import doctest

# Channel Tool class (GUI)
class ChannelTool(Frame):
    '''
    Class for basic data input and output
    '''

    def __init__(self, parent):
        '''
        Ininializes basic GUI
        Calls basic methods
        '''

        # -----------------------------
        # VARIABLES
        # -----------------------------
        
        # List of Washington State HUBs
        self.hubs = ["ABERDEEN","ANACORTES","AVONDALE","BELLEVUE","BELLINGHAM",
                     "BEVERLY LANE","BONNEY LAKE","BREMERTON","BURIEN",
                     "BURLINGTON","CEDAR DOWNS","CENTRALIA","CLEARVIEW","DEMING",
                     "ELMA","ENUMCLAW","EVERETT","FEDERAL WAY","FERNDALE",
                     "FORT LEWIS","FREELAND","GIG HARBOR","GRAHAM","GREEN LAKE",
                     "ISSAQUAH","KENT VISTA","KIRKLAND","LAKE CITY EAST",
                     "LAKE CITY WEST","LAKE STEVENS","LAKEWOOD","LYNDEN",
                     "LYNNWOOD","MADISON PARK","MARYSVILLE","MONROE",
                     "NORTH BEND","NORTH EVERETT","OAK HARBOR","OB2 EAST DATA",
                     "OLYMPIA","TUMWATER","OTN A","OTN B","OTN C","OTN D",
                     "OTN E","OTN F","PARKLAND","PINE LAKE","POULSBO","PUYALLUP",
                     "QUEEN ANNE","RAYMOND","REDMOND","ROOSEVELT","SEA TAC",
                     "SHELTON","SILVER LAKE","SNOHOMISH","SOUTH SEATTLE",
                     "SPOKANE","SPOKANE EAST","SPOKANE WEST","TACOMA",
                     "TACOMA EAST","UNIVERSITY EAST","UNIVERSITY WEST","VASHON",
                     "WESTIN","WESTPORT","WOODINVILLE"]

        # String variables
        # Site Name
        self.sitename_var =     StringVar()
        # JT Number
        self.jt_var =           StringVar()
        # Preterm
        self.preterm_var =      StringVar()
        # Port
        self.port_var =         StringVar()
        # HUB MUX number
        self.hubmuxnum_var =    StringVar()
        # HUB MUX Type
        self.hubmuxtype_var =   StringVar()
        # Field MUX Name
        self.fieldmuxname_var = StringVar()
        # Field MUX Type
        self.fieldmuxtype_var = StringVar()
        # Tower Group
        self.towergroup_var =   StringVar()
        # HUB TX
        self.hubtx_var =        StringVar()
        # Tower TX
        self.twrtx_var =        StringVar()

        # GUI
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.make_widgets()

    def initUI(self):
        self.parent.title('Channel tool')
        self.pack(fill=BOTH, expand=1)

    def make_widgets(self):
        '''
        Creates all basic frames and widgets
        '''
        # -----------------------------
        # FRAMES
        # -----------------------------
        # Main Frame (Holds all other frames)
        self.frm_main = Frame(self)
        self.frm_main.config(relief=RIDGE,bd=2)
        self.frm_main.pack(expand=1,fill=BOTH,side=TOP,anchor=N)

        # ------------------------------
        
        # Menu Frame (Main)
        self.frm_mnu = Frame(self.frm_main)
        self.frm_mnu.pack(side=TOP,anchor=W,fill=X)

        # ------------------------------
        
        # Modify Frame (Main)
        self.frm_modify_main = Frame(self.frm_main)
        self.frm_modify_main.pack(side=TOP,anchor=N)
        
        # Label Top (Modify)
        self.frm_modify_label_01 = Frame(self.frm_modify_main)
        self.frm_modify_label_01.pack(expand=0,fill=Y,side=TOP,anchor=N,padx=1,pady=1)

        # Left Frame (Modify)
        self.frm_modify_left = Frame(self.frm_modify_main)
        self.frm_modify_left.pack(expand=1,fill=Y,side=LEFT,anchor=N,padx=2,pady=1)

        # Right Frame (Modify)
        self.frm_modify_right = Frame(self.frm_modify_main)
        self.frm_modify_right.pack(expand=0,fill=BOTH,side=LEFT,anchor=N,padx=2,pady=0)

        # Right Frame, row-01 (Modify)
        self.frm_modify_right_01 = Frame(self.frm_modify_right)
        self.frm_modify_right_01.pack(side=TOP,anchor=N,fill=BOTH)

        # Right Frame, row-02 (Modify)
        self.frm_modify_right_02 = Frame(self.frm_modify_right)
        self.frm_modify_right_02.pack(side=TOP,anchor=N,fill=BOTH)

        # Right Frame, row-03 (Modify)
        self.frm_modify_right_03 = Frame(self.frm_modify_right)
        self.frm_modify_right_03.pack(side=TOP,anchor=N,fill=BOTH)

        # ------------------------------
        
        # View frame (Main)
        self.frm_view_main = Frame(self.frm_main)
        self.frm_view_main.pack(side=TOP,anchor=N)
        
        # Label Top (View)
        self.frm_view_label_01 = Frame(self.frm_view_main)
        self.frm_view_label_01.pack(expand=0,fill=Y,side=TOP,anchor=N,padx=1,pady=1)

        # Data Frame (View)
        self.frm_view_data = Frame(self.frm_view_main)
        self.frm_view_data.pack(expand=1,fill=Y,side=LEFT,anchor=N,padx=2,pady=1)

        # ------------------------------
        
        # Report frame (Main)
        self.frm_report_main = Frame(self.frm_main)
        self.frm_report_main.pack(side=TOP,anchor=N)
        
        # Label Top (Report)
        self.frm_report_label_01 = Frame(self.frm_report_main)
        self.frm_report_label_01.pack(expand=0,fill=Y,side=TOP,anchor=N,padx=1,pady=1)

        # View Report Frame (Report)
        self.frm_report_view = Frame(self.frm_report_main)
        self.frm_report_view.pack(expand=1,fill=Y,side=LEFT,anchor=N,padx=2,pady=1)

        # Button Frame (Report)
        self.frm_report_button = Frame(self.frm_report_main)
        self.frm_report_button.pack(expand=1,fill=Y,side=LEFT,anchor=N,padx=2,pady=1)

        # ------------------------------
        # WIDGETS
        # ------------------------------

        # ----------Menu----------------
        # File Menu
        self.mnu_file_btn = Menubutton(self.frm_mnu,text='File',underline=0,bg='grey')
        self.mnu_file_btn.pack(side=LEFT)
        file = Menu(self.mnu_file_btn, tearoff=0)
        self.mnu_file_btn.config(menu=file)

        # Menu Exit (File)
        file.add_command(label='Quit...',underline=0,command=sys.exit)
        
        # Tools Menu
        self.mnu_edit_btn = Menubutton(self.frm_mnu,text='Tools',underline=0,bg='grey')
        self.mnu_edit_btn.pack(side=LEFT)
        file = Menu(self.mnu_edit_btn, tearoff=0)
        self.mnu_edit_btn.config(menu=file)

        # New Record (Tools)
        file.add_command(label='New site...',underline=0)

        # Modify (Tools)
        file.add_command(label='Modify site...',underline=0)

        # Remove (Tools)
        file.add_command(label='Remove site...',underline=0)

        # Search jobs (Tools)
        file.add_command(label='Search site...',underline=0)

        # View Menu
        self.mnu_view_btn = Menubutton(self.frm_mnu,text='View',underline=0,bg='grey')
        self.mnu_view_btn.pack(side=LEFT)
        file = Menu(self.mnu_view_btn, tearoff=0)
        self.mnu_view_btn.config(menu=file)

        # Sort (View)
        file.add_command(label='Sort...',underline=0)
        
        # Help Menu
        self.mnu_help_btn = Menubutton(self.frm_mnu,text='Help',underline=0,bg='grey')
        self.mnu_help_btn.pack(side=LEFT)
        file = Menu(self.mnu_help_btn, tearoff=0)
        self.mnu_help_btn.config(menu=file)

        # About (Help)
        file.add_command(label='About...',underline=0)

        # Help (Help)
        file.add_command(label='Help...',underline=0)

        # Filler Button (Menu)
        dummy = Menubutton(self.frm_mnu,text=' '*900,bg='grey',state=DISABLED)
        dummy.pack(side=LEFT,fill=X)

        # ----------Modify--------------
        # Simple Line
        Frame(self.frm_modify_label_01,bg='BLACK',relief=GROOVE,bd=2,height=2).pack(fill=BOTH,expand=1,pady=0,side=TOP,anchor=NW)
        
        # Modify Label
        Label(self.frm_modify_label_01,text='--- MODIFY OR ADD DATA ---',fg='blue').pack(side=TOP)

        # Category Labels
        lbl = 'HUB NAME\t\t      JT #\t        HUB MX\t     FIELD MX\t\t\t\t\tTWR TX\tHUB TX\t        SITE NAME'
        self.txt_desc = Text(self.frm_modify_main,height=1,wrap=NONE)
        self.txt_desc.pack(pady=2,anchor=W,fill=X,expand=1)
        self.txt_desc.insert(END, lbl)
        self.txt_desc.config(state='disabled',font='Arial 9',relief=FLAT,bg='light grey')

        
        

def main():
    """
    Various routines and methods
    """
    # Call dialog
    root = Tk()
    
    # Get screen width
    wid = root.winfo_screenwidth()
    
    # Get screen height
    hgt = root.winfo_screenheight()
    
    # Dialog is full screen
    root.geometry("%dx%d+0+0" % (wid, hgt))
    
    # Create instance and run
    ch_app = ChannelTool(root)
    root.mainloop()

# ---------------------------------------------------------------
    
if __name__ == '__main__':
    main()
