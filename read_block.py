
import struct,binascii,re

indexpath = '/Users/zhaoxiangfei/code/testnet/testnet_node/blockchain/database/block_num_to_block/index'
filepath = '/Users/zhaoxiangfei/code/testnet/testnet_node/blockchain/database/block_num_to_block/blocks'


data = "fef0babe"
bits = ""
for x in range(0, len(data), 2):
    bits += chr(int(data[x:x+2], 16))

class Unpackblock:

    def __init__(self,index_path,block_path):
        self.indexpath = index_path
        self.blockpath = block_path
        self.regop={}
        self.typefun={}
        self.resultfun={}
        self.typefun['uint8']  = self.__unpack_uint8
        self.typefun['uint16'] = self.__unpack_uint16
        self.typefun['uint32'] = self.__unpack_uint32
        self.typefun['uint64'] = self.__unpack_uint64
        self.typefun['uint']   = self.__unpack_uint
        self.typefun['string'] = self.__unpack_string
        self.typefun['bytes']  = self.__unpack_string
        self.typefun['asset_kinds'] =self.__unpack_asset_kinds
        self.typefun['memo']  = self.__unpack_memo_struct
        self.typefun['sig'] = self.__unpack_sig
        self.typefun['pk'] = self.__unpack_public_key
        self.typefun['ripe160'] =self.__unpack_byte20
        self.typefun['authority'] = self.__unpack_authority_struct
        self.typefun['account_options'] = self.__unpack_account_options
        self.typefun['op_authority'] = self.__unpack_op_authority_struct
        self.typefun['op_account_options'] = self.__unpack_op_account_options

        self.resultfun['01']=self.__unpack_op_result_01
        self.resultfun['03'] = self.__unpack_op_result_03

    def __unpack_uint_variant(self,stream):
        by ,v,index = 0 , 0, 0
        while True:
            b = stream[index]
            if by >= 64 or (by == 63 and b > 1):
                break
            v |= (b & 0x7f) << by;
            by += 7
            if stream[index] & 0x80 == 0:
                break
            index += 1
        return v, index + 1

    def __unpack_uint(self,stream):
        value,index = self.__unpack_uint_variant(stream)
        return stream[0:index],stream[index:]

    def __unpack_uint8(self,stream):
        return stream[0:1],stream[1:]

    def __unpack_uint16(self,stream):
        return stream[0:2],stream[2:]

    def __unpack_uint32(self,stream):
        return stream[0:4],stream[4:]

    def __unpack_uint64(self,stream):
        return stream[0:8],stream[8:]

    def __unpack_byte20(self,stream):
        return  stream[0:20],stream[20:]

    # string、vector、bytes
    def __unpack_string(self,stream):
        str_size,str_size_offset = self.__unpack_uint_variant(stream)
        return stream[0:str_size_offset+str_size],stream[str_size_offset+str_size:]

    def __unpack_sig(self,stream):
        return stream[0:65],stream[65:]

    def __unpack_public_key(self,stream):
        return stream[0:33],stream[33:]

    def __unpack_asset_kinds(self,stream):
        msg, stream = self.__unpack_struct_array(stream,
                                                 {'amount': 'uint64', 'id': 'uint'})
        return msg,stream

    def __unpack_memo_struct(self,stream):
        msg,stream =self.__unpack_struct_array(stream,{'memo_from_key':'pk','memo_to_key':'pk','memo_nonce':'uint64','memo_msg(number+buffer':'string'})
        return msg, stream

    def __unpack_authority_struct(self,stream):
        weight_threshold ,stream= self.__unpack_uint32(stream)
        print('weight_threshold:',weight_threshold.hex())
        account_auths,stream =self.__unpack_struct_array(stream,{'account_id_type':'uint','weight_type':'uint16'})
        print('account_auths:',account_auths.hex())
        key_auths, stream = self.__unpack_struct_array(stream, {'public_key_type': 'pk', 'weight_type': 'uint16'})
        print('key_auths:', key_auths.hex())
        address_auths, stream = self.__unpack_struct_array(stream, {'address': 'ripe160', 'weight_type': 'uint16'})
        print('address_auths:', address_auths.hex())
        return weight_threshold+account_auths+key_auths+account_auths,stream

    def __unpack_op_authority_struct(self,stream):
        msg,stream = self.__unpack_uint8(stream)
        if msg[0] == 0:
            print('authority_exist:',hex(msg[0])[2:].zfill(2))
            return msg,stream
        else:
            print('authority_exist:', hex(msg[0])[2:].zfill(2))
            msg2,stream = self.__unpack_authority_struct(stream)
            return msg+msg2,stream

    def __unpack_account_options(self,stream):
        memo_key,stream =self.__unpack_public_key(stream)
        print('memo_key:',memo_key.hex())
        voting_account,stream =self.__unpack_uint(stream)
        print('voting_account:',voting_account.hex())
        num_witness,stream =self.__unpack_uint16(stream)
        print('num_witness:',num_witness.hex())
        num_committee,stream =self.__unpack_uint16(stream)
        print('num_committee:',num_committee.hex())
        votes,stream =self.__unpack_struct_array(stream,{'vote_id':'uint32'})
        print('votes:',votes.hex())
        extensions,stream = self.__unpack_uint(stream)
        print('extensions:',extensions.hex())
        return memo_key+voting_account+num_witness+num_committee+votes+extensions,stream

    def __unpack_op_account_options(self,stream):
        msg,stream = self.__unpack_uint8(stream)
        if msg[0] == 0:
            print('option_exist:',hex(msg[0])[2:].zfill(2))
            return msg,stream
        else:
            print('option_exist:', hex(msg[0])[2:].zfill(2))
            msg2,stream = self.__unpack_account_options(stream)
            return msg+msg2,stream

    def __unpack_struct_array(self,stream,type_mode):
        num, offset = self.__unpack_uint_variant(stream)
        str_msg, stream = self.__unpack_uint(stream)
        msgs = str_msg
        print('\n**** size:',str_msg.hex())
        for i in range(0,num):
            for key,value in type_mode.items():
                msg,stream = self.typefun[value](stream)
                print('****',key,':',msg.hex())
                msgs = msgs +msg
        return msgs,stream

    def __unpack_op_result_01(self,stream):
        msg,stream = self.__unpack_uint(stream)
        print(msg.hex())
        return msg,stream

    def __unpack_op_result_03(self,stream):
        billed_cpu_time_us, stream = self.__unpack_uint32(stream)
        print('billed_cpu_time_us:', billed_cpu_time_us.hex())
        ram_usage_bs, stream = self.__unpack_uint32(stream)
        print('ram_usage_bs:', ram_usage_bs.hex())
        fee_amount, stream = self.__unpack_uint64(stream)
        print('fee_amount:', fee_amount.hex())
        fee_id, stream = self.__unpack_uint(stream)
        print('fee_id:', fee_id.hex())
        return billed_cpu_time_us+ram_usage_bs+fee_amount+fee_id,stream

    def __unpack_op_result(self,stream):
        number, str_offset = self.__unpack_uint_variant(stream)
        str_res,stream = self.__unpack_uint(stream)
        print('op_res_number:',str_res.hex())
        for i in range(0,number):
            op_res_code,stream = self.__unpack_uint(stream)
            print('op_res_code:',op_res_code.hex())
            if op_res_code[0] == 0:
                break
            else:
                self.resultfun[op_res_code.hex()](stream)
        return stream

    def __unpackopdata(self,stream,op_code):
        if op_code in self.regop:
            for pair in self.regop[op_code]:
                (key, value), = pair.items()
                if key in self.typefun:
                    curr_buff,stream = self.typefun[key](stream)
                    print(value,':',curr_buff.hex())
                else :
                    print('not found ',key,' type')
                    break
            return stream
        else :
            print('op not found , please reg op')

    def __unpackenderdata(self,stream):
        ext,stream = self.__unpack_uint8(stream)
        print('tr_extensions:',ext.hex())  #由于该字段多数区块均为0，所以未处理复杂情况，仅当做单字节处理
        signatures, stream = self.__unpack_struct_array(stream,{'signtures':'sig'})
        print('signatures(number+sigs):',signatures.hex())
        stream = self.__unpack_op_result(stream)
        return stream

    def unpackblockbynum(self,blocknumber):
        offset = blocknumber * 0x20
        with open(indexpath, 'rb') as indexifle:
            indexifle.seek(offset, 0)
            lines = indexifle.read(0x20)
            hex_lines = binascii.b2a_hex(lines)
            result = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", str(hex_lines)[2:-1])

            print("\n-------------block index-----------\n")
            print("block index data:", result)
            fmt = 'QI20s'
            offs, size, id = struct.unpack(fmt, lines)
            print('pos:', hex(offs)[2:].zfill(16))
            print('size:', hex(size)[2:].zfill(8))
            print('id:', id.hex(), "\n\n")
            self.__unpackblockdata(offs, size)

    def reg_op_struct(self,op_code,op_struct):
        self.regop[op_code] = op_struct

    def __unpackblockdata(self,offset,size):
        with open(filepath, 'rb') as file:
            file.seek(offset, 0)
            lines = file.read(size)
            hex_lines = binascii.b2a_hex(lines)
            print("\n-------------block header-----------\n")
            print("block raw data:", hex_lines)

            # block_header
            header = lines[0:46]
            fmt_block_header = '20sIB20sB'
            previous, timestamp, witness, transaction_merkle_root, extensions = struct.unpack(fmt_block_header, header)
            print('\nprevious:', previous.hex())
            print('timestamp:', hex(timestamp)[2:].zfill(8))
            print('witness:', hex(witness)[2:].zfill(2))
            print('transaction_merkle_root:', transaction_merkle_root.hex())
            print('extensions', hex(extensions)[2:].zfill(2))

            # signed_block_header
            sign_block_header = lines[46:111]
            fmt_sign_block_header = '65s'
            witness_signature = struct.unpack(fmt_sign_block_header, sign_block_header)
            print('witness_signature:', witness_signature[0].hex())

            # signed_block
            transaction_numbers = lines[111:112]
            print('transaction_numbers', hex(transaction_numbers[0])[2:].zfill(2))
            if lines[111] != 0x0:
                index = 112;
                stream = lines[112:]
                for number in range(0, transaction_numbers[0]):
                    print('\n-------------transaction', number + 1, '-----------\n')
                    fmt_tpos_ref = '=HIIB'
                    temp_stream =stream[0:11]
                    ref_block_num, ref_block_prefix, expiration, operation_nums = struct.unpack(fmt_tpos_ref, temp_stream);
                    stream = stream[11:]
                    print('\n-------------transaction header-----------\n')
                    print('ref_block_num:', hex(ref_block_num)[2:].zfill(4))
                    print('ref_block_prefix:', hex(ref_block_prefix)[2:].zfill(8))
                    print('expiration:', hex(expiration)[2:].zfill(8))
                    print('operation_nums:', hex(operation_nums)[2:].zfill(2))
                    for op_num in range(0,operation_nums):
                        print('\n-------------opreation-----------\n')
                        stream = self.__unpackopdata(stream,stream[0])
                    print('\n-------------transaction ender-----------\n')
                    stream = self.__unpackenderdata(stream)

    def test(self):
        buffer=b'\x04\x09\x87\x96\x64\x00\x87\x33\x09'
        result0, idx0 =self.__unpack_uint(buffer,0)
        print(result0.hex(), hex(buffer[idx0]))
        result1, idx1 =self.__unpack_uint8(buffer,0)
        print(result1.hex(), hex(buffer[idx1]))
        result2, idx2 = self.__unpack_uint16(buffer, 0)
        print(result2.hex(), hex(buffer[idx2]))
        result3, idx3 = self.__unpack_uint32(buffer, 0)
        print(result3.hex(), hex(buffer[idx3]))
        result3, idx3 = self.__unpack_uint32(buffer, 0)
        print(result3.hex(), hex(buffer[idx3]))
        result4, idx4 = self.__unpack_uint64(buffer, 0)
        print(result4.hex(), hex(buffer[idx4]))
        result5, idx5 = self.__unpack_string(buffer, 0)
        print(result5.hex(), hex(buffer[idx5]))

if __name__ == '__main__':

    obj = Unpackblock(indexpath,filepath)

    # 解析调用合约操作
    callcontract_dic = ({"uint8" :'op_code'},{"uint64":'fee_amount'},{"uint" :'fee_id'},{"uint" :'account'},{'uint':'contract_id'},{'asset_kinds':'asset_num'},{'uint64':'method_name'},{'string':'data(size+buffer)'},{'uint8':'op_extensions'})
    obj.reg_op_struct(75,callcontract_dic)

    # 解析部署合约操作
    # todo

    # 解析转账操作
    transfer_dic = ({"uint8":'op_code'},{"uint64":"fee_amount"},{"uint" :'fee_id'},{"uint" :'from'},{'uint':'to'},{"uint64":"amount_amount"},{"uint" :'amount_id'},{"memo":"memo"},{'uint8':'op_extensions'})
    obj.reg_op_struct(0,transfer_dic)

    # 解析创建账户操作
    createaccount_dic =({"uint8":'op_code'},{"uint64":"fee_amount"},{"uint" :'fee_id'},{"uint" :'registrar'},{'uint':'referrer'},{'uint16':'referrer_percent'},{'string':'name'},{'authority':'owner'},{'authority':'active'},{'account_options':'options'},{'uint':'op_extensions'})
    obj.reg_op_struct(5,createaccount_dic)

    # 更新账户操作
    updateacc_dic = (
    {"uint8": 'op_code'}, {"uint64": "fee_amount"}, {"uint": 'fee_id'}, {"uint": 'account'},{'op_authority':'owner'},{'op_authority':'active'},{'op_account_options': 'options'}, {'uint': 'op_extensions'})
    obj.reg_op_struct(6,updateacc_dic)

    # unpack指定区块
    #obj.unpackblockbynum(9841632)
    obj.unpackblockbynum(10023637)
