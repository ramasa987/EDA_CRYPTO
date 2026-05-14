# 📊 **ANALISIS RETANBILIDAD DE CRIPTOACTIVOS EN 2025**

**Autor:** Raúl Marcos Sánchez 

**Fecha:** 15 Mayo 2026

## 🌟 Descripción del Proyecto
Este proyecto presenta un análisis exploratorio de datos (EDA) de la rentabilidad de los 5 criptoactivos del mercado en el año 2025. El proyecto lo dividiremos en 2 partes. 

## 1.ANALISIS Y SELECCION 🔎.
El objetivo del ranking es seleccionar los 5 criptoactivos más relevantes del mercado, no los más rentables, sino los más sólidos, líquidos y representativos.
**Los pesos se asignan según la importancia real de cada métrica en el mercado cripto.**
Los criterios definidos son:
- Market Cap → 40%
- Total Volumen → 30%
- Volatility_24h → 20%
- ATH_distance → 10%

## 2.ESTUDIO DE RENTABILIDAD 💲.
**Para comprobar que criptoactivo de los 5 elegidos es mas retable en el periodo de 2025. Realizo un analisis de retabilidad de los criptoactivos seleccionados, estableciendo unas hipotesis. Las metricas utlizadas son:**
- Rentabilidad Anual.
- Volatilidad.
- Máximo Drawdown.
- Sharpe Ratio

## 3.HIPOTESIS 💲.

**🧪 Hipótesis 1 — Rentabilidad anual**
H0: No existen diferencias significativas en la rentabilidad anual entre los 5 criptoactivos. 
H1: Al menos uno de los 5 criptoactivos presenta una rentabilidad significativamente mayor en 2025.
Métrica: Rentabilidad anual=Preciofin_2025−Precioinicio_2025Precioinicio_2025

**🧪 Hipótesis 2 — Volatilidad vs Rentabilidad**
H0: La volatilidad diaria promedio en 2025 no está relacionada con la rentabilidad anual. 
H1: Existe una correlación significativa entre volatilidad y rentabilidad.
Métrica: desviación estándar de los retornos diarios.

**🧪 Hipótesis 3 — Máximo drawdown**
H0: Los 5 criptoactivos tienen drawdowns similares durante 2025.
H1: Al menos uno presenta un drawdown significativamente menor (mejor perfil de riesgo).

**🧪 Hipótesis 4 — Sharpe Ratio**
H0: No hay diferencias significativas en el Sharpe Ratio entre los 5 activos. 
H1: Uno de los activos tiene un Sharpe Ratio superior, indicando mejor relación riesgo–retorno.
Sharpe Ratio: SR=Ractivo−Rfσ 
(Usa Rf=0 si no tienes tasa libre de riesgo).

# 🧠4.SINTESIS.
Selección de activos  
A partir del dataset top_500_metadata.csv se seleccionaron cinco criptoactivos mediante un ranking multicriterio basado en capitalización de mercado, volumen de trading, volatilidad en 24 horas y distancia al máximo histórico (ATH). Esta metodología permitió identificar los activos más relevantes y líquidos del mercado en 2025.

Rentabilidad y riesgo en 2025  
El análisis de la serie temporal (crypto_ohlc.csv) muestra que el activo BNB fue el más rentable en 2025, con una rentabilidad anual aproximada del [23.92%]. Sin embargo, su volatilidad diaria fue media del 5% en comparación con el resto de activos.

El máximo drawdown indica que BTC presentó el perfil de riesgo MEDIO, con una caída máxima aproximada del [30,85%], mientras que ETH sufrió las mayores pérdidas en términos de caídas desde máximos con caidas del 59%.

Sharpe Ratio y relación riesgo–retorno  
El Sharpe Ratio revela que BNB ofreció la mejor relación riesgo–retorno, combinando una rentabilidad atractiva con una volatilidad relativamente contenida. Esto sugiere que, desde una perspectiva de inversión racional, BNB habría sido el candidato más eficiente para una cartera en 2025.

Correlaciones y diversificación  
El análisis de correlaciones entre retornos diarios muestra que los activos presentan una ALTA correlación entre sí. Esto implica que la combinación de BTC y ETH, por ejemplo, podría mejorar la diversificación de una cartera al no moverse de forma completamente sincronizada.

# 🏁 5. Conclusión final
🥇 El mejor criptoactivo en 2025 fue BNB.
-Fue el único con rentabilidad positiva significativa (+23.9%).
-Tuvo un Sharpe Ratio superior al resto (excluyendo USDT por datos corruptos).
-Su drawdown fue moderado comparado con ETH y XRP.
-Su volatilidad fue razonable.

🥈 BTC fue el activo más estable, pero con rentabilidad negativa.

🥉 ETH y XRP fueron los más arriesgados, con drawdowns muy altos y rentabilidades negativas.

❌ USDT debe excluirse del análisis: Los datos de volatilidad y drawdown están claramente dañados.

---
Este archivo README es un resumen del análisis completo. Si deseas explorar los gráficos y datos en mayor detalle, te invito a consultar los notebooks y recursos visuales disponibles en el repositorio. 🎨📊
H0: El momentum de 90 días no predice la rentabilidad futura en 2025. 
H1: El momentum de 90 días está asociado con mayor rentabilidad posterior.
