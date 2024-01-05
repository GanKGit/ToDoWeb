def readToDoFile():
    file = open("todos.db","r")
    lines=file.readlines()
    file.close()
    local_todos=[]
    for line in lines:
        line = line.rstrip()
        local_todos.append(line)
    return local_todos

def writeToDoFile(local_todos):
    file = open("todos.db", "w")
    for item in local_todos:
        file.write(item + "\n")
    file.close()