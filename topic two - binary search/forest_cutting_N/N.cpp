#include <iostream>
#include <cmath>

bool is_it_possible_time(unsigned long int checked_time, unsigned long int speed_first_el, unsigned long int rest_off_first_el, 
                         unsigned long int speed_second_el, unsigned long int rest_off_second_el, unsigned long int cnt_work)
{
    return (checked_time - (checked_time / rest_off_first_el)) * speed_first_el + (checked_time - (checked_time / rest_off_second_el)) * speed_second_el >= cnt_work;
}

unsigned long int binary_search_amount_of_days(unsigned long int speed_first_el, unsigned long int rest_off_first_el, 
                                               unsigned long int speed_second_el, unsigned long int rest_off_second_el, unsigned long int cnt_work)
{
    unsigned long int left = 0;
    unsigned long int right = ceil(float(cnt_work) / float(speed_first_el)) 
                              + (ceil(float(cnt_work) / float(speed_first_el)) - 1) / (rest_off_first_el - 1) + 1;

    unsigned long int median = 0;

    while(right - left > 1)
    {
        median = (right + left) / 2;

        if(is_it_possible_time(median, speed_first_el, rest_off_first_el, speed_second_el, rest_off_second_el, cnt_work))
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
    unsigned long int speed_first_worker = 0;
    unsigned long int rest_off_day_first_worker = 0;
    unsigned long int speed_second_worker = 0;
    unsigned long int rest_off_day_second_worker = 0;
    unsigned long int amount_of_work = 0;

    std::cin >> speed_first_worker >> rest_off_day_first_worker >> speed_second_worker >> rest_off_day_second_worker >> amount_of_work;

    std::cout << binary_search_amount_of_days(speed_first_worker, rest_off_day_first_worker, speed_second_worker, rest_off_day_second_worker, 
                                              amount_of_work);

    return 0;
}