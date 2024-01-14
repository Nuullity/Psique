import pyodbc

import os
#----------------------------Humor = -1

Humor = -1

#----------------------------Humor = -1
#transforma uma int em uma strin(  Py nao tem Switch Case ;-;)
def Humor_Def(Humor):
    if Humor == 1:
        Humor = "Triste"
    elif Humor == 2:
        Humor = "Levemente Triste"    
    elif Humor == 3:
        Humor = "Indiferente"
    elif Humor == 4:
        Humor = "Levemente Feliz"
    elif Humor == 5:
        Humor = "Feliz"

    return Humor
def Select_Def():
        # Executando a consulta
    Cursor.execute('SELECT * FROM Humor')

    # Obtendo os nomes das colunas
    colunas = [column[0] for column in Cursor.description]

    # Imprimindo os nomes das colunas
    print(', '.join(colunas))

    # Imprimindo os resultados de forma organizada
    for row in Cursor.fetchall():
        print(', '.join(str(value) for value in row))

#----------------------------Humor = -1







dados_conexao = (
        "Driver={SQL Server};"
        #Nome do server ( se for local será o nome da maquina)
        "Server=DESKTOP-HETLCUJ;"
        #Nome da DB
        "database=Nuullity_DB;"
)




#commit de seu humor
with pyodbc.connect(dados_conexao) as Conexao:
    print("UwU")
    
    with Conexao.cursor() as Cursor:

        while Humor < 0 or Humor > 5:
            print("----------------------------")
            print()
            print("1 - Triste")
            print("2 - Levemente Triste")
            print("3 - Indiferente")
            print("4 - Levemente Feliz")
            print("5 - Feliz")
            print("----------------------------")

            Humor = int(input("Como esta seu Humor no momento ?  "))
            os.system('cls')

        Humor = Humor_Def(Humor)
        print("Por favor, descreva como esta se sentindo: ")
        Desc = input()
        os.system('cls')

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



Select_Def()





