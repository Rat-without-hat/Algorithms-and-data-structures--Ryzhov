#include <iostream>
#include <vector>

bool binary_search(std::vector<int> & source_vector, int & search_val)
{
    int left = -1;
    int right = source_vector.size();
    int median = 0;

    while(right - left > 1)
    {
        median = (left + right) / 2;
        if(source_vector[median] == search_val)
        {
            return true;
        }
        else
        {
            if(source_vector[median] > search_val)
            {
                right = median;
            }
            else
            {
                left = median;
            }
        }
    }

    return false;
}

int main()
{
    int len_source_vector = 0;
    int len_search_res_vector = 0;
    int el = 0;

    std::vector<int> source_vector;

    std::cin >> len_source_vector >> len_search_res_vector;

    source_vector.reserve(len_source_vector + 1);

    for(int i = 0; i < len_source_vector; i++)
    {
        std::cin >> el;
        source_vector.push_back(el);
    }

    for(int i = 0; i < len_search_res_vector; i++)
    {
        std::cin >> el;
        std::cout << (binary_search(source_vector, el) ? "YES" : "NO") << std::endl;
    }

    return 0;
}