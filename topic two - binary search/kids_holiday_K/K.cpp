#include <iostream>
#include <vector>

bool is_it_possible_time(int & checked_time, std::vector<std::vector<int>> & source_vector, 
                         int & cnt_els, int & cnt_work)
{
    int possible_cnt_of_work = 0;

    for(int i = 0; i < cnt_els; ++i)
    {
        if(checked_time > source_vector[i][0] * source_vector[i][1])
        {
            int cnt_whole_works = (checked_time - source_vector[i][0] * source_vector[i][1]) / (source_vector[i][2] + source_vector[i][0] * source_vector[i][1]);
            int cnt_part_works = (checked_time - source_vector[i][0] * source_vector[i][1]) % (source_vector[i][2] + source_vector[i][0] * source_vector[i][1]);

            possible_cnt_of_work += source_vector[i][1];
            possible_cnt_of_work += cnt_whole_works * source_vector[i][1];
            possible_cnt_of_work += cnt_part_works > source_vector[i][2] ? (cnt_part_works - source_vector[i][2]) / source_vector[i][0] : 0;
        }
        else
        {
            possible_cnt_of_work += checked_time / source_vector[i][0];
        }
    }

    return possible_cnt_of_work >= cnt_work;
}

void binary_search_work_time(std::vector<std::vector<int>> & source_vector, int & cnt_els, int & cnt_work)
{
    int left = -1;
    int right = source_vector[0][0] * cnt_work + (cnt_work / source_vector[0][1]) * source_vector[0][2];
    int median = 0;

    std::vector<int> work_per_person(cnt_els, 0);

    while(right - left > 1)
    {
        median = (right + left) / 2;

        if(is_it_possible_time(median, source_vector, cnt_els, cnt_work))
        {
            right = median;
        }
        else
        {
            left = median;
        }
    }

    int remaining_cnt_works = cnt_work;

    for(int i = 0; i < cnt_els; ++i)
    {
        if(right > source_vector[i][0] * source_vector[i][1])
        {
            int cnt_whole_works = (right - source_vector[i][0] * source_vector[i][1]) / (source_vector[i][2] + source_vector[i][0] * source_vector[i][1]);
            int cnt_part_works = (right - source_vector[i][0] * source_vector[i][1]) % (source_vector[i][2] + source_vector[i][0] * source_vector[i][1]);

            if(remaining_cnt_works >= source_vector[i][1])
            {
                work_per_person[i] = source_vector[i][1];
                remaining_cnt_works -= source_vector[i][1];
            }
            else
            {
                work_per_person[i] += remaining_cnt_works;
                break;
            }

            if(remaining_cnt_works >= cnt_whole_works * source_vector[i][1])
            {
                work_per_person[i] += cnt_whole_works * source_vector[i][1];
                remaining_cnt_works -= cnt_whole_works * source_vector[i][1];
            }
            else
            {
                work_per_person[i] += remaining_cnt_works;
                break;
            }

            if(cnt_part_works > source_vector[i][2])
            {
                if(remaining_cnt_works >= (cnt_part_works - source_vector[i][2]) / source_vector[i][0])
                {
                    work_per_person[i] += (cnt_part_works - source_vector[i][2]) / source_vector[i][0];
                    remaining_cnt_works -= (cnt_part_works - source_vector[i][2]) / source_vector[i][0];
                }
                else
                {
                    work_per_person[i] += remaining_cnt_works;
                    break;
                }
            }
            
        }
        else
        {
            if(remaining_cnt_works >= right / source_vector[i][0])
            {
                work_per_person[i] = right / source_vector[i][0];
                remaining_cnt_works -= right / source_vector[i][0];
            }
            else
            {
                    work_per_person[i] += remaining_cnt_works;
                    break;
            }
        }
    }

    std::cout << right << std::endl << work_per_person[0];
    for(int i = 1; i < cnt_els; ++i)
    {
        std::cout << " " << work_per_person[i];
    }
}

int main()
{
    int amount_of_ballons = 0;
    int amount_of_helpers = 0;
    std::vector<int> el = {0, 0, 0};
    std::vector<std::vector<int>> info_about_helpers;

    std::cin >> amount_of_ballons >> amount_of_helpers;

    info_about_helpers.reserve(amount_of_helpers + 1);

    for(int i = 0; i < amount_of_helpers; ++i)
    {
        std::cin >> el[0] >> el[1] >> el[2];
        info_about_helpers.push_back(el);
    }

    binary_search_work_time(info_about_helpers, amount_of_helpers, amount_of_ballons);

    return 0;
}