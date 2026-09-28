#include <iostream>
#include <vector>
#include <time.h>

bool is_it_possible_diff(int & checked_diff, std::vector<int> & source_vector, 
                         int & cnt_needed_groups, int & needed_cnt_els_in_group)
{
    int cnt_posible_groups = 0;
    int ind_first_el_in_group = 0;
    int ind_last_el_in_group = needed_cnt_els_in_group - 1;

    while(ind_last_el_in_group < source_vector.size())
    {
        if(source_vector[ind_last_el_in_group] - source_vector[ind_first_el_in_group] <= checked_diff)
        {
            ind_first_el_in_group = ind_last_el_in_group + 1;
            ind_last_el_in_group = ind_first_el_in_group + needed_cnt_els_in_group - 1;
            ++cnt_posible_groups;
        }
        else
        {
            ++ind_first_el_in_group;
            ++ind_last_el_in_group;
        }
    }

    return cnt_posible_groups >= cnt_needed_groups;
}

int binary_search_height_diff(std::vector<int> & source_vector, 
                              int & cnt_needed_groups, int & needed_cnt_els_in_group)
{
    int left = -1;
    int right = source_vector[source_vector.size() - 1] - source_vector[0] + 1;
    int median = 0;

    while(right - left > 1)
    {
        median = (right + left) / 2;
        if(is_it_possible_diff(median, source_vector, cnt_needed_groups, needed_cnt_els_in_group))
        {
            right = median;
        }
        else
        {
            left = median;
        }
    }

    return right;    
}

int main()
{
    int total_amount_of_studs = 0;
    int amount_of_studs_in_group = 0;
    int amount_of_groups = 0;
    int el = 0;

    std::vector<int> students_height_in_class;

    std::cin >> total_amount_of_studs >> amount_of_groups >> amount_of_studs_in_group;

    students_height_in_class.reserve(total_amount_of_studs + 1);

    for(int i = 0; i < total_amount_of_studs; ++i)
    {
        std::cin >> el;
        students_height_in_class.push_back(el);
    }

    std::sort(students_height_in_class.begin(), students_height_in_class.end());

    std::cout << binary_search_height_diff(students_height_in_class, amount_of_groups, amount_of_studs_in_group);

    return 0;
}