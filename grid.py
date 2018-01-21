#!/usr/bin/python

# import ui library

from tkinter import *
from tkinter.font import Font
import tkinter.filedialog as fileDialog
import os

from tkinter import ttk

class Functions:
    def FileChoose(self):
        fileDialog.askopenfile()
class GUI:
    root = Tk()

    text = Text(root)
    myFont = Font(family="Times New Roman", size=62)

    w = Label(root)
    w.grid(row=0, column=0)

    labelframe = LabelFrame(w, text="General Settings")
    labelframe.pack(fill='both', side=LEFT, expand='yes')

    brainRegionFiles = Label(labelframe, text="Brain region files")
    brainRegionFiles.grid(row=0, column=0)

    brainRegionFilesLocation = Entry(labelframe, width=30)
    brainRegionFilesLocation.grid(row=0, column=1)

    selectBrainRegionFilesLocation = Button(labelframe, text="Select")
    selectBrainRegionFilesLocation.grid(row=0, column=2)
    selectBrainRegionFilesLocation.bind("<Button-1>", Functions.FileChoose)

    fileWithVariableLabel = Label(labelframe, text="File with variables")
    fileWithVariableLabel.grid(row=1, column=0)

    fileWithVariableInput = Entry(labelframe, width=30)
    fileWithVariableInput.grid(row=1, column=1, padx=10)

    fileWithVariableSelect = Button(labelframe, text="Select")
    fileWithVariableSelect.grid(row=1, column=2, padx=10)
    fileWithVariableSelect.bind("<Button-1>", Functions.FileChoose)

    selectSubjectsConnMatrixButton = Button(labelframe, text="Select Subjects ( Conn Matrix )", width=40)
    selectSubjectsConnMatrixButton.grid(row=2, column=0, columnspan=3, pady=10)

    createConnectivityMatrixButton = Button(labelframe, text="Create Connectivity Matrix", width=40)
    createConnectivityMatrixButton.grid(row=3, column=0, columnspan=3, pady=10)

    subjectsLabel = Label(labelframe, text="Subjects")
    subjectsLabel.grid(row=4)

    subjectsListBox = Listbox(labelframe, height=5, xscrollcommand=Scrollbar(orient=HORIZONTAL),
                              yscrollcommand=Scrollbar(orient=VERTICAL),width=50)

    for path, subdirs, files in os.walk(
            r'workspaces\SampleWorkspace\data\CorrMatrix'):
        for filename in files:
            subjectsListBox.insert(END,filename)
    subjectsListBox.grid(row=5,column=0, columnspan=3)


    subjectFileNameLabel = Label(labelframe, text="Subject name in Filename ")
    subjectFileNameLabel.grid(row=6)

    curr = StringVar()
    curr.set("da")
    subjectFileNameDisplay = Entry(labelframe, textvariable=curr)
    subjectFileNameDisplay.grid(row=7)


    # LabelFrame to hold the Network Construction components
    networkFrame = LabelFrame(w, text="Network Construction")
    networkFrame.pack(side=LEFT, expand='yes')

    # Threshold group of radio buttons
    thresholdFrame = LabelFrame(networkFrame, text="Threshold")
    # thresholdFrame.pack(fill="both", padx=5)
    thresholdFrame.grid(row=0, column=0, columnspan=4, sticky=W, padx=5)
    v = IntVar()
    Radiobutton(thresholdFrame, text="Significant", variable=v, value=0).grid(row=0, column=0)
    Radiobutton(thresholdFrame, text="Relative", variable=v, value=1).grid(row=0, column=1)
    Radiobutton(thresholdFrame, text="Absolute", variable=v, value=2).grid(row=0, column=2)
    Radiobutton(thresholdFrame, text="SICE", variable=v, value=3).grid(row=0, column=3)
    Radiobutton(thresholdFrame, text="None", variable=v, value=4).grid(row=0, column=4)

    # Weights group of radio buttons
    weightsFrame = LabelFrame(networkFrame, text="Weights")
    weightsFrame.grid(row=1, column=0, columnspan=4, sticky=W, padx=5)
    v = IntVar()
    Radiobutton(weightsFrame, text="No Change", variable=v, value=0).grid(row=0, column=0)
    Radiobutton(weightsFrame, text="absolute weights", variable=v, value=1).grid(row=0, column=1)
    Radiobutton(weightsFrame, text="negative weights to zero", variable=v, value=2).grid(row=0, column=2)

    nodesLabel = Label(networkFrame, text="Network nodes/Brain areas")
    nodesLabel.grid(row=2, column=0, columnspan=2, sticky=NW, pady=10)
    listbox = Listbox(networkFrame, height=5, xscrollcommand=Scrollbar(orient=HORIZONTAL),
                      yscrollcommand=Scrollbar(orient=VERTICAL), width=30)
    listbox.grid(row=3, column=0, columnspan=2, sticky=W, padx=5, pady=2)

    file = open("SampleData//BrainRegions.csv", "r")
    for line in file:
        strings = line.split(';')
        listbox.insert(END, strings[1])


    nodesLabel = Label(networkFrame, text="Network Thresholds")
    nodesLabel.grid(row=2, column=2, columnspan=2, sticky=NW, padx=5, pady=10)
    listbox1 = Listbox(networkFrame, height=5, xscrollcommand=Scrollbar(orient=HORIZONTAL),
                       yscrollcommand=Scrollbar(orient=VERTICAL), width=30)
    listbox1.grid(row=3, column=2, columnspan=2, sticky=W, padx=5, pady=2)

    for i in range(20):
        listbox1.insert(END, "0.1" + str(i))

    CheckVarGenerate = IntVar()
    cbGenerate = Checkbutton(networkFrame, text="Generate", variable=CheckVarGenerate, onvalue=1, offvalue=0)
    cbGenerate.grid(row=4, column=0, sticky=NW, pady=5)
    Entry(networkFrame, width=7).grid(row=4, column=1, pady=5, sticky=NW)
    Label(networkFrame, width=20, text="randomized subject data").grid(row=5, column=0, columnspan=2, sticky=NW)
    Label(networkFrame, width=20, text="(null model network)").grid(row=6, column=0, columnspan=2, sticky=NW)

    listbox2 = Listbox(networkFrame, height=3, width=20, xscrollcommand=Scrollbar(orient=HORIZONTAL),
                       yscrollcommand=Scrollbar(orient=VERTICAL))
    listbox2.insert(0, "nesto")
    listbox2.insert(1, "nestodrugo")
    listbox2.grid(row=4, column=2, sticky=NW)

    CheckVarBinary = IntVar()
    Checkbutton(networkFrame, text="Bin", variable=CheckVarBinary, onvalue=1, offvalue=0).grid(row=5, column=2,
                                                                                               sticky=NW)

    CheckVarWeighted = IntVar()
    Checkbutton(networkFrame, text="Weighted", variable=CheckVarWeighted, onvalue=1, offvalue=0).grid(row=5, column=2,
                                                                                                      padx=40,
                                                                                                      sticky=NW)

    Entry(networkFrame, width=5).grid(row=4, column=3, sticky=NW)
    Button(networkFrame, text="CheckFrag").grid(row=5, column=3, sticky=NW)

    Button(w, text="?", width=2, justify=RIGHT).pack()

    # LabelFrame to hold the Network Calculations components
    networkCalcFrame = LabelFrame(w, text="Network Calculations")
    networkCalcFrame.pack(fill="both", side=LEFT, expand='yes')
    CheckVarCalculate = IntVar()
    Checkbutton(networkCalcFrame, text="Calculate graph metrics", variable=CheckVarCalculate, onvalue=1,
                offvalue=0).grid(row=0, column=0, columnspan=2, sticky=NW)
    Label(networkCalcFrame, text="Brain graph metrics").grid(row=1, column=0)
    v = StringVar()
    v.set("Select Dynamic")
    OptionMenu(networkCalcFrame, v, "Select Dynamic", "sth else").grid(row=1, column=1)

    optionList = ('Weighted: Density - DIR', 'Weighted: Distance - UND/DIR', 'Weighted: Efficiency global - UND',
                  'Weighted: Efficiency local - UND', 'Weighted: Graph radius - UND/DIR')
    listbox = Listbox(networkCalcFrame, height=8, xscrollcommand=Scrollbar(orient=HORIZONTAL),
                      yscrollcommand=Scrollbar(orient=VERTICAL), width=50)
    listbox.grid(row=2, column=0, columnspan=2, sticky=W, padx=15, pady=2)

    for i in optionList:
        listbox.insert(END, str(i))

    CheckVarNormalize = IntVar()
    Checkbutton(networkCalcFrame, text="Normalize graph metric with random networks", variable=CheckVarNormalize,
                onvalue=1, offvalue=0).grid(sticky=NW, row=3, column=0, columnspan=2)
    CheckVarRandomNetUsage = IntVar()
    Checkbutton(networkCalcFrame, text="Use random network to calc smallworldness", variable=CheckVarRandomNetUsage,
                onvalue=0, offvalue=1).grid(sticky=NW, row=4, column=0, columnspan=2)
    Button(networkCalcFrame, text="Calculate variables and export", width=35).grid(row=5, column=0, columnspan=2,
                                                                                   pady=10)

    w1 = Label(root)
    w1.grid(row=1, column=0, sticky=NW)

    noNameFrame = LabelFrame(w1, highlightthickness=3, highlightbackground="red")
    noNameFrame.pack(fill='both', side=LEFT, expand='yes')
    checkButton = IntVar()
    checkButton1 = IntVar()
    checkButton2 = IntVar()
    checkButton3 = IntVar()
    checkButton4 = IntVar()
    checkButton5 = IntVar()
    Checkbutton(noNameFrame, text="Partial corr", variable=checkButton, onvalue=1, offvalue=0).grid(row=0, column=0,
                                                                                                    sticky=NW)
    Checkbutton(noNameFrame, text="Covariance Matrix", variable=checkButton1, onvalue=1, offvalue=0).grid(row=0,
                                                                                                          column=1,
                                                                                                          sticky=NW)
    Checkbutton(noNameFrame, text="Spearman corr", variable=checkButton2, onvalue=1, offvalue=0).grid(row=1, column=0,
                                                                                                      sticky=NW)
    Checkbutton(noNameFrame, text="SICE Target density:", variable=checkButton3, onvalue=1, offvalue=0).grid(row=1,
                                                                                                             column=1,
                                                                                                             sticky=NW)
    Checkbutton(noNameFrame, text="Bend corr", variable=checkButton4, onvalue=1, offvalue=0).grid(row=2, column=0,
                                                                                                  sticky=NW)
    Checkbutton(noNameFrame, text="Mutual inf", variable=checkButton5, onvalue=1, offvalue=0).grid(row=3, column=0,
                                                                                                   sticky=NW)

    entryNoName = StringVar()
    entryNoName.set(0.2)
    Entry(noNameFrame, width=15, textvariable=entryNoName, justify=CENTER).grid(column=1, rowspan=2, sticky=W, row=2)

    randomFrame = LabelFrame(noNameFrame, text="Create random time series")
    randomFrame.grid(row=4, column=0, columnspan=2, sticky=W, padx=5)
    v = IntVar()
    Radiobutton(randomFrame, text="Randomize", variable=v, value=0, ).grid(row=0, column=0)
    Radiobutton(randomFrame, text="Shuffle", variable=v, value=1, width=6).grid(row=0, column=1)
    Radiobutton(randomFrame, text="FFT", variable=v, value=2, width=7).grid(row=0, column=2)

    Label(randomFrame, text="Number of random series").grid(row=1, column=0, pady=10)
    Entry(randomFrame, width=10).grid(row=1, column=1)

    slidingFrame = LabelFrame(noNameFrame, text="Sliding Windows")
    slidingFrame.grid(row=5, column=0, columnspan=2, sticky=W, padx=5)

    Label(slidingFrame, text="Windows Size").grid(row=0, column=0, padx=10, pady=10)
    Entry(slidingFrame, width=20, text=50).grid(row=1, column=0, padx=10)
    Label(slidingFrame, text="Step Size").grid(row=0, column=1, padx=10)
    Entry(slidingFrame, width=20, text=50).grid(row=1, column=1, padx=10, pady=10)

    Button(noNameFrame, text="Generate Conn Matrix", width=40).grid(row=6, column=0, columnspan=2, pady=10)

    rawMatrixFrame = LabelFrame(w1, text="Raw Matrix(link wise)")
    rawMatrixFrame.pack(fill="both", side=LEFT, expand='yes')

    rawMatrixCb1 = IntVar()
    rawMatrixCb2 = IntVar()
    rawMatrixCb3 = IntVar()
    rawMatrixCb4 = IntVar()
    Checkbutton(rawMatrixFrame, text="Raw matrix", variable=rawMatrixCb1, onvalue=1, offvalue=0).grid(row=0,
                                                                                                      column=0,
                                                                                                      sticky=NW)
    Checkbutton(rawMatrixFrame, text="Connectivity Thr.", variable=rawMatrixCb2, onvalue=1, offvalue=0).grid(row=1,
                                                                                                             column=0,
                                                                                                             sticky=NW,
                                                                                                             pady=15)
    Checkbutton(rawMatrixFrame, text="r to z", variable=rawMatrixCb3, onvalue=1, offvalue=0).grid(row=1,
                                                                                                  column=1,
                                                                                                  sticky=NW,
                                                                                                  columnspan=2,
                                                                                                  padx=20, pady=15)
    Checkbutton(rawMatrixFrame, text="Generate", variable=rawMatrixCb4, onvalue=1, offvalue=0).grid(row=2,
                                                                                                    column=1,
                                                                                                    sticky=NW, padx=20)

    # Label(rawMatrixFrame,text="random networks").grid(row=3,column=1,sticky=NW)
    Entry(rawMatrixFrame, width=10).grid(row=2, column=2, sticky=NW)

    v = StringVar()
    v.set("Brain-Network Variability")
    OptionMenu(rawMatrixFrame, v, "dd", "sth else").grid(row=0, column=1, columnspan=2, padx=20)

    optionList2 = ('random_shuffle', 'c_null_model_und_sign', 'null_model_und_sign', 'null_model_dir_sign')
    listbox2 = Listbox(rawMatrixFrame, height=4, xscrollcommand=Scrollbar(orient=HORIZONTAL),
                       yscrollcommand=Scrollbar(orient=VERTICAL), width=30)
    listbox2.grid(row=3, column=1, columnspan=2, sticky=NW, padx=25)

    for i in optionList2:
        listbox2.insert(END, '.' + str(i))

    optionList1 = ('05', '045', '04', '035', '03', '025', '02', '015', '01', '009', '008', '007', '006', '005', '004')
    listbox1 = Listbox(rawMatrixFrame, height=13, xscrollcommand=Scrollbar(orient=HORIZONTAL),
                       yscrollcommand=Scrollbar(orient=VERTICAL), width=18)
    listbox1.grid(row=2, column=0, rowspan=3, sticky=NW, padx=15, pady=2)

    for i in optionList1:
        listbox1.insert(END, '.' + str(i))

    Label(rawMatrixFrame, text="with").grid(row=4, column=1, sticky=N)
    rawMatrixEntry = StringVar()
    rawMatrixEntry.set("1")
    Entry(rawMatrixFrame, width=10, textvariable=rawMatrixEntry, justify=CENTER).grid(row=4, column=2, sticky=NW)
    Label(rawMatrixFrame, text="for each subject").grid(row=5, column=1)

    weightsFrame = LabelFrame(rawMatrixFrame, text="Create random time series")
    weightsFrame.grid(row=6, column=0, columnspan=3, sticky=NW, pady=10, padx=5)

    noChangeCB = IntVar()
    absWeightsCB = IntVar()
    negativeWeightsCB = IntVar()
    Radiobutton(weightsFrame, text="No change", variable=noChangeCB, value=0).grid(row=0, column=0, sticky=NW)
    Radiobutton(weightsFrame, text="absolute weights", variable=absWeightsCB, value=1, width=23).grid(row=0, column=1,
                                                                                                      sticky=NW)
    Radiobutton(weightsFrame, text="negative weights to zero", variable=negativeWeightsCB, value=1).grid(
        row=1,
        column=0)

    glmFrame = LabelFrame(w1, text="GLM")
    glmFrame.pack(fill="both", side=LEFT, expand='yes')

    Label(glmFrame, text="Variables").grid(row=0, column=0, sticky=W, padx=5)
    listboxVariables = Listbox(glmFrame, height=16, width=38, xscrollcommand=Scrollbar(orient=HORIZONTAL),
                               yscrollcommand=Scrollbar(orient=VERTICAL))
    listboxVariables.insert(0, "research_site")
    listboxVariables.insert(1, "beer_pong_score")
    listboxVariables.insert(1, "eating_contest_chill")
    listboxVariables.insert(1, "fantasy_score")
    listboxVariables.grid(row=1, rowspan=12, column=0, sticky=NW, padx=10)

    Button(glmFrame, width=3, text=">>").grid(row=1, column=1, padx=5)
    Button(glmFrame, width=3, text="<<").grid(row=2, column=1, padx=5, sticky=N)
    Button(glmFrame, width=3, text=">>").grid(row=4, column=1, padx=5)
    Button(glmFrame, width=3, text="<<").grid(row=5, column=1, padx=5, sticky=N)
    Button(glmFrame, width=3, text=">>").grid(row=7, column=1, padx=5)
    Button(glmFrame, width=3, text="<<").grid(row=8, column=1, padx=5, sticky=N)
    Button(glmFrame, width=3, text=">>").grid(row=10, column=1, padx=5)
    Button(glmFrame, width=3, text="<<").grid(row=11, column=1, padx=5, sticky=N)

    Label(glmFrame, text="Between covariates").grid(row=0, column=2, padx=10, sticky=W)
    listboxVariables = Listbox(glmFrame, height=2, width=30, xscrollcommand=Scrollbar(orient=HORIZONTAL),
                               yscrollcommand=Scrollbar(orient=VERTICAL))
    listboxVariables.insert(0, "age")
    listboxVariables.grid(row=1, rowspan=2, column=2, padx=10, columnspan=2)

    Label(glmFrame, text="Between factors").grid(row=3, column=2, padx=10, sticky=W)
    listboxVariables = Listbox(glmFrame, height=2, width=30, xscrollcommand=Scrollbar(orient=HORIZONTAL),
                               yscrollcommand=Scrollbar(orient=VERTICAL))
    listboxVariables.insert(0, "sex")
    listboxVariables.grid(row=4, rowspan=2, column=2, padx=10, columnspan=2)

    Label(glmFrame, text="Within covariates").grid(row=6, column=2, padx=10, sticky=W)
    listboxVariables = Listbox(glmFrame, height=2, width=30, xscrollcommand=Scrollbar(orient=HORIZONTAL),
                               yscrollcommand=Scrollbar(orient=VERTICAL))
    listboxVariables.grid(row=7, rowspan=2, column=2, padx=10, columnspan=2)

    Label(glmFrame, text="Nuisance covariates").grid(row=9, column=2, padx=10, sticky=W)
    listboxVariables = Listbox(glmFrame, height=2, width=30, xscrollcommand=Scrollbar(orient=HORIZONTAL),
                               yscrollcommand=Scrollbar(orient=VERTICAL))
    listboxVariables.grid(row=10, rowspan=2, column=2, padx=10, columnspan=2)

    Button(glmFrame, text="Select Within ID", width=20).grid(row=13, column=0, sticky=NW, padx=10)
    interacOM = StringVar()
    interacOM.set("Interactions Second Order")
    OptionMenu(glmFrame, interacOM, "dd", "sth else").grid(row=13, column=2, columnspan=2)

    Label(glmFrame, text="#Rep").grid(row=14, column=3)
    repE = StringVar()
    repE.set(10000)
    Entry(glmFrame, textvariable=repE, width=10, justify=CENTER).grid(row=15, column=3)

    graphMetrFrame = LabelFrame(glmFrame, text="Graph Metrics")
    graphMetrFrame.grid(row=14, column=0, columnspan=3, sticky=W, padx=5)
    graphMRB = IntVar()
    Radiobutton(graphMetrFrame, text="parametric", variable=graphMRB, value=0).grid(row=0, column=0, padx=15)
    Radiobutton(graphMetrFrame, text="rand NW", variable=graphMRB, value=1).grid(row=0, column=1, padx=15)
    Radiobutton(graphMetrFrame, text="permutation", variable=graphMRB, value=2).grid(row=0, column=2, padx=15)

    rawMatrFrame = LabelFrame(glmFrame, text="Raw Matrix")
    rawMatrFrame.grid(row=15, column=0, columnspan=3, sticky=W, padx=5)
    graphMRB = IntVar()
    Radiobutton(rawMatrFrame, text="parametric", variable=graphMRB, value=0).grid(row=0, column=0, padx=15)
    Radiobutton(rawMatrFrame, text="rand NW", variable=graphMRB, value=1).grid(row=0, column=1, padx=15)
    Radiobutton(rawMatrFrame, text="permutation", variable=graphMRB, value=2).grid(row=0, column=2, padx=15)

    w3 = Label(root)
    w3.grid(row=2, column=0)
    buttonsBottomFrame = Label(w3)
    buttonsBottomFrame.pack(fill=None, side=LEFT, expand='yes')
    Button(buttonsBottomFrame, text="Switch Workspace", width=25).grid(row=0, column=0, sticky=W)
    Button(buttonsBottomFrame, text="Open Previous Results", width=25).grid(row=0, column=1, sticky=NW, padx=5)
    Button(buttonsBottomFrame, text="<", width=5).grid(row=0, column=2, sticky=NW, padx=5)
    Button(buttonsBottomFrame, text="Load Interim Results", width=25).grid(row=0, column=3, sticky=NW, padx=5)
    Button(buttonsBottomFrame, text=">", width=5).grid(row=0, column=4, sticky=NW, padx=5)
    Button(buttonsBottomFrame, text="Statistics with already calculated values", width=35, state=DISABLED).grid(row=0,
                                                                                                                column=5,
                                                                                                                sticky=NW,
                                                                                                                padx=5)
    Button(buttonsBottomFrame, text="Calculate & Statistics", width=25).grid(row=0, column=6, sticky=NW, padx=5)
    root.mainloop()


"""
    thresholdFrame1 = ttk.LabelFrame(glmFrame, text="Threshold", style="Red.TLabelframe")
    thresholdFrame1.grid(row=0, column=0, columnspan=4, sticky=W, padx=5)
    v = IntVar()
    Radiobutton(thresholdFrame1, text="Significant", variable=v, value=0).grid(row=0, column=0)
    Radiobutton(thresholdFrame1, text="Relative", variable=v, value=1).grid(row=0, column=1)
    Radiobutton(thresholdFrame1, text="Absolute", variable=v, value=2).grid(row=0, column=2)
   """

#
# MAIN
#
window = GUI()
