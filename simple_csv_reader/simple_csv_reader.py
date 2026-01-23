# | **Beginner** | **Data Manipulation** | **11. Simple CSV Reader** | File I/O, reading and iterating through lines. |
file = input("Enter the name of your csv file along with .csv extension : ")
def read_csv(file_path):
    try:
        with open(file_path, 'r') as f:
            # Iterating directly over 'f' is memory-efficient
            for line in f:
                # .strip() removes the \n at the end of the line
                columns = line.strip().split(',')
                print(" | ".join(columns))
    except FileNotFoundError:
        print(f"File not Found! Check file name or re-enter it.")

read_csv(file)