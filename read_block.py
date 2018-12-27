
import struct,binascii,re

indexpath = '/Users/zhaoxiangfei/code/testnet/testnet_node/blockchain/database/block_num_to_block/index'
filepath = '/Users/zhaoxiangfei/code/testnet/testnet_node/blockchain/database/block_num_to_block/blocks'
callfun={}

class Unpackblock:

    def __init__(self,index_path,block_path):
        self.indexpath = index_path
        self.blockpath = block_path
        self.regop={}
        self.typefun={}
        self.typefun['uint8']  = self.__unpack_uint8
        self.typefun['uint16'] = self.__unpack_uint16
        self.typefun['uint32'] = self.__unpack_uint32
        self.typefun['uint64'] = self.__unpack_uint64
        self.typefun['uint']   = self.__unpack_uint
        self.typefun['string'] = self.__unpack_string
        self.typefun['bytes']  = self.__unpack_string
        self.typefun['asset_kinds'] =self.__unpack_asset_kinds

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
        return stream[0:index],index

    def __unpack_uint8(self,stream):
        return stream[0:1],1

    def __unpack_uint16(self,stream):
        return stream[0:2],2

    def __unpack_uint32(self,stream):
        return stream[0:4],4

    def __unpack_uint64(self,stream,):
        return stream[0:8],8

    # string、vector、bytes
    def __unpack_string(self,stream):
        str_size,str_size_offset = self.__unpack_uint_variant(stream)
        return stream[0:str_size_offset+str_size],str_size_offset+str_size

    def __unpack_sig(self,stream):
        return stream[0:65],65

    def __unpack_op_result(self,stream):
        number, str_offset = self.__unpack_uint_variant(stream)
        str_res,index = self.__unpack_uint(stream)
        stream =stream[index:]
        for i in range(0,number):
            op_res_code,index = self.__unpack_uint(stream)
            print('op_res_code:',op_res_code.hex())
            stream = stream[index:]
            billed_cpu_time_us,index = self.__unpack_uint32(stream)
            print('billed_cpu_time_us:',billed_cpu_time_us.hex())
            stream = stream[index:]
            ram_usage_bs,index = self.__unpack_uint32(stream)
            print('ram_usage_bs:',ram_usage_bs.hex())
            stream = stream[index:]
            fee_amount, index = self.__unpack_uint64(stream)
            print('fee_amount:', fee_amount.hex())
            stream = stream[index:]
            fee_id, index = self.__unpack_uint(stream)
            print('fee_id:', fee_id.hex())
            stream =stream[index:]

    def __unpack_asset_kinds(self,stream):
        str_num, str_size_offset = self.__unpack_uint_variant(stream)
        str_asset,index = self.__unpack_uint(stream)
        asset_kinds = str_asset          #资产种类数目
        stream = stream[index:]
        for i in range(0,str_num):
            amount,index = self.__unpack_uint64(stream)
            stream = stream[index:]
            id,index = self.__unpack_uint(stream)
            stream = stream[index:]
            asset_kinds =asset_kinds +amount +id
        return asset_kinds,index

    def __unpack_sig_struct(self,stream):
        str_num, str_size_offset = self.__unpack_uint_variant(stream)
        str_sig,index = self.__unpack_uint(stream)
        signatures = str_sig
        stream = stream[index:]
        for i in range(0,str_num):
            sig,index = self.__unpack_sig(stream)
            stream = stream[index:]
            signatures =signatures +sig
        return signatures,stream

    def reg_op_struct(self,op_code,op_struct):
        self.regop[op_code] = op_struct

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

    def __unpackopdata(self,stream,op_code):
        if op_code in self.regop:
            for pair in self.regop[op_code]:
                (key, value), = pair.items()
                if key in self.typefun:
                    curr_buff,index = self.typefun[key](stream)
                    print(value,':',curr_buff.hex())
                    stream = stream[index:]
                else :
                    print('not found ',key,' type')
                    break
            return stream
        else :
            print('op not found , please reg op')
    def __unpackenderdata(self,stream):
        ext,index = self.__unpack_uint8(stream)
        print('tr_extensions:',ext.hex())  #由于该字段多数区块均为0，所以未处理复杂情况，仅当做单字节处理
        stream = stream[index:]
        signatures,stream = self.__unpack_sig_struct(stream)
        print('signatures(number+sigs):',signatures.hex())
        #stream = stream[index:]
        self.__unpack_op_result(stream)

    def __unpackblockdata(self,offset,size):
        with open(filepath, 'rb') as file:
            file.seek(offset, 0)
            lines = file.read(size)
            hex_lines = binascii.b2a_hex(lines)
            # result = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", str(hex_lines)[2:-1])
            print("block raw data:", hex_lines[0:-1])

            # block_header
            header = lines[0:46]
            fmt_block_header = '20sIB20sB'
            previous, timestamp, witness, transaction_merkle_root, extensions = struct.unpack(fmt_block_header, header)
            print("\n-------------block header-----------\n")
            print('previous:', previous.hex())
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
                for number in range(0, transaction_numbers[0]):
                    print('\n-------------transaction', number + 1, '-----------\n')
                    tpos_ref = lines[index:index + 11]
                    fmt_tpos_ref = '=HIIB'
                    ref_block_num, ref_block_prefix, expiration, operation_nums = struct.unpack(fmt_tpos_ref, tpos_ref);
                    print('\n-------------transaction header-----------\n')
                    print('ref_block_num:', hex(ref_block_num)[2:].zfill(4))
                    print('ref_block_prefix:', hex(ref_block_prefix)[2:].zfill(8))
                    print('expiration:', hex(expiration)[2:].zfill(8))
                    print('operation_nums:', hex(operation_nums)[2:].zfill(2))
                    for op_num in range(0,operation_nums):
                        print('\n-------------opreation-----------\n')
                        stream = self.__unpackopdata(lines[index+11:],lines[index+11])
                    print('\n-------------transaction ender-----------\n')
                    self.__unpackenderdata(stream)

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
    # todo
    # ........

    # unpack指定区块
    obj.unpackblockbynum(9974382)
