#include <iostream>
#include <vector>

bool is_it_possible_max_min_dist(std::vector<int> & source_vector, int & max_min_dist, int & cnt_els)
{
    int cnt_placed_els = 1;
    int ind_el_last_placed = source_vector[0];

    for(int i = 1; i < source_vector.size(); ++i)
    {
        if(source_vector[i] - ind_el_last_placed >= max_min_dist)
        {
            ++cnt_placed_els;
            ind_el_last_placed = source_vector[i];
        }
    }

    return cnt_els <= cnt_placed_els;
}

int binary_search_max_min_dist(std::vector<int> & source_vector, int & cnt_els)
{
    int left = 0;
    int right = source_vector[source_vector.size() - 1] - source_vector[0] + 1;
    int median = 0;

    while(right - left > 1)
    {
        median = (right + left) / 2;
        if(is_it_possible_max_min_dist(source_vector, median, cnt_els))
        {
            left = median;
        }
        else
        {
            right = median;
        }
    }

    return left;
}

int main()
{
    int cnt_stalls = 0;
    int cnt_cows = 0;
    std::vector<int> vector_stalls;

    std::cin >> cnt_stalls >> cnt_cows;

    vector_stalls.reserve(cnt_stalls + 1);

    for(int i = 0; i < cnt_stalls; ++i)
    {
        int el;
        std::cin >> el;
        vector_stalls.push_back(el);
    }

    std::cout << binary_search_max_min_dist(vector_stalls, cnt_cows);

    return 0;
}