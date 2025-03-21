class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_cook = []
        infinite_supply = set(supplies)
        for _ in range(len(recipes)):
            for i, recipe in enumerate(recipes):
                cook = True
                for j, ingredient in enumerate(ingredients[i]):
                    if ingredient not in infinite_supply:
                        cook = False
                        break
                if cook:
                    infinite_supply.add(recipe)
                    if recipe not in can_cook:
                        can_cook.append(recipe)

        return can_cook