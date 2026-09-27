#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

#define f(x) (x * x + sqrt(x))

double real_binary_search(float & search_val)
{
    double left = 1;
    double right = sqrt(search_val);
    double median;

    while(true)
    {
        median = (right + left) / 2;
        
        if((median <= left) || (median >= right))
        {
            break;
        }

        if(trunc(f(median) * 1000000) == trunc(search_val * 1000000))
        {
            return median;
        }
        else
        {
            if(trunc(f(median) * 1000000) < trunc(search_val * 1000000))
            {
                left = median;
            }
            else
            {
                right = median;
            }
        }
    }

    return median;
}

int main()
{
    float C_val;

    std::cin >> C_val;

    std::cout << std::fixed << std::setprecision(9) << real_binary_search(C_val);

    return 0;
}