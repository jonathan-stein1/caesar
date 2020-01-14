import sys, caesar, reconstruct

def main():
    input = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua."
    password = "The quick brown fox jumps over the lazy dog."

    test(input, password)

def test(input, password):
    print("Input:\n" + input + "\n")
    print("Password:\n" + password + "\n")

    output = caesar.encrypt(input, password)
    print("Output:\n" + output + "\n")

    revInput = caesar.decrypt(output, password)
    print("Reversed input:\n" + revInput)

    if revInput == input:
        print("(Correct)\n")

    else:
        print("\n\nIncorrect en-/decryption!")
        sys.exit(1)

    revPassword = reconstruct.reconstruct(input, output)
    print("Reversed password:\n" + revPassword)

    if reconstruct.compare(reconstruct.convertPassword(password), revPassword):
        print("(Correct)")

    else:
        print("\n\nIncorrect reconstruction!")
        sys.exit(1)

if __name__ == "__main__":
    main()
