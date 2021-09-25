import re

Cadastros_Clientes = []
codigo = []



class Clientes:
    Nome = None
    Cpf = None
    Email = None
    Senha = None
    Limite_Credito = None

class produtos_cadastrados:
    Nome = None
    Valor = 0



# Cadastro dos clientes
def Cadastro_Cliente(Cadastros_Clientes):
    Cliente = Clientes ()
    todos_emails = []

    #Verifica se o nome do cliente é apenas letras
    while True:
        Cliente.Nome = input("Digite seu nome: ")
        if Cliente.Nome.isalpha():
            break
        else:
            print("Seu nome deve conter apenas letras!!")

    while True:
        #Lista aonde fica guardado o cpf em inteiros
        cpf_numerado = []

        def verificador ():
            while True:
                Cliente.cpf = (input("Digite seu cpf: ").replace(".", "").replace("-", ""))
                if len(Cliente.cpf) == 11:
                    break
                else:
                    print("\nSeu cpf precisa conter 11 digitos, digite novamente!!")

        #função para tranformar em lsita de inteiros
        def numerar_cpf():
            for i in Cliente.cpf:
                i = int(i)
                cpf_numerado.append(i)
                
        #Aqui é a função aonde eu faço a primeira parte do calculo
        def primeiro_digito_cpf():

            acumulador = 0
            resultado = 0
            controlador = 10

            for i in cpf_numerado[:9]:
                resultado = i * controlador
                acumulador += resultado
                controlador -= 1
            resto = acumulador % 11

            if resto < 2:
                resultado = 0
            elif resto >= 2:
                resultado = 11 - resto

            if resultado == cpf_numerado[9]:
                return True
            else:
                return False

        #Segunda parte do calcula (Apenas foi acrescentado o valor descoberto no primeiro calculo e aumentado o controlador)
        def segundo_digito_cpf():

            acumulador2 = 0
            resultado2 = 0
            controlador2 = 11

            for i in cpf_numerado[:10]:
                resultado2 = i * controlador2 
                acumulador2 += resultado2
                controlador2 -= 1
            resto2 = acumulador2 % 11

            if resto2 < 2:
                resultado2 = 0
            elif resto2 >= 2:
                resultado2 = 11 - resto2
            
            if resultado2 == cpf_numerado[10]:
                return True
            else:
                return False
        
        verificador ()
        numerar_cpf()
        primeiro_digito_cpf()
        segundo_digito_cpf()

        #Verificando se todas as funções que eu estou puxando são true, caso não seja ele entra no else
        if primeiro_digito_cpf() == True and segundo_digito_cpf() == True:
            break
        else:
            print("\nCpf não existe, digite novamente !!")

        
    # Verifica se o email possui @ e .
    while True:
        validar_email = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}'
        email = input("Digite seu email: ")
        if re.search(validar_email, email):
            todos_emails.append(email)
            break
        else:
            print("\nEmail invalido, digite novamente... ")

    # Verifica se a senha contém 6 digitos       
    while True:
        Cliente.Senha = str(input("Digite sua senha com 6 digitos: "))
        if len(Cliente.Senha) != 6:
            print("\n--Sua senha precisa conter 6 digitos, digite novamente--")
        else:
            senha = input("Confirme sua senha: ")
            if senha != Cliente.Senha:
                print("\nSenha diferente, digite novamente: ")
            else:
                break
    


    # Cria um limite para o cliente. Se o mesmo possuir menos que 300 reais comprovado não é permitido criar crédito
    while True:
        Cliente.Limite_Credito = 1000
        print("\n--------------------------------------------------")
        print(f"Seu limite é de R$ {Cliente.Limite_Credito} reais!!")
        print("--------------------------------------------------")
        break

    Cadastros_Clientes.append(Cliente)

    

#Verifica usuarios cadastrados
def verificar_usuario ():
    while True:
        usuario_pesquisar = input("Digite seu nome: ")
        for i in range(0, len(Cadastros_Clientes)):
            if usuario_pesquisar != Cadastros_Clientes[i].Nome:
                print("Diferente")
            else:
                print("\n--------------------------------------------------")
                print(f"\nNome do usuario: {Cadastros_Clientes[i].Nome}")
                print(f"Numero do cpf: {Cadastros_Clientes[i].cpf}")
                print("--------------------------------------------------")
        break
        # usuario_pesquisar = input("Digite seu nome: ")
        # for i in range(len(Cadastros_Clientes)):
        #     if usuario_pesquisar == Cadastros_Clientes[i].Nome:
        #         print(f"\nProcurar por cliente: {Cadastros_Clientes[i].Nome}\nCpf do cliente: {Cadastros_Clientes[i].cpf}")
        #         break
        #     else:
        #         print("Usuario não encontrado")



# Cadastro de produtos
def cadastro_produto(produtos):
    mouse_razer = produtos_cadastrados ()
    mouse_razer.Nome = "Mouse Razer - Deathadder"
    mouse_razer.Valor = 500
    
    produtos.append(mouse_razer)

    teclado_razer = produtos_cadastrados ()
    teclado_razer.Nome = "Teclado Razer - Huntsman Elite"
    teclado_razer.Valor = 500
    produtos.append(teclado_razer)



#Adiciona dentro do vetor produtos e codigo
def fazer_compras (produtos, informar_codigo):

    #For percorre os produtos 0, 1... e imprime na tela o código e as informações do produto
    for i in range(len(produtos)):
        print(f"Produto código {i}")
        print(f"Nome: {produtos[i].Nome}")
        print(f"Valor: R$: {produtos[i].Valor}\n")

    #Pergunta o código para o usuário e adiciona no parametro informar_codigo
    Codigo = str(input("Digite o código: "))
    informar_codigo.append(Codigo)



def Carrinho_Cliente (produtos, carrinho):
    while True:
        for i in carrinho:
            if i == '0':
                print(f"Produtos: {produtos[0].Nome}")
                print(f"Valor: R$: {produtos[0].Valor}\n")

            elif i == "1":
                print(f"Produtos: {produtos[1].Nome}")
                print(f"Valor: R$: {produtos[1].Valor}\n")
        break    
    for j in carrinho:
        if j == "0" and "1":
            print(f"Total deu R${produtos[0].Valor + produtos[1].Valor} reais")
        


def pagar_conta ():
    while True:
        t = input("Para pagar a conta digite 'SIM' ou 'SAIR' ").lower()
        if t == "sim":
            print("Obrigado por comprar conosco, volte sempre!!")
            codigo.clear()
            break
        else:
            break



def menu ():
    produtos = []
    cadastro_produto(produtos)
    while True:
        print("\n☆┌─┐　─┐☆\n　│▒│ /▒/\n　│▒│/▒/\n　│▒ /▒/─┬─┐\n　│▒│▒|▒│▒│ =]~~\n┌┴─┴─┐-┘─┘\n│▒┌──┘▒▒▒│    BEM VINDO AO MENU. ESCOLHA UMA OPÇÂO A BAIXO\n└┐▒▒▒▒▒▒┌┘\n　└┐▒▒▒▒┌┘ ")
        print("\n1 - Compras\n2 - Carrinho\n3 - Pagar Conta\n4 - Consultar Usuário\n0 - Voltar para menu de cadastro")
        Menu = str(input("\nDigite uma opção: "))
        if Menu == "1":
            print("\n~~Tela de Compras~~")
            fazer_compras (produtos, codigo)
        elif Menu == "2":
            print("\n~~Seu carrinho~~")
            Carrinho_Cliente (produtos, codigo)
        elif Menu == "3":
            print("\n~~Pagar Conta~~")
            pagar_conta ()
        elif Menu == "4":
            print("\n~~Consultar usuário~~")
            verificar_usuario ()
        elif Menu == "0":
            break

while True:
    print("\n☆┌─┐　─┐☆\n　│▒│ /▒/\n　│▒│/▒/\n　│▒ /▒/─┬─┐\n　│▒│▒|▒│▒│ =]~~\n┌┴─┴─┐-┘─┘\n│▒┌──┘▒▒▒│    BEM VINDO LOGUE PARA LIBERAR OU FAÇA UM CADASTRO!!\n└┐▒▒▒▒▒▒┌┘\n　└┐▒▒▒▒┌┘ ")
    print("\n1 - login\n2 - Cadastrar\n0 - Sair do sistema")
    opcao = str(input("\nDigite uma opção: "))
    
    if opcao == '1':
        usuario = input("Digite seu nome: ").lower()
        senha = input("Digite sua senha: ")
        for i in range(0, len(Cadastros_Clientes)):
            if usuario == Cadastros_Clientes[i].Nome:
                if senha == Cadastros_Clientes[i].Senha:
                    menu()
                else:
                    print("Senha incorreta")
        print("\n--------------------------------------------------")
        print("Usuário não cadastrado! Favor realizar o cadastro!")
        print("--------------------------------------------------")
    elif opcao == '2':
        Cadastro_Cliente(Cadastros_Clientes)
    else:
        print("\n~~Volte sempre :)~~\n")
        exit()