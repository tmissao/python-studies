import unittest
import cap

class TestCap(unittest.TestCase):
  def test_one_word(self):
    text = 'python'
    result = cap.cap_text(text)
    expect = 'Python'
    self.assertEqual(result, expect)

  def test_multiple_words(self):
    text = 'python rocks!'
    result = cap.cap_text(text)
    expect = 'Python Rocks!'
    self.assertEqual(result, expect)

if __name__ == '__main__':
  unittest.main()