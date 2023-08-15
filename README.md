```markdown
# Automatização de Certificados usando Python

Este projeto demonstra a automatização da criação de certificados usando Python, OpenCV e ReportLab.

## Como Executar

1. **Pré-requisitos:** Certifique-se de ter o Python instalado em sua máquina.

2. **Clone o Repositório:**
   ```sh
  [ git clone https://github.com/faellm/gerador-certificado.git](https://github.com/faellm/gerador-certificado.git)
   cd SEU_REPOSITORIO
   ```

3. **Instale as Dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Imagem de Fundo:**
   Coloque a imagem de fundo para os certificados no diretório do projeto com o nome `fundo_certificado.png`.

5. **Lista de Nomes e Cursos:**
   Crie um arquivo CSV chamado `lista_de_nomes.csv` contendo os nomes e cursos dos participantes.

6. **Execute o Script:**
   No terminal, execute o seguinte comando para gerar os certificados:
   ```sh
   python main.py
   ```

Os certificados gerados serão salvos individualmente em formato PDF no mesmo diretório.

## Personalização

- Você pode personalizar o design dos certificados alterando a imagem de fundo (`fundo_certificado.png`).
- Adapte o modelo de certificado no script `main.py` conforme necessário.

## Dúvidas ou Contribuição

Se você tiver alguma dúvida sobre a execução do código ou desejar contribuir com melhorias, sinta-se à vontade para entrar em contato ou abrir uma issue neste repositório.
