import os

filename = "todo.csv"


def options():
    print("\n1 - Add task\n"
          "2 - List tasks\n"
          "3 - Edit task\n"
          "4 - Delete task\n"
          "0 - Exit")
    return None


def ask_choice():
    try:
        feed = input("Your choice: ")
        choice = int(feed)
        return choice
    except ValueError:
        print("Unknown option, try again.")


# GOOD TO GO
def readFile():
    content = []
    if os.path.isfile(filename):
        try:
            filehandle = open(filename, "r", encoding="UTF-8")
            line = filehandle.readline()
            while len(line) > 0:
                content.append(line.strip())
                line = filehandle.readline()
            filehandle.close()
        except Exception:
            print(f"Failed to read file '{filename}'")
    else:
        writeFile(content)
    return content


# GOOD TO GO
def writeFile(content):
    try:
        filehandle = open(filename, "w", encoding="UTF-8")
        for line in content:
            filehandle.write(line + "\n")
    except Exception:
        print(f"Failed to write file '{filename}'")


# GOOD TO GO
def addTask():
    try:
        content = readFile()
        taskname = input("Insert task name: ")
        if len(taskname) < 4:
            raise Exception("Error! Task name must contain minimum of '4' characters.")
        elif len(taskname) > 30:
            raise Exception("Error! Task name must contain maximum of '30' characters.")
        else:
            content.append("[ ]"+";"+taskname)
            writeFile(content)
            print("Task added!")
    except Exception as e:
        print(e)
    return None


# FINALLY DONE
def listTasks():
    content = readFile()
    if len(content) == 0:
        print("There are no tasks to display.")
    else:
        print("Tasks below:")
        order_width = 5
        status_width = 6
        name_width = 4
        for i in content:
            name = i.split(";")[1].strip()
            if len(name) > name_width:
                name_width = len(name)

        string = f"| {{:>{order_width}}} | {{:<{status_width}}} | {{:<{name_width}}} |"

        header_line = string.format("order", "status", "name")
        separator_line = f"+{'-' * (order_width + 2)}+{'-' * (status_width + 2)}+{'-' * (name_width + 2)}+"

        print(separator_line)
        print(header_line)
        print(separator_line)

        ordial_num = 1
        for j in content:
            curr_status = ""
            if j.split(";")[0] == "[ ]":
                curr_status = "undone"
            else:
                curr_status = "done"
            row = string.format(ordial_num, curr_status, j.split(";")[1])
            ordial_num += 1
            print(row)
        print(separator_line)
    return None


# GOOD TO GO
def editTask():
    content = readFile()
    feed = input(f"Insert task order num to edit (1-{len(content)}, 0 to cancel): ")
    try:
        choice = int(feed)
        if choice == 0:
            raise Exception("Cancelling...")
        elif choice < 1 or choice > len(content):
            raise Exception(f"Feed '{feed}' is not within the specified range.")
        else:
            print("Edit task:\n"
                  "1 - Status\n"
                  "2 - Name\n"
                  "0 - Cancel")
            choice2 = ask_choice()
            if choice2 == 1:
                editing_part_status = content[choice - 1].split(";")
                if editing_part_status[0] == "[ ]":
                    editing_part_status[0] = "[x]"
                elif editing_part_status[0] == "[x]":
                    editing_part_status[0] = "[ ]"
                else:
                    raise Exception("something went wrong...")
                content[choice - 1] = ";".join(editing_part_status)
                writeFile(content)
                print("Status changed!")
            if choice2 == 2:
                new_name = input("Insert task name: ")
                if len(new_name) < 4:
                    raise Exception("Error! Task name must contain a minimum of '4' characters.")
                if len(new_name) > 30:
                    raise Exception("Error! Task name must contain a maximum of '30' characters.")
                else:
                    editing_part_name = content[choice - 1].split(";")
                    editing_part_name[1] = new_name
                    content[choice - 1] = ";".join(editing_part_name)
                    writeFile(content)
                    print("Task name changed!")
            if choice == 0:
                raise Exception("Cancelling...")
    except ValueError:
        print(f"Feed '{feed}' is not convertible to numeric value.")
        print("Aborting edit task.")
    except Exception as e:
        print(e)
    return None


# HAVING AN ISSUE REGARDING VALUEERROR EXCEPTION, IN PROGRESS. WORKS
def deleteTask():
    content = readFile()
    feed = input(f"Insert task order num to delete (1-{len(content)}, 0 to cancel): ")
    try:
        choice = int(feed)
        if choice == 0:
            raise Exception("Cancelling...")
        elif choice < 1 or choice > len(content):
            raise Exception(f"Feed '{feed}' is not within the specified range.")
        else:
            content.pop(choice-1)
            writeFile(content)
            print("Task deleted!")
    except Exception as e:
        if Exception == ValueError:
            print(f"Feed '{feed}' is not convertible to numeric value.")
        else:
            print(e)
    return None


def main():
    print("Program starting.", end='')
    while True:
        options()
        choice = ask_choice()
        if choice == 0:
            break
        if choice == 1:
            addTask()
        if choice == 2:
            listTasks()
        if choice == 3:
            editTask()
        if choice == 4:
            deleteTask()
    print("\nProgram ending.")
    return None


main()

