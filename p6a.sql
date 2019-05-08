-- not sure that its right way to take data if Non-sensitive customers Has more than 3 million entries, but for now it works
-- taking address for given list of ids
select * from Customer_address where CustomerID in (
    --make a list of id, where customers are active
select CustomerID from Sensitive_customers where IsActive=true union
select CustomerID from Foreign_customers where IsActive=true)