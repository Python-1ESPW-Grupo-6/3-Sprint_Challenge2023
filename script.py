#lista de bairros que tendem a alagar em época de chuva intesa (verão)
# https://imoveis.estadao.com.br/noticias/saiba-quais-sao-os-bairros-mais-suscetiveis-a-enchentes-e-alagamentos-em-sao-paulo/

import sys

# Dados de meses de chuva intensa para consulta
meses_temporal = ['Dezembro', 'Janeiro', 'Fevereiro', 'Março']

# Dados de outros meses para consulta
demais_meses = ['Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro']

# Dicionário que associa bairros a meses de risco de alagamento
bairros_alagados = {
    'Mooca': meses_temporal,
    'Vila Prudente': meses_temporal,
    'Tatuapé': meses_temporal,
    'Belenzinho': meses_temporal,
    'Bela Vista': meses_temporal,
    'Casa Verde': meses_temporal,
    'Vila Leopoldina': meses_temporal,
    'Cidade Jardim': meses_temporal,
    'Chácara Santo Antônio': meses_temporal,
    'Capão Redondo': meses_temporal
}

# Listas para armazenar histórico de pesquisa de bairros e meses
bairro_pesquisados = []
meses_pesquisados = []

# Listas para armazenar histórico de notificações de bairros e causas
notificacao_bairro = []
causa_risco = []

def traco():
    """
    Imprime uma linha de traço para formatação.
    """
    print('-' * 40)

def error():
    """
    Exibe uma mensagem de erro formatada.
    """
    traco()
    print('Opção inválida! Tente novamente!')
    traco()

def consultar_bairro(bairro_user):
    """
    Consulta informações sobre um bairro específico.
    
    Args:
        bairro_user (str): O nome do bairro a ser consultado.
    """
    if bairro_user in bairros_alagados:
        while True:
            mes_user = input('Digite o nome do mês corrente (sem abreviação): ').capitalize()
            print('')
            if mes_user in bairros_alagados[bairro_user]:
                print(f'O bairro {bairro_user} tende a alagar no mês de {mes_user}. Tome cuidado!')
                print('')
                bairro_pesquisados.append(bairro_user)
                meses_pesquisados.append(mes_user)
                break
            elif mes_user in demais_meses:
                print(f'O bairro {bairro_user} não tende a alagar no mês de {mes_user}. Fique tranquilo!')
                print('')
                bairro_pesquisados.append(bairro_user)
                meses_pesquisados.append(mes_user)
                break
            else:
                traco()
                print('Mês não encontrado, verifique se contém abreviação ou erro ortográfico')
                traco()
                print('')
    else:
        print('Bairro não encontrado, verifique se contém abreviação ou erro ortográfico')
        print('')

def notificar_bairro(notificacao_area, causa):
    """
    Registra uma notificação sobre um bairro de risco.

    Args:
        notificacao_area (str): O nome do bairro a ser notificado.
        causa (str): Descrição da possível causa de risco no bairro.
    """
    notificacao_bairro.append(notificacao_area)
    causa_risco.append(causa)
    print('')
    print('Obrigado pela notificação, voltando para o menu de Notificações!')
    print('')

def consultar_bairros():
    """
    Função que permite ao usuário consultar bairros com maior risco de alagamento.

    Esta função exibe um menu interativo que permite ao usuário consultar informações sobre bairros
    que têm maior risco de alagamento durante meses de chuva intensa. O usuário pode selecionar um
    bairro para consultar e receber informações sobre o risco de alagamento naquele bairro durante
    o mês atual.
    """
    traco()
    print('Opção (1 - Consultar bairros com maior risco) escolhida!')
    traco()
    print('')
    while True:
        print('Consultar bairros')
        print('')
        print('1 - Consultar um bairro')
        print('2 - Voltar')
        print('')
        try:
            menu2 = int(input('Insira o número referente ao local que quer ir: '))
            print('')
            if menu2 == 1:
                print(f'Bairros cadastrados: {list(bairros_alagados.keys())}')
                print('')
                bairro_user = input('Digite o bairro que queira consultar: ').title()
                consultar_bairro(bairro_user)
            elif menu2 == 2:
                print('Ok, voltando para o menu!')
                print('')
                break
            else:
                error()
                print('')
        except ValueError:
            error()
            print('')

def notificar():
    """
    Função que permite ao usuário notificar um bairro de risco de alagamento.

    Esta função exibe um menu interativo que permite ao usuário notificar um bairro que ele considera
    estar em risco de alagamento. O usuário pode fornecer o nome do bairro e uma descrição da possível
    causa do alagamento.

    """
    traco()
    print('Opção (2 - Notificar algum bairro de risco) escolhida!')
    traco()
    print('')
    while True:
        print('Notificação')
        print('')
        print('1 - Mandar uma Notificação')
        print('2 - Voltar')
        print('')
        try:
            menu3 = int(input('Insira o número referente ao local que quer ir: '))
            print('')
            if menu3 == 1:
                notificacao_area = input('Notifique qual o bairro de risco: ')
                causa = input('Se souber qual poderia ser a causa de uma possível enchente, pode descrevê-la para nós? ')
                notificar_bairro(notificacao_area, causa)
            elif menu3 == 2:
                print('Ok, voltando para o menu!')
                print('')
                break
            else:
                error()
                print('')
        except ValueError:
            error()
            print('')

def conhecer_projeto():
    """
    Função que fornece informações sobre o projeto "Galo Weather".

    Esta função exibe informações detalhadas sobre o projeto "Galo Weather", incluindo sua motivação,
    funcionalidades e objetivos. O usuário pode ler sobre o projeto e, em seguida, escolher voltar ao menu
    principal.
    """
    traco()
    print('Opção (3 - Conheça mais sobre o projeto) escolhida!')
    traco()
    print('')
    print('Um pouco sobre a história do nosso projeto:')
    print('')
    print("Nosso projeto surgiu da preocupação com o crescente número de enchentes nas áreas urbanas e seus efeitos catastróficos sobre as pessoas. Sabemos que o Brasil é um país com muitas regiões vulneráveis, que sofrem com chuvas intensas que causam inundações, deslizamentos e perdas materiais e humanas. E esse problema não é exclusivo do nosso país, muitas outras cidades no mundo sofrem com essa mesma questão.\n")
    print("Por isso, criamos uma plataforma que utiliza dados em tempo real para prever alagamentos e identificar áreas de risco. Com um algoritmo de previsão de alagamento e um mapeamento das áreas de risco, nossa plataforma envia alertas em tempo real para a população e as autoridades responsáveis, permitindo medidas preventivas antes mesmo da ocorrência das enchentes.\n")
    print("Além disso, temos um hardware de monitoramento que utiliza dados de previsão de chuva e índice pluviométrico para verificar as condições dos bueiros em regiões pré-determinadas. As informações coletadas são armazenadas e repassadas aos órgãos responsáveis, permitindo uma atuação mais rápida e eficiente em caso de problemas.\n")
    print("Temos em mente que a chave para resolver problemas complexos como as enchentes urbanas está em colocar as pessoas em primeiro lugar. E é exatamente isso que nossa plataforma faz: utiliza tecnologia de ponta para proteger e salvar vidas, preservando o bem-estar da população e das comunidades afetadas pelas enchentes.\n")
    print('')
    while True:
        voltar_menu = input('Quando quiser voltar para o menu apenas digite "voltar": ').lower()
        print('')
        if voltar_menu == 'voltar':
            break
        else:
            print('Opção inválida! Tente novamente!')
            print('')

def sair():
    """
    Função que permite ao usuário sair do programa.

    Esta função exibe um menu que permite ao usuário confirmar se deseja sair do programa ou voltar ao menu
    principal. Se o usuário optar por sair, o programa será encerrado e um resumo das operações realizadas
    será exibido.
    """
    while True:
        sair_confirmacao = input('Tem certeza que quer sair? (sim/não) ').lower()
        print('')
        if sair_confirmacao == 'sim':
            traco()
            print('Obrigado pelo seu acesso!')
            traco()
            print('')
            # Histórico de uso da aplicação
            if not bairro_pesquisados and not notificacao_bairro:
                sys.exit()

            if bairro_pesquisados:
                traco()
                print(f'Pesquisas realizadas (bairro + mês): ')
                traco()
                for bairro, meses in zip(bairro_pesquisados, meses_pesquisados):
                    print(f'Bairro: {bairro}')
                    print(f'Mês: {meses}')
                    print('')

            if notificacao_bairro:
                traco()
                print('Notificações adicionadas:')
                traco()
                for bairro, causa in zip(notificacao_bairro, causa_risco):
                    print(f'Bairro: {bairro}')
                    print(f'Causa: {causa}')
                    print('')
            sys.exit()
        elif sair_confirmacao == 'não':
            print('Ok, voltando para o menu!')
            print('')
            break
        else:
            error()
            print('')

while True:
    # Exibe um cabeçalho e menu para o usuário
    traco()
    print('Bem-vindo ao projeto "Galo Weather", sistema preventivo para alagamentos nas vias urbanas')
    traco()
    print('')
    print('1 - Consultar bairros com maior risco')
    print('2 - Notificar algum bairro de risco')
    print('3 - Conheça mais sobre o projeto')
    print('4 - Sair')
    print('')
    try:
        # Solicita uma escolha numérica do usuário
        menu = int(input('Insira o número referente à parte que quer acessar: '))
        print('')

        # Com base na escolha do usuário, chama as funções apropriadas
        if menu == 1:
            consultar_bairros()
        elif menu == 2:
            notificar()
        elif menu == 3:
            conhecer_projeto()
        elif menu == 4:
            sair()
        else:
            # Trata erros de escolha inválida
            error()
            print('')
    except ValueError:
        # Trata erros de entrada inválida (não numérica)
        print('')
        error()
        print('')