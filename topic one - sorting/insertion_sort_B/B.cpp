#include <iostream>
#include <vector>

void InsertionSort(std::vector<int> & source_vector)
{
    std::vector<int>::iterator it = source_vector.begin();
    for(int i = 1; i < source_vector.size(); i++)
    {
        it += i;
        while((it != source_vector.begin()) && (*(it - 1) > *it))
        {
            std::swap(*(it - 1), *it);
            --it;
        }
        it = source_vector.begin();
    }
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

    InsertionSort(test_vector);

    for(std::vector<int>::iterator it = test_vector.begin(); it != test_vector.end(); it++)
    {
        std::cout << *it << " ";
    }

    return 0;
}