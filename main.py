from datetime import datetime
import subprocess
import time
import os


def git_status():
    clear()
    subprocess.run(["git", "status"])
    input("Pressione ENTER para voltar ao menu")


def git_push():
    clear() 
    date= datetime.now()
    subprocess.run(["git", "add", "."])
    response_commit= subprocess.run(["git", "commit", "-m", f"{date.day}/{date.month}/{date.year}"], capture_output=True, text=True)
    if response_commit.returncode != 0:
            print("Nada para commitar (ou erro no commit):")
            print(response_commit.stderr)
    else:
        print("Commitado com sucesso!")
    response_push= subprocess.run(["git", "push"], capture_output= True, text= True)
    if response_push.returncode != 0:
        print("Erro ao fazer push:")
        print(response_push.stderr)
    else:
        print("Push feito com sucesso!")
    input("Pressione ENTER para voltar ao menu")

def git_pull():
    clear()
    response= subprocess.run(["git", "pull"], capture_output=True, text=True)
    if response.returncode != 0:
        print("Erro ao fazer pull:")
        print(response.stderr)
    else:
        print("Atulização feita com sucesso")
    input("Ação finalizada. Pressione ENTER para voltar ao menu")
	
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def verify_update_cloud():
    subprocess.run(["git", "fetch"], capture_output= True)
    response= subprocess.run(["git", "status"], capture_output= True, text= True)
    if "Your branch is up to date with" in response.stdout:
        return False
    else:
        return True

def verify_update_local():
    response= subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if response.stdout != "":
        return True
    else:
        return False

if __name__ == "__main__":
    while(True):
        clear()
        print("-"*35)
        print(" Gerenciamento de Save do Obsidian")
        print("-"*35)
        print("Opções: ")
        print(" 1- Ver status\n",
			"2- Fazer salvamento no GitHub\n",
			"3- Fazer Atualização do conteúdo local\n",
			"4- Fechar terminal")

        response_update_cloud= verify_update_cloud()
        response_update_local= verify_update_local()

        if (response_update_cloud == True) and (response_update_local == True):
            print("AVISO: a versão em cloude e a local tem atulizações.\n      "
                        "Talvez isso pode gerar conflito!")
        elif response_update_local == True:
            print("AVISO: A versão local do conteudo tem atulizações!")
        elif response_update_cloud == True:
            print("AVISO: A versão em cloud do conteudo tem atualizações!")

        option_resp= input("Escolha uma opção: ")
        if option_resp == "1":
            git_status()
        elif option_resp == "2":
            git_push()
        elif option_resp == "3":
            git_pull()
        elif option_resp == "4":
            break
        else:
            clear()
            print("Selecione uma opção valida!")
            time.sleep(2)