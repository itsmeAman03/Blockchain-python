from backend.util.hex_to_binary import hex_to_binary

def test_hex_to_binary():
    original=993
    hex_no=hex(original)[2:]
    binary_no=hex_to_binary(hex_no)

    assert int(binary_no,2)==original