import pyodbc
import os
import tkinter as tk
from tkinter import messagebox


#----------------------------
 
def Select_Def():
    Cursor.execute("""SELECT 
    Id,
    CONVERT(VARCHAR, Dia, 105) AS Dia,
    CONVERT(VARCHAR, Hora, 108) AS Hora,
    Humor,
    Descrição
    FROM Humor;""")
    # Obtendo os nomes das colunas
    colunas = [column[0] for column in Cursor.description]
    # Imprimindo os nomes das colunas
    print(', '.join(colunas))
    # Imprimindo os resultados de forma organizada
    
    for row in Cursor.fetchall():
        print(', '.join(str(value) for value in row))
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")
def handle_selection():
    selected_value = option_var.get()

    # Atualizar a variável "Humor" com o valor escolhido
    global Humor
    Humor = selected_value
    
    # Esconder a janela principal
    root.withdraw()

    # Criar uma nova janela para a entrada de texto
    new_window = tk.Toplevel(root)
    new_window.title('Descreva como está se sentindo')

    # Definir o tamanho da nova janela
    new_window.geometry("500x200")

    # Centralizar a nova janela na tela
    center_window(new_window, 500, 200)

    # Adicionar um fundo mais escuro
    new_window.configure(bg='#333')

    # Label e Entry para a descrição
    label = tk.Label(new_window, text="Por favor, descreva como está se sentindo:", fg='white', bg='#333')
    label.pack(pady=10)
    
    # Aumentar o número de linhas na Entry (input de texto)
    desc_entry = tk.Text(new_window, width=30, height=5, font=('Arial', 12), bd=2, relief='solid')
    desc_entry.pack(pady=10)

    def handle_description():
        global Desc
        Desc = desc_entry.get("1.0", "end-1c")  # Obter todo o texto na caixa de texto

        # Fechar a nova janela
        new_window.destroy()

        # Exibir a janela principal novamente
        root.deiconify()

        # Exibir os resultados
        show_results()

    # Botão para enviar a descrição
    submit_button = tk.Button(new_window, text="Submit", command=handle_description, bg='#4CAF50', fg='white')
    submit_button.pack(pady=10)  
def show_results():
    # Exibir as variáveis "Humor" e "Desc" em uma messagebox
    result_str = f"Humor: {Humor}\nDescrição: {Desc}"
    messagebox.showinfo('Resultados', result_str)
    root.destroy()
def Commit_Def():
   
    Comando = f"""
    INSERT INTO Humor (Dia, Hora, Humor, Descrição)
    VALUES (
        FORMAT(GETDATE(), 'dd-MM-yyyy'), 
        FORMAT(GETDATE(), 'HH:mm:ss'), 
        '{Humor}', 
        '{Desc}'
    );
    """
    Cursor.execute(Comando)
    Conexao.commit()


#----------------------------





# Criar a janela principal

root = tk.Tk()
root.title('Como esta seu Humor')

# Definir o tamanho da janela principal
root.geometry("500x200")

# Centralizar a janela principal na tela
center_window(root, 500, 200)

# Adicionar um fundo mais escuro
root.configure(bg='#333')

# Label para instruções
label = tk.Label(root, text="Escolha um humor:", fg='white', bg='#333')
label.pack(pady=10)

# Variável para armazenar a opção selecionada
option_var = tk.StringVar(root)
option_var.set("Triste")  # Valor padrão

# Opções de 1 a 5
options = ["Triste", "Levemente Triste", "Indiferente", "Levemente Feliz", "Feliz"]

# Menu suspenso para escolher o humor
option_menu = tk.OptionMenu(root, option_var, *options)
option_menu.pack(pady=10)

# Botão para confirmar a seleção
select_button = tk.Button(root, text="Selecionar", command=handle_selection, bg='#808080', fg='white')  # Cor cinza
select_button.pack(pady=10)

# Rodar o loop principal
root.mainloop()


#----------------------------









dados_conexao = (
        "Driver={SQL Server};"
        #Nome do server ( se for local será o nome da maquina)
        "Server=DESKTOP-HETLCUJ;"
        #Nome da DB
        "database=Nuullity_DB;"
)
with pyodbc.connect(dados_conexao) as Conexao:             
    with Conexao.cursor() as Cursor:
        Commit_Def()
        Select_Def()







