--股票基本信息
create table ts_stock_basic_info(
ts_code varchar(10),
exchange
symbol varchar(7),
name varchar(30),
fullname varchar(30),
market varchar(10)
area varchar(20),
industry varchar(30),
is_hs varchar(1),
list_date datetime
);

-- 交易日信息
create table ts_trade_cal(
exchange varchar(4),
cal_date varchar(8),
is_open varchar(2)
);