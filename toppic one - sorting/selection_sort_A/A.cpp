#include <iostream>
#include <vector>

std::vector<int> SelectionSort(std::vector<int> source_vector)
{
    for(std::vector<int>::iterator it_1 = source_vector.begin(); it_1 != source_vector.end(); it_1++)
    {
        std::vector<int>::iterator key_it = it_1;
        for(std::vector<int>::iterator it_2 = it_1 + 1; it_2 != source_vector.end(); it_2++)
        {
            if(*key_it < *it_2)
            {
                key_it = it_2;
            }
        }
        if(key_it != it_1)
        {
            std::swap(*it_1, *key_it);
        }
    }

    return source_vector;
};

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

    std::vector<int> res_vector = SelectionSort(test_vector);

    for(std::vector<int>::iterator it = res_vector.begin(); it != res_vector.end(); it++)
    {
        std::cout << *it << " ";
    }

    return 0;
};