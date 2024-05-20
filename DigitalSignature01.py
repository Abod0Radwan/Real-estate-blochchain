from sympy import mod_inverse

# Given RSA parameters for Alice and Bob
nA = 171024704183616109700818066925197841516671277
nB = 839073542734369359260871355939062622747633109
eA = 1571
eB = 87697
pB = 98763457697834568934613
qB = 8495789457893457345793

# Given encrypted signature pair received by Bob
m1 = 418726553997094258577980055061305150940547956
s1 = 749142649641548101520133634736865752883277237

phi_nB = (pB - 1) * (qB - 1)
d = mod_inverse(eB, phi_nB)
m_decrypted = pow(m1, d, nB)

# Verify if the decrypted signature matches the message using Alice's public key
is_valid_signature = pow(s1, eA, nA) == m1

if is_valid_signature:
    print("The signature is valid.")
    print("The message is:", m_decrypted)
    print("The message came from Alice.")
else:
    print("The signature is not valid.")
