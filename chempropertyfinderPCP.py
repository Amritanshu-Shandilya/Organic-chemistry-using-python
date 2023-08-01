import pubchempy 
import urllib.request
import pillow

img_add = ''

def dataFromCommonName(c):
    compounds = pubchempy.get_compounds(c, 'name')

    print("Important data about ",c," : \n")
    for compound in compounds:
        print("Molecular formula  : ",compound.molecular_formula)
        print("Molecular weight  : ",compound.molecular_weight)
        print("IUPAC NAME  : ",compound.iupac_name.capitalize())


c = input('Enter the name of the compound here  :')
dataFromCommonName(c)
