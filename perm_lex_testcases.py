import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])
        self.assertEqual(perm_lex.perm_gen_lex('a'), ['a'])
        self.assertEqual(perm_lex.perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']) 
        self.assertEqual(perm_lex.perm_gen_lex(''), []) # check empty 
        self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc','acb','bac','bca','cab','cba'])


if __name__ == "__main__":
        unittest.main()
