import plotly.express as px

country = input("Enter the country name: ")
data = {
    'Country': [country],
    'Values': [100]
}
fig = px.choropleth(
    data, 
    locations = "Country",
    locationmode = "Country names",
    color = "Values",
    color_continuous_scale = "Inferno_r",
    title = f"Country Map Highlighting{country}"
)
fig.show()
