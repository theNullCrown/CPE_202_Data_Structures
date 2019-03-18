# Name: Allie Blaising


import unittest
import filecmp
import subprocess
from huffman import *

usediff = True # When comparing files: True to use Linux diff, False to use Python filecmp

class TestList(unittest.TestCase):
    
    def test_cnt_freq(self):
        freqlist	= cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)


    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')
        freqlist2 = cnt_freq("file1.txt")
        hufftree2 = create_huff_tree(freqlist2)
        codes2 = create_code(hufftree2)
        self.assertNotEqual(codes, codes2)

    def test_error(self):
        with self.assertRaises(FileNotFoundError):
            huffman_encode("file.txt", "test.txt")

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("file1_out.txt", "file1_soln.txt"))

    def test_02_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("file2_out.txt", "file2_soln.txt"))


    def test_multiline_textfile(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("multiline_out.txt", "multiline_soln.txt"))


    def test_empty_textfile(self):
        huffman_encode("empty_thing.txt", "empty_thing_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb empty_thing_out.txt empty_thing.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("empty_thing_out", "empty_thing.txt"))

    def test_declaration(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("declaration_out", "declaration_soln.txt"))

    def test_empty_textfile(self):
        huffman_encode("test_only_a.txt", "test_only_a_out_2.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb  test_only_a_out_2.txt  test_only_a_out.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("test_only_a_out_2.txt", "test_only_a_out.txt"))

    def test_2_city(self):
        huffman_encode("2city11.txt", "2city11_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb  test_only_a_out_2.txt  test_only_a_out.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("test_only_a_out_2.txt", "test_only_a_out.txt"))

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")
        self.assertNotEqual(create_header(freqlist), "")

if __name__ == '__main__': 
   unittest.main()
