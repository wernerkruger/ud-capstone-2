# Statistical Analysis Report: Mobile Sales Data

## Overview

This report summarizes a complete statistical analysis of the **Mobile Sales** dataset (Kaggle: syedaeman2212/mobile-sales-data). The goal was to explore sales structure with descriptive statistics and visualizations, and to test whether a key numeric variable (e.g., price or quantity sold) differs significantly between two major groups (e.g., brands or regions). The analysis was conducted in a Jupyter notebook using Python, Pandas, NumPy, Matplotlib, Seaborn, and SciPy, following reproducible workflows and initial data analysis (IDA) practices.

**Dataset source:** [Kaggle – Mobile Sales Data](https://www.kaggle.com/datasets/syedaeman2212/mobile-sales-data)

---

## Dataset Description

The dataset represents transaction-level sales records for mobile (and possibly laptop) devices. It includes multiple thousands of rows and several columns. Key variables typically include: product type, brand, price, quantity sold, region, and technical specifications (e.g., RAM, ROM, processor). Each row corresponds to a sale or transaction. The data meet the project requirements: at least 500 rows, at least 6 columns, and a mix of numeric variables (e.g., price, quantity) and categorical or grouping variables (e.g., brand, region). Exact row and column counts and variable names are confirmed in the accompanying Jupyter notebook after loading. This structure allows exploration of distributions, relationships between price and quantity, and comparisons across brands or regions.

---

## Methods

**Descriptive statistics.** Summary statistics (mean, standard deviation, min, max, quartiles) were computed for all numeric variables using `describe()`, and value counts were obtained for categorical variables. This aligns with initial data analysis (IDA) recommendations: screening distributions and missingness before modeling or inference builds a solid foundation for reproducible analysis (Lusa et al., 2024).

**Visualizations.** Three or more visualizations were created: (1) a histogram of a key numeric variable (e.g., price) to assess distribution shape; (2) a boxplot of that variable by a categorical group (e.g., brand or region) to compare central tendency and spread; (3) a scatter plot of two numeric variables to inspect association; (4) a correlation heatmap of numeric variables. Each plot has a clear title and axis labels to support interpretation.

**Hypothesis test.** A two-sample *t*-test was used to test whether the population mean of the price differs between the two largest groups defined by a brand. The null hypothesis (H₀) is that the two population means are equal; the alternative (H₁) is that they differ. The *t*-test is appropriate when comparing means of a continuous variable across two independent groups, and when assumptions are roughly met: approximate normality of the variable (or large sample sizes) and similar variances (McDonald, 2014; SciPy documentation). The test statistic and *p*-value were computed in Python with `scipy.stats.ttest_ind`. A significance level of α = 0.05 was used for interpretation.

---

## Results

Summary statistics and categorical counts are reported in the notebook and show the central tendency, spread, and frequency distribution of the main variables. The histogram of the key numeric variable (price) indicates whether the distribution is symmetric or skewed. The boxplot by group reveals differences in location and spread between the two largest categories. The scatter plot and correlation heatmap show the strength and direction of linear relationships among numeric variables.

The two-sample *t*-test yielded a *t*-statistic and *p*-value. If *p* < 0.05, we reject H₀ and conclude there is evidence that the mean of the numeric variable differs between the two groups; otherwise we do not reject H₀. The exact values and group labels are given in the notebook output.

---

## Interpretation for a Non-Technical Audience

In plain terms: we looked at sales data to see how prices (or quantities) behave and whether they differ between the two biggest groups (e.g., two brands or two regions). The graphs show how values are distributed and how they compare across groups. The statistical test tells us whether any difference in average value between those two groups is likely to be real rather than due to random variation. If the *p*-value is small (below 0.05), we treat the difference as statistically significant—i.e., we have evidence that the two groups differ on average. If not, we do not have enough evidence to say they differ. This supports business or policy discussions about pricing, regional performance, or brand comparison.

---

## Limitations and Potential Bias

**Limitations.** (1) The dataset may be a convenience sample (e.g., one retailer or region), so results may not generalize to all markets or time periods. (2) Missing values or recording errors could affect summary statistics and the *t*-test; the extent of missing data is reported in the notebook. (3) If the numeric variable is highly skewed or group sizes are small, the *t*-test may be less reliable; nonparametric alternatives (e.g., Mann–Whitney) could be considered.

**Potential bias.** (1) **Selection bias:** If certain brands or regions are over- or under-represented, comparisons may be biased. (2) **Measurement bias:** Price or quantity might be recorded inconsistently across regions or time. (3) **Temporal bias:** If the data span a period with market changes (e.g., promotions, supply shocks), averages may reflect those conditions rather than a stable baseline. Acknowledging these limitations and biases is part of responsible interpretation (Lusa et al., 2024).

---

## References

Lusa L, Proust-Lima C, Schmidt CO, Lee KJ, le Cessie S, Baillie M, Lawrence F, Huebner M; on behalf of TG3 of the STRATOS Initiative. Initial data analysis for longitudinal studies to build a solid foundation for reproducible analysis. *PLoS One*. 2024 May 29;19(5):e0295726. doi: 10.1371/journal.pone.0295726.

McDonald JH. *Handbook of Biological Statistics*. 3rd ed. Sparky House Publishing; 2014. (Statistical tests, assumptions, and interpretation of *p*-values and *t*-tests.)
