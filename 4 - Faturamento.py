sp = float(67836.43)
rj = float(36678.66)
mg = float(29229.88)
es = float(27165.48)
outros = float(19849.53)
total = float(sp + rj + mg + es + outros)

psp = (sp / total) * 100
prj = (rj / total) * 100
pmg = (mg / total) * 100
pes = (es / total) * 100
poutros = (outros / total) * 100

print('O valor total de faturamento foi de R$ {}, onde:'
      '\n'
      '\nSão Paulo corresponde à {:.2f}%'
      '\nRio de Janeiro corresponde à {:.2f}%'
      '\nMinas Gerais corresponde à {:.2f}%'
      '\nEspírito Santo corresponde à {:.2f}%'
      '\nOutros corresponde à {:.2f}%'.format(total, psp, prj, pmg, pes, poutros))
