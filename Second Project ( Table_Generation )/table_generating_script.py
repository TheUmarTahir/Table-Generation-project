"""---To Do List---

1. Generate Multiplication Tables.
2. Save the table in one the following formats, (txt, pdf, csv, excel/xlsv).
3. Table should be generated on user's input.
4. Reverse Table should also be generated if user wants.
5. Table should be generated to as high value as the user wants i.e. 2 X 30 

"""
def generatetable(n):
    
    # 1. Reverse Table/Table Logic Taking User input to determine the what table will it be Reverse or normal also determines if the table multiplication be upto 10 or more no/values.  
    start = int(input("Enter The No Table should begin from i.e (2 X 1) or (2 X 20, for reverse table): "))
    end = int(input("Enter The No Table should end at i.e (2 X 20) or (2 X 1, for reverse table): "))

    # 1.1. Rest of Reverse Table Logic
    if (start > end):
        step = -1
        Title = f"--- Reverse Multiplication Table for {n} ---\n"
        print(Title)
    else:
        step = 1
        Title = f"--- Multiplication Table for {n} ---\n"
        print(Title)

    # Save Logic For Table Heading as it is static hence outside the Table Multipication loop
    with open(f"tables/table_{n}.txt","a") as s:
            s.write(f"\n{Title}\n")
       
        # Multiplication Logic    
            for i in range(start, end + step , step):
                table = (f"{n} X {i} = {n*i}")  # using f string for better readablilty
                print(table)
            # Save Logic For Table content as it depends on (i)/iteration hence inside the Table Multiplication loop
                s.write(f"{table}\n")
         
    # User Input    
n = int(input("Enter The Number You want the table for thanks: "))
generatetable(n)
    
  