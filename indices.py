from threading import Thread

#Find the arrangement of streaks in rows and columns
def arrangement(col_list, row_list, cellMAP):
    # how many cells are in a row/column
    count = 0

    for i in range(len(cellMAP)):
        col_list.append([])
        row_list.append([])

    columnThread = Thread(target=columnStreaks, args=(col_list, cellMAP,))
    columnThread.start()

    rowThread = Thread(target=rowStreaks, args=(row_list, cellMAP,))
    rowThread.start()
    
    columnThread.join()
    rowThread.join()

#Identifies all the streaks in each column
def columnStreaks(list, cellMAP):
    streak = 0
    for col in range(len(cellMAP)):
        for row in range(len(cellMAP)):

            if cellMAP[row][col] == 1:
                # add to the count when a cell is present
                streak += 1
                # what if that cell is the last in the column?
                if row == len(cellMAP) - 1:
                    # add count to list for column data
                    list[col].append(streak)
                    # reset count for next column
                    streak = 0

            # what if a streak of cells stops in column?
            elif cellMAP[row][col] == 0 and streak >= 1:
                # add count to list for column data
                list[col].append(streak)
                # reset for next set of cells in row
                streak = 0

#Identifies all the streaks in each row
def rowStreaks(list, cellMAP):
    streak = 0
    for row in range(len(cellMAP)):
        for col in range(len(cellMAP)):

            # add to the count when a cell is present
            if cellMAP[row][col] == 1:
                streak += 1
                # what if that cell is the last in the row?
                if col == len(cellMAP) - 1:
                    # add streak to list for row data
                    list[row].append(streak)
                    # reset streak for next row
                    streak = 0

            # what that streak of cells stops in row?
            elif cellMAP[row][col] == 0 and streak >= 1:
                # add streak to list for row data
                list[row].append(streak)
                # reset for next set of cells in row
                streak = 0