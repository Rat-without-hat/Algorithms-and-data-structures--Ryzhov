#include <iostream>
#include <vector>

class MinHeap
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
        MinHeap() {}
        
        void add(int new_val)
        {
            heap.push_back(new_val);
            this->shift_up(heap.size() - 1);
        }

        void del_min()
        {
            heap[0] = heap[heap.size() - 1];
            heap.pop_back();
            this->shift_down(0);
        }

        int get_min()
        {
            return heap[0];
        }

        bool is_empty()
        {
            return heap.empty();
        }
};


int main()
{
    MinHeap heap_starts;
    MinHeap heap_ends;
    unsigned int amount_obj = 0;
    int start_time = 0;
    int end_time = 0;

    std::cin >> amount_obj;

    for(int i = 0; i < amount_obj; i++)
    {
        std::cin >> start_time >> end_time;
        end_time += start_time;
        heap_starts.add(start_time);
        heap_ends.add(end_time);
    }

    int amount_devices = 1;

    heap_starts.del_min();

    while(not(heap_starts.is_empty()))
    {
        if(heap_ends.get_min() <= heap_starts.get_min())
        {
            heap_ends.del_min();
            heap_starts.del_min();
        }
        else
        {
            heap_starts.del_min();
            amount_devices += 1;
        }
    }

    std::cout << amount_devices;

    return 0;
}