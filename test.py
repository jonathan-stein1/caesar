import sys
import caesar, reconstruct

from termcolor import cprint
import colorama

def main():
    colorama.init()

    input = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua."
    password = "The quick brown fox jumps over the lazy dog."

    test(input, password)

def test(input, password):
    cprint("Input:", attrs=["bold", "underline"])
    print(input + "\n")

    cprint("Password:", attrs=["bold", "underline"])
    print(password + "\n")

    output = caesar.encrypt(input, password)
    cprint("Output:", attrs=["bold", "underline"])
    print(output + "\n")

    revInput = caesar.decrypt(output, password)
    cprint("Reversed input:", attrs=["bold", "underline"])
    print(revInput)

    if revInput == input:
        cprint("(Correct)\n", "green")

    else:
        cprint("\nIncorrect en-/decryption!", "red")
        sys.exit(1)

    revPassword = reconstruct.reconstruct(input, output)
    cprint("Reversed password:", attrs=["bold", "underline"])
    print(revPassword)

    if reconstruct.compare(reconstruct.convertPassword(password), revPassword):
        cprint("(Correct)", "green")

    else:
        cprint("\nIncorrect reconstruction!", "red")
        sys.exit(1)

if __name__ == "__main__":
    main()
