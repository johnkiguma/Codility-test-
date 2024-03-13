#card payment
#you are given a list of all transactions on a bank account during tthe year 2020 the account was empty at the beginning balance 0 
#each transacttion should specify the date and the amount of money  executed.
#if the amount is negative or less than o then its a card payment otherwiise it was an incoming transfer amount at least 0 (the date should have  the format yyyy mm dd)
#additionally there is a fee for havving a card which is 5 per month. 
#this fee is deducted from the account balance at the end of each month unless there was less than 3 payments made by the card for a total cost of least 100 within that month .
#your task is to find the balance at the end of the year.
#example input:given a=100 ,100 100, -10) and d=2020 01 01, 2020 02 01, 2020 03 01, 2020 04 01, 2 the function should return 230 as the final balance.
#write a function def solution(A,D) that given an array a of n integers representing transaction amounts and an array d of n strings representing transacion ddates ,returns the final balance of the account at the end of year 2020 .transaction number k (for k within range [0..N-1]) was execcuted on the date represented by d[k] for amount a[k

#write  function solution that takes two arrays, A for amounts and D for dates.
#Initialize balance to 0 Initialize monthly_fee to 0 #Extract date and amount from the expense
def solution(A, D):
    balance = 0
    monthly_fee = 0
    #
    
    for i in range(len(A)):
        amount = A[i]
        date = D[i]
        
        if amount < 0:
            balance += amount
## Extract month from date            
                       
        month = int(date[5:7])  
        if month == 1:
            monthly_fee = 5
            ## checking if it's the first day of the month
        #add the expense to the balance.
        if date.endswith('-01'):
            balance -= monthly_fee
            monthly_fee = 0
            
    return balance 
  #dictionaries representing the expenses dates and prices
expenses = [
    {"date": "2022-08-01", "amount": 100},
    {"date": "2022-01-15", "amount": 100},
    {"date": "2022-02-01", "amount": 100},
    {"date": "2022-02-15", "amount": -10}
]
    
total_spent = 0
for expense in expenses:

    date = expense["date"]
    amount = expense["amount"]
    print(f"Spent {amount} on {date}")
    total_spent += amount

#output
print(f"Total spent: {total_spent}")
print(f"Remaining balance: {total_spent - (12*5)}")












   
