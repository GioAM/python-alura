class Program:
    def __init__(self, title, year):
        self._title = title.title()
        self.year = year
        self._likes = 0

    def like(self):
        self._likes += 1

    @property
    def title(self):
        return self._title

    @title.setter
    def name(self, title):
        self._title = title.title()

    def __str__(self):
        return f"Program: {self.title} - {self.year} - {self._likes}"


class Movie(Program):
    def __init__(self, title, year, duration):
        super().__init__(title, year)
        self.duration = duration

    def __str__(self):
        return f"Movie: {self.title} - {self.year} - {self.duration} min - {self._likes}"


class Serial(Program):
    def __init__(self, title, year, seasons):
        super().__init__(title, year)
        self.seasons = seasons

    def __str__(self):
        return f"Serial: {self.title} - {self.year} - {self.seasons} seasons - {self._likes}"


class Playlist():
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    def __len__(self):
        return len(self._programs)


avenger = Movie('vingadores - guerra infinita', 2018, 160)
atlanta = Serial('atlanta', 2018, 2)
panic = Movie('Todo mundo em pânico', 1999, 100)
demo = Serial('Demolidor', 2016, 2)

movies_and_serials = [avenger, atlanta, panic, demo]
playlist_weekend = Playlist('Weekend', movies_and_serials)

print(f"{playlist_weekend.name} - {len(playlist_weekend)} programas")
for program in playlist_weekend:
    print(program)
