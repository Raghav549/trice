from trice.runtime.sql_schema import schema_sql


def test_sql_schema_contains_experiments_and_metrics():
    sql = schema_sql().upper()
    assert "CREATE TABLE IF NOT EXISTS EXPERIMENTS" in sql
    assert "CREATE TABLE IF NOT EXISTS METRICS" in sql
    assert "CREATE INDEX" in sql
