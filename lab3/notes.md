# We continue using robust standard errors, because it's good practice   

coeftest(model2, vcov = vcovHC)

my understanding of that, is that if you don’t have homoskedasticity, then the standard errors from the lm() are invalid (too small). so if you have heteroskedasticity you need to use the robust errors which are bigger


wrap coeftest around the model and pass that to stargazer to get the regression table. 

By default stargatzer uses the non-robust standard errors 


Here is how instructor's team roughly presents it:  "how effective is a face mask requirement against COVID-19".  As part of the measurement, you are looking for a single X variable and relevant specifications. Avoid the search for the general "effective solutions to COVID". Be specific in identifying your input and output variables. 

LAB 3 - NEXT STEPS

Write up your own research focus (focus on total deaths covid)

describe the issue with randomness in the sample, 
describe that mlr.2 can't be met, but explore why you can still do linear modeling

Use residuals


Model v0 - pick main and 2 other variables

Model v1 - v0 + n more important variables

Model v2 - kitchen sink approach

