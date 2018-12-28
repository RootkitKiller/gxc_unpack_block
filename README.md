# gxc_unpack_block

解析gxchain区块数据

### 运行环境:python 3.7

可以解析调用合约操作，其他操作待添加

示例：测试网10001177区块(调用合约operation)

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

测试网10012266区块，转账操作，包含memo

```
-------------block index-----------

block index data: 54 df 92 44 00 00 00 00 34 01 00 00 00 98 c6 6a d2 f4 b3 e1 5b e3 4a d8 6f a5 9f c7 4d d8 ca 16
pos: 000000004492df54
size: 00000134
id: 0098c66ad2f4b3e15be34ad86fa59fc74dd8ca16 


block raw data: b'0098c6699f6e528fab47de618a9104cf853299437a85255c148df8d7f03cae0763e86367b40a8a144271b2fbc900204be6dc1b72615c7a96290af6e56f7bcef0074fef562e0a248abceec1c84a945124c52f36950d3056932b060417b3039eaeff55c710c9235b397d99677979357c0169c69f6e528f8885255c01009b0400000000000001aa03c909a086010000000000010103ea4682e184b0cf5fe0232f48cb2c151c6a16e416760abbcb66afcad8c445e7b202f01f619e03b84bb81db3461474e5a7a32166d4f7b131394442f371f8a2c09020c48a5591f26701001040ca24cd4fdd0fc1314115442ffce41f000001204928c6b5bd473fa443ffc25c69b19b2d3e478bfa91f377c13595b92349423d0d24ed0017868a2119d6b14463dc142b9aa034b3d175850d3b78a23380eaff3a79010'

-------------block header-----------

previous: 0098c6699f6e528fab47de618a9104cf85329943
timestamp: 5c25857a
witness: 14
transaction_merkle_root: 8df8d7f03cae0763e86367b40a8a144271b2fbc9
extensions 00
witness_signature: 204be6dc1b72615c7a96290af6e56f7bcef0074fef562e0a248abceec1c84a945124c52f36950d3056932b060417b3039eaeff55c710c9235b397d99677979357c
transaction_numbers 01

-------------transaction 1 -----------


-------------transaction header-----------

ref_block_num: c669
ref_block_prefix: 8f526e9f
expiration: 5c258588
operation_nums: 01

-------------opreation-----------

op_code : 00
fee_amount : 9b04000000000000
fee_id : 01
from : aa03
to : c909
amount_amount : a086010000000000
amount_id : 01

----memo_number: 01
----memo_from_key: 03ea4682e184b0cf5fe0232f48cb2c151c6a16e416760abbcb66afcad8c445e7b2
----memo_to_key: 02f01f619e03b84bb81db3461474e5a7a32166d4f7b131394442f371f8a2c09020
----memo_nonce: c48a5591f2670100
----memo_msg(number+buffer): 1040ca24cd4fdd0fc1314115442ffce41f
memo_num : 0103ea4682e184b0cf5fe0232f48cb2c151c6a16e416760abbcb66afcad8c445e7b202f01f619e03b84bb81db3461474e5a7a32166d4f7b131394442f371f8a2c09020c48a5591f26701001040ca24cd4fdd0fc1314115442ffce41f
op_extensions : 00

-------------transaction ender-----------

tr_extensions: 00
signatures(number+sigs): 01204928c6b5bd473fa443ffc25c69b19b2d3e478bfa91f377c13595b92349423d0d24ed0017868a2119d6b14463dc142b9aa034b3d175850d3b78a23380eaff3a79
op_res_number: 01
```
