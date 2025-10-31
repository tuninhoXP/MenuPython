
import time
loop = True

#PROGRAMAS:
def calcularsalario():
    global loop
    salario = float(input("DIGITE SEU SALÁRIO: "))
    horas = float(input("DIGITE HORAS TRABALHADAS: "))
    sh = salario / horas
    print("VOCE RECEBE ", sh, " R$ POR HORA")
    time.sleep(1)
    finalizar = int(input("DESEJA FINALIZAR O PROGRAMA? 1 = SIM"))
    if finalizar == 1:
        loop = False
        return loop
    return sh

def calcularfaltas():
    atrasos = int(input("QUANTAS FALTAS VOCÊ TEM?"))
    global loop
    if atrasos >= 3:
        print("Você está suspenso")
    elif atrasos == 2:
        print("Mais um e você estará suspenso")
    elif atrasos == 1:
        print("Vou deixar passar pois é a primeira vez")
    else:
        print("Ok! pode entrar")
    time.sleep(1)
    finalizar = int(input("DESEJA FINALIZAR O PROGRAMA? 1 = SIM"))
    if finalizar == 1:
        loop = False
        return loop

def calcularLiberade():
    disponivel = input("Você está livre? S/N")
    global loop
    if disponivel == "S" or "s":
        print("Estou sim")
    else:
        print("Não estou")
        time.sleep(1)
    finalizar = int(input("DESEJA FINALIZAR O PROGRAMA? 1 = SIM"))
    if finalizar == 1:
        loop = False
        return loop
    
def calcularmedia():
    global loop
    nota1 = float(input("NOTA 1: "))
    nota2 = float(input("NOTA 2: "))
    nota3 = float(input("NOTA 3: "))
    nota4 = float(input("NOTA 4: "))
    media = (nota1 + nota2 + nota3 + nota4 ) /4
    print("SUA MÉDIA É: ",media)
    finalizar = int(input("DESEJA FINALIZAR O PROGRAMA? 1 = SIM"))
    if finalizar == 1:
        loop = False
        return loop





while loop == True:

    print("-----------------------------------------------")
    print("Bem vindo aos meus programas!")
    time.sleep(2)
    selecionarprograma = int(
        input("1 = CALCULAR SALARIO / 2 = CALCULAR FALTAS  / 3 = CALCULARLIBERDADE / 4 = CALCULAR MÉDIA "))
    if selecionarprograma == 1:
        calcularsalario()
    elif selecionarprograma == 2:
        calcularfaltas()
    elif selecionarprograma == 3:
        calcularLiberade()
    elif selecionarprograma == 4:
        calcularmedia()
    else: print("RESPOSTA INVÁLIDA")





