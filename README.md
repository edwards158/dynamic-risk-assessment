# dynamic-risk-assessment


## Dynamic Risk Assessment

Imagine that you're the Chief Data Scientist at a big company that has 10,000 corporate clients. Your company is extremely concerned about attrition risk: the risk that some of their clients will exit their contracts and decrease the company's revenue. They have a team of client managers who stay in contact with clients and try to convince them not to exit their contracts. However, the client management team is small, and they're not able to stay in close contact with all 10,000 clients.

The company needs you to create, deploy, and monitor a risk assessment ML model that will estimate the attrition risk of each of the company's 10,000 clients. If the model you create and deploy is accurate, it will enable the client managers to contact the clients with the highest risk and avoid losing clients and revenue.

Creating and deploying the model isn't the end of your work, though. Your industry is dynamic and constantly changing, and a model that was created a year or a month ago might not still be accurate today. Set up regular monitoring of your model to ensure that it remains accurate and up-to-date. Set up processes and scripts to re-train, re-deploy, monitor, and report on your ML model, so that your company can get risk assessments that are as accurate as possible and minimize client attrition.

## Project Steps Overview
Complete the project by proceeding through 5 steps:

- Data ingestion. Automatically check a database for new data that can be used for model training. Compile all training data to a training dataset and save it to persistent storage. Write metrics related to the completed data ingestion tasks to persistent storage.
- Training, scoring, and deploying. Write scripts that train an ML model that predicts attrition risk, and score the model. Write the model and the scoring metrics to persistent storage.
- Diagnostics. Determine and save summary statistics related to a dataset. Time the performance of model training and scoring scripts. Check for dependency changes and package updates.
- Reporting. Automatically generate plots and documents that report on model metrics. Provide an API endpoint that can return model predictions and metrics.
- Process Automation. Create a script and cron job that automatically run all previous steps at regular intervals.



## Execution

Model training
Model training and test can be done by python **main.py --choice train_model**

Model score
Check score on latest dvs saved model can be done by python **main.py --choice get_score**

Run entire pipeline
To run the entire pipeline in sequence, use python **main.py --choice all**

Test API
If testing FastAPi serving on local is needed, execute **uvicorn app_server:app --reload**

Check Heroku deployed API
Check Heroku deployed API using **python heroku_api_test.py**

## CI/CD
Every new commit triggers a [test pipeline](https://github.com/edwards158/fastapi-heroku/blob/master/.github/workflows/python-app.yml)&nbsp;. This triggers a pull from DVC and exectute Pytest and Flake8 with Github actions.  
