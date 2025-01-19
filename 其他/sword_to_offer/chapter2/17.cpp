

// 打印从1到最大的n位数
# include<bits/stdc++.h>

using namespace std;

// bool Increment(string tmp) {


// }

struct ListNode {
    int m_nValue;
    ListNode *m_pNext;
};

void DeleteNode(ListNode **pListHead, ListNode* pToBeDeleted);

void Print1MaxNDigits(int n) {
    if (n <= 0) {
        return ;
    }
    string tmp(10, '8');

    tmp[0] = '9';

    cout << tmp[0] - '1' << endl;
    
    cout << tmp << endl;
    // while (!Increment(tmp)) {
    //     PrintNumber(tmp);
    // }
}

int main() {
    Print1MaxNDigits(10);
}