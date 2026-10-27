#include <iostream>
#include <vector>
#include <string>

class MinHeap
{
    protected:
        std::vector<int> heap;

        void shift_up(unsigned int ind_el)
        {
            while((ind_el > 0) && (heap[ind_el] < heap[(ind_el - 1)/2]))
            {
                std::swap(heap[ind_el], heap[(ind_el - 1)/2]);
                ind_el = (ind_el - 1)/2;
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
            while(ind_el * 2 + 1 < heap.size())
            {
                unsigned int ind_child_min = this->ind_min_child(ind_el);

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

        void clear()
        {
            heap.clear();
        }

        bool is_empty()
        {
            return heap.empty();
        }

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
};

int main()
{
    MinHeap min_heap;
    std::string command;
    int input_val;

    while(std::cin >> command)
    {
        if(command == "CLEAR")
        {
            min_heap.clear();
        }
        else
        {
            if(command == "ADD")
            {
                std::cin >> input_val;
                min_heap.add(input_val);
            }
            else
            {
                if(command == "EXTRACT")
                {
                    if(not(min_heap.is_empty()))
                    {
                        std::cout << min_heap.extract() << std::endl;
                    }
                    else
                    {
                        std::cout << "CANNOT" << std::endl;
                    }
                }
            }
        }
    }

    return 0;
}