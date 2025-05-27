from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, Select, HoverTool, TableColumn, DataTable, NumberFormatter, Button, Div, LinearAxis, Range1d
from bokeh.plotting import figure
import pandas as pd

# Load and filter dataset
df = pd.read_csv('gapminder.txt')
df = df[(df['Year'] >= 2000) & (df['Year'] <= 2013)]
asian_df = df[df['Region'].str.contains('Asia')].copy()

# Color mapping for regions
color_map = {
    "South Asia": "#e45756",
    "East Asia & Pacific": "#4c78a8",
    "Europe & Central Asia": "#72b7b2"
}

regions = sorted(asian_df['Region'].unique())
years = sorted(asian_df['Year'].unique())
initial_year = years[0]

# Create year-region filtered data with scaled bubble size
def make_data(year, region="All"):
    data = asian_df[asian_df['Year'] == year]
    if region != "All":
        data = data[data['Region'] == region]
    pop_mil = data['pop'] / 1e6
    return {
        'Fertility': data['Fertility'].tolist(),
        'lifeExp': data['lifeExp'].tolist(),
        'Country': data['Country'].tolist(),
        'pop_mil': pop_mil.tolist(),
        'bubble_size': (5 + 2 * (pop_mil**0.5)).tolist(),  # Scaled size
        'Region': data['Region'].tolist(),
        'ID': data['ID'].tolist(),
        'color': data['Region'].map(color_map).fillna("#bab0ab").tolist()
    }

# Set up data source
source = ColumnDataSource(data=make_data(initial_year))

# Country trend line source
line_source = ColumnDataSource(data={"Year": [], "Fertility": [], "lifeExp": []})

# Create plot
p = figure(
    height=500, width=850,
    title=f"Fertility vs Life Expectancy in Asia ({initial_year})",
    x_axis_label="Fertility Rate",
    y_axis_label="Life Expectancy",
    tools="pan,wheel_zoom,box_zoom,reset"
)

# Add scatter plot with scaled bubble sizes
p.scatter(
    x="Fertility", y="lifeExp", size="bubble_size", source=source,
    color="color", fill_alpha=0.6, line_color=None, legend_field="Region"
)

# Hover tool
hover = HoverTool(tooltips=[
    ("Country", "@Country"),
    ("Region", "@Region"),
    ("Fertility", "@Fertility"),
    ("Life Exp", "@lifeExp"),
    ("Population (mil)", "@pop_mil"),
    ("ID", "@ID")
])
p.add_tools(hover)

# Widgets
slider = Slider(start=years[0], end=years[-1], value=initial_year, step=1, title="Year")
dropdown = Select(title="Region", value="All", options=["All"] + regions)
country_select = Select(title="Select a Country", value="Afghanistan", options=sorted(asian_df['Country'].unique()))
play_button = Button(label="► Play", width=60, button_type="success")
pause_button = Button(label="❚❚ Pause", width=60, button_type="warning")

# Dual Y-Axis Trend Line Plot
trend_fig = figure(height=250, width=850, title="Trends for Selected Country",
                   x_axis_label="Year", y_axis_label="Fertility Rate")
trend_fig.extra_y_ranges = {"life": Range1d(start=40, end=90)}
trend_fig.add_layout(LinearAxis(y_range_name="life", axis_label="Life Expectancy"), 'right')

trend_fig.line(x="Year", y="Fertility", source=line_source, color="orange", legend_label="Fertility Rate", line_width=2)
trend_fig.line(x="Year", y="lifeExp", source=line_source, y_range_name="life", color="green", legend_label="Life Expectancy", line_width=2)
trend_fig.legend.location = "top_left"

# Info box for changes
change_info = Div(text="", width=850)

# Update function
def update(attr, old, new):
    year = slider.value
    region = dropdown.value
    new_data = make_data(year, region)
    source.data = new_data
    p.title.text = f"Fertility vs Life Expectancy in Asia ({year})"


# Update country to drop missing values before plotting
def update_country(attr, old, new):
    country = country_select.value
    df_country = asian_df[asian_df['Country'] == country].dropna(subset=["Fertility", "lifeExp"])
    if not df_country.empty:
        line_source.data = {
            "Year": df_country["Year"],
            "Fertility": df_country["Fertility"],
            "lifeExp": df_country["lifeExp"]
        }
    else:
        line_source.data = {"Year": [], "Fertility": [], "lifeExp": []}

def update_change_info():
    country = country_select.value
    df_country = asian_df[asian_df['Country'] == country]

    start = df_country[(df_country["Year"] == 2000) & df_country["Fertility"].notna() & df_country["lifeExp"].notna()]
    end = df_country[(df_country["Year"] == 2013) & df_country["Fertility"].notna() & df_country["lifeExp"].notna()]

    if not start.empty and not end.empty:
        fert_change = end["Fertility"].values[0] - start["Fertility"].values[0]
        life_change = end["lifeExp"].values[0] - start["lifeExp"].values[0]
        text = f"<b>{country} (2000–2013)</b>:<br>Fertility: {fert_change:.2f}<br>Life Expectancy: {life_change:.2f}"
        change_info.text = text
    else:
        change_info.text = f"<b>{country}</b>: Insufficient data to compute changes from 2000 to 2013."

def update_all(attr, old, new):
    update(attr, old, new)
    update_country(attr, old, new)
    update_change_info()

slider.on_change('value', update_all)
dropdown.on_change('value', update_all)
country_select.on_change('value', update_all)

update_country(None, None, None)
update_change_info()


# Data table
columns = [
    TableColumn(field="Country", title="Country"),
    TableColumn(field="Fertility", title="Fertility", formatter=NumberFormatter(format="0.00")),
    TableColumn(field="lifeExp", title="Life Expectancy", formatter=NumberFormatter(format="0.0")),
    TableColumn(field="pop_mil", title="Population (mil)", formatter=NumberFormatter(format="0.0")),
    TableColumn(field="Region", title="Region"),
    TableColumn(field="ID", title="ID")
]
data_table = DataTable(source=source, columns=columns, width=850, height=250)

# Play/Pause animation
callback_id = None

def animate():
    year = slider.value + 1
    if year > years[-1]:
        year = years[0]
    slider.value = year

def start_animation():
    global callback_id
    if callback_id is None:
        callback_id = curdoc().add_periodic_callback(animate, 500)

def stop_animation():
    global callback_id
    if callback_id is not None:
        curdoc().remove_periodic_callback(callback_id)
        callback_id = None

play_button.on_click(start_animation)
pause_button.on_click(stop_animation)

# Layout
layout = column(row(slider, dropdown),row(play_button, pause_button), p, data_table, change_info, row(country_select), trend_fig)
curdoc().add_root(layout)
curdoc().title = "Gapminder Asia"
