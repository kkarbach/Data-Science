# Project 1: Boston and Seattle Airbnb market analysis

Check out the [blog post!](https://medium.com/@keegankarbach_3270/growing-money-in-the-airbnb-market-01635cfbfb07)

This project looks at Airbnb data sets from the Boston and Seattle markets to answer
 - What is the distribution of property and room types in each market and how do they compare?
 - How does property or room type affect rental price? Do both markets have similar patterns?
 - How does location factor into pricing? Are there any geographical patterns with property and room types?
 - What features of the data most affect the rental price?
   
## Software and libraries used

This project was completed using Jupyter Lab v3.5.3 running Python v3.11.9 and the following Python packages:
| Package     |   Version   |
| ----------- | ----------- |
| Numpy       |   v1.26.4   |
| Pandas      |   v2.2.2    |
| Seaborn     |   v0.13.2   |
| Plotly      |   v5.21.0   |
| Matplotlib  |   v3.8.4    |
| Kaggle      |   v1.6.12   |
| Scikit-learn|   v1.4.2    |
| Statsmodels |    v0.14.1  |

## Files included in repository

| File | Description |
|------|-------------|
| Boston| This is the Boston Airbnb data set broken into three CSV subsets: calendars, listings, and reviews.<br>These three sets are uploaded and combined into a single data frame for the purposes of this project.|
| Seattle| This is the Seattle Airbnb data set broken into three CSV subsets: calendars, listings, and reviews.<br>These three sets are uploaded and combined into a single data frame for the purposes of this project.|
| Project_1.ipynb| This is the Jupyter Notebook file containing the code and analysis done on the Airbnb data. |

Data sets were obtained from Kaggle at the following links:
[Boston](https://www.kaggle.com/datasets/airbnb/boston/data)
[Seattle](https://www.kaggle.com/datasets/airbnb/seattle/data)

## Analysis and Results

I was interested in using both data sets to compare rental metrics across the two markets to see what similarities and differences I could find. From a business perspective, I wanted to look at what factors go into pricing across all the data features to gain insight into what types of properties made the most profitable rentals. We'll examine these section by section.

### Distribution of property types and room types across both markets

Room type is broken into three categories: Entire home/apt, Private room, and Shared room. To compare these data, I used a bar chart to examine the overall distributions across the two locations. The distribution of these properties was very similar across both markets and showed that most rentals are for the entire dwelling. There were a significant number of private rooms  and there were very few shared rooms in both markets.

A similar analysis was conducted for property type; however, there were *many* more classes of property type than room type. I selected the four most common property types across both markets: houses, apartments, condominiums, and townhouses. I immediately noticed that, proportionally, there were many more apartments in Boston than there were in Seattle, which had an almost equal proportion of apartments to houses. This became one of the motivations to do more geographic analysis of the rental data.

### Pricing comparison of the two markets based on property distribution

I used box plots to look at the pricing distribution of the property and room types across both markets. Looking at room types showed that Boston is the more expensive market across all three room types. Prices are also higher, overall, for entire dwellings versus singular rooms.

When looking at property types, Boston was again more expensive across all the categories with the exception of houses, in which it was slightly less expensive than Seattle. I'm curious if this is correlated with the lesser availability of houses in Boston, or perhaps the geographical location of the available houses in that market (e.g. are the houses in less-desirable neighborhoods)?

### Geographical pricing analysis

The Airbnb data sets include latitude and longitude features to provide location data. So I used interactive maps (see the next [section](#interactive-usage) from the Plotly express package linking to Mapbox geographical data to be able to analyze geographic trends in the data sets. First, I plotted each rental and colored the points by price. This showed that the higher-priced rentals tended to be near the city center in both markets, but there was a great deal of data that didn't lend easily to making visual inferences. I filtered the data to show only the 20% most expensive rentals to see if I could better understand the geographical trends.

In Boston, the most expensive properties are, indeed, clustered around the downtown area, with a large cluster around Fenway Park. The same was true in Seattle, with the difference that there were many more expensive properties dispersed in the areas North and Southwest of the city center. This may be an explanation of why there are so many more apartment rentals available in the Boston market.

Finally, I plotted the 20% most expensive properties colored by property type and sized by price. Ordinarily, this would be an over-saturation of data due to the points overplotting, but with the interactive maps, I had the ability to zoom in on specific areas and resolve individual properties. This was very interesting in that it showed that apartments and lofts dominate the city center while houses are much more prevalent in the suburbs. It also was a good visualization to see outliers in the pricing data (e.g. very expensive boat rentals in Lake Union in Seattle).

### Multiple regression to determine most important numerical features for price

I selected all the numeric data from the sets and created a baseline linear model to predict price. The initial goodness-of-fit was not great, so I looked at methods to select the most important features. I noticed that there was potential multicollinearity with my predictor variables. To deal with multicollinearity, I used the Variance Inflation Factor (VIF) which can be calculated as:
![vif](/Images/vif.png)

From Investopedia:
>Variance inflation factors allow a quick measure of how much a variable is contributing to the standard error in the regression. When significant multicollinearity issues exist, the variance inflation factor will be very large for the variables involved. After these variables are identified, several approaches can be used to eliminate or combine collinear variables, resolving the multicollinearity issue.

Taking the VIF of all the predictors and eliminating those that were over 10, I was able to increase the adjusted R-squared value of the model from 0.460 to 0.822; however, the mean absolute error increased slightly. I next decided to utilize an algorithmic approach to feature selection, and after research, I landed on Recursive Feature Elimination with Cross-Validation from SciKit-Learn (RFECV). This package ran the regression over five different train-test splits while eliminating features that were not significant predictors. This truncated the feature list from 27 to 12 degrees of freedom and both increased the adjusted R-squared value and decreased the mean absolute error from the baseline.

There are many more methods to refine feature selection in multiple regression, and in a future effort, I could encode categorical data into a pricing model.

## Interactive Usage

This notebook is meant to be run sequentially to ensure necessary libraries are loaded and to prevent any errors from occurring (i.e. from variables being over-written)

Additionally, there are interactive maps in the notebook that look something like this:
```python
fig = px.scatter_mapbox(df_boston[df_boston['price']>boston_price_filter],
                        lat = 'latitude',
                        lon = 'longitude',
                        color = 'property_type',
                        color_discrete_sequence = px.colors.qualitative.Plotly,
                        size = 'price',
                        opacity=.4,
                        width = 800,
                        height = 800)
fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
fig.show()
```
![map image](/Images/Interactive_map.png)

These maps are rich in data and can be zoomed/panned so I encourage you to play around with them!

## License

[MIT Open-source License](LICENSE.txt)
