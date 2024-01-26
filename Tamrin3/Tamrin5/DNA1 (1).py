class MrKrabs:
    def __init__(self, dna):
        self.dna = dna

    def process_dna(self):
        processed_dna = self.dna.replace("tt", "o")
        processed_dna += self.dna[:10]
        return processed_dna


class SpongeBob:
    def __init__(self, dna):
        self.dna = dna

    def process_dna(self):
        sorted_dna = self.merge_sort(self.dna)
        return sorted_dna

    def merge_sort(self, dna):
        sorted_dna = "".join(sorted(dna))
        return sorted_dna


class Squidward:
    def __init__(self, dna):
        self.dna = dna

    def process_dna(self):
        processed_dna = ""
        i = 0
        while i < len(self.dna):
            if i < len(self.dna) - 2 and self.dna[i] == self.dna[i + 1] == self.dna[i + 2]:
                processed_dna += "(0_0)"
                i += 3
            else:
                processed_dna += self.dna[i]
                i += 1
        return processed_dna


def main():
    input_data = input() 
    if input_data.startswith("m"):
        krabs = MrKrabs(input_data)
        print(krabs.process_dna())
    elif input_data.startswith("sb"):
        spongebob = SpongeBob(input_data)
        print(spongebob.process_dna())
    elif input_data.startswith("s") and input_data[1] != "b":
        squidward = Squidward(input_data)
        print(squidward.process_dna())
    else:
        print("invalid input")


if __name__ == "__main__":
    main()

