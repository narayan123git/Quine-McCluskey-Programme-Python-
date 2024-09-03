# Input minterms and split them into a list
minterms = input("Write minterms: ").split()
dontcare = input("Write dontcares(if not there enter nothing): ").split()
print("===============Minterms=================")
print(minterms)
print("===============Don't Cares=================")
print("Don't Care: ",dontcare)
bitSize = int(input("Enter bitsize: "))
unvisited=[]
visited=[]
unvisited=[]
list3=[]
dict1={}
dict2={}
max_space=0
pi_chart=[]
epi=[]
epi_storage=[]
column=[int(m) for m in minterms]
# Convert minterms to binary
minterms_dontcare=[]
minterms_dontcare=minterms+dontcare
def decimal_to_binary(minterm, bits=bitSize):
    # Convert the decimal number to binary and remove the '0b' prefix
    return format(int(minterm), f'0{bits}b')

binary_minterms = [decimal_to_binary(m,bitSize) for m in minterms_dontcare]

# Initialize dictionary to store minterms based on the number of '1's in their binary representation

dict1 = {(i,): [] for i in range(bitSize+1)}

def count1(s):
    s=str(s)
    return s.count('1')

# Populate the dictionary based on the count of '1's
for i in binary_minterms:
    key = (count1(i),)
    dict1[key].append(i)

# Print the contents of the dictionary
print(f"   Group   ".ljust(40),end="")
print("     Binary numbers")
for key in sorted(dict1.keys()):
    a,=key
    print(f'    {str(a).ljust(40)}: ', end="")
    for j in dict1[key]:
        print(f'{j}, ', end="")
    print()  # New line after printing all minterms for a specific key

def comparator(s1,s2):
    s1=str(s1)
    s2=str(s2)
    c=0
    k=0
    for i in range(len(s1)):
        if(s1[i]!=s2[i]):
            c=c+1
            if(c>1):
                break
            if(c==1):
                k=i
    return c,k

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

keys_list=list(dict1.keys())
for i in range(len(keys_list)-1):
    for m in dict1[keys_list[i]]:
        for n in dict1[keys_list[i+1]]:
            a,b=comparator(m,n);
            if(a==1):
                list2=list(m)
                list2[b]='_'
                new_string=''.join(list2)
                a=binary_to_decimal(m)
                b=binary_to_decimal(n)
                if a not in visited:
                    visited.append((a,))
                if b not in visited:
                    visited.append((b,))
                dict2[(a,b)]=[]
                dict2[(a,b)].append(new_string)
print("==========================================")
for i in dict2:
    print(f"{str(i).ljust(40)}",end="")
    print(dict2[i])
for i in minterms_dontcare:
    i=int(i)
    j=(i,)
    if j not in visited:
        k,=j
        binary_str = decimal_to_binary(int(k), bitSize)
        unvisited.append(((k,), binary_str))
def minimization():
    global max_space,unvisited
    # Ensure dict1 is updated from the previous phase
    dict1.clear()
    dict1.update(dict2)
    dict2.clear()

    keys_list = list(dict1.keys())
    
    # Third level minimization
    for i in range(len(keys_list) - 1):
        for j in range(i + 1, len(keys_list)):
            for m in dict1[keys_list[i]]:
                for n in dict1[keys_list[j]]:
                    a, b = comparator(m, n)
                    if a == 1:
                        list2 = list(m)
                        list2[b] = '_'
                        new_string = ''.join(list2)
                        
                        if keys_list[i] not in visited:
                            visited.append(keys_list[i])
                        if keys_list[j] not in visited:
                            visited.append(keys_list[j])
                        
                        # Ensure list3 is initialized
                        list3 = list(keys_list[i] + keys_list[j])
                        list3.sort()
                        
                        # Use tuple of sorted keys as dict key
                        tuple_key = tuple(list3)
                        if tuple_key not in dict2:
                            dict2[tuple_key] = []
                        if new_string not in dict2[tuple_key]:
                            dict2[tuple_key].append(new_string)
    for i in dict1:
        if i not in visited:
            for value in dict1[i]:
                unvisited.append((i, value))                   
                max_space=max(max_space,len(i))  
    print("==========================================")
    for i in dict2:
        print(f"{str(i).ljust(40)}",end="")
        print(dict2[i])         

for i in range(bitSize-2):
    minimization()
print(f"Prime Implicants".ljust(40),end="")
print("Binary value")
for i,j in unvisited:
    print(f"   {str(i).ljust(40)}",end="")
    print(f"{j}")
# print(max_space)
# Populate the PI chart matrix
def PIchart(column,unvisited):
    global pi_chart
    pi_chart=[]
    for row in unvisited:
        pi_row = []
        minterm_tuple, binary_string = row
        for minterm in column:
            if minterm in minterm_tuple:
                pi_row.append("X")
            else:
                pi_row.append(" ")
        pi_chart.append(pi_row)

    # Print the PI chart matrix
def print_PI_chart(pi_chart,unvisited,column):
    width = 4 * max_space
    print("======================================================")
    print("PI Chart Matrix:")
    print("======================================================")
    headers = []
    a=False
    for i in column:
        if(a==False):
            headers.append(str(i))  # Remove the extra quotes and space
            a=True
        elif i < 10:
            headers.append("   " + str(i))
        else:
            headers.append("  " + str(i))
    header = "".join(headers)

    print(f"{' ' * width}:{header}")
    for idx, row in enumerate(pi_chart):
        minterm_tuple, binary_string = unvisited[idx]
        print(f"{str(minterm_tuple).ljust(width)}:{'   '.join(row)}")

def find_epi(pi_chart, column):
    epi_indices = []
    epi_minterms = []
    
    for col_idx in range(len(column)):
        x_count = 0
        last_row_with_x = -1
        for row_idx in range(len(pi_chart)):
            if pi_chart[row_idx][col_idx] == 'X':
                x_count += 1
                last_row_with_x = row_idx
                
        # If only one 'X' is found in the column, it's an EPI
        if x_count == 1:
            epi_indices.append(last_row_with_x)
            epi_minterms.append(column[col_idx])
    
    return epi_indices, epi_minterms

def is_set_empty(my_set):
    return not bool(my_set)

def apply_row_dominance(pi_chart, unvisited):
    rows_to_remove = []

    # Compare each pair of rows to find dominated rows
    for i in range(len(pi_chart)):
        for j in range(i + 1, len(pi_chart)):
            # Get 'X' positions in row i
            x_positions_i = []
            for k in range(len(pi_chart[i])):
                if pi_chart[i][k] == 'X':
                    x_positions_i.append(k)

            # Get 'X' positions in row j
            x_positions_j = []
            for k in range(len(pi_chart[j])):
                if pi_chart[j][k] == 'X':
                    x_positions_j.append(k)

            # Check if row i is dominated by row j
            is_i_subset_j = True
            for pos in x_positions_i:
                if pos not in x_positions_j:
                    is_i_subset_j = False
                    break
            if is_i_subset_j:
                rows_to_remove.append(i)
                continue  # Move to the next pair after marking i for removal

            # Check if row j is dominated by row i
            is_j_subset_i = True
            for pos in x_positions_j:
                if pos not in x_positions_i:
                    is_j_subset_i = False
                    break
            if is_j_subset_i:
                rows_to_remove.append(j)

    # Remove duplicates by converting to a set
    unique_rows_to_remove = set(rows_to_remove)
    if(is_set_empty(unique_rows_to_remove)):
        return -1,-1
    print("==================Rows removed:=================")
    for i in unique_rows_to_remove:
        print(unvisited[i])

    # Create new lists excluding the rows to remove
    new_pi_chart = []
    new_unvisited = []
    for index in range(len(pi_chart)):
        if index not in unique_rows_to_remove:
            new_pi_chart.append(pi_chart[index])
            new_unvisited.append(unvisited[index])

    return new_pi_chart, new_unvisited

def column_dominance(pi_chart):
    global column, unvisited
    columns_to_remove = set()

    num_rows = len(pi_chart)
    num_cols = len(pi_chart[0]) if num_rows > 0 else 0

    # Iterate over each pair of columns
    for i in range(num_cols-1):
        # for j in range(i + 1, num_cols):  # Start j from i+1 to avoid comparing the same pair twice
            # Check if column i is dominated by column j
            dominated = True
            for row in range(num_rows):
                if pi_chart[row][i] == 'X' and pi_chart[row][i+1] != 'X':
                    dominated = False
                    break
            if dominated:
                columns_to_remove.add(i)
                continue  # Move to the next pair after marking i for removal

            # Check if column j is dominated by column i
            dominated = True
            for row in range(num_rows):
                if pi_chart[row][i+1] == 'X' and pi_chart[row][i] != 'X':
                    dominated = False
                    break
            if dominated:
                columns_to_remove.add(i)
    if not columns_to_remove:
        return -1  # No columns were removed
    print("=================Columns deleted:=================")
    for i in sorted((columns_to_remove)):
        print(column[i])
    # Create new column and pi_chart lists excluding the columns to remove
    new_column = [column[i] for i in range(num_cols) if i not in columns_to_remove]
    print(new_column)
    new_pi_chart = []
    # Update the global variables
    column.clear()
    column = new_column.copy()
    PIchart(column, unvisited)  # Recreate the PI chart with updated columns
    new_pi_chart=pi_chart[:]
    return new_pi_chart


PIchart(column,unvisited)
print_PI_chart(pi_chart,unvisited,column)
print("============================================")

def stringtoexpression(s):
    s=str(s)
    list1=list(s)
    list2=[]
    for i in range(len(list1)):
        if list1[i]=='1':
            list2.append(chr(i+65))
        elif(list1[i]=='0'):
            list2.append(chr(i+65)+"'")
    new_string=''.join(list2)
    return new_string

def calculate_pi_cost(pi, minterm_coverage):
    num_literals = pi.count('1') + pi.count('0')  # Count of literals ('0' or '1')
    return num_literals / len(minterm_coverage) 

def select_lowest_cost_pi(pi_chart, unvisited, column):
    min_cost = float('inf')
    selected_pi_index = -1
    
    for i, (minterm_tuple, binary_string) in enumerate(unvisited):
        covered_minterms = [column[j] for j in range(len(column)) if pi_chart[i][j] == 'X']
        cost = calculate_pi_cost(binary_string, covered_minterms)
        
        if cost < min_cost:
            min_cost = cost
            selected_pi_index = i
    
    return selected_pi_index

def minimization2():
    global pi_chart,column,unvisited
    list5=[]
    a1,b1=find_epi(pi_chart,column)
    if  len(a1)==0:
        print("The EPI is empty")
        new_pi_chart,new_unvisited=apply_row_dominance(pi_chart,unvisited)
        if(new_pi_chart==-1):
            print("Row dominance not applied")
            # return -1
            new_pi_chart=[]
            new_pi_chart=column_dominance(pi_chart)
            if(new_pi_chart==-1):
                print("Column dominance not applied")
                new_column=[]
                new_unvisited=[]
                a=select_lowest_cost_pi(pi_chart,unvisited,column)
                print("Semicyclic method applied")
                print("Selected PI: ",end="")
                print(unvisited[a])
                for i in range(len(unvisited)):
                    if i!=a:
                        new_unvisited.append(unvisited[i])
                for i in column:
                    if i!=unvisited[a]:
                        new_column.append(i)
                if len(new_column) == 0:
                    print("All minterms are covered. Exiting.")
                    return 0
                column.clear()
                unvisited.clear()
                column=new_column.copy()
                unvisited=new_unvisited.copy()
                PIchart(column,unvisited)
                print_PI_chart(pi_chart,unvisited,column)
                return 1
            else:
                pi_chart.clear()
                pi_chart=new_pi_chart[:]
                print_PI_chart(pi_chart,unvisited,column)
                return 1
        pi_chart.clear()
        unvisited.clear()
        pi_chart=new_pi_chart[:]
        unvisited=new_unvisited.copy()
        print_PI_chart(pi_chart,unvisited,column)
        return 1
    epi_string,epi_minterms=find_epi(pi_chart,column)
    for i in epi_string:
        a,b=unvisited[i]
        epi_storage.append(unvisited[i])
        list5.extend(a)

    new_column=[]
    new_unvisited=[]
    for i in range(len(unvisited)):
        if i not in epi_string:
            new_unvisited.append(unvisited[i])
    for i in column:
        if i not in list5:
            new_column.append(i)
    if len(new_column) == 0:
        print("All minterms are covered. Exiting.")
        return 0
    column.clear()
    unvisited.clear()
    column=new_column.copy()
    unvisited=new_unvisited.copy()
    PIchart(column,unvisited)
    print_PI_chart(pi_chart,unvisited,column)
    return 1
abc=1
while(abc!=0):
    abc=minimization2()
    print("==================================================")
if len(epi_storage)==0:
    epi_storage=unvisited.copy()
result=[]
b=epi_storage
for i in b:
    r,s=i
    result.append(stringtoexpression(s))
set1={}
set1=set(result)
list3=list(set1)
print("=============================================")
print("Final Expression: ")
i=0
for i in range(len(list3)-1):
    print(str(list3[i]),'+ ',end="")
print(str(list3[i+1]))

# Input: 
# 0 1 2 8 9 15 17 21 24 25 27 31
# 0 2 4 5 8 10 12 13 18 21 22 23 25 26 27 29
#1 2 3 5 7 8 9 12 14
# 1 3 5 7  9 11 13 15 20 21 22 23 28 29 30 31 36 37 38 39 44 45 46 47 49 51 53 55 57 59 61 63
