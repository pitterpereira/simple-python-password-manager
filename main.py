from tkinter import *
# Importa um módulo não trazido pelo *
from tkinter import messagebox
from random import choice, randint, shuffle
# Necessário para copiar a senha para o clipboard
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    # Listas de dados a serem utilizados nas senhas
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Escolhe aleatoriamente, num número dentro do range, um valor na lista e o adiciona
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Junta as 3 listas e embaralha os dados
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Junta os elementos da lista sem separação
    password = "".join(password_list)
    # Insere o password criado no entry 
    password_entry.insert(0, password)

    # Copia a senha para o clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    # Pega os dados dos entries
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Verifica se os campos estão preenchidos
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            # Escreve os dados em um .txt
            with open(r"Dia-29-Password-Manager\data.txt", "a") as data_file:
                # Insere os dados no arquivo data.txt saltando uma linha
                data_file.write(f"{website} | {email} | {password}\n")
                # Limpa os dados digitados nas entries
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# Cria a janela
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Insere a imagem na janela
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file=r"Dia-29-Password-Manager\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entradas
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
# Coloca o cursor no campo ao abrir o programa
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
#email_entry.insert(0, "email@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# Botões
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

# Mantém a janela aberta
window.mainloop()