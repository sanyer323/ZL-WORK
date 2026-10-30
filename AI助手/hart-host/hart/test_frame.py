from hart.frame import build_master_frame, parse_response, wrap_preamble, xor_checksum


def test_roundtrip_short():
    raw = wrap_preamble(build_master_frame(0, b""), 5)
    assert raw[:5] == b"\xff" * 5
    parsed = parse_response(raw)
    assert parsed.command == 0
    body = raw[5:-1]
    assert xor_checksum(body) == raw[-1]


if __name__ == "__main__":
    test_roundtrip_short()
    print("ok")
