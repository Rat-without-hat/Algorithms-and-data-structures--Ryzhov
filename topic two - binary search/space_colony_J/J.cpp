#include <iostream>
#include <vector>

bool is_it_possible_thickness(unsigned long int & checked_thickness, unsigned long int & width_el, unsigned long int & height_el, 
                              unsigned long int & width_base, unsigned long int & height_base, unsigned long int & needed_cnt_of_els)
{
    return ((height_base / (height_el + 2 * checked_thickness)) * (width_base / (width_el + 2 * checked_thickness)) >= needed_cnt_of_els) ||
           ((height_base / (width_el + 2 * checked_thickness)) * (width_base / (height_el + 2 * checked_thickness)) >= needed_cnt_of_els);
}

unsigned long int binary_search_thickness(unsigned long int & cnt_of_els, unsigned long int & width_el, unsigned long int & height_el, 
                            unsigned long int & width_base, unsigned long int & height_base)
{
    unsigned long int left = -1;
    unsigned long int right = width_base > height_base ? width_base : height_base;
    unsigned long int median = 0;

    while(right - left > 1)
    {
        median = (right + left) / 2;

        if(is_it_possible_thickness(median, width_el, height_el, width_base, height_base, cnt_of_els))
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
    unsigned long int cnt_of_resid_complex = 0;

    unsigned long int width_resid_complex = 0;
    unsigned long int height_resid_complex = 0;

    unsigned long int width_base = 0;
    unsigned long int height_base = 0;

    std::cin >> cnt_of_resid_complex >> width_resid_complex >> height_resid_complex >> width_base >> height_base;

    std::cout << binary_search_thickness(cnt_of_resid_complex, width_resid_complex, height_resid_complex, width_base, height_base);

    return 0;
}