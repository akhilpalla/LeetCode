class Solution:
    def countOfAtoms(self, formula: str) -> str:
        i=0
        stack=[{}]
        n=len(formula)
        while i<n:
            element=formula[i]
            if element=="(":
                stack.append({})
                i+=1
            elif element==")":
                i+=1
                mol_set=stack.pop()
                start=i
                while i<len(formula) and formula[i].isdigit():
                    i+=1
                
                if start!=i:
                    val=int(formula[start:i])
                else:
                    val=1
                for atoms in mol_set:
                    mol_set[atoms]*=val
                
                for atoms in mol_set:
                    if atoms not in stack[-1]:
                        stack[-1][atoms]=mol_set[atoms]
                    else:
                        stack[-1][atoms]+=mol_set[atoms]

            else:
                start=i
                i+=1
                while i<len(formula) and formula[i].islower():
                    i+=1
                mol=formula[start:i]
                start=i
                while i<len(formula) and formula[i].isdigit():
                    i+=1
                if start!=i:
                    val=int(formula[start:i])
                else:
                    val=1
                if mol not in stack[-1]:
                    stack[-1][mol]=val
                else:
                    stack[-1][mol]+=val
                

        equation=""
        for mols in sorted(stack[-1].items()):
            if mols[1]==1:
                equation+=mols[0]
            else:
                equation+=mols[0]+str(mols[1])
        return equation