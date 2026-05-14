# 📊 **ANALISIS RETANBILIDAD DE CRIPTOACTIVOS EN 2025**

**Autor:** Raúl Marcos Sánchez 

**Fecha:** 15 Mayo 2026

## 🌟 Descripción del Proyecto
Este proyecto presenta un análisis exploratorio de datos (EDA) de la rentabilidad de los 5 criptoactivos del mercado en el año 2025. El proyecto lo dividiremos en 2 partes. 

## PASO 1: ANALISI Y SELECCION 🔎.
El objetivo del ranking es seleccionar los 5 criptoactivos más relevantes del mercado, no los más rentables, sino los más sólidos, líquidos y representativos.
**Los pesos se asignan según la importancia real de cada métrica en el mercado cripto.**
Los criterios definidos son:
- Market Cap → 40%
- Total Volumen → 30%
- Volatility_24h → 20%
- ATH_distance → 10%

## PASO 2: ESTUDIO DE RENTABILIDAD 💲.
**Para comprobar que criptoactivo de los 5 elegidos es mas retable en el periodo de 2025. Realizo un analisis de retabilidad de los criptoactivos seleccionados, estableciendo unas hipotesis.**

**🧪 Hipótesis 1 — Rentabilidad anual**
H0: No existen diferencias significativas en la rentabilidad anual entre los 5 criptoactivos. 
H1: Al menos uno de los 5 criptoactivos presenta una rentabilidad significativamente mayor en 2025.
Métrica: Rentabilidad anual=Preciofin_2025−Precioinicio_2025Precioinicio_2025

**🧪 Hipótesis 2 — Volatilidad vs Rentabilidad**
H0: La volatilidad diaria promedio en 2025 no está relacionada con la rentabilidad anual. 
H1: Existe una correlación significativa entre volatilidad y rentabilidad.
Métrica: desviación estándar de los retornos diarios.
🧪 Hipótesis 3 — Máximo drawdown
H0: Los 5 criptoactivos tienen drawdowns similares durante 2025.
H1: Al menos uno presenta un drawdown significativamente menor (mejor perfil de riesgo).

🧪 Hipótesis 4 — Sharpe Ratio
H0: No hay diferencias significativas en el Sharpe Ratio entre los 5 activos. 
H1: Uno de los activos tiene un Sharpe Ratio superior, indicando mejor relación riesgo–retorno.
Sharpe Ratio: SR=Ractivo−Rfσ 
(Usa Rf=0 si no tienes tasa libre de riesgo).

🧪 Hipótesis 5 — Momentum
H0: El momentum de 90 días no predice la rentabilidad futura en 2025. 
H1: El momentum de 90 días está asociado con mayor rentabilidad posterior.
