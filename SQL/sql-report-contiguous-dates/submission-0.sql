-- Write your query below
with combined as (
    select fail_date as dt, 'failed' as state from failed where fail_date between '2019-01-01' and '2019-12-31'
    union all
    select success_date as dt, 'succeeded' as state from succeeded where success_date between '2019-01-01' and '2019-12-31'
    order by dt asc
),
ranked as(
select state, dt, 
ROW_NUMBER() OVER (order by dt) as rn,
ROW_NUMBER() OVER (PARTITION BY state order by dt asc) as state_rn FROM combined),
grouped as(
    select state, dt, rn - state_rn as grp from ranked
)
select state as period_state, min(dt) as start_date, max(dt) as end_date FROM
grouped group by state, grp order by start_date asc