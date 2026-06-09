"""
Match current skills against predefined job roles.

Concepts practiced:
- lists
- dictionaries
- for loops
- conditionals
- all()
- membership testing (in)
- list append()
- string join()
"""

# Define data science job roles and required skills
job_roles = [
    {'role': 'Data Analyst',
     'skills': ['Python', 'SQL', 'Excel']},
    {'role': 'Data Scientist',
     'skills': ['Python', 'R', 'Machine Learning', 'Deep Learning']},
    {'role': 'Machine Learning Engineer',
     'skills': ['Python', 'TensorFlow', 'PyTorch', 'Scikit-Learn']},
    {'role': 'Data Engineer',
     'skills': ['Python', 'Apache Spark', 'Hadoop', 'SQL']},
    {'role': 'Business Intelligence Analyst',
     'skills': ['Python', 'SQL', 'Tableau', 'Power BI', 'Excel']},
    {'role': 'Quantitative Analyst',
     'skills': ['R', 'Python', 'MATLAB', 'Statistics']},
    {'role': 'Operations Analyst',
     'skills': ['Python', 'SQL', 'Data Visualization', 'Process Improvement']},
    {'role': 'Database Administrator',
     'skills': ['SQL', 'Oracle', 'MySQL', 'Database Management']},
    {'role': 'AI Engineer',
     'skills': ['Python', 'TensorFlow', 'PyTorch', 'Computer Vision']},
    {'role': 'Statistician',
     'skills': ['R', 'SAS', 'Python', 'Statistical Modeling']}
]

# Current skills
my_skills = ["Python", "SQL", "Excel"]

# Determine which job roles contain all current skills
qualified_roles = []

for job in job_roles:
    # Check whether every skill in my_skills exists in the role requirements
    if all(skill in job["skills"] for skill in my_skills):
        qualified_roles.append(job["role"])

# Display results
if qualified_roles:
    output_message = (
        "Qualified for the following roles: " + ", ".join(qualified_roles)
    )
    print(output_message)
else:
    print("There are no matching job roles for the current skill set.")
