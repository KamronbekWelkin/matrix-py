# Define the dimensions of the matrix
rows = 3
cols = 3

# Create an empty matrix
matrix = []

# Loop through the rows and create empty lists for each row
for i in range(rows):
    row = []
    # Loop through the columns and add 0's to each row
    for j in range(cols):
        row.append(0)
    # Add the row to the matrix
    matrix.append(row)

# Print the matrix
for row in matrix:
    print(row)