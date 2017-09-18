[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

**Exercise: In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women. **

**In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use `scipy.stats.norm.cdf`.**
To calculate this, we can use the CDF of the normal distribution with mean 178cm, and std 7.7cm. Taking the CDF up to 185.42 cm (6'1'') and subtracting the CDF to 177.8 cm (5'10''), we get the percentage of US males in the US between these two heights. The code is as follows:
```python 
import scipy.stats
heigh_dist = scipy.stats.norm(loc=178, scale=7.7)
result = heigh_dist.cdf(185.42) - heigh_dist.cdf(177.8)
print('Using the BRFSS dataset, the percentage of males in the US eligible to join the Blue Man Group, i.e. males with height between 5\'10\" and 6\'1\", is:', round(result*100,2), '%')
```
> Using the BRFSS dataset, the percentage of males in the US eligible to join the Blue Man Group, i.e. males with height between 5'10" and 6'1", is: 34.27 %
