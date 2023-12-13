import pandas as pd

def categorize_project(title):
    title = title.lower()
    if 'climate' in title and ('services' in title or 'early warning' in title or 'forecasting' in title):
        return "Climate Services & Early Warning"
    elif 'governance' in title or 'capacity' in title or 'management' in title or 'institutional' in title:
        return "Governance"
    elif 'water' in title and ('security' in title or 'management' in title or 'sector' in title):
        return "Water Sector"
    elif 'disaster' in title or 'emergency' in title or 'preparedness' in title or 'hazard' in title:
        return "Disaster Preparedness"
    elif 'agriculture' in title or 'food security' in title or 'livelihood' in title:
        return "Agriculture & Food Security"
    elif 'community' in title and ('resilience' in title or 'vulnerable' in title):
        return "Community Resilience"
    elif 'technology' in title or 'innovation' in title:
        return "Technology and Innovation"
    elif 'building' in title or 'infrastructure' in title:
        return "Infrastructure and Building"
    elif 'UNFCCC' in title or 'LDCs' in title or 'union' in title:
        return "International Cooperation"
    elif 'finance' in title or 'investment' in title:
        return "Financial Mechanisms"
    elif 'ecosystem' in title or 'biodiversity' in title:
        return "Ecosystem-based Adaptation"
    elif 'transparency' in title or 'data' in title or 'report' in title:
        return "Climate Data and Transparency"
    elif 'women' in title or 'youth' in title or 'vulnerable' in title:
        return "Gender and Vulnerable Groups"
    else:
        return "Others"

# Read Excel file
excel_file_path = 'C:/Users/nagas/Downloads/cleaned_excel_file.xlsx'
df = pd.read_excel(excel_file_path)

# Initialize the 13 columns with zeros
categories = [
    "Climate Services & Early Warning", "Governance", "Water Sector", "Disaster Preparedness", 
    "Agriculture & Food Security", "Community Resilience", "Technology and Innovation", 
    "Infrastructure and Building", "International Cooperation", "Financial Mechanisms", 
    "Ecosystem-based Adaptation", "Climate Data and Transparency", "Gender and Vulnerable Groups"
]
for category in categories:
    df[category] = 0

df['Total project Amount'] = df['Total project Amount'].replace(',', '', regex=True).astype(float)

for index, row in df.iterrows():
    category = categorize_project(row['Project title'])
    # Assign the already cleaned and converted value
    df.at[index, category] = row['Total project Amount']
    

# Save updated Excel file
df.to_excel("C:/Users/nagas/Downloads/updated_file.xlsx", index=False)


