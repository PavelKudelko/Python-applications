import time


def readfile(filename):
    content = []
    filehandle = open(filename, 'r', encoding="UTF-8")
    line = filehandle.readline()
    while len(line) > 0:
        if line != "\n" and line != "":
            content.append(int(line.strip()))
        line = filehandle.readline()
    filehandle.close()
    return content


def bubbleSort(Values: list[int]):
    ListSize = len(Values)
    for i in range(ListSize):
        Remaining = ListSize - i - 1
        for j in range(0, Remaining):
            CurrentValue = Values[j]
            NextValue = Values[j + 1]
            if CurrentValue > NextValue:
                Values[j] = NextValue
                Values[j + 1] = CurrentValue
    return Values


def quicksort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        less = []
        greater = []
        for i in list[1:]:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)
        values = quicksort(less) + [pivot] + quicksort(greater)
    return values


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    file = readfile(filename)
    print("# --- Measuring starts --- #")
    print(f"{len(file)} values to sort.")
    print("Measuring sorting algorithm speeds in nanoseconds...")
    start_bubble = time.perf_counter_ns()
    sortedbubble = bubbleSort(file.copy())
    stop_bubble = time.perf_counter_ns()
    elapsed_bubble = stop_bubble - start_bubble
    start_quick = time.perf_counter_ns()
    sortedquick = quicksort(file.copy())
    stop_quick = time.perf_counter_ns()
    elapsed_quick = stop_quick - start_quick
    print(f"Bubble sort: {elapsed_bubble} ns")
    print(f"Quick sort: {elapsed_quick} ns")
    print("# --- Measuring ends --- #")
    print("Program ending.")
    return None


main()