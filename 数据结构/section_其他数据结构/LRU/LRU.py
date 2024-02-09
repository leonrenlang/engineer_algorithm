# 需求：
# - 获取数据（get),如果关键字存在于缓存中，则获取关键字的值
# 并且将关键字的优先级提至最高
# - 写入数据，如果关键字已经存在，变更其数据值，如果不存在，在数组
# 中插入该【关键字/值】。当缓存容量到达上限时，先删除最久未使用数据值
# 再进行插入

# 分析：
# 1. cache中的数据必须有时序
# 2. 我们要能够快速找到某个key是否存在
# 3. 每次访问cache中的某个key，我们要将这个元素变为最近
# 使用的，也就是说cache要支持在任意位置快速插入和删除元素


'''

public void addLast(Node x){
    x.prev = tail.prev;
    x.next = tail;
    tail.prev.next = x;
    tail.prev = x;
    size++;
}

remove(Node x){
    x.prev.next = x.next
    x.next.prev = x.prev;
}


makeRecently(key){
    Node x = map.get(key);
    cache.remove(x);
    cache.addLast(x);
}

void addRecently(key, val){
    Node x =

}

'''
