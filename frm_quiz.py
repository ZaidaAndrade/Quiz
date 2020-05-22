from tkinter import Label, LabelFrame, Frame, Entry, Text, Button, messagebox, PhotoImage, Scrollbar
from tkinter.constants import *
from tkinter.ttk import Treeview, Separator, Combobox
from Config.Visual import *
from Config.Data import *
from tkinter import *
from tkscrolledframe import ScrolledFrame


import tkinter as tk

class FormParentQuiz:
    def __init__(self, root):
        sf = ScrolledFrame(root, width=640, height=480)
        sf.pack(side="top", expand=1, fill="both")

        # Bind the arrow keys and scroll wheel
        sf.bind_arrow_keys(root)
        sf.bind_scroll_wheel(root)

        # Create a frame within the ScrolledFrame
        self.frm_parent = sf.display_widget(Frame)

        # container = Frame(root)
        # canvas = tk.Canvas(container)
        # scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        # self.frm_parent = Frame(canvas)
        #
        # self.frm_parent.bind(
        #     "<Configure>",
        #     lambda e: canvas.configure(
        #         scrollregion=canvas.bbox("all")
        #     )
        # )

        # canvas.create_window((0, 0), window=self.frm_parent, anchor="nw")
        #
        # canvas.configure(yscrollcommand=scrollbar.set)

        # for i in range(50):
        #     Label(scrollable_frame, text="Sample scrolling label").pack()

        # self.frm_parent = Frame()
        self.initialize_components()
        self.frm_child = FormChildQuiz(self.frm_parent)


        # container.pack()
        # canvas.pack(side="left", fill="both", expand=True)
        # scrollbar.pack(side="right", fill="y")








        # self.frm_parent = Frame(root)


        # frm_parent1 = ScrolledFrame(window)

        # self.frm_parent = self.frm_parent1.display_widget(self.frm_parent5)
        # self.frm_parent.pack(side="top", expand=15, fill=None)
        # self.frm_parent = Frame(window)
        # vsb_frm_parent = Scrollbar(self.frm_parent, orient="vertical", command=self.frm_parent)
        # vsb_frm_parent.grid(row=2, column=10, pady=10, sticky=E)
        # self.frm_parent.configure(yscrollcommand=vsb_frm_parent.set)

        # vsb_txt_desc = Scrollbar(self.frm_aux1, orient="vertical", command=self.txt_description.yview)
        # vsb_txt_desc.grid(row=2, column=3, pady=10, sticky=NS)
        # self.frm_parent.configure(yscrollcommand=vsb_frm_parent.set)


        # self.initialize_components()
        # self.frm_child = FormChildQuiz(self.frm_parent)




    def initialize_components(self):

        # scrollbar = Scrollbar(self)
        # scrollbar.pack(side=RIGHT, fill=Y)
        #
        # area = Text(self, yscrollcommand=scrollbar.set)
        # area.pack(expand=True, fill='both')
        # scrollbar.config(command=area.yview)


        lbl_experimenter_title = Label(self.frm_parent, text='Quiz')
        lbl_experimenter_title.config(fg=TEXT_COLOR, font=TITLE_FONT)
        lbl_experimenter_title.grid(row=0, column=0, pady=20)

    def show_frm(self):
        self.frm_parent.grid(row=0, column=0)
        self.frm_child.show_frm()

    def hide_frm(self):
        self.frm_parent.grid_forget()
        # self.frm_child.hide_frm()


class FormChildQuiz:

    def __init__(self, frm_parent):

        self.frm_child = Frame(frm_parent)
        self.quiz = Quiz()
        self.quiz.questions = []
        self.questions = []
        self.grid_row1 = 7
        #
        # self.frm_child.config(fg=TEXT_COLOR, font=SUBTITLE_FONT)
        self.frm_question = FormChildQuestions(self.frm_child, self.grid_row1)
        self.initialize_components()

    def initialize_components(self):
        """
        Method that initialize the visual components for each form associated with the local administration
        """
        # Resources for the Forms
        self.new_icon = PhotoImage(file=r"./Resources/create_1.png")
        self.new_icon1 = PhotoImage(file=r"./Resources/create_2.png")
        self.modify_icon = PhotoImage(file=r"./Resources/modify_1.png")
        self.remove_icon = PhotoImage(file=r"./Resources/delete_1.png")
        self.save_icon = PhotoImage(file=r"./Resources/save.png")
        self.cancel_icon = PhotoImage(file=r"./Resources/cancel_1.png")
        self.add_icon = PhotoImage(file=r"./Resources/right.png")
        self.delete_icon = PhotoImage(file=r"./Resources/left.png")
        self.up_arrow = PhotoImage(file=r"./Resources/up_arrow.png")
        self.down_arrow = PhotoImage(file=r"./Resources/down_arrow.png")
        self.star_icon = PhotoImage(file=r"./Resources/star.png")
        self.back_icon = PhotoImage(file=r"./Resources/back.png")
        self.view_icon = PhotoImage(file=r"./Resources/view.png")

        lbl_name = Label(self.frm_child, text='Form Name')
        lbl_name.config(fg=TEXT_COLOR, font=LABEL_FONT)
        lbl_name.grid(row=0, column=1, pady=2, sticky=W)
        self.txt_name = Text(self.frm_child, height=1, width=80)
        self.txt_name.config(font=TEXT_FONT, bg=DISABLED_COLOR)
        self.txt_name.grid(row=2, column=1, columnspan=2)

        lbl_sep1= Label(self.frm_child)
        lbl_sep1.grid(row=3, column=1)
        lbl_descrip = Label(self.frm_child, text='Description')
        lbl_descrip.config(fg=TEXT_COLOR, font=LABEL_FONT)
        lbl_descrip.grid(row=4, column=1, pady=2, sticky=W)

        self.txt_descrip = Text(self.frm_child, height=1, width=80)
        self.txt_descrip.config(font=TEXT_FONT, bg=DISABLED_COLOR)
        self.txt_descrip.grid(row=5, column=1, columnspan=2)

        lbl_sep2 = Label(self.frm_child)
        lbl_sep2.grid(row=6, column=1, columnspan=2)

    def show_frm(self):
        """

        """

        self.frm_child.grid(row=1, column=0, columnspan=9, rowspan=8, pady=10, padx=10)
        self.quiz.questions_forms.append(self.frm_question)
        self.quiz.questions_forms[0].show_frm()
        self.quiz.questions_forms[0].get_info()
        # self.quiz.questions_forms[0].txt_question = Text(self.frm_question, height=3, width=77, Text='PRUEBA')

        # self.questions.append(self.frm_question)
        # self.questions[0].show_frm()
        # self.frm_question.show_frm(grid_row=7)

    # def add_questions_list(self, frm_question):
    #     self.questions.append(frm_question)


class FormChildQuestions():
    def __init__(self, frm_child, grid_row2):

        self.frm_child = frm_child
        self.frm_question = Frame(self.frm_child)

        self.grid_row2 = grid_row2
        #
        # self.frm_child.config(fg=TEXT_COLOR, font=SUBTITLE_FONT)
        self.initialize_components()

    def initialize_components(self):
        """
        Method that initialize the visual components for each form associated with the local administration
        """
        # Resources for the Forms

        self.new_icon = PhotoImage(file=r"./Resources/create_1.png")
        self.new_icon1 = PhotoImage(file=r"./Resources/create_2.png")
        self.modify_icon = PhotoImage(file=r"./Resources/modify_1.png")
        self.remove_icon = PhotoImage(file=r"./Resources/delete_1.png")
        self.save_icon = PhotoImage(file=r"./Resources/save.png")
        self.cancel_icon = PhotoImage(file=r"./Resources/cancel_1.png")
        self.add_icon = PhotoImage(file=r"./Resources/right.png")
        self.delete_icon = PhotoImage(file=r"./Resources/left.png")
        self.up_arrow = PhotoImage(file=r"./Resources/up_arrow.png")
        self.down_arrow = PhotoImage(file=r"./Resources/down_arrow.png")
        self.star_icon = PhotoImage(file=r"./Resources/star.png")
        self.back_icon = PhotoImage(file=r"./Resources/back.png")
        self.view_icon = PhotoImage(file=r"./Resources/view.png")

        # self.frm_aux1 = LabelFrame(self.frm_child)

        self.txt_question = Text(self.frm_question, height=3, width=77)
        self.txt_question.config(font=TEXT_FONT, bg=DISABLED_COLOR)
        self.txt_question.grid(row=0, column=1, columnspan=2, pady=10)
        vsb_txt_ques = Scrollbar(self.frm_question, orient="vertical", command=self.txt_question.yview)
        vsb_txt_ques.grid(row=0, column=3, sticky=NS, pady=10)
        self.txt_question.configure(yscrollcommand=vsb_txt_ques.set)

        self.lbl_qtype = Label(self.frm_question, text='Question Type:')
        self.lbl_qtype.config(fg=TEXT_COLOR, font=LABEL_FONT)
        self.lbl_qtype.grid(row=1, column=1, sticky=NW, pady=2)

        self.cbx_qtype = Combobox(self.frm_question, state="readonly", width=30)
        self.cbx_qtype.config(font=TEXT_FONT)
        self.cbx_qtype.grid(row=2, column=1, sticky=NW)

        self.frm_aux2 = Frame(self.frm_question)

        btn_new_q = Button(self.frm_aux2, image=self.new_icon, command=self.click_new_question)
        btn_new_q.grid(row=0, column=0, pady=5, padx=5, sticky=E)
        btn_new_ttp = CreateToolTip(btn_new_q, 'New question')
        btn_edit = Button(self.frm_aux2, image=self.modify_icon)
        btn_edit.grid(row=1, column=0, pady=5, padx=5, sticky=E)
        btn_edit_ttp = CreateToolTip(btn_edit, 'Edit question')
        btn_delete = Button(self.frm_aux2, image=self.remove_icon)
        btn_delete.grid(row=2, column=0, pady=5, padx=5, sticky=E)
        btn_delete_ttp = CreateToolTip(btn_delete, 'Delete question')

        self.frm_aux2.grid(row=0, column=4, sticky=NW, rowspan=12)

        self.frm_aux3 = Label(self.frm_question)
        self.lbl_options = Label(self.frm_aux3, text='Options')
        self.lbl_options.config(fg=TEXT_COLOR, font=LABEL_FONT)
        self.lbl_options.grid(row=1, column=0, sticky=NW, pady=5)

        self.frm_aux4 = Label(self.frm_aux3)
        self.ent_option1 = Entry(self.frm_aux4, width=85)
        self.ent_option1.grid(row=1, column=0, pady=10, sticky=W, columnspan=3)
        self.btn_cancel_opt= Button(self.frm_aux4, image=self.cancel_icon)
        self.btn_cancel_opt.grid(row=1, column=3, pady=10, sticky=W)
        self.btn_new_opt= Button(self.frm_aux4, image=self.new_icon1)
        self.btn_new_opt.grid(row=1, column=4, pady=10, sticky=W)

        # self.options=[]
        self.frm_aux4.grid(row=2, column=0)
        # self.options.append(self.frm_aux4)
        # self.options[0](Label).grid(row=2, column=0)
        self.frm_aux3.grid(row=3, column=0, sticky=NW, columnspan=4)
        self.frm_question.grid(row=7, column=1, sticky=NW)

    def show_frm(self):
        """

        """
        self.frm_question.grid(row=self.grid_row2, column=1, sticky=NW)
        self.grid_row2 = self.grid_row2 + 1

    def get_info(self):
        quest = self.txt_question.get('1.0', 'end-1c')

    def click_new_question(self):

        frm_new_question = FormChildQuestions(self.frm_child, self.grid_row2)
        # self.frm_child.add_questions_list(frm_new_question)
        frm_new_question.show_frm()