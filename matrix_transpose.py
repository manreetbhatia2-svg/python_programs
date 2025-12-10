# matrix transpose
enter_list = []

rows = int(input('Enter the number of rows '))
columns = int(input('Enter the number of columns '))
for i in range (0,rows ):
  row =[]
  for j in range (0,columns):
    numbers = int (input (f' ({i},{j}) '))
    row.append(numbers)
  enter_list.append(row )
for nested_list in enter_list:
  print(nested_list)

# transpose starts
def transpose_matrix():
  add_elements =[]
  for x in range(0,columns):
    new_row =[]
    for y in range(0,rows):
      new_row.append(enter_list[y][x])
    add_elements.append(new_row)
  print ('transpose of the above matrix is')
  return (add_elements)

nested_transpose_matrix = transpose_matrix()
for transpose in nested_transpose_matrix:
  print(transpose)