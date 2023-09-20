# OrcaleDBConn
A class for quickly connecting to your Oracle databases and writing SQL queries that return pandas DataFrames. Just update the class variables called ```prod_dsn``` and ```test_dsn``` with your connection parameters (I use tnsnames). All the details are in the docstrings.

### Example
```
import OracleDBConn

conn = OracleDBConn(env='test', user='jscott', config_dir='C:/user/tnsnames')<br>
df = conn.query_to_df("select org_unit_no, org_unit_code from org_unit")<br>
print(df)
```
