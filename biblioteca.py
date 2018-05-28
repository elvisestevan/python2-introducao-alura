def gera_nome_convite(nome):
    posicao_final = len(nome)
    posicao_inicial =  posicao_final - 4
    parte1 = nome[0:4]
    parte2 = nome[posicao_inicial:posicao_final]
    return parte1 + " " + parte2

def envia_convite(nome_convidado):
    print "Convite enviado ao: %s" % nome_convidado

def processa_convite(nome):
    nome_formatado = gera_nome_convite(nome)
    envia_convite(nome_formatado)
