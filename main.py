import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import cv2

# Carregar uma imagem de fundo para o certificado usando OpenCV
background_image = cv2.imread('fundo_certificado.png')

data = pd.read_csv('lista_de_nomes.csv')

for index, row in data.iterrows():
    nome = row['Nome']
    curso = row['Curso']  # Nova coluna "Curso"
    
    certificado = canvas.Canvas(f'certificado_{nome}.pdf', pagesize=letter)
    
    # Adicionar a imagem de fundo (usando OpenCV)
    certificado.drawImage('fundo_certificado.png', 0, 0, width=letter[0], height=letter[1])
    
    # Definir cor da letra como branco e tamanho da fonte como 25
    certificado.setFont("Helvetica", 25)
    certificado.setFillColorRGB(1, 1, 1)  # Branco
    
    # Obter largura e altura do texto
    text_width = certificado.stringWidth(f"Certificado para {nome}", "Helvetica", 25)
    text_height = 25  # Tamanho da fonte
    
    # Coordenadas para centralizar o texto no meio da página
    x = (letter[0] - text_width) / 2
    y = (letter[1] - text_height) / 2
    
    # Adicionar texto personalizado centralizado
    certificado.drawString(x, y, f"Certificado para {nome}")
    certificado.drawString(x, y - text_height - 10, f"Curso: {curso}")  # Adiciona o curso
    
    # Adicione mais informações e design ao certificado
    certificado.save()
