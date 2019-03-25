def introducao():
  print("========== JOGO DA VELHA ==========")
  print("Por: Isley Martins e João Vitor\n")
  
  print("=== REGRAS ===")
  print("Jogador 1 = X")
  print("Jogador 2 = O\n")
  
  print("===== Let's Go! =====\n")
  
def mostrar_jogo():
  for i in range(len(jogo)):
  		for j in range(len(jogo[i])):
  			print(jogo[i][j], end = "")
  			if(j<2):
  				print("|", end = "")
  			else:
  				print()

def ganhador(g):
  
  print("\n===== FIM DE JOGO! =====\n")
  if(g==1):
    return "JOGADOR 1 (X) VENCEU !!!"
  else:
    return "JOGADOR 2 (O) VENCEU !!!"

def identificador(j):
  if((j + 1) % 2 != 0):
    print("Jogador 1, sua vez:")
    return 1
  
  else:
    print("Jogador 2, sua vez:")
    return 2

def erros(lin, col):
  
  #ERRO: NÃO FOR NÚMERO
  if lin.isdigit() == False or col.isdigit() == False:
    print("ERRO! O JOGO SÓ ACEITA NÚMEROS\n")
    return False
  else:
    lin = int(lin)
    col = int(col) 
		
  #ERRO: SE FOR <1 OU >3
  if(lin > 3 or lin < 1 or col > 3 or col < 1):
    print("ERRO! SÓ DIGITE NÚMEROS ENTRE 1 E 3!\n")
    return False

  #ERRO: ESPAÇO OCUPADO		
  elif(jogo[lin-1][col-1] == "X" or jogo[lin-1][col-1] == "O"):
    print("ESTE ESPAÇO JÁ ESTÁ OCUPADO, TENTE NOVAMENTE\n")
    return False
    
  else:
    return True

def verificador():
  fim = False
  linha = len(jogo)-1
  coluna = 0
  
  cont = [0, 0, 0, 0]
  par = ["V", "V", "V", "V"]
  
  for i in range(len(jogo)):
    for j in range(len(jogo[i])):
      #Diagonal (Esquerda -> Direita)
      if(i==j and jogo[i][j] != "."):
        if(j==0):
          par[0] = jogo[i][j]
        if(par[0] == jogo[i][j]):
          cont[0]+=1
      
      #Linha
      if(j==0 and jogo[i][j] != "."):
        par[1]=jogo[i][j]
      if(par[1]==jogo[i][j]):
        cont[1]+=1
        
      #Coluna
      if(j==0 and jogo[j][i] != "."):
        par[2]=jogo[j][i]
      if(par[2]==jogo[j][i]):
        cont[2]+=1
    
    #CONTINUAÇÃO DA LINHA
    if(cont[1]<3):
      cont[1]=0
    else:
      fim = True
      
    #CONTINUAÇÃO DA COLUNA
    if(cont[2]==3):
      fim = True
    else:
      cont[2]=0
      
  #CONTINUAÇÃO DA DIAGONAL (Esquerda -> Direita)		
  if(cont[0] == 3):
    fim = True
  else:
    cont[0]=0
    par[0] = "V"
    
  #Diagonal (Direita -> Esquerda)
  while(linha >= 0 and coluna <= len(jogo[0])):
    if(cont[3] == 0 and jogo[linha][coluna] != "."):
      par[3]=jogo[linha][coluna]
      
    if(par[3] == jogo[linha][coluna]):
      cont[3]+=1
      
    linha-=1
    coluna+=1
    
  #CONTINUAÇÃO DA DIAGONAL (Direita -> Esquerda)		
  if(cont[3] == 3):
    fim = True
  else:
    cont[3]=0
    linha = len(jogo)-1
    coluna = 0
    par[3] = "V"
    
  if(fim):
    return True
    
  else:
    return False

jogo = [[".",".","."],
		    [".",".","."],
		    [".",".","."]]

introducao()
mostrar_jogo()

print()

for jogada in range(9):

	#IDENTIFICAÇÃO DO JOGADOR
	vez = identificador(jogada)

	#JOGADOR DIGITA LINHA E COLUNA	
	while(True):
		l = input("Digite a linha (1 a 3):")
		c = input("Digite a coluna (1 a 3):")
		print()
		
		#ERROS
		if(erros(l, c)):
		  break

	if(vez == 1):
		jogo[int(l)-1][int(c)-1] = "X"
	else:
		jogo[int(l)-1][int(c)-1] = "O"

	mostrar_jogo()

	print()

	#IDENTIFICAÇÃO DO GANHADOR
	if (verificador()):
	  print(ganhador(vez))
	  break
	
	#VELHA
	elif(jogada == 8):
		print("DEU VELHA !!!")
		break

	print("\n\n")
