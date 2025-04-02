from PIL import Image
import numpy as np

def AlturaDaFigura(caminho_imagem):
    
    imagem = Image.open(caminho_imagem).convert("L")
    QC, QL = imagem.size # QC = largura, QL = altura
    total_pixels = QL * QC
    alturaPixels = 0
    imagem = np.asarray(imagem)
    print("Total de pixels da altura ", QL)
    #print(imagem)
    for i in range(QL):
        for j in range(QC):
            if imagem[i][j] < 100:
                alturaPixels += 1
                break
    
    
    return alturaPixels

def AlturaDaFiguraAlternativo(caminho_imagem):
    imagem = Image.open(caminho_imagem).convert("L")
    QC, QL = imagem.size # QC = largura, QL = altura
    total_pixels = QL * QC
    alturaPixels = 0
    alturaAuxiliar = 0

    imagem = np.asarray(imagem)
    print("Total de pixels da altura ", QL)
    indiceColuna = 0
    
    while alturaAuxiliar < QL:
        if indiceColuna < QC and imagem[alturaAuxiliar, indiceColuna] < 100:
            alturaPixels += 1
            alturaAuxiliar += 1
            indiceColuna = 0  
        elif indiceColuna >= QC - 1:  
            alturaAuxiliar += 1
            indiceColuna = 0  
        else:
            indiceColuna += 1 

    return alturaPixels
            

caminho = "img/ponto.png"
print(f"Total de pixels da altura da figura: {AlturaDaFiguraAlternativo(caminho)}")
