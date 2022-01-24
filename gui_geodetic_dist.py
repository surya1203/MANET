import tkinter
import math


if __name__ == '__main__':
    mainWindow = tkinter.Tk()
    mainWindow.title('Geodetic Distance Calculate using Haversine')
    mainWindow.geometry('1024x200')

    lat1_var = tkinter.StringVar()
    long1_var = tkinter.StringVar()
    lat2_var = tkinter.StringVar()
    long2_var = tkinter.StringVar()

    def calculate_dist():
        r = 6371
        # lat1 = math.radians(loc1[0])
        # # print(lat1)
        # lat2 = math.radians(loc2[0])
        # long1 = math.radians(loc1[1])
        # long2 = math.radians(loc2[1])
        lat1 = math.radians(float(textbox1.get()))
        lat2 = math.radians(float(textbox3.get()))
        long1 = math.radians(float(textbox2.get()))
        long2 = math.radians(float(textbox4.get()))

        delta_lambda = abs(lat1 - lat2)
        delta_phi = abs(long1 - long2)
        hav_delta_lambda = math.sin(delta_lambda / 2) ** 2
        hav_delta_phi = math.sin(delta_phi / 2) ** 2

        d = 2 * r * math.asin(math.sqrt(hav_delta_phi + (math.cos(lat1) * math.cos(lat2) * hav_delta_lambda)))
        print(d)
        textbox5.insert(tkinter.END, str(d))

    # Configure rows
    # ----------------
    mainWindow.rowconfigure(0, weight=1)    # Row for "Enter latitude and longitude for location 1"
    mainWindow.rowconfigure(1, weight=1)    # Row for "Enter latitude and longitude for location 2"
    mainWindow.rowconfigure(2, weight=1)    # Row for button "Calculate"
    mainWindow.rowconfigure(3, weight=1)    # Row for "Distance between the points"

    # Configure columns
    # -------------------
    mainWindow.columnconfigure(0, weight=2)     # Column for Text
    mainWindow.columnconfigure(1, weight=2)     # Column for textbox
    mainWindow.columnconfigure(2, weight=2)     # Column for text
    mainWindow.columnconfigure(3, weight=2)     # Column for textbox
    mainWindow.columnconfigure(4, weight=1)     # Column for padding

    # ====================== Labels ====================
    tkinter.Label(mainWindow, text='Enter the Latitude of location 1')\
        .grid(row=0, column=0, sticky='w', ipadx=30)
    tkinter.Label(mainWindow, text='Enter the Longitude of location 1', anchor='center') \
        .grid(row=0, column=2, sticky='w', ipadx=30)
    tkinter.Label(mainWindow, text='Enter the Latitude of location 2', anchor='center') \
        .grid(row=1, column=0, sticky='w', ipadx=30)
    tkinter.Label(mainWindow, text='Enter the Longitude of location 2', anchor='center') \
        .grid(row=1, column=2, sticky='w', ipadx=30)

    # ===================== Inout Textbox ====================
    textbox1 = tkinter.Entry(mainWindow, relief='sunken', textvariable=lat1_var)
    textbox1.grid(row=0, column=1, stick='w')
    textbox2 = tkinter.Entry(mainWindow, relief='sunken', textvariable=long1_var)
    textbox2.grid(row=0, column=3, stick='w')
    textbox3 = tkinter.Entry(mainWindow, relief='sunken', textvariable=lat2_var)
    textbox3.grid(row=1, column=1, stick='w')
    textbox4 = tkinter.Entry(mainWindow, relief='sunken', textvariable=long2_var)
    textbox4.grid(row=1, column=3, stick='w')

    # ======================== Button ========================
    calculate_button = tkinter.Button(mainWindow, text='Calculate', command=calculate_dist)\
        .grid(row=2, column=1, sticky='e')

    # ===================== Result Textbox ===================
    result = tkinter.Label(mainWindow, text='Geodetic Distance between location 1 and location 2 is ')\
        .grid(row=3, column=0, sticky='w', ipadx=20)
    textbox5 = tkinter.Text(mainWindow, relief='sunken', height=1, width=20)
    textbox5.grid(row=3, column=1, sticky='w')

    mainWindow.mainloop()
