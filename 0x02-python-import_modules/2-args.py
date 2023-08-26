#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    argv = sys.argv[1:]
    num_args = len(argv)
    
    if num_args == 0:
        print("Number of argument(s): 0.")
        print(":")
    else:
        print(f"Number of argument(s): {num_args}.")
        print(f"Argument{'s' if num_args > 1 else ''}: {', '.join(argv)}:")
        
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
