from trice.ai.goals import Goal
def test_goal_error(): assert Goal("energy",.8).error(.5)==.3
