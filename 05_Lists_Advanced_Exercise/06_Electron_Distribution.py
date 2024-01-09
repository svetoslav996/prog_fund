def fill_shells(electrons):
    shells = []
    shell_number = 1

    while electrons > 0:
        max_electrons_in_shell = 2 * (shell_number ** 2)

        if electrons >= max_electrons_in_shell:
            shells.append(max_electrons_in_shell)
            electrons -= max_electrons_in_shell
        else:
            shells.append(electrons)
            electrons = 0

        shell_number += 1

    return shells

# Get the number of electrons from the user
num_electrons = int(input())

# Fill the shells and print the result
filled_shells = fill_shells(num_electrons)
print(filled_shells)
