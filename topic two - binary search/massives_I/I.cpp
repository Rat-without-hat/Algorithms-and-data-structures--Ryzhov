#include <iostream>
#include <vector>
#include <time.h>

void quick_sort(std::vector<int> & source_vector, int left, int right)
{
    if(left < right)
    {
        srand(time(0));
        int val = source_vector[int(float(rand() / RAND_MAX) * (right - left) + left)];
        int l = left;
        int r = right;

        while(r >= l)
        {
            while(val < source_vector[r])
            {
                --r;
            }

            while(val > source_vector[l])
            {
                ++l;
            }
            
            if(r >= l)
            {
                std::swap(source_vector[l], source_vector[r]);
                ++l;
                --r;
            }
        }

        if(left < r)
        {
            quick_sort(source_vector, left, r);
        }
        if(right > l)
        {
            quick_sort(source_vector, l, right);
        }
    }
}

int binary_search_cnt_of_val(std::vector<int> & source_vector, int & searched_val)
{
    int left = -1;
    int right = source_vector.size();
    int median = 0;

    int res_cnt_of_val = 0;

    while(right - left > 1)
    {
        median = (right + left) / 2;
        if(source_vector[median] > searched_val)
        {
            right = median;
        }
        else
        {
            left = median;
        }
    }

    res_cnt_of_val = right;

    left = -1;
    right = source_vector.size();

    while(right - left > 1)
    {
        median = (right + left) / 2;
        if(source_vector[median] < searched_val)
        {
            left = median;
        }
        else
        {
            right = median;
        }
    }

    res_cnt_of_val -= left + 1;

    return res_cnt_of_val;
}

int main()
{
    int len_compared_vector = 0;
    int len_searched_vector = 0;
    int el = 0;

    std::vector<int> compared_vector;

    std::cin >> len_compared_vector;

    compared_vector.reserve(len_compared_vector + 1);

    for(int i = 0; i < len_compared_vector; ++i)
    {
        std::cin >> el;
        compared_vector.push_back(el);
    }

    quick_sort(compared_vector, 0, compared_vector.size() - 1);

    std::cin >> len_searched_vector;

    for(int i = 0; i < len_searched_vector; ++i)
    {
        std::cin >> el;
        std::cout << binary_search_cnt_of_val(compared_vector, el) << " ";
    }

    return 0;
}