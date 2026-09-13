#include <iostream>
#include <vector>

int BubbleSortCnt(std::vector<int> & source_vector)
{
    bool flag_swapped = 0;
    int cnt_swap = 0;
    for(int cnt_iter = 0; cnt_iter < source_vector.size(); ++cnt_iter)
    {
        flag_swapped = 0;
        for(std::vector<int>::iterator it = source_vector.begin(); it != source_vector.end() - 1 - cnt_iter; ++it)
        {
            if(*it > *(it + 1))
            {
                std::swap(*it, *(it+1));
                flag_swapped = 1;
                cnt_swap += 1;
            }
        }
        if(not(flag_swapped))
        {
            break;
        }
    }

    return cnt_swap;
}

int main()
{
    std::vector<int> test_vector;

    int el = 0;
    int len_vector = 0;

    std::cin >> len_vector;

    for(int i = 0; i < len_vector; ++i)
    {
        std::cin >> el;
        test_vector.push_back(el);
    }

    int cnt_swap = BubbleSortCnt(test_vector);

    std::cout << cnt_swap;
}