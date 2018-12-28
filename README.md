# gxc_unpack_block

解析gxchain区块数据

### 运行环境:python 3.7

可以解析调用合约操作，其他操作待添加

### 调用合约operation 75

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

### 转账operation 0

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
memo : 0103ea4682e184b0cf5fe0232f48cb2c151c6a16e416760abbcb66afcad8c445e7b202f01f619e03b84bb81db3461474e5a7a32166d4f7b131394442f371f8a2c09020c48a5591f26701001040ca24cd4fdd0fc1314115442ffce41f
op_extensions : 00

-------------transaction ender-----------

tr_extensions: 00
signatures(number+sigs): 01204928c6b5bd473fa443ffc25c69b19b2d3e478bfa91f377c13595b92349423d0d24ed0017868a2119d6b14463dc142b9aa034b3d175850d3b78a23380eaff3a79
op_res_number: 01
```
### 创建账户解析示例：operation 5
```
-------------block index-----------

block index data: 2d bf 3c 43 00 00 00 00 5f 01 00 00 00 96 2b e0 be 47 be be 4e 3b 11 14 e1 6f 0a 70 99 55 eb 14
pos: 00000000433cbf2d
size: 0000015f
id: 00962be0be47bebe4e3b1114e16f0a709955eb14 



-------------block header-----------

block raw data: b'00962bdff6226c046984db0f5205c90d70c95f01b2981c5c260de9f4e5a6b0c2643441549da4cf11b1683cabc0001f05b54ea6bb69e04b9cd99b670ccc641c8b373017b0ca506a3628ed52409418313c2e2e972d13e8317f4fa64adb9dd3f1ef9d5f2135291070de2f799a5fb5425601df2bf6226c04cd981c5c0105660000000000000001fb01fb010000097a68616f2d31323132010000000001034f12dcf134d5f63bef5accb42950ff11d47d0cf2b8e2e58abe5d7fe29cca6a2601000001000000000102f01f619e03b84bb81db3461474e5a7a32166d4f7b131394442f371f8a2c0902001000002f01f619e03b84bb81db3461474e5a7a32166d4f7b131394442f371f8a2c09020050000000000000000012027dafdf11e9ef516d1a52877617788102c4ad2d2cd2f3b3aaa5ba6e36ff7c52960dfb095f13394647b095a9bbd30da251afad7edfe68824ae396f09860333bbe0101c904000000000201'

previous: 00962bdff6226c046984db0f5205c90d70c95f01
timestamp: 5c1c98b2
witness: 26
transaction_merkle_root: 0de9f4e5a6b0c2643441549da4cf11b1683cabc0
extensions 00
witness_signature: 1f05b54ea6bb69e04b9cd99b670ccc641c8b373017b0ca506a3628ed52409418313c2e2e972d13e8317f4fa64adb9dd3f1ef9d5f2135291070de2f799a5fb54256
transaction_numbers 01

-------------transaction 1 -----------


-------------transaction header-----------

ref_block_num: 2bdf
ref_block_prefix: 046c22f6
expiration: 5c1c98cd
operation_nums: 01

-------------opreation-----------

op_code : 05
fee_amount : 6600000000000000
fee_id : 01
registrar : fb01
referrer : fb01
referrer_percent : 0000
name : 097a68616f2d31323132
weight_threshold: 01000000

**** size: 00
account_auths: 00

**** size: 01
**** public_key_type : 034f12dcf134d5f63bef5accb42950ff11d47d0cf2b8e2e58abe5d7fe29cca6a26
**** weight_type : 0100
key_auths: 01034f12dcf134d5f63bef5accb42950ff11d47d0cf2b8e2e58abe5d7fe29cca6a260100

**** size: 00
address_auths: 00
owner : 010000000001034f12dcf134d5f63bef5accb42950ff11d47d0cf2b8e2e58abe5d7fe29cca6a26010000
weight_threshold: 01000000

**** size: 00
account_auths: 00

**** size: 01
**** public_key_type : 02f01f619e03b84bb81db3461474e5a7a32166d4f7b131394442f371f8a2c09020
**** weight_type : 0100
key_auths: 0102f01f619e03b84bb81db3461474e5a7a32166d4f7b131394442f371f8a2c090200100

**** size: 00
address_auths: 00
active : 01000000000102f01f619e03b84bb81db3461474e5a7a32166d4f7b131394442f371f8a2c09020010000
memo_key: 02f01f619e03b84bb81db3461474e5a7a32166d4f7b131394442f371f8a2c09020
voting_account: 05
num_witness: 0000
num_committee: 0000

**** size: 00
votes: 00
extensions: 00
options : 02f01f619e03b84bb81db3461474e5a7a32166d4f7b131394442f371f8a2c0902005000000000000
op_extensions : 00

-------------transaction ender-----------

tr_extensions: 00

**** size: 01
**** signtures : 2027dafdf11e9ef516d1a52877617788102c4ad2d2cd2f3b3aaa5ba6e36ff7c52960dfb095f13394647b095a9bbd30da251afad7edfe68824ae396f09860333bbe
signatures(number+sigs): 012027dafdf11e9ef516d1a52877617788102c4ad2d2cd2f3b3aaa5ba6e36ff7c52960dfb095f13394647b095a9bbd30da251afad7edfe68824ae396f09860333bbe
op_res_number: 01
op_res_code: 01
c904
```
### 更新账户operation 6
```
-------------block index-----------

block index data: 08 6e c5 44 00 00 00 00 f8 00 00 00 00 98 f2 d5 3a ce 52 81 a9 80 c7 fd 83 28 27 9e dd 90 5d 04
pos: 0000000044c56e08
size: 000000f8
id: 0098f2d53ace5281a980c7fd8328279edd905d04 



-------------block header-----------

block raw data: b'0098f2d4a495ebdac0f1aa8c386271185e9853515e1f265c16cbc8f590638de0dffc8e9fc86bcda289242ea653001f03cefa6b1038f6f36a53e0fcbdb9461983bb4f26423377540b36c19208e02bba1a5980479061d015c534f15111668a2bb748d4d0771e0dc1a448630b126e24f701d3f2085cab5c761f265c0106690000000000000001aa0300000103ea4682e184b0cf5fe0232f48cb2c151c6a16e416760abbcb66afcad8c445e7b2050000000000000000011c0216214148abf6592e71e171e7fcb2b6ae3a0a8b79da96d9eb9908390222d9624c0ad3a5afa099a7dffd56c100e81d4383172ad0ad7fe4e5c2d42071d9acc0680100'

previous: 0098f2d4a495ebdac0f1aa8c386271185e985351
timestamp: 5c261f5e
witness: 16
transaction_merkle_root: cbc8f590638de0dffc8e9fc86bcda289242ea653
extensions 00
witness_signature: 1f03cefa6b1038f6f36a53e0fcbdb9461983bb4f26423377540b36c19208e02bba1a5980479061d015c534f15111668a2bb748d4d0771e0dc1a448630b126e24f7
transaction_numbers 01

-------------transaction 1 -----------


-------------transaction header-----------

ref_block_num: f2d3
ref_block_prefix: 5cab5c08
expiration: 5c261f76
operation_nums: 01

-------------opreation-----------

op_code : 06
fee_amount : 6900000000000000
fee_id : 01
account : aa03
authority_exist: 00
owner : 00
authority_exist: 00
active : 00
option_exist: 01
memo_key: 03ea4682e184b0cf5fe0232f48cb2c151c6a16e416760abbcb66afcad8c445e7b2
voting_account: 05
num_witness: 0000
num_committee: 0000

**** size: 00
votes: 00
extensions: 00
options : 0103ea4682e184b0cf5fe0232f48cb2c151c6a16e416760abbcb66afcad8c445e7b205000000000000
op_extensions : 00

-------------transaction ender-----------

tr_extensions: 00

**** size: 01
**** signtures : 1c0216214148abf6592e71e171e7fcb2b6ae3a0a8b79da96d9eb9908390222d9624c0ad3a5afa099a7dffd56c100e81d4383172ad0ad7fe4e5c2d42071d9acc068
signatures(number+sigs): 011c0216214148abf6592e71e171e7fcb2b6ae3a0a8b79da96d9eb9908390222d9624c0ad3a5afa099a7dffd56c100e81d4383172ad0ad7fe4e5c2d42071d9acc068
op_res_number: 01
op_res_code: 00
```
