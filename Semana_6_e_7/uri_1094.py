def main():
   n_testes = int(input("Número de testes: "))
   testes = ""
   qnt = []
   tipo = []
   cobaias = 0
   coelho = 0
   sapo = 0
   rato = 0

   for i in range(n_testes):
       testes += " " + input("Quantidade e Tipo: ")
       i += 1

   for k in range(n_testes):
       dados = testes.split()
       qnt.append(int(dados[2*k]))
       tipo.append(str(dados[2*k+1]))

   for j in range(n_testes):
       cobaias += qnt[j]
       if tipo[j] == 'C':
           coelho += qnt[j]
       elif tipo[j] == 'S':
           sapo += qnt[j]
       elif tipo[j] == 'R':
           rato += qnt[j]
       j+=1
   
   perc_coelho = 100*coelho/cobaias
   perc_rato = 100*rato/cobaias
   perc_sapo = 100*sapo/cobaias

   print("Total: %d cobaias" %cobaias)
   print("Total de coelhos: %d" %coelho)
   print("Total de ratos: %d" %rato)
   print("Total de sapos: %d" %sapo)
   print("Percentual de coelhos: %.2f " %perc_coelho,"%")
   print("Percentual de ratos: %.2f " %perc_rato,"%")
   print("Percentual de sapos: %.2f " %perc_sapo,"%")

main()