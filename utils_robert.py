"""
File: utils_robert.py

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Robert Davis
"""

#####################################
# Import Modules
#####################################

import statistics

#####################################
# Declare Global Variables
#####################################

has_us_clients: bool = True
has_international_clients: bool = True

years_experience: int = 5
years_in_operation: int = 10

avg_rating: float = 4.85
average_client_satisfaction: float = 4.7

tools_used: list = ["Python", "SQL", "Tableau", "Power BI"]
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

project_ratings: list = [4.9, 4.8, 5.0, 4.7, 4.6]
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# Calculate statistics for client satisfaction
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

byline: str = f"""
---------------------------------------------------------
Robert Davis Analytics: Insight-Driven Decision Making
---------------------------------------------------------
Has US Clients:               {has_us_clients}
Has International Clients:    {has_international_clients}
Years of Experience:          {years_experience}
Years in Operation:           {years_in_operation}
Tools Used:                   {tools_used}
Skills Offered:               {skills_offered}
Client Satisfaction Scores:   {client_satisfaction_scores}
Minimum Satisfaction Score:   {min_score}
Maximum Satisfaction Score:   {max_score}
Mean Satisfaction Score:      {mean_score:.2f}
Standard Deviation of Scores: {stdev_score:.2f}
"""

#####################################
# Define global functions
#####################################

def get_byline() -> str:
    """
    Get a byline for my analytics projects.

    Returns a string byline that illustrates my specific skills.
    """
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    """
    Print results of get_byline() when main() is called.

    This function prints the byline to the console.
    """
    print("START main() in utils_robert.py")
    print(get_byline())
    print("END main() in utils_robert.py")

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
