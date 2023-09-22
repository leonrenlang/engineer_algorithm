# 正常的交换整数
# int c = a;
# a = b;
# b = c

# 初始： a = a0, b = b0;
# a = a ^ b;  ==> a = a0 ^ b0, b = b0;
# b = a ^ b;  ==> a = a0 ^ b0, b = a0 ^ b0 ^ b0 = a0;
# a = a ^ b;  ==> a = a0 ^ b0 ^ a0 = b0, b = a0;





