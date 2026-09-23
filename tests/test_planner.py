from trice.ai.planner import Planner
from trice.ai.goals import Goal
def test_planner_selects_goal():
    g=Planner().choose({"energy":.2,"comfort":.9},[Goal("energy",.8),Goal("comfort",.5)])
    assert g is not None and g.name=="energy"
