from rsa import (
    common,
    pkcs1,
    transform,
)


def mgf1(seed: bytes, length: int, hasher: str = "SHA-1") -> bytes:
    """
    MGF1 is a Mask Generation Function based on a hash function.

    A mask generation function takes an octet string of variable length and a
    desired output length as input, and outputs an octet string of the desired
    length. The plaintext-awareness of RSAES-OAEP relies on the random nature of
    the output of the mask generation function, which in turn relies on the
    random nature of the underlying hash.

    :param bytes seed: seed from which mask is generated, an octet string
    :param int length: intended length in octets of the mask, at most 2^32(hLen)
    :param str hasher: hash function (hLen denotes the length in octets of the hash
        function output)

    :return: mask, an octet string of length `length`
    :rtype: bytes

    :raise OverflowError: when `length` is too large for the specified `hasher`
    :raise ValueError: when specified `hasher` is invalid
    """

    try:
        hash_length = pkcs1.HASH_METHODS[hasher]().digest_size
    except KeyError as ex:
        raise ValueError(
            "Invalid `hasher` specified. Please select one of: {hash_list}".format(
                hash_list=", ".join(sorted(pkcs1.HASH_METHODS.keys()))
            )
        ) from ex

    # If l > 2^32(hLen), output "mask too long" and stop.
    if length > (2 ** 32 * hash_length):
        raise OverflowError(
            "Desired length should be at most 2**32 times the hasher's output "
            "length ({hash_length} for {hasher} function)".format(
                hash_length=hash_length,
                hasher=hasher,
            )
        )

    # Looping `counter` from 0 to ceil(l / hLen)-1, build `output` based on the
    # hashes formed by (`seed` + C), being `C` an octet string of length 4
    # generated by converting `counter` with the primitive I2OSP
    output = b"".join(
        pkcs1.compute_hash(
            seed + transform.int2bytes(counter, fill_size=4),
            method_name=hasher,
        )
        for counter in range(common.ceil_div(length, hash_length) + 1)
    )

    # Output the leading `length` octets of `output` as the octet string mask.
    return output[:length]


__all__ = [
    "mgf1",
]

if __name__ == "__main__":
    print("Running doctests 1000x or until failure")
    import doctest

    for count in range(1000):
        (failures, tests) = doctest.testmod()
        if failures:
            break

        if count % 100 == 0 and count:
            print("%i times" % count)

    print("Doctests done")
