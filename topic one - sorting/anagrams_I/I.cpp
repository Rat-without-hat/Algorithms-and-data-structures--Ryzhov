#include <iostream>
#include <string>

int main()
{
    std::string str_1;
    std::string str_2;

    std::cin >> str_1;
    std::cin >> str_2;

    if(str_1.length() == str_2.length())
    {
        while(str_1.length() > 0)
        {
            int it = str_2.find(*(str_1.rbegin()));
            if(it != -1)
            {
                str_2.erase(it, 1);
                str_1.pop_back();
            } 
            else
            {
                std::cout << "NO";
                break;
            }
        }
        if(str_1.length() == 0)
        {
           std::cout << "YES"; 
        }
    }
    else
    {
        std::cout << "NO";
    }
    
    return 0;
}