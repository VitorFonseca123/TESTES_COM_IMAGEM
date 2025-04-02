from PIL import Image
import numpy as np

def contar_pixels_figura(caminho_imagem):
    
    imagem = Image.open(caminho_imagem).convert("L")
    QC, QL = imagem.size # QC = largura, QL = altura
    total_pixels = QL * QC
    figura_pixels = 0
    imagem = np.asarray(imagem)
    #print(imagem)
    for i in range(QL):
        for j in range(QC):
            if imagem[i][j] == 0:
                figura_pixels += 1
    
    
    return figura_pixels


caminho = "img/pokeball.jpg"
print(f"Total de pixels da figura: {contar_pixels_figura(caminho)}")
