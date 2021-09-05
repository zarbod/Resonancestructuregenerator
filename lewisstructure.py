class LewisStructure:
    def __init__(self, structure=None):
        if structure is None:
            self.structure = []
            # the above structure will be filled with lists in the following format: [<element>, <bonds>,
            # <lone pairs>, [[<other indices that it is connected to>, <single bond, double bond, or triple bond>]]
        else:
            self.structure = structure

    def check_octet(self, i):
        if i[0] == "H":
            if i[1] != 1:
                return False
        else:
            if 2 * i[1] + 2 * i[2] > 8:
                return False

    def check_for_no_bonds(self,i):
        if i[1] < 1:
            return False

    def check_validity(self):
        for i in self.structure:
            self.check_octet(i)
            self.check_for_no_bonds(i)


