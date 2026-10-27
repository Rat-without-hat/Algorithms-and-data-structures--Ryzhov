#include <iostream>
#include <vector>
#include <iomanip>

class HeapComCal
{
    protected:
        std::vector<int> heap;

        void shift_up(unsigned int ind_el)
        {
            while((ind_el > 0) && (heap[ind_el] < heap[(ind_el - 1) / 2]))
            {
                std::swap(heap[ind_el], heap[(ind_el - 1) / 2]);
                ind_el = (ind_el - 1) / 2;
            }
        }

        unsigned int ind_min_child(unsigned int ind_el)
        {
            unsigned int res_ind = ind_el * 2 + 2;

            if((ind_el * 2 + 2 >= heap.size()) || (heap[ind_el * 2 + 1] < heap[ind_el * 2 + 2]))
            {
                res_ind = ind_el * 2 + 1;
            }

            return res_ind;
        }

        void shift_down(unsigned int ind_el)
        {
            unsigned int ind_child_min = 0;

            while(ind_el * 2 + 1 < heap.size())
            {
                ind_child_min = this->ind_min_child(ind_el);

                if(heap[ind_el] > heap[ind_child_min])
                {
                    std::swap(heap[ind_el], heap[ind_child_min]);
                    ind_el = ind_child_min;
                }
                else
                {
                    break;
                }
            }
        }

    public:
        HeapComCal() {}

        void add(int new_val)
        {
            heap.push_back(new_val);
            this->shift_up(heap.size() - 1);
        }
        
        int extract()
        {
            int extract_val = heap[0];
            heap[0] = heap[heap.size() - 1];
            heap.pop_back(); 
            this->shift_down(0);

            return extract_val;
        }

        int size()
        {
            return heap.size();
        }

        int get_min()
        {
            return heap[0];
        }
};

int main()
{
    unsigned int amount_vals = 0;
    int input_val = 0;
    HeapComCal cal_heap;
    std::cin >> amount_vals;

    for(int i = 0; i < amount_vals; i++)
    {
        std::cin >> input_val;
        cal_heap.add(input_val);
    }

    int cur_sum = 0;
    float res_mon = 0;

    cur_sum = cal_heap.extract() + cal_heap.extract();
    res_mon += float(cur_sum) * 0.05;
    cal_heap.add(cur_sum);

    while(cal_heap.size() > 1)
    {
        cur_sum = cal_heap.extract() + cal_heap.extract();
        res_mon += float(cur_sum) * 0.05;
        cal_heap.add(cur_sum);
    }

    std::cout << std::fixed << std::setprecision(2) << res_mon;

    return 0;
}