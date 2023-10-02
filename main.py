import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Read the dataset
df = pd.read_excel('Test_Files.xlsx')

# Log a message when reading the dataset
logging.info('Reading the dataset.')

# Assuming the dataset contains a 'Name' column and an empty 'Email' column
student_names = df['Student Name']

# Generate email addresses and save them in the 'Email' column
def generate_email(name):
    parts = name.split()
    if len(parts) >= 2:
        first_name = parts[0]
        last_name = parts[-1]
        email = f"{first_name[0].lower()}{last_name.lower()}@gmail.com"
        return email
    else:
        return None

# Apply the generate_email function to create email addresses
df['Email Address'] = student_names.apply(generate_email)

# Remove special characters from email addresses
df['Email Address'] = df['Email Address'].str.replace('[^a-zA-Z0-9]', '')

# Ensure email addresses are unique
df.drop_duplicates(subset='Email Address', inplace=True)

# Save the updated DataFrame to TSV
df.to_csv('output.tsv', sep='\t', index=False)

# Save the updated DataFrame to CSV
df.to_csv('output.csv', index=False)

# Generate Separate Lists of Male and Female Students

# Filter male and female students
male_students = df[df['Gender'] == 'M']
female_students = df[df['Gender'] == 'F']

# Log the lists of male and female students
logging.info('Male Students:')
logging.info(male_students.to_string(index=False))

logging.info('Female Students:')
logging.info(female_students.to_string(index=False))

# Count and log the number of male and female students
num_male_students = len(male_students)
num_female_students = len(female_students)

# Log the number of male and female students
logging.info(f'Number of male students: {num_male_students}')
logging.info(f'Number of female students: {num_female_students}')

print(f"Number of male students: {num_male_students}")
print(f"Number of female students: {num_female_students}")

# List Names of Students with Special Characters

# Define a regular expression pattern to match special characters
special_char_pattern = r'[^\w\s]'

# Find students with special characters in their names
students_with_special_chars = df[df['Student Name'].str.contains(special_char_pattern)]

# Log the names of students with special characters
logging.info('Students with special characters in their names:')
for name in students_with_special_chars['Student Name']:
    logging.info(name)

# Log the names of students with special characters
print("Students with special characters in their names:")
for name in students_with_special_chars['Student Name']:
    print(name)


# Merge the dataframes if you have additional student information

# Log message for shuffling the fields
logging.info(f'Shuffling the fields in the dataset')

# Shuffle the fields (columns) in the DataFrame
shuffled_df = df.sample(frac=1, axis=1, random_state=42)


# Log message for saving as JSON
logging.info('Saved shuffled data as JSON.')

# Save the shuffled DataFrame as a JSON file
shuffled_df.to_json('shuffled_data.json', orient='records', lines=False)

# Log message for saving as JSONL
logging.info('Saved shuffled data as JSONL.')

# Save the shuffled DataFrame as a JSONL (JSON Lines) file
shuffled_df.to_json('shuffled_data.jsonl', orient='records', lines=True)