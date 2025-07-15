import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data_science_salaries.csv')
print(df.head(5))
salary = df['salary_in_usd']
company_size = df['company_size']
experience_level = df['experience_level']
work_models = df['work_models']
work_year = df['work_year']


# BoxPlot 
plt.subplot(1, 2, 2)
sns.boxplot(y=salary)
plt.title("Salary Distribution (Boxplot)")
plt.ylabel("Salary (USD)")
plt.tight_layout()
plt.show()


# scatterplot
plt.figure(figsize=(12, 8))  
sns.scatterplot(x=experience_level, y=salary, hue=company_size)
plt.title('The impact of company size and experience level on salary', fontsize=16)
plt.xlabel('experience_level', fontsize=12)
plt.ylabel('Salary (USD)', fontsize=12)
plt.legend(title='company_size',loc='upper right')
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show()


# Density plot
plt.figure(figsize=(10, 6))
sns.kdeplot(x=salary, hue=work_models, fill=True, common_norm=False, palette='Set2')
plt.title('Work models and salary density distribution', fontsize=16)
plt.xlabel('Salary (USD)', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.tight_layout()
plt.show()




# HeatMap

# Calculate average salary for each company size and experience level
salary_by_company_experience = df.groupby(['company_size', 'experience_level'])['salary_in_usd'].mean().unstack()

plt.figure(figsize=(10, 6))
sns.heatmap(salary_by_company_experience, annot=True, fmt='.1f', linewidths=0.5)
plt.title('Average salary by company size and experience level', fontsize=16)
plt.xlabel('experience_level', fontsize=12)
plt.ylabel('company_size', fontsize=12)
plt.tight_layout()
plt.show()





# Strip plot 
salary_variance_by_year_and_model = df.groupby(['work_year', 'work_models'])['salary_in_usd'].var().reset_index()
plt.figure(figsize=(12, 8))
sns.stripplot(x=work_year, y=salary, hue=work_models, data=salary_variance_by_year_and_model, jitter=True, dodge=True, palette='Set2')
plt.title('Variance of salary under different working years and working modes', fontsize=16)
plt.xlabel('work_year', fontsize=12)
plt.ylabel('Salary (USD)', fontsize=12)
plt.legend(title='work_models', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

