#include <iostream>
#include <string>
#include <vector>

void BubbleSort(std::vector<std::string> & source_vector)
{
    bool flag_swapped = 0;
    for(int cnt_iter = 0; cnt_iter < source_vector.size(); ++cnt_iter)
    {
        flag_swapped = 0;
        for(std::vector<std::string>::iterator it = source_vector.begin(); it != source_vector.end() - 1 - cnt_iter; ++it)
        {
            if((*it + *(it + 1)) < (*(it + 1) + *it))
            {
                std::swap(*it, *(it+1));
                flag_swapped = 1;
            }
        }
        if(not(flag_swapped))
        {
            break;
        }
    }
}

int main()
{
    std::string str;
    std::vector<std::string> source_vector;

    while(std::cin >> str)
    {
         source_vector.push_back(str);
    }

    std::cout << std::endl;

    BubbleSort(source_vector);

    for(std::vector<std::string>::iterator it = source_vector.begin(); it != source_vector.end(); ++it)
    {
        std::cout << *it;   
    }

    return 0;
}