#include <iostream>
#include <vector>

bool is_it_possible_len(int & checked_len, std::vector<int> & source_vector, int & needed_els)
{
    int cnt_possible_els = 0;

    for(std::vector<int>::iterator it = source_vector.begin(); it != source_vector.end(); ++it)
    {
        cnt_possible_els += *it / checked_len;
    }

    return cnt_possible_els >= needed_els;
}

int binary_search_len(std::vector<int> & source_vector, int & needed_els)
{
    int left = 0;
    int right = *std::max_element(source_vector.begin(), source_vector.end()) + 1;
    int median = 0;

    while(right - left > 1)
    {
        median = (right + left) / 2;

        if(is_it_possible_len(median, source_vector, needed_els))
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
    int cnt_avilable_wires = 0;
    int cnt_needed_wires = 0;
    int el = 0;
    std::vector<int> vector_of_avilable_wires;

    std::cin >> cnt_avilable_wires >> cnt_needed_wires;

    vector_of_avilable_wires.reserve(cnt_avilable_wires + 1);

    for(int i = 0; i < cnt_avilable_wires; ++i)
    {
        std::cin >> el;
        vector_of_avilable_wires.push_back(el);
    }

    std::cout << binary_search_len(vector_of_avilable_wires, cnt_needed_wires);

    return 0;
}