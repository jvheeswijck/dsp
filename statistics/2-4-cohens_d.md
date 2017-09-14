[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

**Using the variable `totalwgt_lb`, investigate whether first babies are lighter or heavier than others. 
Compute Cohen’s effect size to quantify the difference between the groups.  How does it compare to the difference in pregnancy length?**

To investigate whether first babies are heavier or lighter than others we first examine the means of the two groups. We find the mean weight of first babies is 7.20 lbs while the mean of other babies is 7.33 lbs. It looks as though other babies may be heavier. To test this, we conduct a independant samples t-test and measure the effect size with Cohen's D. The following code is used on the data frames to perform these tests:
```python
from scipy import stats
a = firsts.dropna(subset=['totalwgt_lb']).totalwgt_lb
b = others.dropna(subset=['totalwgt_lb']).totalwgt_lb
a.mean()
b.mean()
F = stats.variation(a) / stats.variation(b)
df1 = len(a) - 1, 
df2 = len(b) - 1
p_value = stats.f.cdf(F, df1, df2)
print('The p_value for the f-test of equal variances is', p_value)
# Equal Variance t-test
print('The p-value for the t-test is ', stats.ttest_ind(a,b)[1])
# p-value is less than 0.05, therefore we conclude that there is a difference in means
# to measure the effect size, we use cohen's D
print("Cohen's D is measured to be", CohenEffectSize(a,b))
```
The outputs are:
```
The mean weight of first babies is 7.201094430437772
The mean weight of other babies is 7.325855614973262
The p_value for the f-test of equal variances is [ 0.88622698]
The p-value for the t-test is  2.55059572705e-05
Cohen's D is measured to be -0.088672363332
```
We see from these tests that there is a significant difference between means, if we chose an alpha of 0.05. However, despite there being a significant difference, Cohen's D tells us that the effect is very small with a value of -0.089.  
Compared to Cohen's D of pregnancy length between the two groups, which was found to be 0.0288 in an earlier problem, we see that both are relatively small effects.
