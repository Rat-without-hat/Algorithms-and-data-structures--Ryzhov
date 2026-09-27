#include <iostream>

bool is_it_possible_time_work(int & cnt_work, int & time_1_work, int & time_2_work, long int & min_time_worked)
{
    int cnt_completed_work = 0;
    int min_time_work = time_1_work < time_2_work ? time_1_work : time_2_work;
    int max_time_work = time_1_work > time_2_work ? time_1_work : time_2_work;
    
    cnt_completed_work += min_time_worked / min_time_work;
    cnt_completed_work += (min_time_worked - min_time_work) / max_time_work;

    return cnt_completed_work >= cnt_work;
}

int binary_search_min_time_work(int & cnt_work, int & time_1_work, int & time_2_work)
{
    long int left = 0;
    long int right = (time_1_work < time_2_work ? time_1_work : time_2_work) * cnt_work + 1;
    long int median = 0;

    while(right - left > 1)
    {
        median = (right + left) / 2;
        if(is_it_possible_time_work(cnt_work, time_1_work, time_2_work, median))
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
    int cnt_docs = 0;
    int time_x_works = 0;
    int time_y_works = 0;

    std::cin >> cnt_docs >> time_x_works >> time_y_works;

    std::cout << binary_search_min_time_work(cnt_docs, time_x_works, time_y_works);

    return 0;
}