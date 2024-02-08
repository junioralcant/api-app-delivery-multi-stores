from sqlalchemy import create_engine

class DBConnectionHandler: 
    def __init__(self) -> None:
        self.__connection_string = "mssql+pyodbc://{}:{}@localhost:3306/{}".format(
            'root',
            'toor',
            'multi_stores',
        )

        self.__engine = self.__create_database_connection()

    def __create_database_connection(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine
    