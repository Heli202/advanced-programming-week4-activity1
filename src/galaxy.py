
class Galaxy:

    def __init__(self, galaxy_name: str):
        self.galaxy_name = galaxy_name

    def __str__(self):
        return f'Galaxy Name: {self.galaxy_name}'

    def __hash__(self):
        return hash(self.galaxy_name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Galaxy):
            return self.galaxy_name == other.galaxy_name
        if isinstance(other, int):
            return self.galaxy_name == other
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Galaxy):
            return self.galaxy_name < other.galaxy_name
        if isinstance(other, int):
            return self.galaxy_name < other
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Galaxy):
            return self.galaxy_name > other.galaxy_name
        if isinstance(other, int):
            return self.galaxy_name > other
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Galaxy):
            return self.galaxy_name <= other.galaxy_name
        if isinstance(other, int):
            return self.galaxy_name <= other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Galaxy):
            return self.galaxy_name >= other.galaxy_name
        if isinstance(other, int):
            return self.galaxy_name >= other
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Galaxy):
            return self.galaxy_name != other.galaxy_name
        if isinstance(other, int):
            return self.galaxy_name != other
        return NotImplemented

if __name__ == '__main__':

    galaxies = [
        "Milky Way",
        "Andromeda",
        "Triangulum",
        "Whirlpool",
        "Sombrero",
        "Pinwheel",
        "Messier 87",
        "Centaurus A",
        "Large Magellanic Cloud",
        "Small Magellanic Cloud",
        "NGC 1300",
        "NGC 6744",
        "IC 1101",
        "Messier 81",
        "Messier 82",
        "Cartwheel Galaxy",
        "NGC 253",
        "NGC 4038",
        "NGC 4039",
        "NGC 4414"
    ]

    print(Galaxy(galaxies).__ne__(Galaxy(galaxies)))