


# 问题：有一个整型数组arr和一个大小为w的窗口，窗口每次向右边滑一个位置。
# 返回窗口最大值组成的数组
# 举例：
# arr = [4, 3, 5, 4, 3, 3, 6, 7]   ==>  [5, 5, 5, 4, 6, 7]



# 思想：
# - 窗口用双端队列，就是双向链表，头尾增加东西非常快
# - 当前的元素，如果大于等于队尾的元素，则弹出队尾的元素，仍大于等于继续弹出
# 这样，就能保证双端队列的头一定是当前窗口的最大值，
# - 题目要求窗口大小为3，每次进元素后，判断窗口是否大于3，大于，则弹出一个队头元素
# - 时间复杂度O(N),因为所有的数都只会进来一次，出去一次


'''

public static int[] getMaxWindow(int[] arr, int w){
     # Java里面LinkedList就是双向链表，双向链表中只存元素的下标
     LinkedList<Integer> qmax = new LinkedList<Integer>();
     int[] res = new int[arr.length - w + 1];
     int index = 0;
     for (int i=0; i<arr.length; i++){
        #如果不为空，并且尾部值小于等于当前元素
        while (!qmax.isEmpty() && arr[qmax.peekLast()] <= arr[i]){
            qmax.pollLast(); # 弹出尾部值
        }
        qmax.addLast(i);  #当前值加到尾部

        #如果双端队列的头的下标超过了给定窗口长度
        if (qmax.peekFirst() == i - w){
            qmax.pollFirst();   # 头部就应该弹出
        }
        if (i >= w-1){
            res[index++] = arr[qmax.peekFirst()];
        }
     }
    return res;
}

'''