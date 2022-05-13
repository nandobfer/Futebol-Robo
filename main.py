from computador import visao
from input_sensores import sensores

state = 'still'


def getBall(visao):
    ''' Função recebe a visão do computador e retorna
    a posição da bola em X'''
    return position


def motores(speed, motor):
    ''' Função recebe por parâmetro uma velocidade e um motor 
    e envia o comando de ativação do motor pro módulo de integração 
    com o microcontrolador'''
    return True


def ajustarPosicao():
    ''' Função para ajustar a posição do robô após girar
    para algum dos lados'''
    return True


def girar(direcao):
    ''' Função para girar o goleiro para algum lado '''
    if direcao == 'direita':
        motores(speed, esquerda)
        motores(0, direita)

    elif direcao == 'esquerda':
        motores(speed, direita)
        motores(0, esquerda)

    ajustarPosicao()
    return True


def mirarBola(posicao_da_bola, posicao_goleiro):
    ''' Função para manter o robô de frente para a bola '''
    if posicao_da_bola > posicao_goleiro:
        girar('direita')
    elif posicao_goleiro > posicao_da_bola:
        girar('esquerda')

    return True


def mainLoop():
    ''' Loop principal do robô '''
    posicao_da_bola = getBall(visao)
    mirarBola(posicao_da_bola, self.position)
