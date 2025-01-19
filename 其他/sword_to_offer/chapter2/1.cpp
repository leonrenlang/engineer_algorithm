


class CMyString {

public:
    CMyString(char* pData = nullptr);
    CMyString(const CMyString& str);
    ~CMyString(void);
private:
    char* m_pData;

};


CMyString& CMyString::operator=(const CMyString &str){
    if (this == &str) {
        return *this;
    }
    
    delete []m_pData;
    m_pData = nullptr;


}


public sealed class Singleton1 {
    
}
