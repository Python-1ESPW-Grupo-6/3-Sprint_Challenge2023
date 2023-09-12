#lista de bairros que tendem a alagar em época de chuva intesa (verão)
# https://imoveis.estadao.com.br/noticias/saiba-quais-sao-os-bairros-mais-suscetiveis-a-enchentes-e-alagamentos-em-sao-paulo/

import sys

# Lista de meses de chuva intensa
meses_temporal = ['Dezembro', 'Janeiro', 'Fevereiro', 'Março']


# Lista de demais meses para consulta
demais_meses = ['Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro']


# Dicionário de bairros alagados com os meses correspondentes
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


#Histórico de pesquisa dos possiveis alagamentos em bairros
bairro_pesquisados = []
meses_pesquisados = []


#Histórico de notificação de bairros
notificacao_bairro = []
causa_risco = []


def traco():
    print('-'*30)

def error():
    traco()
    print('Opção invalida! Tente novamente!')
    traco()

def consultar_bairros():
    traco()
    print('Opção (1 - Consultar bairros com maior risco) escolhida!')
    traco()
    print('')
    while True:
        print('Consultar bairros')
        print('')
        print('1 - Consulte um bairro')
        print('2 - Voltar')
        print('')
        try:
            menu2 = int(input('Insira o número referente ao local que quer ir: '))
            print('')
            if menu2 == 1:
                print(f'Bairros cadastrados: {list(bairros_alagados.keys())}')
                print('')
                bairro_user = input('Digite o bairro que queira consultar: ').title()  # Normalização do bairro inserido
                bairro_pesquisados.append(bairro_user)
                print('')
                if bairro_user in bairros_alagados:
                    while True:
                        mes_user = input('Digite o nome do mês corrente (sem abreviação): ').capitalize()  # Normalização do mês inserido
                        print('')
                        if mes_user in bairros_alagados[bairro_user]:
                            print(f'O bairro {bairro_user} tende a alagar no mês de {mes_user}. Tome cuidado!')
                            print('')
                            meses_pesquisados.append(mes_user)
                            break
                        elif mes_user in demais_meses:
                            print(f'O bairro {bairro_user} não tende a alagar no mês de {mes_user}. Fique tranquilo!')
                            print('')
                            meses_pesquisados.append(mes_user)
                            break
                        else:
                            traco()
                            print('Mês não encontrado, verifique se contém abreviação ou erro ortográfico')  # Mensagem de erro ao usuário
                            traco()
                            print('')
                else:
                    print('Bairro não encontrado, verifique se contém abreviação ou erro ortográfico')
                    print('')
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

print('-------------------------------------------------------------------------------------------')
print('Bem-vido ao projeto "Galo Weather", sistema preventivo para alagamentos nas vias urbanas')
print('-------------------------------------------------------------------------------------------')
print('')
while True:
    traco()
    print('Seja bem vindo ao hub da Galo Weather!')
    traco()
    print('')
    print('1 - Consultar bairros com maior risco')
    print('2 - Notifique algum bairro de risco')
    print('3 - Conheça mais sobre o projeto')
    print('4 - Sair')
    print('')
    try:
        menu = int(input('Insira o número referente a parte que quer acessar: '))
        print('')
        match menu:
            case 1: #Consultar bairros com maior risco
                consultar_bairros()
            case 2: #Notifique algum bairro de risco
                traco()
                print('Opção (2 - Notifique alguma area de risco) escolhida!')
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
                            notificacao_area = input('Notifique qual o bairro de risco: ') #coleta do bairro alagado
                            notificacao_bairro.append(notificacao_area) #Adicionando bairro a lista de notificação de possível enchente
                            causa = input('Se souber qual poderia ser a causa de uma possivel enchente, podeiria descreve-la para nós? ') #coleta da causa
                            causa_risco.append(causa) #armazena a possível causa
                            print('')
                            print('Obrigado pela notificação, voltando para o menu de Notificações!')
                            print('')
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
            case 3: #Conheça mais sobre o projeto
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
                        print('Opção invalida! Tente novamente!')
                        print('')
            case 4: #Sair
                while True:
                    sair = input('Tem certeza que quer sair? (sim/não) ').lower()
                    print('')
                    if sair == 'sim':
                        traco()
                        print('Obrigado pelo seu acesso!')
                        traco()
                        print('')
                        #Histórico de uso da aplicação
                        if len(bairro_pesquisados) == 0 and len(notificacao_bairro) == 0:
                            sys.exit()
                        elif len(bairro_pesquisados) >= 1 and len(notificacao_bairro) == 0:
                            print('Esse é o seu histório no nosso site:')
                            print('')
                            print(f'Procurou esses bairros: {bairro_pesquisados} ')
                            print(f'Nesses respectivos meses: {meses_pesquisados} ')
                            sys.exit()
                        elif len(bairro_pesquisados) == 0 and len(notificacao_bairro) >= 1:
                            print('Esse é o seu histório no nosso site:')
                            print('')
                            print(f'{notificacao_bairro}')
                            print(f'{causa_risco}')
                            sys.exit()
                        else:
                            print('Esse é o seu histório no nosso site:')
                            print('')
                            print(f'Procurou esses bairros: {bairro_pesquisados} ')
                            print(f'Nesses respectivos meses: {meses_pesquisados} ')
                            print('')
                            print('Além de fazer essas notificações: ')
                            print('')
                            print(f'Sobre os seguintes bairros: {notificacao_bairro}')
                            print(f'Tendo as seguintes descrições: {causa_risco}')
                            sys.exit()
                    elif sair == 'não':
                        print('Ok, voltando para o menu!')
                        print('')
                        break
                    else:
                        error()
                        print('')
            case _:
                error()
                print('')
    except ValueError:
        print('')
        error()
        print('')