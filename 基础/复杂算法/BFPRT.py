# 问题：无序数组中，找到第k小/大的数


# 解法1:堆,时间复杂度O(n*logk)


# 解法2： 使用partition方法（荷兰国旗）
# 时间复杂度：如果每次partition都选到最偏的，为O(n2),但是长期期望是O(n)
def partition():
    pass

# 解法3：BFPRT，时间复杂度严格O(N)
# - 1.分组, 一般选5个为一组
# - 2. 小组内排序  O(N)
# - 3. 把每个组的中位数拿出来构成一个新的数组，大小的N/2  O(N)
# - 4. num = BFPRT(新数组， 新数组长度/2) #找新数组中的中位数  T(N/5)
# - 5. 拿这个num来将原数组划分荷兰国旗问题    O(N)
# 小于num放左边，等于放中间，大于的放右边如果中间就是，找到了
# - 否则，只取一边，继续。 # 最差情况，多的一半最多为7/10    (1 - N/10* (5//2+1))
# 时间复杂度T(N) = T(N/5) + T(7/10*N)+ O(N)   ==> O(N) 很难证
"""

public static int medianOfMedians(int[] arr, int begin, int end){
    # 获取每5个元素一组的中位数组成的数组
    int num = end - begin + 1;
    int offset = num % 5 == 0 ? 0 : 1;
    int[] mArr = new int[num/5 + offset];
    for(int i=0; i < mArr.length; i++){
        int beginI = begin + i * 5;
        int endI = beginI + 4;
        mArr[i] = getMedian(arr, beginI, Math.min(end, endI));
    }
    # 找到该数组的中位数     
    return bfprt(mArr, 0, mArr.length - 1. mArr.length / 2);
}

public static int[] partition(int[] arr, int begin, int end, int pivotValue){
    int small = begin - 1;
    int cur  = begin;
    int big = end + 1;
    while (cur != big){
        if (arr[cur] < pivotValue){
            swap(arr, ++small, cur++);
        }else if(arr[cur] > pivotValue){
            swap(arr, cur, --big);
        }else{
            cur++;
        }
        int[] range = new int[2];
        range[0] = small + 1;
        range[1] = big - 1;
        return range;
    }
}

public static int bfprt(int[] arr, int begin, int end, int i){
    # 在begin
    if (begin == end){
        return arr[begin]
    }
    # 中位数数组中的中位数作为划分值
    int pivot = medianOfMedians(arr, begin, end);
    # pivotRange是等于区域的大小
    int[] pivotRange = partition(arr, begin, end, pivot)
    # 如果就在等于区域了，找到了
    if (i >= pivotRange[0] && i <= pivotRange[1]{
        return arr[i]
    }else if (i < pivotRange[0]){
        return bfprt(arr, begin, pivotRange[0]-1, i);
    }else{
        return bfprt(arr, pivotRange[1]+1， end, i);
    }
}
"""