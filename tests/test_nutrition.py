from trice.physiology.nutrition import NutritionModel
def test_nutrition_pools():
    s=NutritionModel().step(protein=2,fat=1,omega3=.2,vitamins=.5,minerals=.4)
    assert s["protein"]==2 and s["omega3"]>.1
