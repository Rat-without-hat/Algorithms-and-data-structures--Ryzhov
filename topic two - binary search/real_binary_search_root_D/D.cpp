#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

double f(int a, int b, int c, int d, double x)
{
    return a * pow(x, 3) + b * pow(x, 2) + c * x + d;
}

double root_binary_search(int a, int b, int c, int d)
{
    double left = - 11000;
    double right = 11000;
    double median = 0;
    int flag_increase = 1;

    if(a < 0)
    {
        flag_increase = -1;
    }

    while(true)
    {
        median = (right + left) / 2;

        if((median >= right) || (median <= left))
        {
            return median;
        }

        if(f(a, b, c, d, trunc(median * pow(10, 4)) / pow(10, 4)) == 0)
        {
            return median;
        }
        else
        {
            if(f(a, b, c, d, trunc(median * pow(10, 4)) / pow(10, 4)) * flag_increase > 0)
            {
                right = median;
            }
            else
            {
                left = median;
            }
        }
    }
}

int main()
{
    int a = 0;
    int b = 0;
    int c = 0;
    int d = 0;

    std::cin >> a >> b >> c >> d;

    std::cout << std::fixed << std::setprecision(15) << root_binary_search(a, b, c, d);

    return 0;
}