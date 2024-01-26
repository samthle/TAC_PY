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
        sorted_dna = self._merge_sort(self.dna)
        return sorted_dna

    @staticmethod
    def _merge_sort(dna):
        sorted_dna = "".join(sorted(dna))
        return sorted_dna


class Squidward:
    def __init__(self, dna):
        self.dna = dna

    def process_dna(self):
        processed_dna = ""
        i = 0
        while i < len(self.dna):
            if i < len(self.dna) - 2 and self.dna[i:i + 3] == self.dna[i] * 3:
                processed_dna += "(0_0)"
                i += 3
            else:
                processed_dna += self.dna[i]
                i += 1
        return processed_dna


def main():
    input_data = input().strip().lower()  # Convert to lowercase for case-insensitivity and strip whitespace
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
        print("Invalid input")


if __name__ == "__main__":
    main()
