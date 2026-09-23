from trice.runtime.sqlite_store import SQLiteStore


def test_sqlite_store_persists_experiment_and_metrics():
    store = SQLiteStore()
    experiment_id = store.add_experiment("baseline", 7, '{"lr":0.001}')
    store.add_metrics(experiment_id, 1, {"loss": 0.2})
    row = store.connection.execute(
        "SELECT name, seed FROM experiments WHERE id = ?", (experiment_id,)
    ).fetchone()
    metric = store.connection.execute(
        "SELECT value FROM metrics WHERE experiment_id = ?", (experiment_id,)
    ).fetchone()
    assert row == ("baseline", 7)
    assert metric == (0.2,)
    store.close()
