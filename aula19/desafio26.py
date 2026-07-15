# Criar a estrutura capaz de calcular salários de funcionários diferentes

# |Funcionario{abstract}
# |+nome
# |+sal_bruto
# |+salario
# |+sal_min = 1612
# |+inss = 7,5
# ================
# |+calc_sal() {abstract}
# |+analisar_sal()


# |Horista(Funcionario)
# |+valor_hora
# |+horas_trab
# ================
# |+calc_sal()

# |Mensalista(Funcionario)
#
# ================
# |+calc_sal()