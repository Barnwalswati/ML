import plotly.express as px
# import plotly.io as pio
# pio.renderers.default = "chrome"
import plotly.io as pio
print(pio.renderers)

df = px.data.iris()
fig = px.scatter(df,x='sepal_width',y='sepal_length',color='species')
fig.show()