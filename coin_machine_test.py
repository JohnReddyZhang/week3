from coin_machine import CoinMachine
import unittest

class CoinMachineTest(unittest.TestCase):

    def test_zero(self):
        machine = CoinMachine()
        coins = machine.dispense(0)
        self.assertEqual([0,0,0,0], coins)

    def test_1(self):
        machine = CoinMachine()
        coins = machine.dispense(1)
        self.assertEqual([0,0,0,1], coins)

    def test_4(self):
        machine = CoinMachine()
        coins = machine.dispense(4)
        self.assertEqual([0,0,0,4], coins)

    def test_5(self):
        machine = CoinMachine()
        coins = machine.dispense(5)
        self.assertEqual([0,0,1,0], coins)

    def test_6(self):
        machine = CoinMachine()
        coins = machine.dispense(6)
        self.assertEqual([0,0,1,1], coins)

    def test_10(self):
        machine = CoinMachine()
        coins = machine.dispense(10)
        self.assertEqual([0,1,0,0], coins)
    #
    # def test_15(self):
    #     machine = CoinMachine()
    #     coins = machine.dispense(15)
    #     self.assertEqual([0,1,1,0], coins)
    #
    # def test_25(self):
    #     machine = CoinMachine()
    #     coins = machine.dispense(25)
    #     self.assertEqual([1,0,0,0], coins)
    #
    # def test_50(self):
    #     machine = CoinMachine()
    #     coins = machine.dispense(50)
    #     self.assertEqual([2,0,0,0], coins)
    # #
    # def test_99(self):
    #     machine = CoinMachine()
    #     coins = machine.dispense(99)
    #     self.assertEqual([3,2,0,4], coins)

unittest.main()
