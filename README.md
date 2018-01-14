根据ZB.com上的交易记录，计算一定时间内的账户盈亏。

使用方法：
1. 安装requests 的库（Python3）
2. 在代码文件中，根据自己需要修改transaction_file，coin_type，currency_type
   这3个参数。transaction_file指的是存放交易数据的文件，coin_type指的是虚拟货
   币类型，比如hsr，btc等。currency_type指的是法币类型，比如qc或者usdt
3. 打开 [https://trans.zb.com/record](https://trans.zb.com/record) ，
   选择你所要计算的货币类型，选择委托时间，交易状态改为已完成，点击搜索，获取交
   易记录
4. 复制搜索出来的内容，到transaction_file指定的目录
5. 运行程序，得到结果

结果说明：
1. final coin：当前交易记录中，虚拟货币的余额，表示在这些交易中你购买/出售了多少
   虚拟货币
2. final money：当前交易记录中，法币的余额，表示你在这些交易中你总共得到/支付了
   多少法币
3. Next buy：当前交易的成本。若希望扩大盈利，下次购买的价格应当低于这个成本，出售
   价格应当高于这个成本
4. The last price：你所选择的货币的最新成交价格
5. Actual Benefit：按照当前成交价格，若虚拟货币余额恢复到0，你的账户盈利水平
