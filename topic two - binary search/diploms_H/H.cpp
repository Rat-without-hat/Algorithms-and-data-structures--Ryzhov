#include <iostream>

bool is_it_possible_len(long int & checked_len, long int & source_width, long int & source_height, long int & source_cnt)
{
    return ((checked_len / source_height) * (checked_len / source_width)) >= source_cnt;
}

long int binary_search_len(long int & source_width, long int & source_height, long int & source_cnt)
{
    long int left = -1;
    long int right = (source_width > source_height ? source_width : source_height) * source_cnt + 1;
    long int median = 0;

    while(right - left > 1)
    {
        median = (right + left) / 2;

        if(is_it_possible_len(median, source_width, source_height, source_cnt))
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
    long int width_of_diplom = 0;
    long int height_of_diplom = 0;
    long int cnt_of_diplom = 0;

    std::cin >> width_of_diplom >> height_of_diplom >> cnt_of_diplom;

    std::cout << binary_search_len(width_of_diplom, height_of_diplom, cnt_of_diplom);

    return 0;
}