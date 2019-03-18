## Name: Allie Blaising 

import unittest
from sep_chain_ht import *

class TestList(unittest.TestCase):

   def test_insert1(self):
      hash1 = MyHashTable()
      hash1.insert(11, "a") 
      hash1.insert(3, "b")
      self.assertEqual(hash1.size(), 2)

   def test_get1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      self.assertEqual(hash1.get_item(3), 'b')
      self.assertEqual(hash1.get_item(11), 'a')
      
   def test_get2(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      with self.assertRaises(LookupError):
            hash1.get_item(6)

   def test_remove1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      self.assertEqual(hash1.remove(11), (11, 'a'))
      self.assertEqual(hash1.size(), 0)

   def test_table_size(self):
      table1, table2, table3 = MyHashTable(1), MyHashTable(90), MyHashTable(22)
      self.assertEqual(table1.table_size(), 1)
      self.assertEqual(table2.table_size(), 90)
      self.assertEqual(table3.table_size(), 22)

   def test_load_factor1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      hash1.insert(1, "g")
      hash1.insert(2, "h")
      self.assertEqual(hash1.load_factor(), 1.4)


   # Check the right # of collisons

   def test_load_over_load_factor(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      hash1.insert(1, "g")
      hash1.insert(2, "h")
      hash1.insert(3, "k")
      hash1.insert(7, "l")
      hash1.insert(1, "o")
      self.assertEqual(hash1.table_size, 11) 


   def test_collisions2(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a") 
      hash1.insert(3, "b") 
      hash1.insert(1, "c") 
      hash1.insert(8, "d") 
      hash1.insert(4, "e") 
      hash1.insert(5, "f") 
      hash1.insert(1, "g") 
      hash1.insert(2, "h")
      self.assertEqual(hash1.collisions(), 2) 
        


if __name__ == '__main__': 
   unittest.main()


