agenda = []

def pede_nome():
     return(input("Nome: "))

def pede_rua():
     return(input("Rua: "))
def pede_bairro():
     return(input("Bairro: "))
def pede_cep():
     return(input("CEP: "))
def pede_estado():
     return(input("Estado: "))
def pede_telefone():
     return(input("Telefone: "))

def mostra_dados(nome, rua, bairro, cep, estado, telefone):

     print("Nome:", nome, "Rua: ", rua,"Bairro:", bairro, "Cep: ", cep,"Estado:",estado, "Telefone: " , telefone)

def pesquisa(nome):
     mnome = nome.lower()
     for p, e in enumerate(agenda):
         if e[0].lower() == mnome:
               return p
     return None

def novo():
     global agenda
     nome = pede_nome()
     rua = pede_rua()
     bairro = pede_bairro()
     cep= pede_cep()
     estado= pede_estado()
     telefone = pede_telefone()
     agenda.append([nome, rua, bairro, cep, estado , telefone])

def altera():
     p = pesquisa(pede_nome())
     if p != None:
         nome = agenda[p][0]
         rua = agenda[p][1]
         bairro= agenda[p][2]
         cep = agenda[p][3]
         estado = agenda[p][4]
         telefone = agenda[p][5]
         
         print("Encontrado Digite os novos dados")
         mostra_dados(nome, telefone, rua, bairro, cep, estado)
         nome = pede_nome()
         rua = pede_rua()
         bairro = pede_bairro()
         cep = pede_cep()
         estado = pede_estado()
         telefone = pede_telefone()
         agenda[p] = [nome, rua, bairro, cep, estado, telefone]
     else:
         print("Nome não encontrado. Escolha outro nome")

def lista(): 
     print("\nMostra os dados da Agenda\n\n------")
     for e in agenda:
         mostra_dados(e[0], e[1], e[2], e[3], e[4], e[5])
     print("------\n")

def lê():
     global agenda
     arquivo = open("agenda.txt", "r", encoding = "utf-8")
     agenda = []
     for l in arquivo.readlines():
         nome, rua, bairro, cep, estado, telefone = l.strip().split("#")
         agenda.append([nome, rua, bairro, cep, estado, telefone])
     arquivo.close()

def grava():
     arquivo = open("agenda.txt", "w", encoding = "utf-8")
     for e in agenda:
         arquivo.write("NOME: %s, Rua: %s , Bairro: %s Cep: %s , Estado %s Telefone %s\n" % (e[0], e[1], e[2], e[3], e[4], e[5]))
     arquivo.close()

def valida_faixa_inteiro(pergunta, inicio, fim):
     while True:
         try:
               valor = int(input(pergunta))
               if inicio <= valor <= fim:
                   return(valor)
         except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))
 
def menu():
     print("""
   1 - Novo Contato
   2 - Fazer Alteração de Dados
   4 - Agenda
   5 - Gravar em arquivo de Texto
   6 - Lê ** nao ta funcionando

   0 - Sai
""")
     return valida_faixa_inteiro("Escolha uma opção: ",0,6)

while True:
     opção = menu()
     if opção == 0:
         break
     elif opção == 1:
         novo()
     elif opção == 2:
         altera()
     elif opção == 3:
         apaga()
     elif opção == 4:
         lista()
     elif opção == 5:
         grava()
     elif opção == 6:
         lê()
