#include <iostream>
#include <vector>

void CountSort(std::vector<int> & source_vector)
{
    int max_el = *(std::max_element(source_vector.begin(), source_vector.end()));

    std::vector<int> cnt_vector;
    cnt_vector.resize(max_el + 1, 0);

    for(unsigned long i = 0; i < source_vector.size(); ++i)
    {
        cnt_vector[source_vector[i]] += 1;
    }

    source_vector.clear();

    for(unsigned long i_1 = 0; i_1 < cnt_vector.size(); ++i_1)
    {
        for(unsigned long i_2 = 0; i_2 < cnt_vector[i_1]; ++i_2)
        {
            source_vector.push_back(i_1);
        }
    }
}

int main() 
{
    int el = 0;
    std::vector<int> test_vector;

    while(std::cin >> el)
    {
        test_vector.push_back(el);

        if(std::cin.peek() == '\n')
        {
            break;
        }
    }

    CountSort(test_vector);

    for(std::vector<int>::iterator it = test_vector.begin(); it != test_vector.end(); ++it)
    {
        std::cout << *it << " ";
    }

    return 0;
}