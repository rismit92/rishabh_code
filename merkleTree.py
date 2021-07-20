import hashlib
import binascii


def generate_hash(left_node, right_node):
    rev_left_node = binascii.unhexlify(left_node)[::-1]
    rev_right_node = binascii.unhexlify(right_node)[::-1]
    parent_node = rev_left_node + rev_right_node
    parent_hash = hashlib.sha256(hashlib.sha256(parent_node).digest()).digest()
    return binascii.hexlify(parent_hash[::-1])


def get_merkle_root(transaction_hash):
    temp_block = transaction_hash
    while len(temp_block) != 1:
        temp = list()
        for idx in range(0, len(temp_block), 2):
            left_node = temp_block[idx]
            if idx+1 < len(temp_block):
                right_node = temp_block[idx+1]
            else:
                right_node = temp_block[idx]
            temp.append(generate_hash(left_node,right_node))
        temp_block = temp
    merkle_root = temp_block[0]
    return merkle_root


if __name__ == '__main__':
    block = ["d440c2e3e0a708ce82c1b8e01155f9f350b41b97020d754a77bc0621730ac2e5",
              "9842893448d6f7534f5f82737094804c4fe9ec551de0fc6844d945f4736db3e8",
              "fdacd62551099230552d776d1d92cff1a928172ea6e4970c976be939287e86ec",
              "af762cf30b5a536601f5159852de776d73942bf48e1d5adaf91937b3d8f773f3",
              "a4d26e4e35f0c821c9e71286fdcf4566f3bfc77dcd092684ab21ef34becb78f9",
              "828f1be2e3896a62c7a1ae1b5033a6f8540002d3b06b889181ec0e35612b3315",
              "0456df2b357f041d414211f10ed3e5b8dbf29141bd9de9c9594b97f843c9ae6c",
              "ca3789839b6e838343b089c6d206ccbfd5b1caa611453297b130cfb835e2dccb",
              "9255a032a8b52f4ab23a349344a601f016b8997a3b8a533c8a64779f66b759ac"]
    root = get_merkle_root(block)
    print(root)







