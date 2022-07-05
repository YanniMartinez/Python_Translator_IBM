import unittest 

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        self.assertEqual(englishToFrench(""),"") 
        self.assertEqual(englishToFrench(None),"") 
        self.assertNotEqual(englishToFrench("Hello"),"Hola")  

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello") 
        self.assertEqual(frenchToEnglish(""),"") 
        self.assertEqual(englishToFrench(None),"") 
        self.assertNotEqual(frenchToEnglish("Bonjour"),"Hola")  

unittest.main() #*Llamado al test principal