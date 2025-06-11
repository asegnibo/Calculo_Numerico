# Carregar as bibliotecas necessárias
library(ggplot2)
library(dplyr)

# --- Seus dados ---
x_dados <- 1:60
y_dados <- c(
  144.4, 150.0, 125.8, 94.0, 111.0, 262.2, 149.8, 186.0, 188.4, 231.3,
  341.4, 182.7, 149.6, 82.4, 84.0, 35.9, 40.3, 207.0, 82.4, 250.0,
  237.2, 101.2, 242.7, 60.4, 43.2, 0.0, 1.1, 33.1, 22.3, 17.1,
  115.3, 193.2, 130.4, 397.8, 239.0, 153.6, 141.4, 82.6, 80.8, 15.6,
  11.8, 88.0, 90.0, 196.6, 189.2, 234.2, 55.4, 76.4, 185.4, 362.0,
  198.8, 76.4, 0.0, 44.8, 197.3, 192.8, 73.1, 268.0, 39.0, 15.8
)

# Criar um data frame com os dados originais
dados_df <- data.frame(x = x_dados, y = y_dados)

# --- Passo 1: Criar a função de Spline Cúbica ---
# A função `splinefun` do R base cria uma função de interpolação
# É o equivalente ao `scipy.interpolate.CubicSpline`
cs <- splinefun(x_dados, y_dados, method = "fmm")

# --- Passo 2: Preparar os dados para as camadas do gráfico ---

# 2.1 - Dados para a curva suave da spline
# Criamos uma sequência densa de pontos no eixo X para que a curva fique suave
curva_df <- data.frame(x = seq(1, 60, length.out = 500))
curva_df$y <- cs(curva_df$x) # Usamos a função spline para calcular os valores de Y

# 2.2 - Dados para as faixas verticais (os retângulos)
anos_df <- data.frame(
  Ano = factor(1:5), # Cria um fator para cada ano, que será usado na legenda
  xmin = seq(0.5, 48.5, by = 12),
  xmax = seq(12.5, 60.5, by = 12)
)

# --- Passo 3: Construir o Gráfico com ggplot2 ---

ggplot() +
  
  # Camada 1: Faixas verticais para cada ano (o fundo)
  # Usamos `geom_rect` para desenhar os retângulos
  geom_rect(
    data = anos_df,
    aes(xmin = xmin, xmax = xmax, ymin = -Inf, ymax = Inf, fill = Ano),
    alpha = 0.15 # Transparência
  ) +
  
  # Camada 2: Linha da Spline Cúbica
  geom_line(
    data = curva_df,
    aes(x = x, y = y),
    color = "black",
    linewidth = 1 # Equivalente ao linewidth do matplotlib
  ) +
  
  # Camada 3: Pontos dos dados originais
  geom_point(
    data = dados_df,
    aes(x = x, y = y),
    color = "black",
    size = 1.5
  ) +
  
  # Passo 4: Customização e Rótulos
  labs(
    title = "Interpolação por Spline Cúbica com Anos Destacados (em R)",
    x = "Mês (x)",
    y = "Precipitação (mm)",
    fill = "Ano" # Título da legenda de cores
  ) +
  
  # Define uma paleta de cores manual para as faixas
  scale_fill_manual(values = c("#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd")) +
  
  # Aplica um tema visual limpo
  theme_minimal() +
  
  # Ajustes finos no tema (opcional)
  theme(
    plot.title = element_text(hjust = 0.5, size = 16), # Centraliza o título
    legend.position = "bottom" # Posição da legenda
  )
