import ee

# Inicializa a biblioteca
ee.Initialize()
# Substitua 'seu-projeto-id' pelo ID que aparece no console do Google Cloud
ee.Initialize(project='credit-scoring-verde')


# Coordenadas aproximadas de uma área de SAF em Tomé-Açu
lon = -48.46
lat = -2.29
ponto = ee.Geometry.Point([lon, lat])

# Busca a imagem mais recente do satélite Sentinel-2 (Nível 2A - corrigida)
imagem = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
          .filterBounds(ponto)
          .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10)) # Filtra nuvens
          .sort('system:time_start', False) # Pega a mais recente
          .first())

# Calcula o NDVI: (Infravermelho Próximo - Vermelho) / (Soma deles)
ndvi = imagem.normalizedDifference(['B8', 'B4']).rename('NDVI')

# Extrai o valor do NDVI no ponto específico
info = ndvi.sample(ponto, 10).first().getInfo()

print(f"--- Conexão com Tomé-Açu Estabelecida ---")
print(f"Data da Imagem: {imagem.date().format('YYYY-MM-dd').getInfo()}")
print(f"Valor do NDVI no ponto: {info['properties']['NDVI']:.4f}")
print("-----------------------------------------")
