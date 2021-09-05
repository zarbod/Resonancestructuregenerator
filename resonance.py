from lewisstructure import LewisStructure as Lewis


class Resonance:

    def __init__(self, structure):
        structure = Lewis()

    def create_lewis(self):
        formula = input("Enter chemical structure: ")
        # work in progress

        return formula

    def generate_resonance_structure(self):
        lewis = self.create_lewis()
        for element in lewis:
            if element[2] > 0:
                for i in range(0, len(lewis)):
                    if lewis[i] is element:
                        continue
                    else:
                        temp = lewis[i]
                        temp[2] += 1
                        if Lewis.check_octet(temp):
                            break
                        else:
                            temp[2] -= 1
                            continue

        return lewis
