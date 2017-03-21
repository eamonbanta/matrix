from matrix import Matrix


class MatrixProgram(object):
    commands = set(['q', 'c', 'm', 'a', 'n', 'p'])

    def __init__(self):
        self.matrices = {}

    def loop(self):
        while True:
            command = raw_input("(q)uit; (c)reate; (m)ultiply; (a)dd; matrice (n)ames; (p)rint matrix: ")
            if command == 'q':
                return 0
            elif command not in self.commands:
                continue

            if command == 'c':
                self.create_matrix()
            elif command == 'm':
                self.multiply_matrices()
            elif command == 'a':
                self.add_matrices()
            elif command == 'n':
                self.print_names()
            elif command == 'p':
                self.print_matrix()
            else:
                raise Excpetion()

    def print_names(self):
        print self.matrices.keys()

    def print_matrix(self):
        name = raw_input("Choose a matrix {}: ".format(self.matrices.keys()))
        print self.matrices[name]

    def multiply_matrices(self):
        a = raw_input("First matrix? ")
        b = raw_input("Second matrix? ")

        a = self.matrices[a]
        b = self.matrices[b]

        print a.multiply(b)

    def add_matrices(self):
        a = raw_input("First matrix? ")
        b = raw_input("Second matrix? ")

        a = self.matrices[a]
        b = self.matrices[b]

        print a.add(b)

    def create_matrix(self):
        name = raw_input("Name: ").strip()
        data = raw_input("Define matrix: ")
        self.matrices[name] = Matrix(data)


if __name__ == "__main__":
    p = MatrixProgram()
    exit(p.loop())
