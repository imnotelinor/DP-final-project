## Project Description

**Introduction**

This project aims to explore how fertility rates and life expectancy have changed over time in Asian countries between 2000 and 2013. Fertility rates and life expectancy are two of the most fundamental indicators of a country's demographic and developmental status. They are closely linked to broader themes, such as public health, policy development, and social change. I chose to focus on Asian countries because the region includes a wide range of economic and cultural contexts (ranging from rapidly developing nations to high-income countries). Therefore, I wanted to explore how these two variables relate to each other in different Asian countries between 2000 and 2013. As part of our Data Processing course, I created an interactive visualization using the Bokeh library that helps users investigate patterns and relationships between these two key demographic indicators, and how they might reflect broader social and economic changes.

**Research question:** How did fertility rates and life expectancy change across Asian countries between 2000 and 2013, and is there a noticeable correlation between these two indicators?

**Sub-Question:** Are there clear regional differences within Asia (e.g., between South Asia, East Asia & Pacific, and Europe & Central Asia) in the relationship between fertility and life expectancy?

**Data Used for visualization**

To answer my research question, I used part of gapminder dataset. I focused on data from 2000 to 2013, specifically looking at Asian countries. The dataset includes values for fertility rate (children per woman), life expectancy (in years), population size and country ID, which were all necessary for building the visualization. I filtered out only Asian countries and cleaned the data to make sure it was consistent across all selected years. 
The core of the project is a dynamic bubble chart, where each bubble’s x-position indicates the fertility rate, the y-position shows life expectancy, and the size of the bubble reflects the population. Users can filter by region, select a specific year using a slider, and even animate the chart through time to watch demographic changes unfold. A second figure allows users to select a country and track its trends in both fertility and life expectancy over time using a dual-axis line chart.

**Answer the research question**

The interactive visualization clearly answers both the main and sub research questions.
By observing the bubble chart, where the x-axis represents fertility rate and the y-axis shows life expectancy, we can see a clear inverse relationship: as fertility decreases, life expectancy tends to increase. This pattern holds for most Asian countries over the years 2000 to 2013. The trend becomes particularly evident when using the interactive year slider to animate changes over time. For example, countries such as Hong Kong, Japan, and Singapore consistently appear on the top-left of the plot, representing low fertility and high life expectancy. On the other hand, countries like Pakistan and Afghanistan initially appear toward the bottom-right, showing higher fertility and lower life expectancy, though they shift slightly toward the center in later years, indicating some improvement.
The color coding of the bubbles by region (red for South Asia, green for Europe & Central Asia, and blue for East Asia & Pacific) helps answer the sub-question. East Asia & Pacific countries (e.g., Taiwan, South Korea, and Hong Kong) mostly cluster in the low fertility–high life expectancy quadrant, suggesting advanced development and aging populations. In contrast, South Asia shows a more dispersed pattern, with some countries like India moving leftward and upward over time—indicating improving conditions, but still relatively high fertility compared to East Asia. Europe & Central Asia tends to have moderate fertility and relatively high life expectancy, forming a middle ground between the other two regions. The bubble sizes, which represent population, further enrich the analysis. Large bubbles like India and China dominate visually, showing how demographic giants can influence regional averages. 
The data table and line chart below the graph provide additional support for tracking specific countries. For example, selecting Taiwan in the dropdown and reviewing its line chart shows how its fertility remained low while life expectancy continued to rise, reinforcing the bubble chart insights.
In conclusion, the visualization successfully demonstrates that in Asia, from 2000 to 2013, fertility and life expectancy are inversely related, and this relationship varies across regions.

**Reflection on the Design**

Overall, I believe the key elements are present in the visualization. The x-axis represents fertility rates, the y-axis represents life expectancy, and each country is plotted as a bubble whose size reflects its population. Additionally, the bubbles are color-coded by region, which helps users easily identify and compare trends across South Asia, East Asia & Pacific, and Europe & Central Asia. The interactive slider allows users to move through the years from 2000 to 2013, making temporal changes visible. The hover tool provides exact values for each country, which makes exploration intuitive and informative. The data table and line chart also update dynamically, which adds depth to the visualization and supports more detailed investigation.
However, if I were to redesign the visualization, I would consider a few improvements. One limitation is that there is no legend to explain what the bubble sizes mean. While the population-based sizing is visually effective, the absence of a legend might confuse users who are less familiar with interpreting bubble charts. Including a legend or a tooltip explaining the scale would make the design more user-friendly. I would also enhance the usability of the line chart by allowing users to select multiple countries at once, making regional comparisons easier over time. 







