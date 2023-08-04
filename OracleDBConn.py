import oracledb
import getpass
import pandas as pd

class OracleDBConn:
    '''
    A class to quickly connect to your Oracle databases and retrieve data as pandas DataFrames using SQL.

    ...
    Class Variables
    ---------------
    test_dsn : the DSN for your test DB
    prod_dsn : the DSN for your production DB

    ...
    Attributes
    ----------
    env : str
        Either 'test' or 'prod', which refer to your test DSN and prod DSN, respectively.
        DSN is not required when env is not None.
    user : str
        Your username. User input will be requested if None.
    password : str
        Your password. User input will be requested if None.
    dsn : str
        Your DSN
        DSN is not required if env is not None.
    config_dir : str
        Your configurations Directory.
    '''
    test_dsn = '''
        (DESCRIPTION=
            (ADDRESS=
                (PROTOCOL=[YOUR PROTOCOL])
                (HOST=[YOUR HOST])
                (PORT=[YOUR PORT])
            )
            (CONNECT_DATA=
                (SERVER=[YOUR SERVER])
                (SERVICE_NAME=[YOUR SERVICE NAME])
            )
        )
    '''

    prod_dsn = '''
        (DESCRIPTION=
            (ADDRESS=
                (PROTOCOL=[YOUR PROTOCOL])
                (HOST=[YOUR HOST])
                (PORT=[YOUR PORT])
            )
            (CONNECT_DATA=
                (SERVER=[YOUR SERVER])
                (SERVICE_NAME=[YOUR SERVICE NAME])
            )
        )
    '''

    def __init__(self, env=None, user=None, password=None, dsn=None, config_dir=None):
        '''
        Constructs an OracleDBConn object.

        ...
        Parameters
        ----------
        env : str
            Either 'test' or 'prod', which refer to your test DSN and prod DSN, respectively.
            DSN is not required when env is not None.
        user : str
            Your username. User input will be requested if None.
        password : str
            Your password. User input will be requested if None.
        dsn : str
            Your DSN
            DSN is not required if env is not None.
        config_dir : str
            Your configurations Directory.
        '''
        self.env = env
        self.user = user
        self.password = password
        self.dsn = dsn 
        self.config_dir = config_dir 
        self.cursor = None
        self.get_user()
        self.get_password()
        self.get_dsn()
        self.get_config_dir()
        self.get_cursor()

    def get_user(self):
        if self.user == None:
            self.user = input("Enter user: ")

    def get_password(self):
        if self.password == None:
            self.password = getpass.getpass("Enter password: ")

    def get_dsn(self):
        if self.env == 'test' and self.dsn == None:
            self.dsn = self.test_dsn
        elif self.env == 'prod' and self.dsn == None:
            self.dsn = self.prod_dsn
        elif self.dsn == None:
            raise Exception("self.env must be 'prod' or 'test' since self.dsn is None")
        
    def get_config_dir(self):
        if self.config_dir == None:
            self.config_dir = input("Enter configuration directory: ")

    def get_cursor(self):
        connection = oracledb.connect(
            user=self.user,
            password=self.password,
            dsn=self.dsn,
            config_dir=self.config_dir
        )
        
        print("Successfully connected to Oracle Database")

        cursor = connection.cursor()
        self.cursor = cursor

    def cursor(self):
        return self.cursor
    
    def close_cursor(self):
        self.cursor.close()
        print('cursor closed')
    
    def query_to_df(self, query_string):
        '''
        Returns a pandas df for the query in query_string
        '''
        cursor = self.cursor
        cursor.execute(query_string)
        data = cursor.fetchall()
        df = pd.DataFrame(data)
        df.columns = [column[0] for column in cursor.description]
        return df
    

### Examples ###

conn = OracleDBConn(env='test', user='jscott', config_dir='//JSCOTT/tnsnames')

df = conn.query_to_df("select org_unit_no, org_unit_code from org_unit")
print(df)