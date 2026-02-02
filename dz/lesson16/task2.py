class Mathematician:

    def square_nums(self, nums):
        return [n ** 2 for n in nums]

    def remove_positives(self, nums):
        return [n for n in nums if n <= 0]

    def filter_leaps(self, years):
        def is_leap(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        
        return [year for year in years if is_leap(year)]


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
