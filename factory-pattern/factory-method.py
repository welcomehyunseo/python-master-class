import json
import xml.etree.ElementTree as ET


class Movie:
    def __init__(self, title, year, director) -> None:
        self.title = title
        self.year = year
        self.director = director

    def print_info(self):
        print(self.title, "came out in", self.year, "that made by", self.director)


class JSONFileReader:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.data = {}

    def parser(self) -> None:
        file = open(self.file_path)
        data = json.load(file)
        self.data = data
        file.close()

    def create_movie_object(self) -> Movie:
        if not self.data:
            self.parser()

        movie = Movie(
            self.data["Title"],
            self.data["Year"],
            self.data["Director"],
        )
        return movie


class XMLFileReader:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.data = {}

    def parser(self) -> None:
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        self.root = root

    def create_movie_object(self) -> Movie:
        if not self.data:
            self.parser()

        movie = Movie(
            self.root.find("Title").text,
            self.root.find("Year").text,
            self.root.find("Director").text,
        )
        return movie


file_path_list = [
    "movies/Avatar.json",
    "movies/interstellar.xml",
]


def factory_method(file_path_list):
    for file_path in file_path_list:
        extension = file_path.split(".")[1]
        if extension == "json":
            reader = JSONFileReader(file_path)
            movie = reader.create_movie_object()
            movie.print_info()
        elif extension == "xml":
            reader = XMLFileReader(file_path)
            movie = reader.create_movie_object()
            movie.print_info()


factory_method(file_path_list)
