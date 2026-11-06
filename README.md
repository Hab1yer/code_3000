# code_3000
Collection of Assignments for CSE 3000: Contemporary Issues in Computer Science and Engineering

_Note_: Odd-numbered assignments are in HuskyCT, while even-numbered assignments are found in this repo and can be submitted to Gradescope via a Github connection.

## Outline of Assignments

### Module 02: Bot Predictor
Your goal is to build a machine learning model using given data and a Python template. You'll make changes to the GradientBoostingClassifer in mod02_build_bot_predictor.py and then test your changes in mod02_test_bot_predictor.ipynb. Can you minimize the misclassification rate on the test set?

### Module 04: Model Bias
You are given a model that was built to predict a mystery variable using zip code, income, and education level. The variable "group" represents a demographic that is prohibited and was NOT used in the model. Your goal is to use the SHAP package to review this model for bias.

### Module 06: Data De-Anonymization
Your goal is to connect anonymized data back to its source data and check the match rate. To complete this activity, write functions in the "deanonymize" script to (1) link the records in the two datasets and (2) calculate the rate at which you are successful doing so. 

### Module 08: Sustainability in Computing
You will be given a toy dataset and have the opportunity to explore the potential effects of choosing sustainable energy sources to perform computations. You'll code the energy calculation in "sustainability calculations" script, and then you can review the results of various decisions in the "check calculations" notebook.

## Personal Ethics Statement

After reading chapter 5 of *Ethical Machines*, I think ethics should show up in the decisions I make when building something. Saying I care about fairness or privacy is a start, but it doesn't mean much unless I can explain what I would actually do to protect people. As a computer science student, I want to build software that people can use without being misled or having their information taken advantage of.

For me, that means collecting only the data a project needs, clearly explaining how it will be used, and checking whether a system's mistakes affect some groups more than others. I would consider hiding a known bias or using someone's data for an unrelated purpose without their understanding unacceptable. The chapter also made me think about the difference between a goal and a tool for reaching it. Having a person review an AI's output only helps if that review actually prevents harm. I want to ask who could be hurt by my work, test for those problems, and take responsibility for fixing them when they appear.
