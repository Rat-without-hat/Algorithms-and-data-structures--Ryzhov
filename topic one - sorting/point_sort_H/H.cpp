#include <iostream>
#include <cmath>
#include <vector>
#include <time.h>

struct Point 
{
    int x;
    int y;

    float GetLength()
    {
        return sqrt(pow(x, 2) + pow(y, 2));
    }
};

std::ostream& operator<< (std::ostream &out, Point const& point)
{
    return out << point.x << " " << point.y << std::endl;
}

void QuickSort(std::vector<Point>& source_list, int left, int right)
{
    if(left < right)
    {
        int l = left;
        int r = right;
        srand(time(0));
        int val_ind = float(rand() / RAND_MAX) * (right - left) + left;
        float val = source_list[val_ind].GetLength();
        while(l <= r)
        {
            while(source_list[l].GetLength() < val)
            {
                l += 1;
            }
            while(source_list[r].GetLength() > val)
            {
                r -= 1;
            }
            if(l <= r)
            {
                std::swap(*(source_list.begin() + l), *(source_list.begin() + r));
                l += 1;
                r -= 1;
            }
        }
        if(left < r)
        {
            QuickSort(source_list, left, r);
        }
        if(right > l)
        {
            QuickSort(source_list, l, right);
        }
    }
}


int main()
{
    std::vector<Point> test_vector;
    int list_len = 0;

    std::cin >> list_len;

    Point el = {0, 0};
    for(int i = 0; i < list_len; ++i)
    {

        std::cin >> el.x >> el.y;

        test_vector.push_back(el);
    }

    QuickSort(test_vector, 0, list_len - 1);

    for(std::vector<Point>::iterator it = test_vector.begin(); it != test_vector.end(); ++it)
    {
        std::cout << *it;
    }

    return 0;
}