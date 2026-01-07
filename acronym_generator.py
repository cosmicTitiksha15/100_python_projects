# This program is an acronym generator
# | **Beginner** | **Console/CLI** | **7. Acronym Generator** | String splitting, looping, character indexing. |

def acronym_generator():
    query = input("Enter the phrase : ")
    query_list = query.split()
    print(query_list)
    acronym = ''
    for item in query_list:
        acronym += item[0].upper()

    return f"Abbreviation for {query} is : {acronym}."

while True:
    acronym = acronym_generator()
    print(acronym)
    query = input("Another acronym to generate ? (y/n) : ")
    if query.lower() == 'y':
        continue
    else:
        break