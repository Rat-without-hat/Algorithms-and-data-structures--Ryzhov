#include <iostream>
#include <vector>

class MaxHeap
{
    protected:
        std::vector<int> heap;

        void shift_up(unsigned int ind_el)
        {
            unsigned int ind_child = ind_el;

            while((ind_child > 0) && (heap[ind_child] > heap[(ind_child - 1) / 2]))
            {
                std::swap(heap[ind_child], heap[(ind_child - 1) / 2]);
                ind_child = (ind_child - 1) / 2;
            }
        }

        unsigned int ind_max_child(unsigned int ind_el)
        {
            if(ind_el * 2 + 2 >= heap.size())
            {
                return ind_el * 2 + 1;
            }
            if(heap[ind_el * 2 + 2] < heap[ind_el * 2 + 1])
            {
                return ind_el * 2 + 1;
            }

            return ind_el * 2 + 2;
        }

        void shift_down(unsigned int ind_el)
        {
            unsigned int ind_par = ind_el;
            unsigned int ind_child_max = 0;

            while(ind_par * 2 + 1 <= heap.size() - 1)
            {
                ind_child_max = this->ind_max_child(ind_par);

                if(heap[ind_par] < heap[ind_child_max])
                {
                    std::swap(heap[ind_par], heap[ind_child_max]);
                    ind_par = ind_child_max;
                }
                else
                {
                    break;
                }
            }
        }

    public:

    MaxHeap() {}

    void insert(int new_val)
    {
        heap.push_back(new_val);
        this->shift_up(heap.size() - 1);
    }

    int extract()
    {
        int extrcted_val = heap[0];
        std::swap(heap[0], heap[heap.size() - 1]);
        heap.pop_back();
        this->shift_down(0);
        return extrcted_val;
    }
};

int main()
{
    MaxHeap work_heap;
    int input_val;
    unsigned int cnt_com;
    char input_com;

    std::cin >> cnt_com;

    for(int i = 0; i < cnt_com; i++)
    {
        std::cin >> input_com;
        switch(input_com)
        {
        case '0':
            std::cin >> input_val;
            work_heap.insert(input_val);
            break;
        
        case '1':
            std::cout << work_heap.extract() << std::endl;
            break;
        default:
            break;
        }
    }

    return 0;
}