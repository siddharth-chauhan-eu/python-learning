"""
Convert string-based job data into typed Python objects.

Concepts practiced:
- datetime parsing
- ast.literal_eval()
- dictionaries
- loops
- data cleaning
"""

from datetime import datetime
import ast

data_science_jobs = [
    {
        'job_title': 'Data Scientist',
        'job_skills': "['Python', 'SQL', 'Machine Learning']",
        'job_date': '2023-05-12'
    },
    {
        'job_title': 'Machine Learning Engineer',
        'job_skills': "['Python', 'TensorFlow', 'Deep Learning']",
        'job_date': '2023-05-15'
    },
    {
        'job_title': 'Data Analyst',
        'job_skills': "['SQL', 'R', 'Tableau']",
        'job_date': '2023-05-10'
    },
    {
        'job_title': 'Business Intelligence Developer',
        'job_skills': "['SQL', 'PowerBI', 'Data Warehousing']",
        'job_date': '2023-05-08'
    },
    {
        'job_title': 'Data Engineer',
        'job_skills': "['Python', 'Spark', 'Hadoop']",
        'job_date': '2023-05-18'
    },
    {
        'job_title': 'AI Specialist',
        'job_skills': "['Python', 'PyTorch', 'AI Ethics']",
        'job_date': '2023-05-20'
    }
]

# Convert string values into Python objects
for job in data_science_jobs:
    job['job_date'] = datetime.strptime(
        job['job_date'],
        '%Y-%m-%d'
    )
    job['job_skills'] = ast.literal_eval(
        job['job_skills']
    )

print(data_science_jobs)
