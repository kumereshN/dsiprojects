# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Standardized Testing, Statistical Summaries and Inference

### N Kumeresh, DSI-18-Singapore

## Problem Statement

To recommend to the College Board the actions to take to increase the participation rates of high school students taking SAT and ACT exams.

## Executive Summary

The project reviews the data covering scores and participation rates for high school students taking the ACT and SAT exams. The data is ordered by state level and contains the 2017 and 2018 participation rates, Total, Composite and their sub tests scores. The arrangement allows a state-by-state comparison of the participation rates and scores for each test. 


Many states have made it mandatory to take one of the two tests as a requirement for high school graduation and the data set has shown to be aligned with this observation with majority of the students taking either one of the tests. There is a strong negative correlation found between average test score and participation rates. States with high participation rates are more likely to see lower average scores compared to states with lower participation on the same test. Hence, it's not recommended to compare the average scores among states with large participation differences.

## Conclusions and Recommendations

After reviewing the state college entrance exam testing policy and examining the datasets, there is clear evidence that the respective state's policy has a huge influence in the student's participation in these tests. Currently, there are 25 states that require students to take the [SAT or ACT](https://www.edweek.org/ew/section/multimedia/states-require-students-take-sat-or-act.html).

For the tests participation to increase, states can choose to enact a policy of making one of the two tests a mandatory high school graduation requirement if they have not done so. This provides benefits to the state's education systems and to the students. One advantage would be that the standardized test can be used to measure the effectiveness of the high-school educational systems. It can also be used to benchmark students and provides students the guidance to complete one common college application requirement. This will be useful in guiding students to consider their school of choice.  

Let's look at Illinois, where students are mandated to take a standardized test to enter colleges and universities. After Illinois State Board of Education (ISBE) reviewed both tests,  ISBE switched to SAT from ACT. This resulted a large decrease in ACT participation and a large increase in SAT participation from 2017 to 2018. These changes in participation were followed by a decrease in average score for the SAT and an increase in ACT average scores. This shows what happens when a state make a test mandatory - a large drop in the participation rate of the other test.

To resolve this, states need to provide incentives to encourage students to take both tests. Incentives such as giving students time off for test taking, subsidizing the fees and integrating the test into high school curriculum can help to remove the barriers.

Research into other factors such as the median household incomes for each state to see if there's any corrleations into the participation rates would be useful to increase the participation rates.

---

### Datasets

#### Provided Data

2017 SAT and ACT datasets were provided as part of the project:

- [2017 SAT Scores](./data/sat_2017.csv)
- [2017 ACT Scores](./data/act_2017.csv)

Comparisons were made at these sites:
- [SAT](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/)
- [ACT](https://www.act.org/content/dam/act/unsecured/documents/cccr2017/ACT_2017-Average_Scores_by_State.pdf)

#### Additional Data

2018 state-by-state average results and participation for the SAT are available in PDF reports [here](https://reports.collegeboard.org/sat-suite-program-results/state-results). 2018 ACT state-by-state mean composite scores and participation rates are [here](http://www.act.org/content/dam/act/unsecured/documents/cccr2018/Average-Scores-by-State.pdf).

---
## Data Dictionary

|Feature|Type|Dataset|Description|Range|
|---|---|---|---|---|
|state|object|final.csv|State of the data|NA|
|sat_17_participation|float|final.csv|State participation rate in 2017|2-100|
|sat_17_erw|integer|final.csv|State average Evidence-Based Reading and Writing score in 2017|482-644|
|sat_17_math|integer|final.csv|State average Math score in 2017|468-651|
|sat_17_total|integer|final.csv|State average Total score in 2017|950-1295|
|act_17_participation|float|final.csv|State participation rate in 2017|8-100|
|act_17_english|float|final.csv|State average English score in 2017|16.3-25.5|
|act_17_math|float|final.csv|State average Math score in 2017|18-25.3|
|act_17_reading|float|final.csv|State average Reading score in 2017|18.1-26.0|
|act_17_science|float|final.csv|State average Science score in 2017|18.2-24.9|
|act_17_composite|float|final.csv|State average Composite score in 2017|17.8-25.5|
|sat_18_participation|float|final.csv|State participation rate in 2018|2-100|
|sat_18_erw|integer|final.csv|State average Evidence-Based Reading and Writing score in 2018|480-643|
|sat_18_math|integer|final.csv|State average Math score in 2018|480-655|
|sat_18_total|integer|final.csv|State average Total score in 2018|977-1298|
|act_18_participation|float|final.csv|State participation rate in 2018|7-100|
|act_18_english|float|final.csv|State average English score in 2018|16.6-26.0|
|act_18_math|float|final.csv|State average Math score in 2018|17.8-25.2|
|act_18_reading|float|final.csv|State average Reading score in 2018|18.0-26.1|
|act_18_science|float|final.csv|State average Science score in 2018|17.9-24.9|
|act_18_composite|float|final.csv|State average Composite score in 2018|17.7-25.6|