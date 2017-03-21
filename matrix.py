


class Matrix(object):
    def __init__(self, data, rows=None, cols=None):
        try:
            data = data.split(';')
        except AttributeError:
            pass
   
        try:
            for i, row in enumerate(data):
                data[i] = [int(x) for x in row.strip().split(' ')]
        except AttributeError:
            pass

        self.rows = len(data)
        if rows and rows != self.rows:
            raise Exception("Data does not match definition.")
        
        self.cols = len(data[0])
        if cols and self.cols != cols:
            raise Exception("Data does not match definition.")

        for row in data:
            if self.cols != len(row):
                raise Exception("Data does not match definition.")

        self.data = data

    def __str__(self):
        s = ["{rows} x {cols} Matrix".format(rows=self.rows, cols=self.cols)]
        for i in xrange(self.rows):
            s.append(" ".join([str(x) for x in self.data[i]]))
        s.append("\n")
        return "\n".join(s)

    def add(self, b):
        if self.rows != b.rows or self.cols != b.cols:
            raise Exception("{}x{} matrix can't be added to a {}x{} matrix".format(self.rows, self.cols, b.rows, b.cols))

        data = []
        for i in xrange(self.rows):
            row = []
            for j in xrange(self.cols):
                row.append(self.data[i][j] + b.data[i][j])
            data.append(row)

        return Matrix(data, self.rows, self.cols)

    def multiply(self, b):
        if self.cols != b.rows:
            raise Exception("Can't multiply a {}x{} matrix with a {}x{} matrix".format(self.rows, self.cols, b.rows, b.cols))

        a_rows = self.data
        b_cols = b.make_columns()

        result_data = []
        for i in xrange(self.rows):
            result_data.append([])
            row = self.data[i]

            for j in xrange(b.cols):
                col = b_cols[j]
                v = 0
                for k in xrange(self.cols):
                    v += row[k]*col[k]
                result_data[i].append(v)

        return Matrix(result_data, self.rows, b.cols) 

    def make_columns(self):
        data = []
        for i in xrange(self.cols):
            col = []
            for j in xrange(self.rows):
                col.append(self.data[j][i])
            data.append(col)
        return data


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
