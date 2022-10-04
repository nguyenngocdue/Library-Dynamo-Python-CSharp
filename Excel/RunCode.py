from tkinter import*
from tkinter import messagebox

window =Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()

#out = messagebox.askyesno('Greeting', 'Helo! Welcome to my script')
out = messagebox.askyesno('Greeting', 'Hello! Do you want to create excel file?')

window.deiconify()
window.destroy()
window.quit()

if out == True:
    import xlsxwriter
    import os
############################################################################## 
    path = r'C:\Users\admin\Desktop\Sheet'
    if not os.path.exists(path):
        os.makedirs(path)
############################################################################## 
    createFile = open(r'C:\Users\admin\Desktop\Sheet\Sheet.xlsx',"w")
    createFile.close()
############################################################################## 

    wbook = xlsxwriter.Workbook(r'C:\Users\admin\Desktop\Sheet\Sheet.xlsx', None)
    s = wbook.add_worksheet("Create Sheet")
############################################################################## 

    format1 = wbook.add_format(
        {
        "bg_color": "#00ff00",
        "font" : "Tahoma",
        "font_size": 12,
        "bold" : True,
        'border': 10,

        }
        )
#help(wbook.formats[0])
    format2 = wbook.add_format(
        {
        "bg_color": "#FF00FF",
        "font" : "Tahoma",
        "font_size": 20,
        "bold" : True,
        'border': 1
        }
        )
############################################################################## 

# Set the default height of all the rows, efficiently.
    s.set_default_row(23)
# Set width Column
    set_dis = s.set_column(2,3,40)
    setWith_stt = s.set_column(0,0,5)
    setWidth_sNum = s.set_column(1,1,20)

    nameTable = "Create Sheet From Excel"
    my_format = wbook.add_format()
    my_format.set_align('center')
    set_merge = s.merge_range(0,0,0,3,None,my_format)
    s.write("A1",nameTable,format2)


    stt = "STT"
    sNum = "Sheet Number"
    sName = "Sheet Name"
    tBlock = "Title Block"

    s.write("A2",stt,format1)
    s.write(1,1,sNum,format1)
    s.write(1,2,sName,format1)
    s.write(1,3,tBlock,format1)


    wbook.close()
    ####RUN -OPEN FILE
    import os
    file = r'C:\Users\admin\Desktop\Sheet\Sheet.xlsx'
    os.startfile(file)
else:
    from tkinter import*
    from tkinter import messagebox
    window =Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()
    messagebox.showinfo('Greeting', 'Thank you,Goodbye!')
