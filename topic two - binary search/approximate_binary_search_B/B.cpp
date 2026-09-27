#include <iostream>
#include <vector>
#include <cmath>

int approximate_binary_search(std::vector<int> & source_vector, int & search_val)
{
    int left = -1;
    int right = source_vector.size();
    int median = 0;

    while(right - left > 1)
    {
        median = (right + left) / 2;

        if(source_vector[median] == search_val)
        {
            return source_vector[median];
        }
        else
        {
            if(source_vector[median] < search_val)
            {
                left = median;
            }
            else
            {
                right = median; 
            }
        }
    }

    left = left >= 0 ? left : 0;
    right = right != source_vector.size() ? right : source_vector.size() - 1;

    if(abs(search_val - source_vector[left]) > abs(source_vector[right] - search_val))
    {
        return source_vector[right];
    }
    else
    {
        return source_vector[left];
    }
}

int main()
{
    int len_sorce_vector = 0;
    int len_search_val = 0;
    int el = 0;

    std::vector<int> sorce_vector;

    std::cin >> len_sorce_vector >> len_search_val;

     sorce_vector.reserve(len_sorce_vector + 1);

    for(int i = 0; i < len_sorce_vector; ++i)
    {
        std::cin >> el;
        sorce_vector.push_back(el);
    }

    for(int i = 0; i < len_search_val; ++i)
    {
        std::cin >> el;
        std::cout << approximate_binary_search(sorce_vector, el) << std::endl;
    }

    return 0;
}