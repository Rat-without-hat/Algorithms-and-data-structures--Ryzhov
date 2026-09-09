#include <iostream>
#include <vector>

void BubbleSort(std::vector<int> & source_vector)
{
    bool flag_swapped = 0;
    for(int cnt_iter = 0; cnt_iter < source_vector.size(); ++cnt_iter)
    {
        flag_swapped = 0;
        for(std::vector<int>::iterator it = source_vector.begin(); it != source_vector.end() - 1 - cnt_iter; ++it)
        {
            if(*it < *(it + 1))
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
    std::vector<int> test_vector;

    int el = 0;

    while(std::cin >> el)
    {
        test_vector.push_back(el);
        if(std::cin.peek() == '\n')
        {
            break;
        }
    }

    BubbleSort(test_vector);

    for(std::vector<int>::iterator it = test_vector.begin(); it != test_vector.end(); it++)
    {
        std::cout << *it << " ";
    }

    return 0;
}