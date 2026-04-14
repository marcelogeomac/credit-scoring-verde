# Credit Scoring Verde 🍫🌴

Solução de Data Science para avaliação de risco de crédito agrícola baseada em critérios ESG, focada nas cadeias produtivas de **Cacau** e **Dendê** na região do Pará.

## 🚀 Objetivo
Desenvolver um algoritmo que utilize dados geoespaciais e indicadores de sustentabilidade para gerar um "Score Verde". O objetivo é facilitar o acesso a crédito para produtores que adotam Sistemas Agroflorestais (SAFs).

## 🛠️ Tecnologias
- **Linguagem:** Python 3.x
- **Dados Satelitais:** Google Earth Engine (Sentinel-2)
- **Análise Geoespacial:** GeoPandas, Rasterio
- **Machine Learning:** Scikit-learn, XGBoost

## 📈 Fontes de Dados
- **CAR (Cadastro Ambiental Rural):** Limites das propriedades.
- **MapBiomas:** Histórico de uso do solo.
- **Copernicus/Sentinel:** Índices de vegetação (NDVI/EVI).

## 📂 Estrutura do Projeto
- `src/`: Scripts de processamento e modelos.
- `notebooks/`: Prototipagem e análise exploratória.
- `data/`: Arquivos shapefiles e bases locais (não versionados).