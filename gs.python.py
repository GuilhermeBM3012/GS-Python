# INTEGRANTES:
# GUILHERME BARONE MILANI - RM: 562114
# LEANDRO AFONSO SILVA SANTOS JUNIOR - RM:561344
# LUIGI ESCUDERO GRIGOLETTO - RM: 562505


import tkinter as tk

# TROCA DE TEMA

# Funções para trocar o tema
def modo_claro():
    janela.config(bg='white') # MUDA O FUNDO DA JANELA PARA BRANCO
    label.config(bg='white', fg='black') # MUDA O FUNDO DO LABEL PARA BRANCO E O TEXTO PARA PRETO

def modo_escuro():
    janela.config(bg='#1e1e1e') # MUDA O FUNDO DA JANELA DO LABEL PARA CINZA ESCURO
    label.config(bg='#1e1e1e', fg='white') # MUDA O TEXTO DO LABEL PARA BRANCO

def modo_personalizado():
    janela.config(bg='#add8e6')  # MUDA A COR DE FUNDO PARA AZUL CLARO
    label.config(bg='#add8e6', fg='black') # MUDA O TEXTO DO LABEL PARA PRETO

# Interface
janela = tk.Tk() # CRIA UMA JANELA PRINCIPAL DE INTERFACE GRAFICA
janela.title("Troca de Tema") # TÍTULO DA JANELA
janela.geometry("300x200") # DEFINE O TAMANHO DA JANELA

label = tk.Label(janela, text="Escolha um tema:", font=("Arial", 14))
label.pack(pady=20)

# Botões de tema
# CRIA UM BOTÃO PARA CADA TEMA QUE QUANDO CLICADO ATIVA A FUNÇÃO DESSE BOTÃO
btn_claro = tk.Button(janela, text="Modo Claro", command=modo_claro)
btn_escuro = tk.Button(janela, text="Modo Escuro", command=modo_escuro)
btn_personalizado = tk.Button(janela, text="Modo Azul Claro", command=modo_personalizado)

# ADD UM PADDING DE 5 PIXELS ACIMA E ABIAXO DOS BOTÕES PARA QUE NÃO FIQUEM COLADOS
btn_claro.pack(pady=5)
btn_escuro.pack(pady=5)
btn_personalizado.pack(pady=5)

janela.mainloop()  # ABRE E MANTÉM A JANELA FUNCIONANDO


# LOGIN OU CRIAÇÃO DE CONTA

listUsuarios = []


def criarConta():
    print('HYDROSAFE')
    print("\n=== Criar Conta ===")
    nome = input("Nome completo: ")
    email = input("Email: ")

    # VERIFICA SE O EMAIL JÁ EXISTE
    for usuario in listUsuarios:
        if usuario['email'] == email:
            print("Esse email já está cadastrado!")
            return

    senha = input("Senha: ")
    listUsuarios.append({'nome': nome, 'email': email, 'senha': senha})  # ADD AS INFORMAÇÕES EM UM DICIONÁRIO, Q ESTÃO NA LISTA
    print("Conta criada com sucesso!")

def login():
    print("\n=== Login ===")
    email = input("Email: ")
    senha = input("Senha: ")
    for usuario in listUsuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            print(f"Seja bem vindo, {usuario['nome']}!")
            return True
    print("Você não tem uma conta aqui!")
    return False


conta = input('Você tem uma conta cadastrada [S/N]:\n-> ').upper()
while conta not in 'SN':
    conta = input('Você tem uma conta cadastrada [S/N]:\n-> ').upper()
if conta == 'N':
    criarConta()
else:
    login()


# FUNÇÃO PARA MOSTRAR O NOME DA EMPRESA E A SUA DESCRIÇAO ENTRE LINHAS
largura = 70
def lin():
    print('---'*40)


lin()
print('HydroSafe:    Início - Problema - Solução - Objetivos - Público - Benefícios - Uso - Tecnologias - Login - Registrar')
print('HYDROSAFE'.center(largura))
print('Proteção à comunidade'.center(largura))
lin()


def topico(msg, listaOpcoes):
    opcoes = '\n'.join(listaOpcoes)
    escolha = input(f'{msg}\n{opcoes}\n->')
    numeros = [str(i + 1) for i in range(len(listaOpcoes))]
    while escolha not in numeros:
        escolha = input(f'{msg}\n{opcoes}\n-> ')
    return int(escolha)

# MOSTRA UMA LISTA COM AS OPÇÕES PARA VER
lista = ['1- Problema', '2- Soluçao', '3- Objetivos', '4- Público',
         '5- Benefícios', '6- Uso', '7- Tecnologias']

# MOSTRA UM DICIONÁRIO COM OS TEXTOS DE CADA TÓPICO
textos = {
    1: ('\nFalta de monitoramento em tempo real de áreas de risco'
        '\nAusência de conscientização da população'
        '\nPerda de bens materiais e documentos pessoais'
        '\nSolos impermeáveis'),

    2: ('\nA HydroSafe propõe a instalação de sensores inteligentes em pontos críticos '
        '\nda cidade, como margens de rios e bueiros, para monitorar em tempo real o nível '
        '\nda água e da chuva, permitindo uma atuação rápida diante de enchentes. Além disso, '
        '\noferecerá um módulo educativo no site, com conteúdos interativos e vídeos explicativos '
        '\npara conscientizar a população sobre prevenção e segurança. O sistema contará com alertas '
        '\nautomatizados, enviados via WhatsApp, SMS, notificações no site e alto-falantes instalados '
        '\nem parceria com o governo, garantindo que mesmo as comunidades mais vulneráveis recebam '
        '\navisos a tempo. Por fim, a HydroSafe facilitará o acesso a ONGs parceiras, indicando no site '
        '\na localização dos pontos de apoio para quem for afetado pelas enchentes.'),

    3: ('\nGarantir que os sistemas sejam acessíveis para pessoas com deficiência '
        '\nou com baixa alfabetização digital, usando interfaces simples e inclusivas'),

    4: 'O público-alvo são comunidades com dificuldade de acesso à água tratada.',

    5: ('\nA solução fortalece a resiliência das comunidades vulneráveis, salva vidas, '
        '\nprotege patrimônios e contribui para cidades mais seguras, sustentáveis e '
        '\ninclusivas, democratizando o acesso à informação com alertas acessíveis e '
        '\nparcerias sociais'),

    6: 'O uso é simples: basta coletar água, filtrar e consumir.',

    7: ('\nArduino, sensores para medir nível da água, chuva, umidade e Buzzer'
        '\nSoftwares que usam dados de sensores e previsão do tempo para gerar'
        'alertas antecipados, minimizando riscos'
        '\nInterface do site simples e fácil de ser utilizada, mesmo por aqueles '
        'com dificuldades em manusear a tecnologia')
}


# DAR A ESCOLHA DA PESSOA QUERER SABER MAIS E SE SIM, MOSTRA OS OUTROS TÓPICOS DO SITE
while True:
    resposta = input('\nDeseja ver algum tópico? [S/N]\n-> ').upper()
    while resposta not in 'SN':
        resposta = input('\nDeseja ver algum tópico? [S/N]\n-> ').upper()
    if resposta == 'N':
        break

    escolha = topico('Diga qual opção você deseja ver:', lista)  # APENAS COLOCAR O NÚMERO
    print(f"\n{lista[escolha - 1]}:\n{textos[escolha]}\n")
print('Obrigado pela visita :) ! ')