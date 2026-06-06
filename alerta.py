import os
import sys
import mysql.connector
from datetime import datetime, timedelta

# Diagnóstico inicial
print(">>> alerta.py iniciado", flush=True)

def registrar_log(mensagem):
    pasta_script = os.path.dirname(os.path.abspath(__file__))
    caminho_log = os.path.join(pasta_script, "registro_rega.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(caminho_log, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} - {mensagem}\n")

def verificar_rega():
    registrar_log("Iniciando verificação automatizada integrada ao MySQL")
    data_hoje = datetime.now().date()
    
    print(f"\n--- VERIFICAÇÃO AUTOMATIZADA DO BANCO DE DADOS ({data_hoje.strftime('%d/%m/%Y')}) ---")
    
    try:
        config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'bianck98',
            'database': 'meu_refugio' # Ajustado conforme o seu print
        }
        
        conexao = mysql.connector.connect(**config)
        cursor = conexao.cursor()
        
        #  Ajustado para a sua tabela 'alerta_rega_hoje'
        query = "SELECT nome, local_armazenamento, ultima_rega, tipo FROM plantas"
        cursor.execute(query)
        plantas_banco = cursor.fetchall()
        
        plantas_urgentes = 0
        
        for planta in plantas_banco:
            nome = planta[0]
            local = planta[1]
            ultima_rega = planta[2]
            tipo = planta[3]

            if ultima_rega is None:
                continue

            if isinstance(ultima_rega, str):
                ultima_rega = datetime.strptime(ultima_rega, '%Y-%m-%d').date()
            elif isinstance(ultima_rega, datetime):
                ultima_rega = ultima_rega.date()

            # Regra: 10 dias para suculentas / 5 dias para folhagens
            intervalo = 10 if str(tipo).lower() == 'suculenta' else 5
            data_limite = ultima_rega + timedelta(days=intervalo)

            if data_limite <= data_hoje:
                print(f"⚠️ REGA URGENTE: {nome} (Local: {local}) -> Atrasada desde {data_limite.strftime('%d/%m/%Y')}")
                plantas_urgentes += 1

        if plantas_urgentes > 0:
            print(f"\nTotal de plantas necessitando de atenção: {plantas_urgentes}")
            registrar_log(f"Sucesso: {len(plantas_banco)} plantas analisadas. {plantas_urgentes} alertas.")
        else:
            print(f"\nTodas as {len(plantas_banco)} plantas do banco 'meu_refugio' estão em dia!")
            registrar_log(f"Sucesso: {len(plantas_banco)} plantas analisadas. Tudo em dia.")

        cursor.close()
        conexao.close()

    except mysql.connector.Error as erro:
        print(f"\n❌ Erro no MySQL: {erro}")
        registrar_log(f"Erro no banco: {erro}")
    except Exception as e:
        print(f"\n❌ Erro no processamento: {e}")

if __name__ == "__main__":
    verificar_rega()