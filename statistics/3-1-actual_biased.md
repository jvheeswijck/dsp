[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

In this exercise, we examine how data can become biased. If we look at a case of students under 18 in a household. If the data is reported by the students under 18, we see that a bias may arise. With the following code, we plot and observe the distribution of means of the actual data, and the theoretical data that may arise if the data is reported by those being measured.
```python
resp = nsfg.ReadFemResp()
# Actual Distribution
numkdhh_pmf = {x:y for x,y in enumerate(resp['numkdhh'].value_counts())}
# Biased Distribution
numkdhh_pmf_bias = {x:x*y for x,y in numkdhh_pmf.items()}
# Plots
fig,axs = plt.subplots(2,1)
axs[0].bar(list(numkdhh_pmf.keys()), numkdhh_pmf.values())
axs[1].bar(list(numkdhh_pmf_bias.keys()), numkdhh_pmf_bias.values())
axs[0].set_title('Actual')
axs[1].set_title('Biased')
fig.tight_layout()
```
![plots](img/actualvsbiased.png)
