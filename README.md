# gxc_unpack_block

解析gxchain区块数据

### 运行环境:python 3.7

可以解析调用合约操作，其他操作待添加

示例：测试网1001177块

```
-------------block index-----------

block index data: 3e c6 7e 44 00 00 00 00 fa 00 00 00 00 98 9b 19 d6 e3 85 ad 01 81 70 1a 04 e7 5b 5a 73 99 6f 17
pos: 00000000447ec63e
size: 000000fa
id: 00989b19d6e385ad0181701a04e75b5a73996f17 


block raw data: b'00989b18c689f533c14e0ed82db5662dda88cb9958e1245c1a8d567dfaee449d2f6a45c93d8dced74552e56d3f002070744aff983b6a389f0a26cdf8d7467dd5fdcd60b6252e446c18fb83e7f6f5426826e86811a646a16443671e26493ce47ea3cfef5ba1d8a81d75934d5266c40301189bc689f53367e1245c014b640000000000000001aa03860a00000000000000806b100f68656c6c6f68656c6c6f68656c6c6f0000011f3f6baeac5034a2c46148c13b160f022deec65515d03910be564b8a23d8169a415e4932949efed477c0632e0c7ab26070583107a4578208410466488d626c49d701037f0000000000000064000000000000000'

-------------block header-----------

previous: 00989b18c689f533c14e0ed82db5662dda88cb99
timestamp: 5c24e158
witness: 1a
transaction_merkle_root: 8d567dfaee449d2f6a45c93d8dced74552e56d3f
extensions 00
witness_signature: 2070744aff983b6a389f0a26cdf8d7467dd5fdcd60b6252e446c18fb83e7f6f5426826e86811a646a16443671e26493ce47ea3cfef5ba1d8a81d75934d5266c403
transaction_numbers 01

-------------transaction 1 -----------


-------------transaction header-----------

ref_block_num: 9b18
ref_block_prefix: 33f589c6
expiration: 5c24e167
operation_nums: 01

-------------opreation-----------

op_code : 4b
fee_amount : 6400000000000000
fee_id : 01
account : aa03
contract_id : 860a
asset_num : 00
method_name : 000000000000806b
data(size+buffer) : 100f68656c6c6f68656c6c6f68656c6c6f
op_extensions : 00

-------------transaction ender-----------

tr_extensions: 00
signatures(number+sigs): 011f3f6baeac5034a2c46148c13b160f022deec65515d03910be564b8a23d8169a415e4932949efed477c0632e0c7ab26070583107a4578208410466488d626c49d7
op_res_number: 01
op_res_code: 03
billed_cpu_time_us: 7f000000
ram_usage_bs: 00000000
fee_amount: 6400000000000000
fee_id: 01
```
