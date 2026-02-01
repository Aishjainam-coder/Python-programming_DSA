# Write your MySQL query statement below
select max(num)  AS num from myNumbers 
where num in (
    select num  from myNumbers 
    group by num having count(*) =1
)