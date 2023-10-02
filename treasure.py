row1 = ["😀","😀","😀"]
row2 = ["😀",'😀','😀']
row3 = ["😀","😀","😀"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position_to_treasure = input("the position value you want to treasure: ")

column_position = int(position_to_treasure[0])
row_position = int(position_to_treasure[1])

# map[column_position-1][row_position-1] = "X"
map[row_position-1][column_position-1] = "X"
print(f"{row1}\n{row2}\n{row3}")