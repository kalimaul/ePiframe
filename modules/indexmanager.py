import os


class IndexManager:

    __index = -1
    __id = None
    __path = None

    def __init__(self, path: str):
        self.__path = path

        # read index from file to change after each run
        if os.path.exists(path):
            with open(path, "r") as file_lines:
                lines = file_lines.readlines()
                if len(lines) == 2:
                    self.__id = str(lines[0]).rstrip()
                    self.__index = int(lines[1])
                file_lines.close()

    def save(self):
        with open(self.__path, "w") as file_data:
            file_data.write(str(self.__id))
            file_data.write("\n")
            file_data.write(str(self.__index))
            file_data.close()

    def get_index(self) -> int:
        return self.__index

    def get_id(self) -> str:
        return self.__id

    def set_index(self, value: int):
        self.__index = value

    def set_id(self, value: str):
        self.__id = value

    def check_index(self, max_value: int):
        self.__index = 0 if self.__index >= max_value else self.__index
