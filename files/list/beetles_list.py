def beatleslist_sort():
    """
    Function to collect and sort Beatles band members' names.
    """
    beetles_names = []

    print("Enter the names of Beatles members (type 'done' to finish):")

    while True:
        inp = input("Enter a name: ").strip()
        if inp.lower() == 'done':
            break
        if inp and inp not in beetles_names:
            beetles_names.append(inp)
        elif inp in beetles_names:
            print(f"'{inp}' is already in the list. Please enter a different name.")

    beetles_names.sort()
    return beetles_names


# Run the function and print the sorted list
if __name__ == "__main__":
    sorted_beetles_names = beatleslist_sort()
    print("\nSorted Beatles names:")
    for name in sorted_beetles_names:
        print(f"- {name}")
