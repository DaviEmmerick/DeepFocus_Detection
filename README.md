# 📌 Visão Computacional & Deep Learning

🎯 Sobre o Projeto
Este repositório serve como um portfólio prático, demonstrando a aplicação de algoritmos clássicos e redes neurais profundas para resolver problemas do mundo real.

O projeto está dividido em duas partes principais:

Odometria Visual com ICP (Iterative Closest Point): O objetivo é desenvolver um algoritmo capaz de estimar a trajetória de um veículo. Para isso, implementamos o ICP do zero, um método fundamental em robótica e visão computacional para alinhar nuvens de pontos 3D ou conjuntos de features 2D. Ele calcula iterativamente a transformação de rotação e translação entre dois frames consecutivos.

Detecção de Máscaras com DeepFace: Utilizando um modelo de Deep Learning pré-treinado da biblioteca deepface, este módulo analisa uma imagem de entrada e determina se a pessoa detectada está usando uma máscara de proteção. É uma demonstração de como modelos complexos podem ser facilmente integrados para tarefas de análise de atributos faciais.

# ✨ Funcionalidades

1. Projeção de Trajetória Veicular: Implementação de um algoritmo Iterative Closest Point (ICP) do zero para estimar o deslocamento de um veículo a partir de dados visuais sequenciais.
2. Detecção de Uso de Máscara: Análise de imagens para identificar se pessoas estão utilizando máscaras de proteção, com o auxílio da biblioteca deepface.

# ✏️ Tecnologias Utilizadas

• Python 3.x

• OpenCV (cv2) para processamento de imagem

• Trimesh para manipulação de geometrias 3D

• Scipy e NumPy para cálculos científicos e otimizações

• Matplotlib para visualização de dados e trajetórias

• DeepFace para análise facial e detecção de atributos

• Jupyter Notebook para experimentação e desenvolvimento

## 🚀 Como Rodar o Projeto

1️⃣ Crie e ative um ambiente virtual:
É altamente recomendado criar um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

2️⃣ Clone o repositório e acesse a pasta correta:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_DIRETORIO>
```

2️⃣ Instalação:

```bash
pip install -r requirements.txt
```

2️⃣ Execução:

1. Adicione as imagens que deseja processar na pasta database/ (ou na pasta designada no código).
2. Execute o script principal:

```bash
python run.py
```

# ✨ Implementações Futuras

-> Pretendo melhorar a acurácia da estimativa de trajetória do veículo
-> Provavelmente vou disponibilizar no hugging face para a comunidade usar

# 📄 Liçenca

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
