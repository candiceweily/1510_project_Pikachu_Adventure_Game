def display_welcome_message() -> None:
    """
    Print a welcome message and an ASCII art representation of Pikachu.
    """
    print("Welcome to Pikachu adventure game!")
    print("\033[93m" + r"""
                  \:.             .:/
                   \``._________.''/ 
                    \             / 
             .--.--, / .':.   .':. \
            /__:  /  | '::' . '::' |
               / /   |`.   ._.   .'|
              / /    |.'         '.|
             /___-_-,|.\  \   /  /.|
                  `==|:=         =:|
                     `.          .'
                       :-._____-.:
                      `''       `'' 
    """ + "\033[0m")


def print_congratulations() -> None:
    """
    Print a congratulatory message and an ASCII art representation to celebrate defeating the final boss.
    """
    print("You've defeated the final boss!")
    print("\033[93m" + r"""
                   ___________
                  '._==_==_=_.'
                  .-\:      /-.
                 | (|:.     |) |
                  '-|:.     |-'
                    \::.    /
                     '::. .'
                       ) (
                     _.' '._
                    `-------` 
    """ + "\033[0m")

    print("Pikachu is enjoying the triumph!")