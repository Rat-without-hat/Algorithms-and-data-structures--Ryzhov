#include <iostream>
#include <vector>

bool is_it_possible_len(int & checked_len, int & cnt_needed, std::vector<int> & source_vector, int & source_len)
{
    int cnt_possible = 0;
    for(std::vector<int>::iterator it = source_vector.begin(); it != source_vector.end(); ++it)
    {
        cnt_possible += (*it) / checked_len;
    }

    return cnt_possible >= cnt_needed;
}

int binary_search_len(int & cnt_needed, std::vector<int> & source_vector, int & source_len)
{
    int left = 0;
    int right = *(std::max_element(source_vector.begin(), source_vector.end())) + 1;
    int median = 0;

    while(true)
    {
        median = (right + left) / 2;

        if((median >= right) || (median <= left))
        {
            break;
        }

        if(is_it_possible_len(median, cnt_needed, source_vector, source_len))
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
    int cnt_ropes_available = 0;
    int cnt_ropes_needed = 0;
    int el = 0;

    std::vector<int> available_ropes;

    std::cin >> cnt_ropes_available >> cnt_ropes_needed;

    available_ropes.reserve(cnt_ropes_available + 1);

    for(int i = 0; i < cnt_ropes_available; ++i)
    {
        std::cin >> el;
        available_ropes.push_back(el);
    }

    std::cout << binary_search_len(cnt_ropes_needed, available_ropes, cnt_ropes_available);

    return 0;
}