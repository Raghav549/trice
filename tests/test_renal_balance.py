from trice.physiology.renal_balance import RenalBalance
def test_renal_balance():
    s=RenalBalance().step(water_input=2,sodium_input=1,acid_load=.2)
    assert 0<=s["acid_base"]<=1
