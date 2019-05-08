--looking for interests of all customers that were born in 1986
--taking interests for given list of ids
select * from Customer_interests where CustomerID in (
    --make a list of id, where DateOfBirth between '1986-01-01' and '1986-12-31'
    --maybe need to avoid hardcoded frames and use extraction year from DateOfBirth
select CustomerID from Sensitive_customers where DateOfBirth>='1986-01-01' and DateOfBirth<='1986-12-31' union
select CustomerID from NonSensitive_customers where DateOfBirth>='1986-01-01' and DateOfBirth<='1986-12-31' union
select CustomerID from Foreign_customers where DateOfBirth>='1986-01-01' and DateOfBirth<='1986-12-31')