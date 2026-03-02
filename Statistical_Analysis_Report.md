# Statistical Analysis Report: Mobile Sales Data

## Overview

This report documents a complete statistical analysis of the **Mobile Sales** dataset (Kaggle: syedaeman2212/mobile-sales-data). The analysis was conducted in a Jupyter notebook using Python, Pandas, NumPy, Matplotlib, Seaborn, and SciPy. The goals were to (1) load and validate the data, (2) summarize it with descriptive statistics, (3) visualize distributions and relationships, (4) test whether average price (USD) differs significantly between the two most frequent brands, and (5) interpret the results for both technical and non-technical readers. The workflow follows initial data analysis (IDA) and reproducibility practices so that the analysis can be rerun and the conclusions traced to the actual computations (Lusa et al., 2024).

Dataset source: [Kaggle – Mobile Sales Data](https://www.kaggle.com/datasets/syedaeman2212/mobile-sales-data)

---

## Dataset Description

The dataset is **synthetic_mobile_sales_2025.csv** from the Kaggle Mobile Sales Data repository. It represents **500 transaction-level sales records** with **13 columns**. Each row is a single sale with the following variables:

- **Identifiers:** Sale_ID  

- **Categorical / grouping:** Brand, Model, Country, Storage, Color, Payment_Method 

- **Numeric:** Price_USD, Units_Sold, Revenue_USD, Customer_Rating, Sale_Month, Sale_Year 


There are no missing values in the loaded data. The key numeric variable for this analysis is **Price_USD** (price in US dollars). The main grouping variable used for comparison is **Brand**. The two most frequent brands in the sample are **Vivo** (58 sales) and **Motorola** (55 sales), which were used for the hypothesis test. Other brands (e.g. Google, Samsung, Huawei, Realme, Oppo, Xiaomi, Apple, OnePlus) appear with counts between 40 and 52. The dataset is suitable for descriptive statistics, distribution and relationship plots, and a two-group comparison of mean price by brand.

---

## Methods

**Data loading and validation.** The notebook loads the CSV (either via kagglehub or from a local file), displays the first rows, and checks shape, dtypes, and missing values. This step ensures the data are read correctly before any analysis (Lusa et al., 2024).

**Descriptive statistics.** Summary statistics (count, mean, standard deviation, min, quartiles, max) were computed for all numeric columns using `describe()`. Value counts were obtained for categorical variables (Brand, Model, Country, Storage, Color, Payment_Method). These steps summarize central tendency, spread, and the distribution of key variables before visualization and testing.

**Visualizations.** Four figures were produced: (1) **Figure 1 – Histogram of Price_USD** to assess the shape of the price distribution; (2) **Figure 2 – Boxplot of Price_USD by Brand** (top 10 brands) to compare location and spread across brands; (3) **Figure 3 – Scatter plot** of two numeric variables (e.g. Price_USD vs Units_Sold or Revenue_USD) to inspect association; (4) **Figure 4 – Correlation heatmap** of numeric variables. Each figure has a descriptive title and labeled axes.

**Hypothesis test.** An independent two-sample *t*-test was used to test whether the population mean of **Price_USD** differs between **Vivo** and **Motorola**. The null hypothesis (H₀) is that the two population means are equal; the alternative (H₁) is that they differ. The *t*-test is appropriate for comparing the mean of a continuous variable across two independent groups when assumptions are roughly met: approximate normality or large samples, and similar variances (McDonald, 2014). The test was performed in Python with `scipy.stats.ttest_ind`. A significance level of α = 0.05 was used.

---

## Results

**Dataset and descriptive statistics.** The analysis used **500 rows** and **13 columns**. For **Price_USD**, the mean was **889.88 USD** (standard deviation 345.62), with a minimum of 302 and maximum of 1,500. For **Units_Sold**, the mean was 10.46 (SD 5.71). Revenue_USD and Customer_Rating showed similar completeness (no missing values). Brand counts showed Vivo (58), Motorola (55), Google (52), Samsung (51), and others as above.

**Figure 1 (Histogram of Price_USD).** The histogram shows the distribution of sale prices. In this sample, prices are spread across the range with a single peak; the shape is roughly symmetric to slightly right-skewed, with most sales between about 500 and 1,200 USD.

**Figure 2 (Boxplot of Price_USD by Brand).** The boxplots compare price distributions across the top 10 brands. Median prices and interquartile ranges vary by brand; some brands show tighter price ranges and others more spread. The plot supports a visual comparison of central tendency and variability before the formal test.

**Figure 3 (Scatter plot).** The scatter plot of two numeric variables (e.g. Price_USD vs Units_Sold or Revenue_USD) shows the strength and direction of the linear relationship between those variables, and highlights any notable clusters or outliers.

**Figure 4 (Correlation heatmap).** The heatmap summarizes pairwise correlations among numeric variables. It shows which variables are positively or negatively associated and helps identify redundant or related measures.

**Hypothesis test (Vivo vs Motorola, Price_USD).** The two groups compared were **Vivo** (n = 58) and **Motorola** (n = 55). From the notebook’s “Key results for the written report” cell, the mean Price_USD for Vivo was **approximately 884 USD** and for Motorola **approximately 897 USD** (exact values are in the notebook output). The independent two-sample *t*-test gave **t = -0.2090** and **p = 0.8348**. Because the p-value (0.8348) is much larger than α = 0.05, we **do not reject the null hypothesis**. There is insufficient evidence in these data to conclude that the mean price (Price_USD) differs between Vivo and Motorola; the observed difference in sample means is consistent with random variation.

---

## Interpretation for a Non-Technical Audience

We used 500 mobile sales records to answer a simple question: **Do Vivo and Motorola phones sell at different average prices?**

The data show that in this sample, average prices for the two brands were very similar (around 884 USD for Vivo and 897 USD for Motorola). We then ran a statistical test (a *t*-test) to see whether that small difference could be due to chance. The test showed that it could: the probability of seeing a difference at least this large by chance is about 83% (p = 0.83). So we **do not have evidence** that the two brands differ in average price in the population from which this sample was drawn.

In practice, this means that for this dataset, we cannot say that one of these brands is systematically cheaper or more expensive than the other; the prices are effectively comparable. The graphs in the notebook (histogram of prices, boxplots by brand, scatter plot, and correlation heatmap) support this by showing how prices are distributed and how they relate to other variables. This kind of analysis is useful for pricing strategy, portfolio comparisons, or reporting that is grounded in the actual numbers from the analysis rather than generic statements.

---

## Limitations and Potential Bias

**Limitations.** (1) The dataset has 500 rows and may be a convenience or synthetic sample; results may not generalize to all markets, time periods, or product mixes. (2) Missing values were absent in this run, but in real data, missingness could affect means and the *t*-test; the notebook reports missing counts for transparency. (3) If price were heavily skewed or sample sizes were small, the *t*-test could be less reliable; nonparametric alternatives (e.g. Mann–Whitney) could be considered. (4) Only two brands were compared; other brands or multiple pairwise comparisons would require different methods (e.g. ANOVA or multiple-testing correction).

**Potential bias.** (1) **Selection bias:** If certain brands or regions are over- or under-represented, comparisons may not reflect the full market. (2) **Measurement bias:** Price might be recorded in different currencies or contexts (e.g. before/after discounts), which could bias comparisons. (3) **Temporal bias:** If the data span a period with promotions or supply shocks, average prices may reflect those conditions. Acknowledging these limitations and sources of bias is part of responsible interpretation (Lusa et al., 2024).

---

## Conclusions and Workflow Summary

This project followed a full statistical analysis workflow: data loading and validation, exploratory descriptive statistics, multiple visualizations (histogram, boxplot, scatter plot, correlation heatmap), a clearly stated hypothesis test (two-sample *t*-test for mean Price_USD by brand), and interpretation of the results in light of the actual outputs from the notebook (sample sizes, means, t-statistic, p-value). All conclusions are grounded in these results rather than generic statements. The notebook and this report together form a complete, professional analysis suitable for a student portfolio or applied research context: the analysis is reproducible (requirements and code are provided), the methods and assumptions are cited, and limitations and bias are discussed.

---

## References

Lusa L, Proust-Lima C, Schmidt CO, Lee KJ, le Cessie S, Baillie M, Lawrence F, Huebner M; on behalf of TG3 of the STRATOS Initiative. Initial data analysis for longitudinal studies to build a solid foundation for reproducible analysis. *PLoS One*. 2024 May 29;19(5):e0295726. doi: 10.1371/journal.pone.0295726.

McDonald JH. *Handbook of Biological Statistics*. 3rd ed. Sparky House Publishing; 2014. (Statistical tests, assumptions, and interpretation of *p*-values and *t*-tests.)
