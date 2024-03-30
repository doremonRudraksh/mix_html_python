from tkinter import *
root=Tk()
root.title("My Weather App")
root.geometry("350x300")

root.configure(background="white")
#Setting labels
city_name_label=Label(root, text="City Name",font=("Helvetica", 18,'bold'),bg="white")
city_name_label.place(relx=0.28,rely=0.15,anchor=CENTER)

city_entry=Entry(root)
city_entry.place(relx=0.28,rely=0.35,anchor=CENTER)

weather_info_label = Label(root,text="Weather: ", bg="white", font=("bold", 10))
weather_info_label.place(relx=0.23,rely=0.6,anchor=CENTER) 

humidity_info_label = Label(root,text="Humidity: ", bg="white", font=( "bold",10)) 
humidity_info_label.place(relx=0.22,rely=0.7,anchor=CENTER) 
    
root.mainloop()
