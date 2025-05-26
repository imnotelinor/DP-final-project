## Date of entry: 2025-05-18

**What I’ve worked on:**
- Reviewed the project brief and research questions about fertility and life expectancy in Asian countries.
- Downloaded and explored the Gapminder dataset to understand available variables and structure.
- Planned the visualization approach: an interactive bubble chart showing fertility vs life expectancy by year and region.

**What problems I encountered:** 
- Understanding how to handle multi-year data efficiently for interaction.
- Figuring out the best way to filter the dataset for Asian countries and relevant years.

**What I learned:**
- How to load and preprocess data using pandas for Bokeh visualization.
- The importance of structuring data for fast filtering and updates.

**Which resources did I use:**
- [Gapminder dataset documentation](https://www.gapminder.org/data/)
- [Bokeh introductory tutorials](https://docs.bokeh.org/en/latest/index.html)

## Date of entry: 2025-05-19

**What I’ve worked on:**
- Started coding the initial Bokeh plot: set up figure, axis labels, and basic scatter plot.
- Created a ColumnDataSource from filtered data for the first year (2000).
- Added bubbles sized by population and colored by region.

**What problems I encountered:** 
- Issues with correctly mapping colors to regions.
- Figuring out appropriate bubble size scaling for better visualization.

**What I learned:**
- Issues with correctly mapping colors to regions.
- Figuring out appropriate bubble size scaling for better visualization.

**Which resources did I use:**
- [Bokeh documentation on glyphs and ColumnDataSource](https://docs.bokeh.org/en/latest/docs/gallery.html)
- [Color palette references](https://docs.bokeh.org/en/latest/docs/reference/colors.html)


## Date of entry: 2025-05-20

**What I’ve worked on:**
- Added interactivity: year slider, region dropdown filter.
- Connected widgets to update plot with .on_change() callbacks.
- Added hover tool with rich country info (Fertility, Life Expectancy, Population).

**What problems I encountered:**
- Callback functions for slider and dropdown did not update the plot initially.
- Confusion on how to properly update ColumnDataSource inside callbacks.

**What I learned:**
- The correct way to update ColumnDataSource data with .data assignment.
- How to connect widget events with plot updates using .on_change().

**Which resources did I use:**
- [Bokeh callback documentation](https://docs.bokeh.org/en/latest/docs/examples/interaction/js_callbacks/slider.html)
- [Example Bokeh with interactive widgets](https://docs.bokeh.org/en/latest/docs/examples/interaction/js_callbacks/color_sliders.html)
  

## Date of entry: 2025-05-21

**What I’ve worked on:**
- Embedded the Bokeh server directly in a Jupyter notebook using bokeh.io.show and bokeh.server.
- Restructured layout using column() and row() for clean design.
- Made plot reactive to all input.

**What problems I encountered:**
- Setting up and running Bokeh server correctly.
- Minor bugs with data filtering logic in callbacks.

**What I learned:**
- How to embed and run a Bokeh server in Jupyter Notebook, manage sessions, and route layout functions.

**Which resources did I use:**
- [Embedding a Bokeh server in a Notebook](https://github.com/bokeh/bokeh/blob/3.7.3/examples/server/api/notebook_embed.ipynb)
- [Bokeh server documentation](https://docs.bokeh.org/en/latest/docs/gallery.html)
- [Examples of the Bokeh repository](https://github.com/bokeh/bokeh/tree/3.7.3/examples)

## Date of entry: 2025-05-22

**What I’ve worked on:**
- Added a DataTable below the scatter plot, linked to the same ColumnDataSource.
- Synced selections between plot and table.
- Enhanced visual clarity by defining distinct color palettes per region.

**What problems I encountered:**
- Linking the data table with the plot required careful handling of shared data sources.
- Adjusting bubble sizes for better visual effect with population scaling.

**What I learned:**
- How to integrate DataTable with ColumnDataSource in Bokeh.
- Importance of visual hierarchy in interactive plots.

**Which resources did I use:**
- [Bokeh examples on DataTable](https://docs.bokeh.org/en/latest/docs/examples/interaction/linking/data_table_plot.html)
- [Online tutorial for Data Sources and Transformation](https://raw.githubusercontent.com/spcourse/dataproject/main/bokeh/notebooks/3.bokeh_data_sources.ipynb)

## Date of entry: 2025-05-23

**What I’ve worked on:**
- Improved bubble sizing using square root of population for more natural scaling.
- Intergrated data transformation in a single make_data(year, region) function.
- Implemented Play/Pause buttons to animate through years with add_periodic_callback().

**What problems I encountered:**
- Adjusting bubble sizes required careful transformation to avoid overwhelming visual imbalance.
- Setting up the animation loop required managing periodic callbacks with Bokeh’s server.

**What I learned:**
- How to scale bubble sizes effectively using square root transformation in make_data().
- How to implement basic animation in Bokeh using add_periodic_callback() and remove_periodic_callback().

**Which resources did I use:**
- [Bokeh examples on DataTable](https://docs.bokeh.org/en/latest/docs/examples/interaction/linking/data_table_plot.html)
- [Examples of the Bokeh repository](https://docs.bokeh.org/en/latest/docs/gallery.html#gallery)


## Date of entry: 2025-05-24

**What I’ve worked on:**
- Developed a secondary line plot for selected country trends (Fertility & Life Expectancy).
- Set up dual y-axes with different scales for both metrics.
- Created responsive update based on country dropdown.

**What problems I encountered:**
- Plotting two different metrics with distinct.
- Ensuring the dual-axis chart updated correctly upon changing country selection.

**What I learned:**
- How to configure dual y-axes in Bokeh.
- How to synchronize dropdown selection with trend line updates.

**Which resources did I use:**
- [Bokeh guide on Ranges and axes](https://docs.bokeh.org/en/latest/docs/user_guide/basic/axes.html)
- [Examples for demographic trend plotting](https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html)


## Date of entry: 2025-05-25
  
**What I’ve worked on:**
- Finalized layout, added titles, and adjusted tooltips and labels for clarity.
- Added comments to the notebook.
- Pushed complete project to GitHub with process book.md, gapminder.txt, and viz.ipynb notebook.

**Problems I encountered:**
- Had to restructure folders and manage version control with Git.

**What I learned:**
- [Git lecture](https://www.youtube.com/watch?v=NcoBAfJ6l2Q)
- [Bokeh server reference](https://docs.bokeh.org/en/latest/docs/reference/server.html)
  

  
