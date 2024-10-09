import customtkinter

# Set appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x400")
root.title("Temperature Converter")

def check():
    if(cel_input.get() != ""):
        ipVal = cel_input.get()

        fah_res = (float(ipVal) * 9/5) + 32
        fah_input.delete(0,"end")
        fah_input.insert(0,round(fah_res,2))
        
        kel_res = float(ipVal) + 273.15
        kel_input.delete(0,"end")
        kel_input.insert(0,round(kel_res,2))

    elif(fah_input.get() != ""):
        ipVal = fah_input.get()

        cel_res = (float(ipVal) - 32) * 5/9
        cel_input.delete(0,"end")
        cel_input.insert(0,round(cel_res,2))
        
        kel_res = (float(ipVal) - 32) * 5/9 + 273.15
        kel_input.delete(0,"end")
        kel_input.insert(0,round(kel_res,2))

    elif(kel_input.get() != ""):
        ipVal = kel_input.get()

        fah_res = (float(ipVal) - 273.15) * 9/5 + 32
        fah_input.delete(0,"end")
        fah_input.insert(0,round(fah_res,2))
        
        cel_res = float(ipVal) - 273.15
        cel_input.delete(0,"end")
        cel_input.insert(0,round(cel_res,2))
 
def clear():
    cel_input.delete(0,"end")
    fah_input.delete(0,"end")
    kel_input.delete(0,"end")

frame = customtkinter.CTkFrame(master=root)
frame.grid(row=0, column=0, pady=55, padx=85, sticky="nsew")

label = customtkinter.CTkLabel(master=frame, text="Temperature Converter", font=("Comic-Sans", 25))
label.grid(row=0, column=0, columnspan=2, pady=12, padx=10)

cel_input = customtkinter.CTkEntry(master=frame, placeholder_text="--Celsius--")
cel_input.grid(row=1, column=1, pady=12, padx=10)
cel_label = customtkinter.CTkLabel(master=frame, text="°C", font=("Comic-Sans", 25,))
cel_label.grid(row=1, column=0, pady=12, padx=10)

fah_input = customtkinter.CTkEntry(master=frame, placeholder_text="--Fahrenheit--")
fah_input.grid(row=2, column=1, pady=12, padx=10)
fah_label = customtkinter.CTkLabel(master=frame, text="°F", font=("Comic-Sans", 25,))
fah_label.grid(row=2, column=0, pady=12, padx=10)

kel_input = customtkinter.CTkEntry(master=frame, placeholder_text="--Kelvin--")
kel_input.grid(row=3, column=1, pady=12, padx=10)
kel_label = customtkinter.CTkLabel(master=frame, text="K", font=("Comic-Sans", 25,))
kel_label.grid(row=3, column=0, pady=12, padx=10)

check_btn = customtkinter.CTkButton(master=frame, text="Check", command = check)
check_btn.grid(row=4, column=0, padx=(10, 5), pady=10)

clr_btn = customtkinter.CTkButton(master=frame, text="Clear", command= clear)
clr_btn.grid(row=4, column=1, padx=(10, 5), pady=10)

root.mainloop()
