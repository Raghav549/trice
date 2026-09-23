from trice.physiology.absorption import AbsorptionModel
def test_nutrient_absorption():
    s=AbsorptionModel().step(digested=2,protein=1,fat=1,vitamins=1,minerals=1,water=2)
    assert s["glucose"]>0 and s["amino_acids"]>0 and s["water"]>0
