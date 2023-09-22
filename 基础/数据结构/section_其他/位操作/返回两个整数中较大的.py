# 问题： 给定两个32位整数a和b，返回较大的，但是不能用任何比较判断


# public static int flip(int n){
#     return n ^ 1;
# }
# public static int sign(int n){
#     return flip((n >> 31) & 1);
# }
#
# public static int getMax1(int a, int b){
#     int c = a - b;
#     int scA = sign(c);  // 如果a-b的符号为负，则scA为0
#     int scB = flip(scA);
#     return a * scA + b * scB
# }
