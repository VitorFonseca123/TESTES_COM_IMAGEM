from PIL import Image
import numpy as np

def AlturaDaFigura(caminho_imagem):
    
    imagem = Image.open(caminho_imagem).convert("L")
    QL, QC = imagem.size
    total_pixels = QL * QC
    alturaPixels = 0
    imagem = np.asarray(imagem)
    
    #print(imagem)
    for i in range(QL):
        for j in range(QC):
            if imagem[i][j] < 100:
                alturaPixels += 1
                break
    
    
    return alturaPixels


caminho = "img/ponto.png"
print(f"Total de pixels da figura: {AlturaDaFigura(caminho)}")
