# Criar classes capazes de calcular fretes de veículos diferentes

# Transporte(ABC){abstract}
# -distancia
# -frete
# calc_frete(){abstract}

# Moto(Transporte)
# -fator = 0.50
# calc_frete()
# observação -> frete livre independente da distância

# Caminhao(Transporte)
# -fator = 1.20
# calc_frete()
# observação -> frete apenas para distância maiores ou igual a 50km

# Drone(Transporte)
# -fator = 9.50
# calc_frete()
# observação -> frete para distância até 10 km