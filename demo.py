import sys


def fix_name(name: str) -> str:
    """
    Fix the name by removing leading and trailing white spaces and capitalizing the first
    letter of each word.

    Parameters:
        name (str): The name to be fixed.

    Returns:
        str: The fixed name.
    """
    name = name.strip().title()
    return ''.join(ch for ch in name if ch.isalpha())


def print_greeting(name: str = '') -> None:
    """
    Print a greeting to the given name. If no name is provided, it defaults to 'World'.

    Parameters:
        name (str, optional): The name to greet. Defaults to ''.

    Returns:
        None
    """
    name = fix_name(name) if name else 'World'
    print(f'Hello, {name}!')


if __name__ == "__main__":
    args = sys.argv[1] if len(sys.argv) >= 2 else ''
    print_greeting(args)