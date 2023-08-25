import pandas as pd

class Element:
    """
    Represents an element in the periodic table
    """
    def __init__(self):
        pass
    
    @classmethod
    def create_element_object(cls, i, df):
        elem = cls()
        elem.element = df['element'][i]
        for attr in df.columns:
            elem.__dict__[attr] = df[attr][i]
        return elem

    @classmethod
    def create_all_element_objects(cls):
        df = pd.read_csv("data.csv")
        for i in range(len(df)):
            ele = cls.create_element_object(i, df)
            globals()[ele.element] = ele
        
    def is_more_electronegative(self, element2):
        return self.Electronegativity > element2.Electronegativity
    
    def __str__(self):
        return self.name

    def atomic_number(self):
        return self.AtomicNumber

class Chem:
    def __init__(self):
        Element().create_all_element_objects()
    
    def main(self):
        print(He.atomic_number())

Chem().main()
