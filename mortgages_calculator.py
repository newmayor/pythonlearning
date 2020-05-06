"""Numair Ahmed - self learning
Textbook: Intro to Computation and Programming Using Python by John Guttag
Ch. 8.4: Mortgages, an Extended Example
This exercise will examine the costs of three kinds of loans:
 - A fixed rate mortgage with no points
 - A fixed rate mortgage with points
 - A mortgage with an initial teaser rate followed by a higher rate for the duration

Requirements:
1. include a Mortgage class
2. include a subclass for each type of mortgage mentioned above
3. __init__ will have instance variables corresponding to: 
    - the initial loan amount, 
    - the monthly interest rate, 
    - the duration of the loan in months, 
    - a list of payments that have been made at the start of each month,
    - a list with the balance of the loan that is outstanding each month,
    - the amount of money to be paid each month,
    - and a description of the mortgage (typically None)
"""

def findPayment(loan, r, m):
    """Assum: loan and r are floats, m an int.
    Returns the monthly payment for a mortgage of size loan at a monthly rate of r for m months """
    return loan*((r*(1+r)**m)/((1+r)**m-1)) #loan calculation equation

class Mortgage(object):
    """Abstract class for building different kinds of mortgages. This means that all of the below equations and methods (w/in this class) are common to all three types of mortgage lending schemes. """
    def __init__(self, loan, annRate, months):
        """Assumes loan and annRate are floats, months an int.
        Creates a new mortgage of size loan, duration months, and annual rate annRate """
        self.loan = loan
        self.rate = annRate/12
        self.months = months
        self.paid = [0.0] #start with $0.00 paid of the mortgage
        self.outstanding = [loan] #I'm guessing this is in a list bc it will catalog outstanding loan balances every month into a list
        self.payment = findPayment(loan, self.rate, months) #why do we need to init with this inside __init__ ?
        self.legend = None #description of mortgage. Will this be changed later?

    def makePayment(self):
        """Make a payment """
        self.paid.append(self.payment) #my hunch was correct: each payment is appended to the end of the self.paid list
        reduction = self.payment - self.outstanding[-1]*self.rate #calculate how much the payment will reduce the outstanding PRINCIPLE balance
        self.outstanding.append(self.outstanding[-1] - reduction) #apply that reduction to the outstanding PRINCIPLE balance

    def getTotalPaid(self):
        """Return the total amount paid so far"""
        return sum(self.paid) #because all payments are tabulated to this list, you can sum down the whole list to get a total amount paid

    def __str__(self):
        return self.legend #why is this needed?
