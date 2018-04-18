class PrimeFactors:
    def generate(arg):
        factors = []
        divisor = 2
        while arg > 1:
            while arg % divisor == 0:
                factors.append(divisor)
                arg = arg / divisor
            divisor += 1
        # if arg > 1:
        #     factors.append(arg)
        return factors
        # cheating?
        # as few as keystroks would be reasonable?
        # When (hard) coding violates the principle of minimum strokes,
        # think about a change
        # what you need to work on and find that it works?
        
