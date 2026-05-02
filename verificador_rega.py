import mysql.connector
from datetime import datetime

def verificar_rega():
    try:
        #  Informe a senha do MySQL entre as aspas abaixo:
        config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'SUA_SENHA_AQUI',
            'database': 'meu_refugio'
        }

        conexao = mysql.connector.connect(**config)
        cursor = conexao.cursor()

        # consulta a View criada e testada no MySQL Workbench
        query = "SELECT nome, local_casa FROM v_agenda_rega WHERE proxima_rega <= CURDATE()"
        
        cursor.execute(query)
        resultados = cursor.fetchall()

        print(f"\nRELATÓRIO DE REGA: {datetime.now().strftime('%d/%m/%Y')}")
        
        if resultados:
            print(f"\nPlantas que necessitam de rega: {len(resultados)}\n")
            for nome,local in resultados:
                print(f"-{nome} (Local: {local})")
        else:
            print("\nTodas as plantas estão com a rega em dia.")

    except mysql.connector.Error as erro:
        print(f"\nErro ao conectar ao banco: {erro}")
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

if __name__ == "__main__":
    verificar_rega()
    
