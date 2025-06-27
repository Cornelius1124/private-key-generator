from ecdsa import SECP256k1, SigningKey

sk = SigningKey.generate(curve=SECP256k1)
vk = sk.verifying_key

private_key_bytes = sk.to_string()
private_key_int = int.from_bytes(private_key_bytes, byteorder='big')

public_key_bytes = vk.to_string()
public_key_hex = public_key_bytes.hex()

print("Private Key (hex):", private_key_bytes.hex())
print("Private Key (int):", private_key_int)
print("Public Key (uncompressed):", public_key_hex)

# Keeps the window open for goddamn manual way but optional only
input("\nPress Enter to exit...")
