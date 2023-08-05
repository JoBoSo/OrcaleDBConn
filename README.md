# OrcaleDBConn
A class for quickly connecting to your Oracle databases and writing SQL queries that return pandas DataFrames

### Example
```
conn = OracleDBConn(env='test', user='jscott', config_dir='C:/user/tnsnames')<br>
df = conn.query_to_df("select org_unit_no, org_unit_code from org_unit")<br>
print(df)
```
