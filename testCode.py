import unittest
import prog as app

class TestMyProga(unittest.TestCase):
    def setUp(self):
        self.app = app

    def test_write(self):
        # Перевірка на правильний клас
        for i in range(100):
            if(i==7 or i==6):
                self.assertEqual(app.class_filter(i), 1)
            elif(i==8):
                self.assertEqual(app.class_filter(i), 2)
            elif(i==9):
                self.assertEqual(app.class_filter(i), 3)
            elif(i==10):
                self.assertEqual(app.class_filter(i), 4)
            else:
                self.assertEqual(app.class_filter(i), "none")

        # Перевірка на виникнення помилки
        self.assertEqual(app.class_filter("asdasd"), "ValueError")
        self.assertEqual(app.class_filter("/\&!"), "ValueError")
        
        

if __name__ == "__main__":
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner (output='test-reports'))
